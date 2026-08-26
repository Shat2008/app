document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const slides = document.querySelectorAll(".slide");
    const prevButton = document.querySelector(".prev");
    const nextButton = document.querySelector(".next");

    if (!slider || slides.length === 0 || !prevButton || !nextButton) {
        console.error("Один или несколько элементов не найдены!");
        return;
    }

    let currentIndex = 0;

    function showSlide(index) {
        if (index < 0) {
            currentIndex = slides.length - 1;
        } else if (index >= slides.length) {
            currentIndex = 0;
        } else {
            currentIndex = index;
        }
        slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    prevButton.addEventListener("click", () => {
        showSlide(currentIndex - 1);
    });

    nextButton.addEventListener("click", () => {
        showSlide(currentIndex + 1);
    });

    setInterval(() => {
        showSlide(currentIndex + 1);
    }, 3000);
});