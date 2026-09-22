/**
 * AgroGuard — Simple & Professional Client Diagnostic Controller
 * Zero Emojis · Clean SVG Indicators · Professional Terminology
 */

let lastDiagnosis = null;
let currentCropFilter = 'all';

// Clean SVG Icons
const SVG_ICONS = {
  check: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  alert: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`,
  clock: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>`
};

// Crop Filter Toggle
function setCropFilter(crop, btnElement) {
  currentCropFilter = crop;
  document.querySelectorAll('.crop-pill').forEach(c => c.classList.remove('active'));
  if (btnElement) btnElement.classList.add('active');

  const badge = document.getElementById('activeFilterBadge');
  if (badge) {
    if (crop === 'all') {
      badge.innerText = 'All Crops';
    } else {
      badge.innerText = crop.replace('_', ' ');
    }
  }

  // If a file is currently selected, re-predict with selected crop filter
  const fileInput = document.getElementById('fileInput');
  if (fileInput && fileInput.files && fileInput.files[0]) {
    uploadAndPredict(fileInput.files[0]);
  }
}

// File Triggers
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

// Drag & Drop
const uploadZone = document.getElementById('uploadZone');

if (uploadZone) {
  ['dragenter', 'dragover'].forEach(name => {
    uploadZone.addEventListener(name, (e) => {
      e.preventDefault();
      uploadZone.classList.add('drag-over');
    }, false);
  });

  ['dragleave', 'drop'].forEach(name => {
    uploadZone.addEventListener(name, (e) => {
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

// Process Image
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

  previewImage.src = imageSrc;
  previewContainer.style.display = 'block';
  scanLaser.style.display = 'block';

  // Smooth scroll for mobile
  if (window.innerWidth < 960) {
    previewContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Update view
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('resultContent').style.display = 'block';
  document.getElementById('confidenceValue').innerText = 'Analyzing...';
  document.getElementById('diseaseNameDisplay').innerText = 'Diagnosing Leaf...';
}

function stopLaser() {
  const scanLaser = document.getElementById('scanLaser');
  if (scanLaser) scanLaser.style.display = 'none';
}

// Send to FastAPI /api/predict
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
    console.error('Diagnosis error:', error);
    alert(error.message || 'Diagnostic request failed. Please check server connection.');
  }
}

// Load Benchmark Sample
async function loadSample(sampleClass) {
  try {
    const res = await fetch(`/api/sample/${sampleClass}`);
    if (!res.ok) throw new Error("Could not load sample image");
    const blob = await res.blob();
    const file = new File([blob], `${sampleClass}.jpg`, { type: 'image/jpeg' });
    processFile(file);
  } catch (err) {
    console.error("Error loading sample:", err);
    alert("Could not load test sample image from server.");
  }
}

// Render Results
function renderDiagnosis(data) {
  lastDiagnosis = data;
  const isHealthy = data.is_healthy;

  // Status Badge
  const badge = document.getElementById('diagnosisBadge');
  const badgeIcon = document.getElementById('badgeIcon');
  const badgeText = document.getElementById('badgeText');

  if (badge) {
    if (isHealthy) {
      badge.className = 'status-badge badge-success';
      if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.check;
      if (badgeText) badgeText.innerText = 'Healthy Crop';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'none';
    } else {
      badge.className = 'status-badge badge-danger';
      if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.alert;
      if (badgeText) badgeText.innerText = 'Disease Detected';
      const chemSec = document.getElementById('chemicalSection');
      if (chemSec) chemSec.style.display = 'block';
    }
  }

  // Confidence
  const confPct = (data.confidence * 100).toFixed(1);
  const confValEl = document.getElementById('confidenceValue');
  if (confValEl) confValEl.innerText = `${confPct}%`;

  // Headline
  document.getElementById('cropNameDisplay').innerText = data.crop_en;
  document.getElementById('diseaseNameDisplay').innerText = data.disease_en;
  document.getElementById('pathogenDisplay').innerText = data.pathogen || 'Plant Pathogen';

  // Differential List
  const diffList = document.getElementById('diffList');
  if (diffList && data.top3_predictions && data.top3_predictions.length > 0) {
    diffList.innerHTML = '';
    data.top3_predictions.forEach(item => {
      const pct = (item.confidence * 100).toFixed(1);
      const row = document.createElement('div');
      row.className = 'diff-row';
      row.innerHTML = `
        <div class="diff-labels">
          <span>${item.crop_en} — ${item.disease_en}</span>
          <span>${pct}%</span>
        </div>
        <div class="diff-bar">
          <div class="diff-bar-fill" style="width: ${Math.max(5, pct)}%;"></div>
        </div>
      `;
      diffList.appendChild(row);
    });
  }

  // Symptoms
  const list = document.getElementById('symptomsList');
  list.innerHTML = '';
  const symptoms = (data.symptoms && data.symptoms.length > 0) ? data.symptoms : [
    "Foliar lesions present across leaf lamina.",
    "Tissue discoloration and reduced vitality."
  ];
  symptoms.forEach(sym => {
    const li = document.createElement('li');
    li.innerText = sym;
    list.appendChild(li);
  });

  // Treatments
  document.getElementById('chemicalText').innerText = data.chemical_control || 'No chemical treatment needed.';
  document.getElementById('organicText').innerText = data.organic_control || 'Apply standard organic bio-fertilizer or compost tea.';
  document.getElementById('preventionText').innerText = data.prevention || 'Maintain field sanitation, proper irrigation, and crop scouting.';
}

// Audio Advisory
function speakDiagnosis() {
  if (!('speechSynthesis' in window) || !lastDiagnosis) {
    alert("Speech synthesis is not supported in this browser.");
    return;
  }

  window.speechSynthesis.cancel();

  let textToSpeak = "";
  if (lastDiagnosis.is_healthy) {
    textToSpeak = `Plant identified as ${lastDiagnosis.crop_en}. The foliage is healthy with no disease symptoms detected. Continue normal crop care.`;
  } else {
    textToSpeak = `Diagnosis report for ${lastDiagnosis.crop_en}. Condition identified: ${lastDiagnosis.disease_en}. Pathogen: ${lastDiagnosis.pathogen || 'Plant pathogen'}. Chemical treatment: ${lastDiagnosis.chemical_control}. Organic treatment: ${lastDiagnosis.organic_control}. Prevention: ${lastDiagnosis.prevention}.`;
  }

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.lang = 'en-US';
  utterance.rate = 0.95;
  window.speechSynthesis.speak(utterance);
}

// Check Model Status
async function checkModelStatus() {
  try {
    const res = await fetch('/api/model-info');
    if (!res.ok) return;
    const info = await res.json();
    const textEl = document.getElementById('headerStatusText');
    if (info.is_model_loaded) {
      if (textEl) textEl.innerText = 'Operational (48 Classes)';
    } else {
      if (textEl) textEl.innerText = 'Awaiting Weights';
    }
  } catch (err) {
    console.warn("Could not check model status:", err);
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
    badge.className = 'status-badge badge-danger';
    if (badgeIcon) badgeIcon.innerHTML = SVG_ICONS.clock;
    if (badgeText) badgeText.innerText = 'Weights Pending';
  }

  document.getElementById('confidenceValue').innerText = '0.0%';
  document.getElementById('cropNameDisplay').innerText = 'Model Offline';
  document.getElementById('diseaseNameDisplay').innerText = 'Awaiting best_agroguard_model.pth';
  document.getElementById('pathogenDisplay').innerText = 'Please place trained weights in project root';

  const list = document.getElementById('symptomsList');
  list.innerHTML = `
    <li>Place <b>best_agroguard_model.pth</b> directly into the project folder.</li>
    <li>The server will automatically detect the weights and activate AI diagnosis.</li>
  `;

  const chemSec = document.getElementById('chemicalSection');
  if (chemSec) chemSec.style.display = 'none';
  const orgSec = document.getElementById('organicSection');
  if (orgSec) orgSec.style.display = 'none';
  const prevSec = document.getElementById('preventionSection');
  if (prevSec) prevSec.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', checkModelStatus);
