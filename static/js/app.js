/**
 * 🌾 AgroGuard — Frontend Client Logic
 * Handles file upload, drag-and-drop, laser scan animation,
 * FastAPI prediction requests, diagnostic rendering, and English Voice Readout.
 */

let lastDiagnosis = null;
let currentCropFilter = 'all';

// ── Crop Filter Selection ──
function setCropFilter(crop, btnElement) {
  currentCropFilter = crop;
  document.querySelectorAll('.crop-filter-chip').forEach(c => c.classList.remove('active'));
  if (btnElement) btnElement.classList.add('active');

  const badge = document.getElementById('activeFilterBadge');
  if (badge) {
    if (crop === 'all') {
      badge.innerText = '✨ Auto-Detect All Crops';
    } else {
      badge.innerText = `Filtered: ${crop.replace('_', ' ')}`;
    }
  }

  // If an image is currently previewed/uploaded, re-diagnose with selected filter
  const fileInput = document.getElementById('fileInput');
  if (fileInput && fileInput.files && fileInput.files[0]) {
    uploadAndPredict(fileInput.files[0]);
  }
}

// ── File Input Triggers ──
function triggerFileInput() {
  const input = document.getElementById('fileInput');
  input.removeAttribute('capture');
  input.click();
}

function triggerCamera() {
  const input = document.getElementById('fileInput');
  input.setAttribute('capture', 'environment');
  input.click();
}

// ── Drag & Drop Event Listeners ──
const uploadZone = document.getElementById('uploadZone');

if (uploadZone) {
  ['dragenter', 'dragover'].forEach(eventName => {
    uploadZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      uploadZone.classList.add('drag-over');
    }, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    uploadZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
    }, false);
  });

  uploadZone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files && files.length > 0) {
      processFile(files[0]);
    }
  });
}

function handleFileSelect(event) {
  const file = event.target.files[0];
  if (file) {
    processFile(file);
  }
}

// ── Process & Upload Image ──
function processFile(file) {
  const reader = new FileReader();
  reader.onload = function(e) {
    showPreview(e.target.result);
    uploadAndPredict(file);
  };
  reader.readAsDataURL(file);
}

