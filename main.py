"""
AgroGuard — Single Unified Agricultural Vision Diagnostic Engine
================================================================
Architecture: State-of-the-Art ConvNeXt-Tiny (Single End-to-End Vision Model)
Dataset: Field Leaf Images across 48 Unified Joint Classes (9 Major Crops)
Advisory Synthesis: TNAU-Aligned Brief & Professional Agricultural Advisory (English Only)

Farmer-friendly, high-contrast, outdoor daylight optimized.
"""
import os
import sys
import io
import json
import time
import random
import socket
from typing import Dict, Any, List, Optional
from PIL import Image, ImageOps, ImageFilter, ImageStat

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import torch
import torch.nn as nn
from torchvision import transforms

# Knowledge base import
try:
    from AgroGuard.knowledge_base import get_unified_advisory, DISEASE_DB, CROP_INFO
except ImportError:
    try:
        from knowledge_base import get_unified_advisory, DISEASE_DB, CROP_INFO
    except ImportError:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if base_dir not in sys.path:
            sys.path.insert(0, base_dir)
        from knowledge_base import get_unified_advisory, DISEASE_DB, CROP_INFO

app = FastAPI(
    title="AgroGuard Agricultural Vision API",
    description="Single Unified SOTA Model for Crop Disease Detection & Farmer Advisory",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DATASET_DIR = os.path.join(BASE_DIR, "Dataset")

def locate_file(filename: str) -> str:
    """Locate file in standard project or environment paths."""
    candidates = [
        os.path.join(BASE_DIR, "Dataset Information", filename),
        os.path.join(BASE_DIR, filename),
        os.path.join(os.getcwd(), "Dataset Information", filename),
        os.path.join(os.getcwd(), filename),
        os.path.join("/kaggle/working", filename),
        os.path.join("/kaggle/working/AgroGuard", filename),
        os.path.join("/content", filename),
        os.path.join("/content/AgroGuard", filename),
        os.path.join(os.path.dirname(BASE_DIR), filename),
    ]
    for cand in candidates:
        if os.path.exists(cand):
            return cand
    if os.path.exists("/kaggle/input"):
        for root, _, files in os.walk("/kaggle/input"):
            if filename in files:
                return os.path.join(root, filename)
    return os.path.join(BASE_DIR, filename)

CLASSES_PATH = locate_file("unified_classes.json")
if not os.path.exists(CLASSES_PATH):
    CLASSES_PATH = locate_file("disease_classes.json")
if not os.path.exists(CLASSES_PATH):
    CLASSES_PATH = locate_file("Dataset Stats Information.json")

STATS_PATH = locate_file("dataset_stats.json")
if not os.path.exists(STATS_PATH):
    STATS_PATH = locate_file("Dataset Stats Information.json")

SPLIT_PATH = locate_file("Dataset Split Information.json")

MODEL_PATH = locate_file("best_agroguard_model.pth")

# Mount static directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"[AgroGuard v1.0] Active Device: {device}")

# ── Normalization Constants ──
AGRO_MEAN = [0.4678, 0.4931, 0.3542]
AGRO_STD = [0.2114, 0.1983, 0.2248]
TOTAL_DATASET_IMAGES = 51320

if os.path.exists(STATS_PATH):
    try:
        with open(STATS_PATH, "r", encoding="utf-8") as f:
            stats = json.load(f)
        if "total_images" in stats:
            TOTAL_DATASET_IMAGES = stats["total_images"]
        if "mean" in stats and "std" in stats:
            AGRO_MEAN = stats["mean"]
            AGRO_STD = stats["std"]
            print(f"[AgroGuard v1.0] Loaded empirical dataset normalization: mean={AGRO_MEAN}, std={AGRO_STD}")
    except Exception as e:
        print(f"[WARN] Error reading stats: {e}")

if os.path.exists(SPLIT_PATH):
    try:
        with open(SPLIT_PATH, "r", encoding="utf-8") as f:
            split_info = json.load(f)
        if "total_dataset_images" in split_info:
            TOTAL_DATASET_IMAGES = split_info["total_dataset_images"]
    except Exception as e:
        print(f"[WARN] Error reading split info: {e}")

# ── Load 48 Unified Classes (9 Species) ──
UNIFIED_CLASSES: List[str] = []
if os.path.exists(CLASSES_PATH):
    with open(CLASSES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            UNIFIED_CLASSES = data
        elif isinstance(data, dict) and "classes" in data:
            UNIFIED_CLASSES = data["classes"]
else:
    train_dir = os.path.join(DATASET_DIR, "train")
    if os.path.exists(train_dir):
        UNIFIED_CLASSES = sorted([d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))])
    else:
        UNIFIED_CLASSES = [
            "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___Healthy", "Apple___Scab",
            "Black_gram___Anthracnose", "Black_gram___Healthy", "Black_gram___Leaf_crinkle", "Black_gram___Powdery_mildew", "Black_gram___Yellow_mosaic",
            "Corn___Cercospora_leaf_spot", "Corn___Common_rust", "Corn___Healthy", "Corn___Northern_Leaf_Blight",
            "Grape___Black_rot", "Grape___Esca", "Grape___Healthy", "Grape___Leaf_blight",
            "Orange___Black_spot", "Orange___Canker", "Orange___Citrus_greening", "Orange___Healthy", "Orange___Melanose", "Orange___Scab",
            "Paddy___Bacterial_leaf_blight", "Paddy___Bacterial_leaf_streak", "Paddy___Bacterial_panicle_blight", "Paddy___Blast", "Paddy___Brown_spot", "Paddy___Dead_heart", "Paddy___Downy_mildew", "Paddy___Healthy", "Paddy___Hispa", "Paddy___Tungro",
            "Pepper___Bacterial_spot", "Pepper___Healthy",
            "Potato___Early_blight", "Potato___Healthy", "Potato___Late_blight",
            "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Healthy", "Tomato___Late_blight", "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites", "Tomato___Target_Spot", "Tomato___Tomato_mosaic_virus", "Tomato___Tomato_Yellow_Leaf_Curl_Virus"
        ]

