const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("file-input");
const fileNameDisplay = document.getElementById("file-name");
const browseBtn = document.getElementById("browse-btn");
const form = document.getElementById("upload-form");
const resultBox = document.getElementById("result-box");

// Drag over effect
dropZone.addEventListener("dragover", function (e) {
  e.preventDefault();
  dropZone.classList.add("dragover");
});

// Remove drag effect
dropZone.addEventListener("dragleave", function () {
  dropZone.classList.remove("dragover");
});

// Drop file into input
dropZone.addEventListener("drop", function (e) {
  e.preventDefault();
  dropZone.classList.remove("dragover");

  const files = e.dataTransfer.files;
  if (files.length > 0) {
    fileInput.files = files;
    fileNameDisplay.innerText = `📄 ${files[0].name}`;
  }
});

// Browse button triggers file input
browseBtn.addEventListener("click", function () {
  fileInput.click();
});

// Show selected file name
fileInput.addEventListener("change", function () {
  if (fileInput.files.length > 0) {
    fileNameDisplay.innerText = `📄 ${fileInput.files[0].name}`;
  }
});

// Handle form submit via JS (prevent full refresh)
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const formData = new FormData(form);

  fetch("/predict", {
    method: "POST",
    body: formData
  })
    .then(response => response.text())
    .then(data => {
      resultBox.innerHTML = data;
    })
    .catch(error => {
      resultBox.innerHTML = `<span style="color: red;">❌ Error: ${error}</span>`;
    });
});