function showPreview(imageSrc) {
  const previewContainer = document.getElementById('previewContainer');
  const previewImage = document.getElementById('previewImage');
  const scanLaser = document.getElementById('scanLaser');
  const scanGrid = document.getElementById('scanGrid');

  previewImage.src = imageSrc;
  previewContainer.style.display = 'block';
  scanLaser.style.display = 'block';
  scanGrid.style.display = 'block';

  // Scroll smoothly to preview if on mobile
  if (window.innerWidth < 768) {
    previewContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Hide empty state, reveal result container with scanning indicator
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('resultContent').style.display = 'block';
  document.getElementById('confidenceValue').innerText = 'Analyzing...';
  document.getElementById('diseaseNameDisplay').innerText = 'Scanning foliage...';
}

function stopLaser() {
  const scanLaser = document.getElementById('scanLaser');
  const scanGrid = document.getElementById('scanGrid');
  if (scanLaser) scanLaser.style.display = 'none';
  if (scanGrid) scanGrid.style.display = 'none';
}

// ── Send to FastAPI /api/predict ──
async function uploadAndPredict(file) {
  const formData = new FormData();
  formData.append('file', file);
  if (currentCropFilter && currentCropFilter !== 'all') {
    formData.append('crop', currentCropFilter);
  }

  try {
    const response = await fetch('/api/predict', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    stopLaser();

    if (response.status === 503 || data.error === 'model_not_loaded') {
      showModelPendingCard(data.message);
      return;
    }

    if (!response.ok) {
      throw new Error(data.detail || `Server error: ${response.statusText}`);
    }

    renderDiagnosis(data);
  } catch (error) {
    stopLaser();
    console.error('Diagnostic error:', error);
    alert(error.message || 'Prediction failed. Please check server connection.');
  }
}

// ── Load Sample Image from Server ──
async function loadSample(sampleClass) {
  try {
    const res = await fetch(`/api/sample/${sampleClass}`);
    if (!res.ok) throw new Error("Failed to load sample image");
    const blob = await res.blob();
    const file = new File([blob], `${sampleClass}.jpg`, { type: 'image/jpeg' });
    processFile(file);
  } catch (err) {
    console.error("Error loading sample:", err);
    alert("Could not load sample image from server.");
  }
}

// ── Render Diagnosis Result on Dashboard ──
function renderDiagnosis(data) {
  lastDiagnosis = data;
  const isHealthy = data.is_healthy;

  // Status Badge
  const badge = document.getElementById('diagnosisBadge');
  const badgeIcon = document.getElementById('badgeIcon');
  const badgeText = document.getElementById('badgeText');

  if (badge) {
    if (isHealthy) {
      badge.className = 'diagnosis-badge badge-healthy';
      if (badgeIcon) badgeIcon.innerText = '✅';
      if (badgeText) badgeText.innerText = 'Healthy Foliage';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'none';
    } else {
      badge.className = 'diagnosis-badge badge-affected';
      if (badgeIcon) badgeIcon.innerText = '⚠️';
      if (badgeText) badgeText.innerText = 'Disease Detected';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'block';
    }
  }

  // Diagnostic Certainty
  const confPct = (data.confidence * 100).toFixed(1);
  const confValEl = document.getElementById('confidenceValue');
  if (confValEl) confValEl.innerText = `${confPct}%`;

  // Single Unified Vision Model Indicators
  const engineTitleEl = document.getElementById('modelEngineTitle');
  if (engineTitleEl && data.model_engine) {
    engineTitleEl.innerText = data.model_engine.name || 'Unified SOTA Model · ConvNeXt-Tiny';
  }

  const targetDispEl = document.getElementById('modelTargetDisplay');
  if (targetDispEl) {
    targetDispEl.innerText = `${data.crop_en} — ${data.disease_en}`;
  }

  const pipelineSubEl = document.getElementById('modelPipelineSub');
  if (pipelineSubEl && data.model_engine) {
    pipelineSubEl.innerText = data.model_engine.pipeline || 'Single-Stage End-to-End Joint Crop & Pathology Inference';
  }

  const meterEl = document.getElementById('unifiedMeter');
  if (meterEl) {
    meterEl.style.width = `${Math.min(100, Math.max(15, confPct))}%`;
  }

  const confLabelEl = document.getElementById('unifiedConfLabel');
  if (confLabelEl) {
    confLabelEl.innerText = `Certainty: ${confPct}%`;
  }

  // Quality Alert
  const qualityAlert = document.getElementById('qualityAlert');
  if (data.is_low_quality || data.confidence < 0.65) {
    qualityAlert.style.display = 'block';
  } else {
    qualityAlert.style.display = 'none';
  }

  // Ambiguity / Low Confidence Notice
  const ambAlert = document.getElementById('ambiguityAlert');
  const ambText = document.getElementById('ambiguityAlertText');
  if (ambAlert) {
    if (data.is_ambiguous) {
      ambAlert.style.display = 'flex';
      if (ambText && data.ambiguity_message) ambText.innerText = data.ambiguity_message;
    } else {
      ambAlert.style.display = 'none';
    }
  }

  // Render Top-3 Differential Diagnosis Candidates
  const diffList = document.getElementById('diffList');
  const diffBadge = document.getElementById('diffModeBadge');

  if (diffBadge) {
    if (data.selected_crop_filter && data.selected_crop_filter !== 'all') {
      diffBadge.innerText = `Filtered: ${data.selected_crop_filter.replace('_', ' ')}`;
    } else {
      diffBadge.innerText = 'Auto-Detect Mode';
    }
  }

  if (diffList && data.top3_predictions && data.top3_predictions.length > 0) {
    diffList.innerHTML = '';
    data.top3_predictions.forEach((item, index) => {
      const isPrimary = index === 0;
      const probPct = (item.confidence * 100).toFixed(1);

      const div = document.createElement('div');
      div.className = `diff-item ${isPrimary ? 'diff-primary' : ''}`;
      div.innerHTML = `
        <div class="diff-rank">${index + 1}</div>
        <div class="diff-info">
          <div class="diff-target-row">
            <span class="diff-target-name">${item.crop_en} — ${item.disease_en} ${item.is_healthy ? '✅' : ''}</span>
            <span class="diff-prob-val">${probPct}%</span>
          </div>
          <div class="diff-bar-container">
            <div class="diff-bar-fill" style="width: ${Math.max(8, probPct)}%;"></div>
          </div>
        </div>
      `;
      diffList.appendChild(div);
    });
  }

  // Crop & Disease Headline
  document.getElementById('cropNameDisplay').innerText = data.crop_en;
  document.getElementById('diseaseNameDisplay').innerText = data.disease_en;
  document.getElementById('pathogenDisplay').innerText = data.pathogen || 'Plant Pathogen';

  // Rapid Field Sign
  document.getElementById('fieldSignText').innerText = data.field_sign || 'Distinct foliar symptoms visible on leaf lamina.';

  // Key Symptoms
  const list = document.getElementById('symptomsList');
  list.innerHTML = '';
  const symptoms = (data.symptoms && data.symptoms.length > 0) ? data.symptoms : [
    "Foliar lesions visible on lamina affecting chlorophyll density.",
    "Cellular discoloration and localized tissue necrosis."
  ];
  symptoms.forEach(sym => {
    const li = document.createElement('li');
    li.innerText = sym;
    list.appendChild(li);
  });

  // Treatments & Prevention
  document.getElementById('chemicalText').innerText = data.chemical_control || 'No chemical intervention required.';
  document.getElementById('organicText').innerText = data.organic_control || 'Apply standard organic bio-fertilizer or compost tea.';
  document.getElementById('preventionText').innerText = data.prevention || 'Ensure field sanitation, balanced fertilization, and weekly scouting.';
}

// ── Text-to-Speech (English Voice Output for Farmers) ──
function speakDiagnosis() {
  if (!('speechSynthesis' in window) || !lastDiagnosis) {
    alert("Speech synthesis is not supported in this browser.");
    return;
  }

  window.speechSynthesis.cancel();

  let textToSpeak = "";
  if (lastDiagnosis.is_healthy) {
    textToSpeak = `Good news! Plant identified as ${lastDiagnosis.crop_en}. The foliage is healthy with no disease symptoms detected. Continue regular irrigation and organic soil nutrition.`;
  } else {
    textToSpeak = `Diagnosis report for ${lastDiagnosis.crop_en}. Condition identified: ${lastDiagnosis.disease_en}. Recommended chemical treatment: ${lastDiagnosis.chemical_control}. Recommended organic treatment: ${lastDiagnosis.organic_control}. Future prevention: ${lastDiagnosis.prevention}.`;
  }

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.lang = 'en-US';
  utterance.rate = 0.95;
  utterance.pitch = 1.0;
  window.speechSynthesis.speak(utterance);
}

// ── Dynamic Model Status Verification & Hot-Reload Polling ──
async function checkModelStatus() {
  try {
    const res = await fetch('/api/model-info');
    if (!res.ok) return;
    const info = await res.json();
    const textEl = document.getElementById('headerStatusText');
    const badgeEl = document.getElementById('headerStatusBadge');
    if (info.is_model_loaded) {
      if (textEl) textEl.innerText = 'ConvNeXt-Tiny Neural Network Active (Weights Loaded)';
      if (badgeEl) badgeEl.className = 'agro-badge badge-emerald';
    } else {
      if (textEl) textEl.innerText = 'Model Offline: Awaiting best_agroguard_model.pth';
      if (badgeEl) badgeEl.className = 'agro-badge badge-pending';
    }
  } catch (err) {
    console.warn("Could not check model info:", err);
  }
}

function showModelPendingCard(msg) {
  const resultContent = document.getElementById('resultContent');
  const emptyState = document.getElementById('emptyState');
  if (emptyState) emptyState.style.display = 'none';
  if (resultContent) resultContent.style.display = 'block';

  const badge = document.getElementById('diagnosisBadge');
  const badgeIcon = document.getElementById('badgeIcon');
  const badgeText = document.getElementById('badgeText');
  if (badge) {
    badge.className = 'diagnosis-badge badge-affected';
    if (badgeIcon) badgeIcon.innerText = '⏳';
    if (badgeText) badgeText.innerText = 'Weights Pending';
  }

  document.getElementById('confidenceValue').innerText = '0.0%';
  document.getElementById('cropNameDisplay').innerText = 'AI Model Offline';
  document.getElementById('diseaseNameDisplay').innerText = 'Awaiting best_agroguard_model.pth';
  document.getElementById('pathogenDisplay').innerText = 'Please paste trained weights into c:\\AgroGuard to activate';
  document.getElementById('fieldSignText').innerText = msg || "Neural network model weights ('best_agroguard_model.pth') not found on disk. Please train Model.ipynb on your GPU laptop or Kaggle Model.ipynb, and place the resulting 'best_agroguard_model.pth' into the c:\\AgroGuard folder.";

  const list = document.getElementById('symptomsList');
  list.innerHTML = `
    <li>Open <b>c:\\AgroGuard\\Model.ipynb</b> on your GPU laptop (or <b>Kaggle Model.ipynb</b> on Kaggle Cloud).</li>
    <li>Run the notebook to train ConvNeXt-Tiny across the unified standardized dataset images.</li>
    <li>Paste the generated <b>best_agroguard_model.pth</b> directly into <b>c:\\AgroGuard\\</b>.</li>
    <li>The web application will instantly hot-reload and run true AI vision predictions on all leaves.</li>
  `;

  const chemSec = document.getElementById('chemicalSection');
  if (chemSec) chemSec.style.display = 'none';
  const orgSec = document.getElementById('organicSection');
  if (orgSec) orgSec.style.display = 'none';
  const prevSec = document.getElementById('preventionSection');
  if (prevSec) prevSec.style.display = 'none';

  // Update header badge to pending
  const badgeEl = document.getElementById('headerStatusBadge');
  const textEl = document.getElementById('headerStatusText');
  if (badgeEl) badgeEl.className = 'agro-badge badge-pending';
  if (textEl) textEl.innerText = 'Model Offline: Awaiting best_agroguard_model.pth';
}

document.addEventListener('DOMContentLoaded', checkModelStatus);