print(f"[AgroGuard v1.0] Loaded {len(UNIFIED_CLASSES)} Unified Crop Disease Classes across 9 Major Botanical Species.")

# ── Transforms ──
eval_transforms = transforms.Compose([
    transforms.Resize((256, 256), interpolation=transforms.InterpolationMode.BICUBIC),
    transforms.ToTensor(),
    transforms.Normalize(mean=AGRO_MEAN, std=AGRO_STD)
])

def predict_with_tta(model: nn.Module, tensor_img: torch.Tensor) -> torch.Tensor:
    """Perform 3-view Test-Time Augmentation (Original, H-Flip, V-Flip)."""
    with torch.no_grad():
        p1 = torch.softmax(model(tensor_img), dim=1)
        p2 = torch.softmax(model(torch.flip(tensor_img, dims=[3])), dim=1)
        p3 = torch.softmax(model(torch.flip(tensor_img, dims=[2])), dim=1)
    return (p1 + p2 + p3) / 3.0

def assess_image_quality(pil_img: Image.Image) -> Dict[str, Any]:
    """Assess blurriness, lighting glare, and contrast of field photos."""
    gray = pil_img.convert("L")
    stat = ImageStat.Stat(gray)
    mean_val = stat.mean[0]
    std_val = stat.stddev[0]

    edges = gray.filter(ImageFilter.FIND_EDGES)
    edge_stat = ImageStat.Stat(edges)
    edge_mean = edge_stat.mean[0]

    is_blurry = edge_mean < 8.0
    is_glare = mean_val > 215.0 or (mean_val > 185.0 and std_val < 35.0)
    is_dark = mean_val < 35.0

    return {
        "is_low_quality": is_blurry or is_glare or is_dark,
        "is_blurry": is_blurry,
        "is_glare": is_glare,
        "is_dark": is_dark,
        "contrast_score": round(float(std_val), 1)
    }

