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

    modal.querySelector("textarea").innerHTML = getSelectionText()
})

let mistakes = []
const inputSubmit = document.querySelector("#input-submit"), inputAnswer = document.querySelector("#input-answer"),
    inputComment = document.querySelector("#input-comment")

const essay_id = inputSubmit.getAttribute("data-essayId")

fetch(`/get_essay_errors/${essay_id}`, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.

    headers: {
        'Content-Type': 'application/json'
    },
})
    .then(res => res.json())
    .then(res => {
        console.log(res)
        mistakes = res.error_list.map((item, index) => {
            return {...item, id: index + 1}
        })
        checkMistake(mistakes)
    })


function checkMistake(mistakes) {
    const modal = document.querySelector(".modal")

    mistakes.map(item => {
        p.innerHTML = p.innerHTML.replace(item.mistake, `<div class="checked" data-id=${item.id}>${item.mistake}
                            <div>
                                <div class="mistake">
                                    ${item.mistake}
                                </div>
                                <div class="answer">
                                    ${item.answer}
                                </div>
                                <div class="comment">
                                     ${item.comment}
                                </div>
                                <div class="btns">
                                    <div class="btns__item accept" data-id=${item.id}>accept</div>
                                    <div class="btns__item dismiss" data-id=${item.id}>dismiss</div>
                                </div>
                            </div>
                        </div>`)
    })

    acceptClick(mistakes)
    dismissClick(mistakes)


}

inputSubmit.addEventListener("click", (e) => {
    e.preventDefault()

    const modal = document.querySelector(".modal")

    const elem = {
        id: mistakes.length + 1,
        mistake: modal.querySelector("textarea").value,
        answer: inputAnswer.value,
        comment: inputComment.value,
        mistake_type: modal.querySelector("#select-type").value
    }

    p.innerHTML = p.innerHTML.replace(modal.querySelector("textarea").value, `<div class="checked" data-id=${mistakes.length + 1}>${modal.querySelector("textarea").value}
                        <div>
                            <div class="mistake">
                                ${modal.querySelector("textarea").value}
                            </div>
                            <div class="answer">
                                ${inputAnswer.value}
                            </div>
                            <div class="comment">
                                 ${inputComment.value}
                            </div>
                            <div class="btns">
                                <div class="btns__item accept" data-id=${mistakes.length + 1}>accept</div>
                                <div class="btns__item dismiss" data-id=${mistakes.length + 1}>dismiss</div>
                            </div>
                        </div>
                    </div>`)
    mistakes.push(elem)

    acceptClick(mistakes)
    dismissClick(mistakes)


    fetch("/send_errors/" + essay_id, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        body: JSON.stringify({
            "mistake": elem
        }), headers: {
            'Content-Type': 'application/json'
        },
    })

    modal.classList.remove("active")


})


function acceptClick(currentMistakes) {

    const buttons = document.querySelectorAll(".accept")
    const pChecked = p.querySelectorAll(".checked")
    buttons.forEach(item => {
        item.addEventListener("click", () => {
            const id = item.getAttribute("data-id")
            const filteredMistake = currentMistakes.filter(mis => mis.id === +id)


            pChecked.forEach(check => {
                const checkId = check.getAttribute("data-id")
                if (checkId === id) {
                    p.innerHTML = p.innerHTML.replace(check.outerHTML, filteredMistake[0].answer)
                }
            })

            mistakes = currentMistakes.filter(miss => miss.id !== +id)


            acceptClick(mistakes)
        })
    })


}

function dismissClick(currentMistakes) {
    const buttons = document.querySelectorAll(".dismiss")
    const pChecked = p.querySelectorAll(".checked")
    buttons.forEach(item => {
        item.addEventListener("click", () => {
            const id = item.getAttribute("data-id")
            const filteredMistake = currentMistakes.filter(mis => mis.id === +id)


            pChecked.forEach(check => {
                const checkId = check.getAttribute("data-id")
                if (checkId === id) {
                    p.innerHTML = p.innerHTML.replace(check.outerHTML, filteredMistake[0].mistake)
                }
            })

            mistakes = currentMistakes.filter(miss => miss.id !== +id)

            dismissClick(mistakes)

        })
    })
}


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

function activeMenu() {
    // let e = window.event
    const modal = document.querySelector(".modal")
    modal.classList.add("active")
}

const modal = document.querySelector(".modal")


modal.addEventListener("click", (e) => {
    if (e.target.classList.contains("modal")) {
        modal.classList.remove("active")
    }
})


// createWords(text)

