/**
 * AgroGuard Enterprise — Diagnostic Controller & Client Logic
 * Standardized for clinical agricultural telemetry · Zero Emojis
 */

let lastDiagnosis = null;
let currentCropFilter = 'all';

// -- SVG Icon Templates --
const SVG_ICONS = {
  check: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  alert: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`,
  clock: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>`
};

// -- Crop Taxon Scope Selection --
function setCropFilter(crop, btnElement) {
  currentCropFilter = crop;
  document.querySelectorAll('.taxa-chip').forEach(c => c.classList.remove('active'));
  if (btnElement) btnElement.classList.add('active');

  const badge = document.getElementById('activeFilterBadge');
  if (badge) {
    if (crop === 'all') {
      badge.innerText = 'Autonomous Multi-Taxa Detection';
    } else {
      badge.innerText = `Constrained Scope: ${crop.replace('_', ' ')}`;
    }
  }

  // If an image is currently loaded, re-evaluate with the selected taxon scope
  const fileInput = document.getElementById('fileInput');
  if (fileInput && fileInput.files && fileInput.files[0]) {
    uploadAndPredict(fileInput.files[0]);
  }
}

// -- File Input Triggers --
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

// -- Drag & Drop Event Listeners --
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

// -- Process & Upload Specimen --
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

  // Smooth scroll for smaller viewports
  if (window.innerWidth < 1120) {
    previewContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Hide standby state, display result container with analyzing indicator
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('resultContent').style.display = 'block';
  document.getElementById('confidenceValue').innerText = 'Computing...';
  document.getElementById('diseaseNameDisplay').innerText = 'Scanning Lamina Architecture...';
}

function stopLaser() {
  const scanLaser = document.getElementById('scanLaser');
  const scanGrid = document.getElementById('scanGrid');
  if (scanLaser) scanLaser.style.display = 'none';
  if (scanGrid) scanGrid.style.display = 'none';
}

// -- Execute Inference Request to FastAPI Backend --
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
      throw new Error(data.detail || `Diagnostic service error: ${response.statusText}`);
    }

    renderDiagnosis(data);
  } catch (error) {
    stopLaser();
    console.error('Diagnostic error:', error);
    alert(error.message || 'Inference request failed. Please check backend connection.');
  }
}

// -- Ingest Standardized Benchmark Sample --
async function loadSample(sampleClass) {
  try {
    const res = await fetch(`/api/sample/${sampleClass}`);
    if (!res.ok) throw new Error("Unable to retrieve reference specimen from server");
    const blob = await res.blob();
    const file = new File([blob], `${sampleClass}.jpg`, { type: 'image/jpeg' });
    processFile(file);
  } catch (err) {
    console.error("Error loading benchmark specimen:", err);
    alert("Could not load reference benchmark specimen from server.");
  }
}