# ── Single Unified Model Instance ──
model_agroguard = None
active_mode = "simulated_unified"

def load_unified_model():
    """Load the Single Unified ConvNeXt-Tiny Agricultural Model with dynamic re-scanning."""
    global model_agroguard, active_mode, MODEL_PATH
    num_classes = len(UNIFIED_CLASSES)
    
    # Dynamically re-scan disk for best_agroguard_model.pth
    target_path = locate_file("best_agroguard_model.pth")
    if not os.path.exists(target_path):
        base_cand = os.path.join(BASE_DIR, "best_agroguard_model.pth")
        if os.path.exists(base_cand):
            target_path = base_cand

    MODEL_PATH = target_path

    if os.path.exists(target_path):
        print(f"[AgroGuard v1.0] Found model weights on disk: {target_path}")
        try:
            try:
                checkpoint = torch.load(target_path, map_location=device, weights_only=True)
            except Exception:
                checkpoint = torch.load(target_path, map_location=device, weights_only=False)

            # Extract state dict if saved in a wrapper dict
            if isinstance(checkpoint, dict):
                if "model_state_dict" in checkpoint:
                    raw_sd = checkpoint["model_state_dict"]
                elif "state_dict" in checkpoint:
                    raw_sd = checkpoint["state_dict"]
                elif "model" in checkpoint:
                    raw_sd = checkpoint["model"]
                else:
                    raw_sd = checkpoint
            elif isinstance(checkpoint, nn.Module):
                model_agroguard = checkpoint.to(device).eval()
                active_mode = "convnext_tiny_unified"
                print(f"[OK] Full model object loaded directly into {device}")
                return
            else:
                raw_sd = checkpoint

            # Strip module. or model. prefixes if present
            clean_sd = {}
            for k, v in raw_sd.items():
                k_clean = k
                if k_clean.startswith("module."):
                    k_clean = k_clean[7:]
                if k_clean.startswith("model."):
                    k_clean = k_clean[6:]
                clean_sd[k_clean] = v

            # Attempt 1: Load via timm
            try:
                import timm
                m = timm.create_model("convnext_tiny", pretrained=False, num_classes=num_classes)
                m.load_state_dict(clean_sd, strict=False)
                m.to(device).eval()
                model_agroguard = m
                active_mode = "convnext_tiny_unified"
                print(f"[OK] Single Unified Model (ConvNeXt-Tiny via timm) loaded from {target_path}")
                return
            except Exception as e_timm:
                print(f"[NOTE] timm loader message: {e_timm}. Attempting torchvision...")

            # Attempt 2: Load via torchvision
            from torchvision import models
            m = models.convnext_tiny(weights=None)
            m.classifier[2] = nn.Linear(m.classifier[2].in_features, num_classes)
            m.load_state_dict(clean_sd, strict=False)
            m.to(device).eval()
            model_agroguard = m
            active_mode = "convnext_tiny_unified"
            print(f"[OK] Single Unified Model (ConvNeXt-Tiny via torchvision) loaded from {target_path}")
            return
        except Exception as ex:
            print(f"[WARN] Failed loading model checkpoint: {ex}")

    model_agroguard = None
    active_mode = "model_pending"
    print(f"[NOTE] No model weights loaded yet. Awaiting 'best_agroguard_model.pth' at: {target_path}")

load_unified_model()

