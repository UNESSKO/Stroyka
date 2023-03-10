//CONST
const reqFormCont = document.getElementById("request_form_container");
const reqForm = document.getElementById("request_form");
const reqFormButton = document.querySelectorAll('.request-button');
const slides = document.querySelectorAll(".carousel-item");
const button = document.querySelectorAll(".carousel-button");
const reviewsCarousel = document.querySelector(".reviews-carousel")
const reviewsList = document.querySelector(".reviews-list")
const plusReview = document.querySelector(".plus-review")
const formReview = document.querySelector(".review-form-wrap")
//VARIABLES
let current = Math.floor(Math.random()*slides.length);
let prev = current > 0 ? current - 1 : slides.length - 1;
let next = current < slides.length - 1 ? current + 1 : 0;
//SHOW-HIDE Elements
function show(id) {
    document.getElementById(id).classList.remove("hidden")
}
function hide(id) {
    document.getElementById(id).classList.add("hidden")
}
//CAROUSEL
const update = () => {
    slides.forEach(it => {
        it.classList.remove("active");
        it.classList.remove("prev");
        it.classList.remove("next");
    });

    slides[current].classList.add("active");
    slides[prev].classList.add("prev");
    slides[next].classList.add("next");
}
for (let i = 0; i < button.length; i++) {
    button[i].addEventListener("click", () => i === 0 ? gotoPrev() : gotoNext());
}
const gotoPrev = () => current > 0 ? gotoNum(current - 1) : gotoNum(slides.length - 1);
const gotoNext = () => current < slides.length - 1 ? gotoNum(current + 1) : gotoNum(0);
const gotoNum = number => {
    current = number;
    prev = current > 0 ? current - 1 : slides.length - 1;
    next = current < slides.length - 1 ? current + 1 : 0;
    update();
}
update();
//REVIEWS
const scrollReviews = () => {
    let windowWidth = document.documentElement.clientWidth;
    let reviewsWindowCount = Math.floor((windowWidth-250)/350);
    if (reviewsWindowCount > 5) {reviewsWindowCount = 5}
    reviewsCarousel.style.width = reviewsWindowCount * 374 - 24 + 'px';
    if (reviewsWindowCount % 2 === 0) {
        reviewsList.querySelectorAll (".review").forEach((e) => e.style.scrollSnapAlign = 'start');
    }
    else {
        reviewsList.querySelectorAll (".review").forEach((e) => e.style.scrollSnapAlign = 'center' );
    }
    reviewsCarousel.scrollTo(((reviewsList.offsetWidth/2)-((reviewsWindowCount/2)*364)), 0);
    plusReview.style.height = reviewsList.querySelector("figure").querySelector("blockquote").clientHeight +'px';
}
scrollReviews()
//Reviews carousel resize
window.addEventListener('resize', (e) => {
    scrollReviews();
});
//Add review
document.querySelector(".plus-review").addEventListener( 'click', (e) => {
    plusReview.classList.add("hidden");
    formReview.classList.remove("hidden");

})
//Modal window closing listener
document.addEventListener( 'click', (e) => {
    let checkClickPosition = false;
    for (let i =0; i < reqFormButton.length; i++)
    {
        if (e.composedPath().includes(reqFormButton[i]))
        {
            checkClickPosition = true;
            break;
        }
    }
    if (!reqFormCont.classList.contains("hidden") && !e.composedPath().includes(reqForm) && checkClickPosition === false)
    {
        hide(reqFormCont.id)
    }
})