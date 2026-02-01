// Get DOM elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const uploadSection = document.getElementById('uploadSection');
const processingSection = document.getElementById('processingSection');
const resultSection = document.getElementById('resultSection');
const errorSection = document.getElementById('errorSection');
const originalImage = document.getElementById('originalImage');
const resultImage = document.getElementById('resultImage');
const downloadBtn = document.getElementById('downloadBtn');
const newImageBtn = document.getElementById('newImageBtn');
const tryAgainBtn = document.getElementById('tryAgainBtn');
const errorMessage = document.getElementById('errorMessage');

let processedImageBlob = null;
let originalFileName = '';
let currentImageUrl = null;

// Drag and drop handlers
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
});

// Click to upload
uploadArea.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
    }
});

// Handle file upload and processing
async function handleFile(file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
        showError('Please upload an image file (PNG, JPG, JPEG)');
        return;
    }
    
    // Validate file size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
        showError('File size must be less than 10MB');
        return;
    }
    
    originalFileName = file.name;
    
    // Show original image
    const reader = new FileReader();
    reader.onload = (e) => {
        originalImage.src = e.target.result;
    };
    reader.readAsDataURL(file);
    
    // Show processing state
    showSection(processingSection);
    
    // Upload and process
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/api/remove-background', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to process image');
        }
        
        // Get the processed image
        processedImageBlob = await response.blob();
        
        // Revoke previous URL if exists to prevent memory leak
        if (currentImageUrl) {
            URL.revokeObjectURL(currentImageUrl);
        }
        
        currentImageUrl = URL.createObjectURL(processedImageBlob);
        resultImage.src = currentImageUrl;
        
        // Show result
        showSection(resultSection);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Failed to process image. Please try again.');
    }
}

// Download result
downloadBtn.addEventListener('click', () => {
    if (processedImageBlob) {
        const url = URL.createObjectURL(processedImageBlob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `no-bg-${originalFileName.replace(/\.[^/.]+$/, '')}.png`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
});

// Try another image
newImageBtn.addEventListener('click', () => {
    resetUpload();
});

// Try again button
tryAgainBtn.addEventListener('click', () => {
    resetUpload();
});

// Show specific section
function showSection(section) {
    uploadSection.style.display = 'none';
    processingSection.style.display = 'none';
    resultSection.style.display = 'none';
    errorSection.style.display = 'none';
    
    section.style.display = 'block';
}

// Show error
function showError(message) {
    errorMessage.textContent = message;
    showSection(errorSection);
}

// Reset upload
function resetUpload() {
    fileInput.value = '';
    processedImageBlob = null;
    originalFileName = '';
    
    // Revoke object URL to free memory
    if (currentImageUrl) {
        URL.revokeObjectURL(currentImageUrl);
        currentImageUrl = null;
    }
    
    showSection(uploadSection);
}

// Prevent default drag and drop on the whole page
document.addEventListener('dragover', (e) => {
    e.preventDefault();
});

document.addEventListener('drop', (e) => {
    e.preventDefault();
});
