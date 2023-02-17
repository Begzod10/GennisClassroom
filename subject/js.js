const hamburger = document.querySelector("#hamburger"),
    navbar = document.querySelector(".subject-nav"),
    subject = document.querySelector("#subject"),
    menuList = document.querySelector(".menu-list"),
    questions = document.querySelector("#questions"),
    questionSection = document.querySelector(".question"),
    subjectVideo = document.querySelector(".subject-video"),
    createQuestionBtn = document.querySelector(".create-question-btn"),
    createQuestionSection = document.querySelector(".create-question");

hamburger.addEventListener('click', () => {
    navbar.classList.toggle("active-nav")
})
subject.addEventListener("click", () => {
    menuList.classList.toggle("list-active")
})
questions.addEventListener("click", () => {
    subjectVideo.classList.toggle("active-video")
    questionSection.classList.toggle("question-active")
})
createQuestionBtn.addEventListener("click",()=>{
    createQuestionSection.classList.add("active-create");
    questionSection.classList.remove("question-active")
})