# ── Sample Aliases for Quick Farmer Testing ──
SAMPLE_ALIASES = {
    "rice___blast": "Paddy___Blast",
    "rice_blast": "Paddy___Blast",
    "paddy___blast": "Paddy___Blast",
    "tomato___early_blight": "Tomato___Early_blight",
    "potato___late_blight": "Potato___Late_blight",
    "corn___common_rust": "Corn___Common_rust",
    "citrus___greening": "Orange___Citrus_greening",
    "orange___citrus_greening": "Orange___Citrus_greening",
    "orange___healthy": "Orange___Healthy",
    "orange_healthy": "Orange___Healthy",
    "citrus___healthy": "Orange___Healthy",
    "orange___canker": "Orange___Canker",
    "orange___black_spot": "Orange___Black_spot",
    "orange___melanose": "Orange___Melanose",
    "orange___scab": "Orange___Scab",
    "apple___scab": "Apple___Scab",
    "apple_scab": "Apple___Scab",
    "apple___black_rot": "Apple___Black_rot",
    "apple___cedar_apple_rust": "Apple___Cedar_apple_rust",
    "apple___healthy": "Apple___Healthy",
    "apple_healthy": "Apple___Healthy",
    "paddy___healthy": "Paddy___Healthy",
    "rice___healthy": "Paddy___Healthy",
    "tomato___healthy": "Tomato___Healthy",
    "potato___healthy": "Potato___Healthy",
    "corn___healthy": "Corn___Healthy",
}

