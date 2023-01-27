function getSelectionText() {
    let text = "";
    if (window.getSelection) {
        text = window.getSelection().toString();
    } else if (document.selection && document.selection.type != "Control") {
        text = document.selection.createRange().text;
    }
    return text;
}
const p = document.querySelector(".desc")

p.addEventListener('contextmenu', (event) => {
    event.preventDefault()
    activeMenu()
    const modal = document.querySelector(".modal")

    modal.querySelector("textarea").value = getSelectionText()

})






// function createWords(text) {
//
//     const words = text.split(/\s+/g)
//
//     for (let i = 0; i < words.length; i++) {
//         if (!containsSpecialChars(words[i])) {
//             p.innerHTML += `<span class="word">${words[i]}</span>`
//         } else {
//             p.innerHTML += `<span class="character">${words[i]}</span>`
//         }
//     }
//
//     const spans = document.querySelectorAll(".word")
//     spans.forEach(item => {
//         item.addEventListener("contextmenu",() => {
//             console.log(item.innerHTML)
//             activeMenu()
//         })
//     })
//
// }

//
// function containsSpecialChars(str) {
//     const specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
//
//     return specialChars.split('').some(specialChar => {
//         return !!str.includes(specialChar);
//     });
// }
//
function activeMenu() {
    // let e = window.event
    const modal = document.querySelector(".modal")
    modal.classList.add("active")
}
function deActiveMenu() {
    const modal = document.querySelector(".modal")
    modal.classList.remove("active")
}



// createWords(text)

