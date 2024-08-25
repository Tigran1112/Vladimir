let slideIndex = 0;
const slides = document.querySelectorAll('.gallery-slide');
const totalSlides = slides.length;

function showSlide(index) {
    if (index >= totalSlides) slideIndex = 0;
    if (index < 0) slideIndex = totalSlides - 1;
    const offset = -slideIndex * 100;
    document.querySelector('.gallery-slides').style.transform = `translateX(${offset}%)`;
}

function changeSlide(step) {
    slideIndex += step;
    showSlide(slideIndex);
}

function autoSlide() {
    slideIndex++;
    showSlide(slideIndex);
    setTimeout(autoSlide, 10000); // 10 секунд
}

autoSlide(); // Запуск автоперелистывания