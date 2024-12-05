document.addEventListener("DOMContentLoaded", function() {
  const video = document.querySelector("#video");
  const link_button = document.getElementById('link-button');

    // Registro del componente A-Frame
    AFRAME.registerComponent('mytarget', {
      init: function () {
        this.el.addEventListener('targetFound', () => {
          video.play();  // Reproduce el video
        });
        
        this.el.addEventListener('targetLost', () => {
          video.pause();  // Pausa el video
          video.currentTime = 0; // Reinicia el video (opcional)
        });
      }
    });

    // Mostrar el botón cuando el video termine por primera vez
    video.addEventListener('ended', function () {
      link_button.style.display = 'block';
      video.loop = true;
    });


});
