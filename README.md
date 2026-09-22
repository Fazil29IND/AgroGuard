# 🌿 AgroGuard — Unified Agricultural Vision Diagnostic Engine (v1.0.0)

<div align="center">

---

## 🌟 What is AgroGuard v1.0.0?

**AgroGuard v1.0.0** is the inaugural flagship release of an end-to-end agricultural computer vision and diagnostic platform designed for farmers, researchers, and agronomists.

Instead of fragmented multi-model pipelines, AgroGuard operates on a single unified **ConvNeXt-Tiny** deep neural network trained on **51,320 standardized field leaf images** across **48 joint crop-pathology classes**. When a leaf image is captured, the system performs instantaneous inference and pairs the diagnosis with **Tamil Nadu Agricultural University (TNAU) Crop Protection Compendium (CPCPP)** phytosanitary recommendations (chemical, organic, and cultural protocols).

---

## ✨ Key Features

- 🧠 **Unified Vision Architecture**: Single end-to-end **ConvNeXt-Tiny** backbone with 28M parameters, achieving high accuracy with fast inference latency.
- 🌾 **48 Unified Classes across 9 Crops**: Covers staple cereals, pulses, fruits, and nightshades (Rice, Maize, Black Gram, Apple, Citrus, Grape, Tomato, Potato, Pepper).
- ☀️ **Field-Condition Robustness**: Specialized training augmentations simulating harsh midday sunlight, specular leaf glare, canopy shadows, and handheld camera blur.
- ⚖️ **Imbalance-Resilient Training**: Employs `WeightedRandomSampler` and smoothed inverse-frequency loss weighting to neutralize extreme 550:1 class imbalances.
- 🚜 **Actionable Agronomic Advisory**: Instant phytosanitary treatment steps, chemical dosages, organic controls, and preventive cultural practices.
- ⚡ **Triple Training Ecosystem**:
  1. **Google Colab Cloud GPU** (`Colab/Colab AgroGuard Model.ipynb` + `Colab/Dataset.zip`)
  2. **Kaggle Cloud GPU** (`Kaggle/Kaggle Model.ipynb` + `Kaggle/Dataset.zip`)
  3. **Local Dedicated GPU** (`AgroGuard Model.ipynb`)
- 💻 **Modern Glassmorphic Web App**: FastAPI backend paired with high-contrast, responsive client dashboard and automatic hot-reloading for model checkpoints.

---

## 📁 Project Architecture & Directory Layout

```text
AgroGuard/
│
├── .github/                               # GitHub workflows & community health templates
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md                  # Bug report template
│   │   └── feature_request.md             # Feature proposal template
│   ├── pull_request_template.md           # PR checklist
│   └── workflows/
│       └── ci.yml                         # Automated CI linting & smoke test pipeline
│
├── Colab/                                 # Google Colab Cloud GPU Ecosystem
│   ├── Colab AgroGuard Model.ipynb        # Colab GPU training notebook (Drive integration + AMP)
│   ├── Dataset.zip                        # Complete 48-class ready-to-mount archive (1.58 GB)
│   └── .gitkeep
│
├── Dataset/                               # Standardized 48-Class Agricultural Dataset
│   ├── train/                             # 41,057 images (48 classes)
│   ├── val/                               # 5,130 images (48 classes)
│   ├── test/                              # 5,133 images (48 classes)
│   ├── Dataset.zip                        # Local offline backup archive
│   └── .gitkeep
│
├── Dataset Information/
│   ├── Dataset Stats Information.json     # Normalization stats (mean/std), 48 classes, 9 species
│   └── Dataset Split Information.json     # Stratified split counts per class
│
├── Kaggle/                                # Kaggle Cloud GPU Ecosystem
│   ├── Kaggle Model.ipynb                 # Distributed Kaggle GPU P100 / dual T4 notebook
│   ├── Dataset.zip                        # Complete 48-class archive ready for Kaggle datasets
│   └── .gitkeep
│
├── static/                                # Modern dark/light glassmorphic UI assets
│   ├── css/style.css                      # Ergonomic CSS tokens, animations & responsive layout
│   └── js/app.js                          # Diagnosis controller, camera handler & sample test chips
│
├── templates/
│   └── index.html                         # Interactive farmer dashboard & diagnostic console
│
├── .gitattributes                         # Line endings & binary formatting rules
├── .gitignore                             # Clean exclusion of cache, heavy binaries & checkpoints
├── AgroGuard Model.ipynb                  # Local computer GPU training & evaluation notebook
├── Amanullah Fazil S (44111431).pptx      # Project presentation slide deck
├── best_agroguard_model.pth               # Pre-trained ConvNeXt-Tiny weights checkpoint (~111 MB)
├── Code of Conduct.md                     # Contributor Covenant v2.1
├── Contribution.md                        # Open-source contribution guidelines
├── knowledge_base.py                      # TNAU CPCPP 48-class phytosanitary advisory engine
├── LICENSE                                # MIT License (Amanullah Fazil S)
├── main.py                                # Production FastAPI diagnostic web server
├── Plant and Disease Information.md       # Botanical taxonomy, symptoms & agronomic matrix
├── pyproject.toml                         # Standard PEP 518/621 project configuration
├── README.md                              # Repository documentation & quickstart guide
└── requirements.txt                       # Version-pinned Python dependencies
```

---

## 🌾 Supported Botanical Crops & 48 Pathology Classes

