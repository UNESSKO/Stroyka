const reqFormCont = document.getElementById("request_form_container");
const reqForm = document.getElementById("request_form");
const reqFormButton = document.querySelectorAll('.request-button');

function show(id) {
    document.getElementById(id).classList.remove("hidden")
}
function hide(id) {
    document.getElementById(id).classList.add("hidden")
}

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