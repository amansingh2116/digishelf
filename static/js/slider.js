document.addEventListener('DOMContentLoaded', function() {
    console.log('Slider script loaded');
    
    // Slider functionality
    const sliderContainer = document.querySelector('.slider-container');
    const slides = document.querySelectorAll('.slide');
    const dotsContainer = document.querySelector('.slide-dots');
    const prevBtn = document.querySelector('.prev-slide');
    const nextBtn = document.querySelector('.next-slide');
    
    console.log('Slider elements:', {
        sliderContainer: !!sliderContainer,
        slides: slides.length,
        dotsContainer: !!dotsContainer,
        prevBtn: !!prevBtn,
        nextBtn: !!nextBtn
    });
    
    if (!sliderContainer || !dotsContainer || !prevBtn || !nextBtn || slides.length === 0) {
        console.error('Slider elements not found');
        return; // Exit if elements don't exist
    }
    
    let currentIndex = 0;
    let slideInterval;
    const slideDuration = 5000; // 5 seconds
    
    // Clear any existing dots first
    dotsContainer.innerHTML = '';
    
    // Create dots
    slides.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    // Initialize slider with proper display style
    function updateSlider() {
        console.log('Updating slider to index:', currentIndex);
        
        // Hide all slides first
        slides.forEach(slide => {
            slide.style.display = 'none';
        });
        
        // Show only the current slide
        if (slides[currentIndex]) {
            slides[currentIndex].style.display = 'block';
            console.log('Set slide to display:block');
        }
        
        // Update dots
        document.querySelectorAll('.slide-dots .dot').forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Go to specific slide
    function goToSlide(index) {
        currentIndex = (index + slides.length) % slides.length;
        updateSlider();
        resetInterval();
    }
    
    // Next slide
    function nextSlide() {
        goToSlide(currentIndex + 1);
    }
    
    // Previous slide
    function prevSlide() {
        goToSlide(currentIndex - 1);
    }
    
    // Auto slide
    function startInterval() {
        clearInterval(slideInterval); // Clear any existing interval first
        slideInterval = setInterval(nextSlide, slideDuration);
        console.log('Started auto-sliding interval');
    }
    
    // Reset interval when user interacts
    function resetInterval() {
        clearInterval(slideInterval);
        startInterval();
    }
    
    // Event listeners
    nextBtn.addEventListener('click', () => {
        console.log('Next button clicked');
        nextSlide();
    });
    
    prevBtn.addEventListener('click', () => {
        console.log('Previous button clicked');
        prevSlide();
    });
    
    // Pause on hover
    sliderContainer.addEventListener('mouseenter', () => {
        clearInterval(slideInterval);
        console.log('Slider hover - paused interval');
    });
    
    sliderContainer.addEventListener('mouseleave', () => {
        startInterval();
        console.log('Slider exit - resumed interval');
    });
    
    // Touch support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    sliderContainer.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
        clearInterval(slideInterval);
    }, {passive: true});
    
    sliderContainer.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
        startInterval();
    }, {passive: true});
    
    function handleSwipe() {
        const difference = touchStartX - touchEndX;
        if (difference > 50) { // Swipe left
            nextSlide();
        } else if (difference < -50) { // Swipe right
            prevSlide();
        }
    }
    
    // Force the first slide to be visible on load
    slides.forEach((slide, index) => {
        slide.style.display = index === 0 ? 'block' : 'none';
    });
    
    // Initial setup
    updateSlider(); // Set the initial slide
    startInterval(); // Start auto-sliding
    
    console.log('Slider initialized successfully');
});