//CONST
const reqFormCont = document.getElementById("request_form_container");
const reqForm = document.getElementById("request_form");
const reqFormButton = document.querySelectorAll('.request-button');
const slider = document.querySelector(".carousel");
const slides = document.querySelectorAll(".carousel-item");
const button = document.querySelectorAll(".carousel-button");
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
//Modal window closing listner
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