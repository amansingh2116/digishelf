document.addEventListener('DOMContentLoaded', function() {
  const slider = document.querySelector('.slider');
  const slides = document.querySelectorAll('.slide');
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');
  let currentSlide = 0;
  const totalSlides = slides.length;

  function updateSlider() {
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
  }

  prevBtn.addEventListener('click', () => {
    currentSlide = (currentSlide > 0) ? currentSlide - 1 : totalSlides - 1;
    updateSlider();
  });

  nextBtn.addEventListener('click', () => {
    currentSlide = (currentSlide < totalSlides - 1) ? currentSlide + 1 : 0;
    updateSlider();
  });

  // Auto-slide (optional)
  setInterval(() => {
    currentSlide = (currentSlide < totalSlides - 1) ? currentSlide + 1 : 0;
    updateSlider();
  }, 5000);
});