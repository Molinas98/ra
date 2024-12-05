document.addEventListener("DOMContentLoaded", function() {
  const dropZone = document.getElementById('dropZone_imagen');
  const inputImagen = document.getElementById('imagen');
  const dropZone_video = document.getElementById('dropZone_video');
  const inputVideo = document.getElementById('video');

  // Funciones para imágenes
  dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone.classList.add('dragover');
  });

  dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');
  });

  dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');

    if (e.dataTransfer && e.dataTransfer.files.length) {
      inputImagen.files = e.dataTransfer.files;
      handleImage(e.dataTransfer.files[0]);
    }
  });

  inputImagen.addEventListener('change', function() {
    handleImage(this.files[0]);
  });

  function handleImage(file) {
    const reader = new FileReader();
    reader.onload = function() {
      document.getElementById('imagenIcono').src = ''; // Resetear ícono
      document.getElementById('nombre_imagen').innerHTML = file.name;
    };
    reader.readAsDataURL(file);
  }

  // Funciones para videos
  dropZone_video.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone_video.classList.add('dragover');
  });

  dropZone_video.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone_video.classList.remove('dragover');
  });

  dropZone_video.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone_video.classList.remove('dragover');

    if (e.dataTransfer && e.dataTransfer.files.length) {
      inputVideo.files = e.dataTransfer.files;
      handleVideo(e.dataTransfer.files[0]);
    }
  });

  inputVideo.addEventListener('change', function() {
    handleVideo(this.files[0]);
  });

  function handleVideo(file) {
    const reader = new FileReader();
    reader.onload = function() {
      document.getElementById('videoIcono').src = ''; // Resetear ícono
      document.getElementById('nombre_video').innerHTML = file.name;
    };
    reader.readAsDataURL(file);
  }
});
