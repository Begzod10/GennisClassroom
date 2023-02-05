const navItems = document.querySelectorAll(".subject-nav__content-title")


navItems.forEach(item => {
    item.addEventListener("click", () => {
        const parent = item.parentElement.querySelector(".subject-nav__content-container")
        if (item.classList.contains("active")) {
            item.classList.remove("active")
            parent.style.height = 0 + "px"
        } else {
            parent.style.height = parent.scrollHeight + "px"
            item.classList.add("active")
        }

    })
})

const variant = document.querySelectorAll(".var");
const inp = document.querySelectorAll(".inp");

variant.forEach((item,index) => {
    item.addEventListener("change", () => {
        inp[index].value = item.dataset.id
    })
})
console.log(variant)