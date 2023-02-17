const navbar = document.querySelector("#subject"),
    hamburger = document.querySelector("#hamburger");
hamburger.addEventListener("click", () => {
    navbar.classList.toggle("active")
})
