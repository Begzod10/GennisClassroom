let subjects = [];


const renderSubjects = (subjects) => {
    const subjectsWrapper = document.querySelector(".courses__item-container")

    subjectsWrapper.innerHTML = ""

    for (let i = 0; i < subjects.length; i++) {

        const active = subjects[i].checked ? `${"opacity:" + 1}` : null

        const elem = `<div class="courses__item-container__item">
                            <img src=${subjects[i].img} alt="">
                            <h1>${subjects[i].title}</h1>
                            <div style=${active}  class="checked">
                                <i class="fa-solid fa-check"></i>
                            </div>
                        </div>`

        subjectsWrapper.innerHTML += elem
    }


    const elems = document.querySelectorAll(".courses__item-container__item")


    elems.forEach((item, index) => {
        item.addEventListener("click", () => {
            subjects = subjects.map((subject, i) => {
                if (i === index) {
                    if (subject.checked) {
                        return {...subject, checked: false}
                    }
                    return {...subject, checked: true}
                }
                return subject
            })
            renderSubjects(subjects)
            renderSelectedSubjects(subjects)
        })
    })

}


const renderSelectedSubjects = (subjects) => {


    const selectedSubjects = document.querySelector(".courses__selected-container")


    selectedSubjects.innerHTML = ""
    for (let i = 0; i < subjects.length; i++) {

        if (subjects[i].checked) {
            const elem = `<div class="courses__selected-item"  data-id=${subjects[i].id}>
                        ${subjects[i].title}
                        <div class="delSelected"  ><i class="fa-solid fa-xmark"></i></div>
                    </div>`

            selectedSubjects.innerHTML += elem
        }

    }


    const elems = document.querySelectorAll(".courses__selected-item")


    elems.forEach((item, index) => {
        item.addEventListener("click", () => {

            const itemId = item.getAttribute("data-id")

            subjects = subjects.map((subject) => {
                if (subject.id === +itemId) {
                    if (subject.checked) {
                        return {...subject, checked: false}
                    }
                    return {...subject, checked: true}
                }
                return subject
            })

            renderSubjects(subjects)
            renderSelectedSubjects(subjects)
        })
    })

}

renderSubjects(subjects)
renderSelectedSubjects(subjects)


async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        }, body: JSON.stringify({data}) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}


const submit = document.querySelector(".submit")

submit.addEventListener("click", () => {

    fetch("/receive_subjects/", {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        body: JSON.stringify({
            "subjects": subjects
        }), headers: {
            'Content-Type': 'application/json'
        },
    })
    window.location.href = 'http://127.0.0.1:5000/my_subjects/';

})


fetch("/get_subjects/", {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    headers: {
        'Content-Type': 'application/json'
    },
})
    .then(res => res.json())
    .then(res => {
        subjects = res.subjects
        renderSubjects(subjects)
        renderSelectedSubjects(subjects)
    })

