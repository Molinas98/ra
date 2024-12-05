document.addEventListener("DOMContentLoaded", function() {
  const btn_aceptar = document.getElementById('aceptar');
  const overlay = document.querySelector('.overlay');
  const mensaje = document.querySelector('.mensaje');

  btn_aceptar.addEventListener('click', function() {
    overlay.remove();
    mensaje.remove();
  });
});