# ── API Endpoints ──

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    """Serve AgroGuard Agricultural White & Green UI."""
    index_file = os.path.join(TEMPLATES_DIR, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>AgroGuard Engine Running</h1>")

@app.get("/api/classes")
async def get_classes():
    """Return all 48 unified agricultural classes across 9 major crops."""
    crops = sorted(list(set(c.split("___")[0] for c in UNIFIED_CLASSES)))
    return {
        "total_classes": len(UNIFIED_CLASSES),
        "total_crops": len(crops),
        "crops": crops,
        "classes": UNIFIED_CLASSES
    }

@app.get("/api/model-info")
async def get_model_info():
    """Return single unified model metadata and architecture details."""
    global model_agroguard, active_mode, TOTAL_DATASET_IMAGES
    if model_agroguard is None:
        load_unified_model()

    return {
        "model_name": "ConvNeXt-Tiny (Single Unified Agricultural Vision Model)",
        "framework": "PyTorch / timm",
        "num_classes": len(UNIFIED_CLASSES),
        "total_dataset_images": TOTAL_DATASET_IMAGES,
        "pipeline": f"Single-Stage End-to-End Joint Crop & Pathology Inference · {TOTAL_DATASET_IMAGES:,} Images",
        "normalization": {"mean": AGRO_MEAN, "std": AGRO_STD},
        "is_model_loaded": model_agroguard is not None,
        "active_mode": active_mode,
        "model_path": MODEL_PATH,
        "model_exists_on_disk": os.path.exists(MODEL_PATH)
    }

@app.get("/api/reload-model")
async def reload_model():
    """Dynamically re-scans disk and loads best_agroguard_model.pth after user pastes it."""
    global model_agroguard, active_mode
    load_unified_model()
    return {
        "status": "success",
        "is_model_loaded": model_agroguard is not None,
        "active_mode": active_mode,
        "model_path": MODEL_PATH,
        "model_exists_on_disk": os.path.exists(MODEL_PATH)
    }

@app.get("/api/sample/{sample_class}")
async def get_sample_image(sample_class: str):
    """Retrieve a real sample image from test dataset for 1-click farmer demo."""
    sample_clean = sample_class.replace(".jpg", "").replace(".jpeg", "").replace(".png", "")
    target_class = SAMPLE_ALIASES.get(sample_clean.lower(), sample_clean)

    # 1. Check static/samples
    sample_file = os.path.join(STATIC_DIR, "samples", f"{target_class}.jpg")
    if os.path.exists(sample_file):
        return FileResponse(sample_file, media_type="image/jpeg")

    # 2. Check Dataset test, val, train folders
    search_dirs = [
        os.path.join(DATASET_DIR, "test"),
        os.path.join(DATASET_DIR, "val"),
        os.path.join(DATASET_DIR, "train"),
    ]
    for split_dir in search_dirs:
        if not os.path.exists(split_dir):
            continue
        # Exact match
        p_dir = os.path.join(split_dir, target_class)
        if os.path.exists(p_dir) and os.path.isdir(p_dir):
            files = [f for f in os.listdir(p_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
            if files:
                return FileResponse(os.path.join(p_dir, files[0]), media_type="image/jpeg")

        # Case-insensitive / normalized match
        target_norm = target_class.lower().replace("___", "_").replace(" ", "_")
        for folder in os.listdir(split_dir):
            folder_norm = folder.lower().replace("___", "_").replace(" ", "_")
            if target_norm == folder_norm or target_norm in folder_norm or folder_norm in target_norm:
                fp = os.path.join(split_dir, folder)
                if os.path.isdir(fp):
                    files = [f for f in os.listdir(fp) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
                    if files:
                        return FileResponse(os.path.join(fp, files[0]), media_type="image/jpeg")

    raise HTTPException(status_code=404, detail=f"Sample image for '{sample_class}' not found")

# ── Crop Botanical Aliases for Farmer Disambiguation ──
CROP_FILTER_MAP = {
    "apple": "Apple",
    "paddy": "Paddy",
    "rice": "Paddy",
    "tomato": "Tomato",
    "potato": "Potato",
    "corn": "Corn",
    "maize": "Corn",
    "orange": "Orange",
    "citrus": "Orange",
    "grape": "Grape",
    "grapes": "Grape",
    "pepper": "Pepper",
    "bell pepper": "Pepper",
    "black_gram": "Black_gram",
    "black gram": "Black_gram",
    "urad": "Black_gram",
}

@app.post("/api/predict")
async def predict_leaf(
    file: UploadFile = File(...),
    crop: Optional[str] = Form(None)
):
    """
    Single Unified Vision CNN Prediction (End-to-End Joint Classification):
    Single forward pass evaluates 39 agricultural classes simultaneously.
    Supports optional crop filtering (Auto-Detect by default or narrowed to farmer's selected crop).
    Provides Top-3 multi-hypothesis differential diagnosis with confidence calibration.
    """
    try:
        contents = await file.read()
        pil_img = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file uploaded.")

    quality_info = assess_image_quality(pil_img)
    # Direct normalization without destructive autocontrast color alteration
    input_tensor = eval_transforms(pil_img).unsqueeze(0).to(device)

    # 0. Hot-reload check: Automatically loads weights if newly pasted onto disk
    if model_agroguard is None:
        target_path = locate_file("best_agroguard_model.pth")
        if os.path.exists(target_path) or os.path.exists(os.path.join(BASE_DIR, "best_agroguard_model.pth")):
            load_unified_model()

    # Reject prediction if weights are not available on disk
    if model_agroguard is None:
        return JSONResponse(
            status_code=503,
            content={
                "error": "model_not_loaded",
                "message": "Model weights ('best_agroguard_model.pth') not found. Please train Model.ipynb and paste 'best_agroguard_model.pth' into c:\\AgroGuard to activate live AI inference.",
                "hint": "Run Model.ipynb on your GPU laptop or Kaggle Model.ipynb, then paste 'best_agroguard_model.pth' into c:\\AgroGuard."
            }
        )

    # 1. Pure Model Forward Pass (ConvNeXt-Tiny with 3-view TTA)
    try:
        with torch.no_grad():
            raw_probs = predict_with_tta(model_agroguard, input_tensor)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Neural network inference error: {str(e)}")

    # 2. Determine Crop Filtering
    requested_crop = (crop if isinstance(crop, str) else "").strip().lower()
    canonical_crop = CROP_FILTER_MAP.get(requested_crop, None) if requested_crop and requested_crop != "all" else None

    if canonical_crop:
        candidate_indices = [idx for idx, c in enumerate(UNIFIED_CLASSES) if c.startswith(f"{canonical_crop}___")]
    else:
        candidate_indices = list(range(len(UNIFIED_CLASSES)))

    if not candidate_indices:
        candidate_indices = list(range(len(UNIFIED_CLASSES)))
        canonical_crop = None

    # Slice probabilities for candidate classes and re-normalize
    sub_probs = raw_probs[candidate_indices]
    sub_sum = sub_probs.sum()
    if sub_sum > 0:
        norm_sub_probs = sub_probs / sub_sum
    else:
        norm_sub_probs = sub_probs

    # 3. Top-3 Multi-Hypothesis Ranking
    k = min(3, len(candidate_indices))
    top_k_probs, top_k_sub_indices = torch.topk(norm_sub_probs, k)

    top3_predictions = []
    for p, sub_idx in zip(top_k_probs, top_k_sub_indices):
        real_idx = candidate_indices[sub_idx.item()]
        class_name = UNIFIED_CLASSES[real_idx]
        adv = get_unified_advisory(class_name)
        top3_predictions.append({
            "class_id": class_name,
            "crop_en": adv["crop_en"],
            "disease_en": adv["disease_en"],
            "is_healthy": adv["is_healthy"],
            "confidence": round(float(p.item()), 4)
        })

    # Primary predicted class
    primary_pred = top3_predictions[0]
    predicted_class = primary_pred["class_id"]
    confidence = primary_pred["confidence"]

    # Low quality adjustments
    if quality_info["is_low_quality"]:
        confidence = max(0.35, confidence * 0.85)
        primary_pred["confidence"] = round(float(confidence), 4)

    # 4. Ambiguity / Out-of-Distribution Guard
    is_ambiguous = (confidence <= 0.45 and canonical_crop is None) or (quality_info["is_low_quality"] and confidence < 0.55)
    ambiguity_message = ""
    if is_ambiguous:
        ambiguity_message = (
            "Foliage condition is ambiguous or diagnostic certainty is low across general crop classes. "
            "Please ensure the leaf is clearly centered with good lighting, or select your specific crop from the filter above."
        )

    # 5. Retrieve Structured Advisory from Knowledge Base
    advisory = get_unified_advisory(predicted_class)

    response_data = {
        "class_id": predicted_class,
        "crop_en": advisory["crop_en"],
        "disease_en": advisory["disease_en"],
        "is_healthy": advisory["is_healthy"],
        "confidence": round(float(confidence), 4),
        "top3_predictions": top3_predictions,
        "selected_crop_filter": canonical_crop or "all",
        "is_ambiguous": is_ambiguous,
        "ambiguity_message": ambiguity_message,
        
        # Single Unified Vision Model Card Info
        "model_engine": {
            "name": "ConvNeXt-Tiny (Single Unified Model)",
            "architecture": "Modernized 7x7 Depthwise ConvNet",
            "pipeline": "Single-Stage End-to-End Joint Inference" if not canonical_crop else f"Crop-Focused Diagnostic Mode ({canonical_crop})",
            "confidence": round(float(confidence), 4),
            "total_classes": len(UNIFIED_CLASSES),
            "evaluated_classes": len(candidate_indices)
        },

        # Brief & Professional Agricultural Farm Advisory (English Only)
        "pathogen": advisory.get("pathogen", ""),
        "field_sign": advisory.get("field_sign", ""),
        "symptoms": advisory.get("symptoms", []),
        "chemical_control": advisory.get("chemical_control", ""),
        "organic_control": advisory.get("organic_control", ""),
        "prevention": advisory.get("prevention", ""),
        "is_low_quality": quality_info["is_low_quality"],
        "quality_details": quality_info
    }

    return JSONResponse(content=response_data)

if __name__ == "__main__":
    import uvicorn

    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 8000))

    def is_port_in_use(h: str, p: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((h, p)) == 0

    if is_port_in_use(host, port) and "PORT" not in os.environ:
        print(f"[WARN] Port {port} is currently occupied by another process.")
        for candidate_port in range(8001, 8015):
            if not is_port_in_use(host, candidate_port):
                print(f"[INFO] Automatically switching to available port: http://{host}:{candidate_port}")
                port = candidate_port
                break

    print(f"[AgroGuard v1.0] Unified Vision Engine starting on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)
