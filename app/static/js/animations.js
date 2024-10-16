document.addEventListener('DOMContentLoaded', function() {
    const lottieButtons = document.querySelectorAll('.btn-lottie');
    
    lottieButtons.forEach(button => {
      const animation = lottie.loadAnimation({
        container: button.querySelector('.button-lottie'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'https://assets9.lottiefiles.com/packages/lf20_1pxqjqps.json'
      });
  
      button.addEventListener('mouseover', function() {
        animation.play();
      });
  
      button.addEventListener('mouseleave', function() {
        animation.stop();
      });
    });
  });
  