| # | Crop Species                     | Botanical Name                         | Total Classes | Included Pathologies & Health States                                                                                                                      |
| - | -------------------------------- | -------------------------------------- | :-----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | **Apple**                  | *Malus domestica*                    |       4       | Apple Scab, Black Rot, Cedar Apple Rust, Healthy                                                                                                          |
| 2 | **Black Gram**             | *Vigna mungo*                        |       5       | Anthracnose, Leaf Crinkle, Powdery Mildew, Yellow Mosaic, Healthy                                                                                         |
| 3 | **Corn / Maize**           | *Zea mays*                           |       4       | Cercospora Leaf Spot (Gray Spot), Common Rust, Northern Leaf Blight, Healthy                                                                              |
| 4 | **Grape**                  | *Vitis vinifera*                     |       4       | Black Rot, Esca (Black Measles), Leaf Blight, Healthy                                                                                                     |
| 5 | **Orange (Citrus)**        | *Citrus sinensis* / *aurantifolia* |       6       | Black Spot, Canker, Citrus Greening (HLB), Melanose, Scab, Healthy                                                                                        |
| 6 | **Paddy / Rice**           | *Oryza sativa*                       |      10      | Bacterial Leaf Blight, Bacterial Leaf Streak, Bacterial Panicle Blight, Blast, Brown Spot, Dead Heart, Downy Mildew, Hispa, Tungro, Healthy               |
| 7 | **Pepper (Bell / Chilli)** | *Capsicum annuum*                    |       2       | Bacterial Spot, Healthy                                                                                                                                   |
| 8 | **Potato**                 | *Solanum tuberosum*                  |       3       | Early Blight, Late Blight, Healthy                                                                                                                        |
| 9 | **Tomato**                 | *Solanum lycopersicum*               |      10      | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Tomato Mosaic Virus, Yellow Leaf Curl Virus, Healthy |

> For exhaustive botanical descriptions, visual symptoms, chemical protocols, and Tamil regional common names, refer to [Plant and Disease Information.md](<Plant%20and%20Disease%20Information.md>).

---

## 📊 Dataset Distribution & Stratification

The standardized dataset comprises **51,320 leaf images** partitioned with fixed seed `42`:

- **Training Split (`Dataset/train/`)**: **41,057 images** (80.00%)
- **Validation Split (`Dataset/val/`)**: **5,130 images** (10.00%)
- **Test Split (`Dataset/test/`)**: **5,133 images** (10.00%)
- **Total Standardized Dataset**: **51,320 images** across **48 classes**

---

## ⚡ Triple Training Ecosystem

AgroGuard provides three complete, self-contained training pipelines tailored to different compute environments:

### 1. Google Colab Cloud GPU Training (`Colab/`)

- Open [`Colab/Colab AgroGuard Model.ipynb`](<Colab/Colab%20AgroGuard%20Model.ipynb>) or click the badge: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<https://colab.research.google.com/github/AgroGuard/AgroGuard/blob/main/Colab/Colab%20AgroGuard%20Model.ipynb>)
- In Colab, select: **Runtime ➔ Change runtime type ➔ T4 GPU**.
- Upload `Colab/Dataset.zip` or mount Google Drive directly in the notebook.
- Run all cells to train with mixed precision (AMP) and download `best_agroguard_model.pth`.

### 2. Kaggle Cloud GPU Training (`Kaggle/`)

- In Kaggle, create a new notebook and attach `Kaggle/Dataset.zip` as a dataset.
- Import [`Kaggle/Kaggle Model.ipynb`](<Kaggle/Kaggle%20Model.ipynb>).
- Select accelerator **GPU Tesla T4 x 2** or **P100**.
- Train and download the resulting weights from `/kaggle/working/best_agroguard_model.pth`.

### 3. Local Dedicated GPU Training

- Open [`AgroGuard Model.ipynb`](<AgroGuard%20Model.ipynb>) in JupyterLab or VS Code.
- Uses local NVIDIA CUDA acceleration and directly writes `best_agroguard_model.pth` into the repository root.

---

## 🚀 Quickstart & Local Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/AgroGuard/AgroGuard.git
cd AgroGuard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Diagnostic Server

```bash
python main.py
```

### 4. Access the Dashboard

Open your browser and navigate to:

```text
http://localhost:8000
```

> **Automatic Model Hot-Reloading**: When you place `best_agroguard_model.pth` into the project root directory, the running FastAPI server automatically detects the checkpoint and loads the ConvNeXt-Tiny weights into memory without requiring a server restart!

---

## 📦 Large Files & Dataset Management

To adhere to GitHub's **100 MB per-file limit**:

- Model checkpoints (`*.pth`) and dataset archives (`*.zip`) are excluded from normal Git commits via `.gitignore`.
- Skeletons for `Colab/`, `Kaggle/`, and `Dataset/` are preserved via `.gitkeep`.
- The complete dataset can be downloaded from our [GitHub Releases](https://github.com/AgroGuard/AgroGuard/releases) or mounted using Google Drive / Kaggle as described above.

---

## 📚 Academic Citations & Attribution

1. **Hughes, D.P., Salathé, M. (2015).** *An open access repository of images on plant health to enable the development of mobile disease diagnostics through machine learning and crowdsourcing.* **arXiv:1511.08060** (PlantVillage, **CC0-1.0**).
2. **Rauf, H.T., Saleem, B.A., Lali, M.I.U., Khan, M.A., Sharif, M., Bukhari, S.A.C. (2019).** *A citrus fruits and leaves dataset for detection and classification of citrus diseases through machine learning.* **Data in Brief**, 26, 104340. [https://doi.org/10.17632/3f83gxmv57.2](https://doi.org/10.17632/3f83gxmv57.2) (**CC BY 4.0**).
3. **Tamil Nadu Agricultural University (TNAU).** *Crop Protection Compendium (CPCPP) & Agritech Portal Phytosanitary Protocols.*

---

## 📄 License & Authorship

Developed with ❤️ by **Amanullah Fazil S**.
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for terms.
