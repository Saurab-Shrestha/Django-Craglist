const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector("#menu");

hamburger.addEventListener("click",()=>{
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
})


