const iconMenu = document.querySelector('.menu__icon');

if (iconMenu) {
    const menuBody = document.querySelector('.menu__body');
    iconMenu.addEventListener("click", (e) => {
        document.body.classList.toggle("_lock");
        iconMenu.classList.toggle("_active");
        menuBody.classList.toggle("_active");
    });
}

const swiperWelcome = new Swiper('.slider-welcome', {
    centeredSlides: true,
    effect: "fade",
    loop: true,
    autoplay: {
        delay: 8000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.slider-welcome__pagination.swiper-pagination',
        clickable: true,
        renderBullet: function (index, className) {
            return `<span class="${className}"></span>`;
        },
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

const swiperReviews = new Swiper('.slider-reviews', {
    spaceBetween: 30,
    centeredSlides: true,
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".slider-reviews__arrow.swiper-button-next",
        prevEl: ".slider-reviews__arrow.swiper-button-prev",
    },
});