// -- Render Diagnostic Assessment Dossier --
function renderDiagnosis(data) {
  lastDiagnosis = data;
  const isHealthy = data.is_healthy;

  // Pathological Status Badge
  const badge = document.getElementById('diagnosisBadge');
  const badgeIcon = document.getElementById('badgeIcon');
  const badgeText = document.getElementById('badgeText');

  if (badge) {
    if (isHealthy) {
      badge.className = 'clinical-status-badge status-healthy';
      if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.check;
      if (badgeText) badgeText.innerText = 'Asymptomatic Foliar Specimen';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'none';
    } else {
      badge.className = 'clinical-status-badge status-affected';
      if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.alert;
      if (badgeText) badgeText.innerText = 'Pathology Identified';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'block';
    }
  }

  // Diagnostic Certainty Index
  const confPct = (data.confidence * 100).toFixed(1);
  const confValEl = document.getElementById('confidenceValue');
  if (confValEl) confValEl.innerText = `${confPct}%`;

  // Neural Engine Telemetry
  const engineTitleEl = document.getElementById('modelEngineTitle');
  if (engineTitleEl && data.model_engine) {
    engineTitleEl.innerText = data.model_engine.name || 'ConvNeXt-Tiny · Single-Stage Joint Vision';
  }

  const targetDispEl = document.getElementById('modelTargetDisplay');
  if (targetDispEl) {
    targetDispEl.innerText = `${data.crop_en} — ${data.disease_en}`;
  }

  // Optical Quality & Focal Lighting Notice
  const qualityAlert = document.getElementById('qualityAlert');
  if (data.is_low_quality || data.confidence < 0.65) {
    qualityAlert.style.display = 'flex';
  } else {
    qualityAlert.style.display = 'none';
  }

  // Ambiguity Advisory Notice
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

  // Render Differential Diagnosis Distribution
  const diffList = document.getElementById('diffList');
  const diffBadge = document.getElementById('diffModeBadge');

  if (diffBadge) {
    if (data.selected_crop_filter && data.selected_crop_filter !== 'all') {
      diffBadge.innerText = `Constrained: ${data.selected_crop_filter.replace('_', ' ')}`;
    } else {
      diffBadge.innerText = 'Autonomous Mode';
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
            <span class="diff-target-name">${item.crop_en} — ${item.disease_en} ${item.is_healthy ? '<span style="color: #15803d; font-weight: 700; margin-left: 6px; font-size: 0.72rem;">[Asymptomatic]</span>' : ''}</span>
            <span class="diff-prob-val">${probPct}%</span>
          </div>
          <div class="diff-bar-container">
            <div class="diff-bar-fill" style="width: ${Math.max(6, probPct)}%;"></div>
          </div>
        </div>
      `;
      diffList.appendChild(div);
    });
  }

  // Primary Pathological Profile Display
  document.getElementById('cropNameDisplay').innerText = data.crop_en;
  document.getElementById('diseaseNameDisplay').innerText = data.disease_en;
  document.getElementById('pathogenDisplay').innerText = data.pathogen || 'Etiological Agent';

  // Macroscopic Lesion Sign
  document.getElementById('fieldSignText').innerText = data.field_sign || 'Distinct macroscopic foliar symptoms identified on specimen lamina.';

  // Clinical Symptomatology Criteria
  const list = document.getElementById('symptomsList');
  list.innerHTML = '';
  const symptoms = (data.symptoms && data.symptoms.length > 0) ? data.symptoms : [
    "Foliar lesions present across leaf lamina impacting photosynthetic capacity.",
    "Localized cellular chlorosis and vascular tissue necrosis."
  ];
  symptoms.forEach(sym => {
    const li = document.createElement('li');
    li.innerText = sym;
    list.appendChild(li);
  });

  // TNAU CPCPP Treatment Protocols
  document.getElementById('chemicalText').innerText = data.chemical_control || 'Therapeutic chemical intervention not required for this specimen state.';
  document.getElementById('organicText').innerText = data.organic_control || 'Administer certified organic bio-stimulant or foliar compost tea.';
  document.getElementById('preventionText').innerText = data.prevention || 'Implement standard agronomic sanitation, balanced nutrient management, and biosecurity scouting.';
}

// -- Clinical Verbal Consultation (Speech Synthesis) --
function speakDiagnosis() {
  if (!('speechSynthesis' in window) || !lastDiagnosis) {
    alert("Speech synthesis service is unavailable in this environment.");
    return;
  }

  window.speechSynthesis.cancel();

  let textToSpeak = "";
  if (lastDiagnosis.is_healthy) {
    textToSpeak = `Diagnostic evaluation complete for specimen classified as ${lastDiagnosis.crop_en}. Foliar lamina exhibits no active lesion morphology or necrosis. Tissue condition is verified asymptomatic. Continue calibrated irrigation and agronomic nutrient monitoring.`;
  } else {
    textToSpeak = `Diagnostic assessment complete. Specimen classified as ${lastDiagnosis.crop_en}, presenting with ${lastDiagnosis.disease_en}. Etiological agent: ${lastDiagnosis.pathogen || 'Plant Pathogen'}. Recommended therapeutic chemical intervention: ${lastDiagnosis.chemical_control || 'Standard treatment'}. Recommended biological biocontrol: ${lastDiagnosis.organic_control || 'Standard bio-control'}. Prophylactic biosecurity measures: ${lastDiagnosis.prevention || 'Standard prevention'}.`;
  }

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.lang = 'en-US';
  utterance.rate = 0.95;
  utterance.pitch = 1.0;
  window.speechSynthesis.speak(utterance);
}

// -- Model Status Verification & Telemetry Ping --
async function checkModelStatus() {
  try {
    const res = await fetch('/api/model-info');
    if (!res.ok) return;
    const info = await res.json();
    const textEl = document.getElementById('headerStatusText');
    const badgeEl = document.getElementById('headerStatusBadge');
    if (info.is_model_loaded) {
      if (textEl) textEl.innerText = 'Operational · 48 Classes Active';
      if (badgeEl) badgeEl.className = 'telemetry-item badge-operational';
    } else {
      if (textEl) textEl.innerText = 'Standby · Awaiting Weights';
      if (badgeEl) badgeEl.className = 'telemetry-item';
    }
  } catch (err) {
    console.warn("Telemetry status check failed:", err);
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
    badge.className = 'clinical-status-badge status-affected';
    if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.clock;
    if (badgeText) badgeText.innerText = 'Model Weights Pending';
  }

  document.getElementById('confidenceValue').innerText = '0.0%';
  document.getElementById('cropNameDisplay').innerText = 'Diagnostic Engine Standby';
  document.getElementById('diseaseNameDisplay').innerText = 'Model Checkpoint Not Detected';
  document.getElementById('pathogenDisplay').innerText = 'Requires best_agroguard_model.pth in project root';
  document.getElementById('fieldSignText').innerText = msg || "Neural network model weights ('best_agroguard_model.pth') not found on disk. Please train the model via AgroGuard Model.ipynb, Colab, or Kaggle, and place the resulting 'best_agroguard_model.pth' into the repository root.";

  const list = document.getElementById('symptomsList');
  list.innerHTML = `
    <li>Execute <b>c:\\AgroGuard\\AgroGuard Model.ipynb</b>, <b>Colab AgroGuard Model.ipynb</b>, or <b>Kaggle Model.ipynb</b>.</li>
    <li>Place the exported <b>best_agroguard_model.pth</b> directly into <b>c:\\AgroGuard\\</b>.</li>
    <li>The FastAPI diagnostic server will automatically hot-reload the weights and activate full inference.</li>
  `;

  const chemSec = document.getElementById('chemicalSection');
  if (chemSec) chemSec.style.display = 'none';
  const orgSec = document.getElementById('organicSection');
  if (orgSec) orgSec.style.display = 'none';
  const prevSec = document.getElementById('preventionSection');
  if (prevSec) prevSec.style.display = 'none';

  const badgeEl = document.getElementById('headerStatusBadge');
  const textEl = document.getElementById('headerStatusText');
  if (badgeEl) badgeEl.className = 'telemetry-item';
  if (textEl) textEl.innerText = 'Standby · Awaiting Weights';
}

document.addEventListener('DOMContentLoaded', checkModelStatus);
