import requests

from app import *
from backend.basics.models import *
from backend.lessons.models import *
from werkzeug.utils import secure_filename
from backend.basics.settings import *
from datetime import datetime

headers = {
    'Content-type': 'application/json'

}


# Copyleaks.set_identity_uri("88e15773-2877-4e58-965e-71625684c962")

def subject_folder():
    upload_folder = 'static/img/subject_img'
    return upload_folder


def lesson_folder():
    upload_folder = 'static/img/lesson_img'
    return upload_folder


def question_folder():
    upload_folder = 'static/img/question'
    return upload_folder


def answer_folder():
    upload_folder = 'static/img/answer'
    return upload_folder


def checkFile(filename):
    value = '.' in filename
    type_file = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    return value and type_file


@app.route("/subject", methods=["GET", "POST"])
def subject():
    myobj = json.dumps({'email': 'rimefara22@gmail.com', 'key': '88e15773-2877-4e58-965e-71625684c962'})
    response = requests.post('https://id.copyleaks.com/v3/account/login/api', headers=headers, data=myobj)

    print(response)
    if request.method == "POST":
        subject = request.form.get("subject")
        photo = request.files['file']
        folder = subject_folder()
        if photo and checkFile(photo.filename):
            photo_file = secure_filename(photo.filename)
            photo_url = "/" + folder + "/" + photo_file
            app.config['UPLOAD_FOLDER'] = folder
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
            add = Subject(name=subject, img=photo_url)
            db.session.add(add)
            db.session.commit()
    return render_template("creat/subject.html")


@app.route("/types", methods=["GET", "POST"])
def types():
    if request.method == "POST":
        name = request.form.get("name")
        add = ExerciseTypes(name=name)
        db.session.add(add)
        db.session.commit()
    return render_template("creat/types.html")


@app.route("/choose_lesson", methods=["GET", "POST"])
def choose_lesson():
    lesson = Lesson.query.all()

    return render_template("creat/choose lesson.html", lesson=lesson)


@app.route("/exercise/<int:lesson_id>", methods=["GET", "POST"])
def exercise(lesson_id):
    types = ExerciseTypes.query.all()
    # level = SubjectLevel.query.all()
    return render_template("creat/exercise.html", types=types, lesson_id=lesson_id)


@app.route("/fetch_exercise", methods=["GET", "POST"])
def fetch_exercise():
    result = request.get_json()['result']
    for item in result:
        type_id = item["type_id"]
        desc = item["desc"]
        add = Exercise(desc=desc, type_id=type_id)
        db.session.add(add)
        db.session.commit()
    return True


@app.route("/creat_level", methods=["GET", "POST"])
def creat_level():
    if request.method == "POST":
        name = request.form.get("name")
        subject_id = request.form.get("subject")
        add = SubjectLevel(name=name, subject_id=subject_id)
        db.session.add(add)
        db.session.commit()
    subject = Subject.query.all()
    return render_template("creat/creat_level.html", subject=subject)


@app.route("/test/", methods=["POST"])
def test():
    test = request.get_json()['list']
    # level_id = SubjectLevel.qury.filter(SubjectLevel.id == level_id).first()
    for item in test:
        question = item["question"]
        variants = item["variants"]
        type = item["type"]
        lesson_id = item["lesson_id"]
        lesson = Lesson.query.filter(Lesson.id == lesson_id).first()
        addquestions = Exercise(desc=question, level_id=lesson.level_id,
                                subject_id=lesson.subject_id, type_id=type, lesson_id=lesson_id)
        db.session.add(addquestions)
        db.session.commit()
        for var in variants:
            variant = var["value"]
            checked = var["checked"]
            addvariants = ExerciseAnswers(desc=variant, answer=checked, level_id=lesson.level_id,
                                          subject_id=lesson.subject_id, exercise_id=addquestions.id, type_id=type,
                                          lesson_id=lesson_id)
            db.session.add(addvariants)
            db.session.commit()
    return jsonify({
        'success': True
    })


@app.route("/lesson_home", methods=["GET", "POST"])
def lesson_home():
    return render_template("creat/home.html")


@app.route("/choose_subject_lesson", methods=["GET", "POST"])
def choose_subject_lesson():
    subjects = Subject.query.all()
    return render_template("creat/choose_subject_lesson.html", subjects=subjects)


@app.route("/choose_level_lesson/<int:subject_id>", methods=["GET", "POST"])
def choose_level_lesson(subject_id):
    levels = SubjectLevel.query.filter(SubjectLevel.subject_id == subject_id).order_by(SubjectLevel.id)
    return render_template("creat/choose_level_lesson.html", levels=levels)


@app.route("/lesson/<int:level_id>", methods=["GET", "POST"])
def lesson(level_id):
    types = ExerciseTypes.query.all()
    level_id = SubjectLevel.query.filter(SubjectLevel.id == level_id).first()
    if request.method == "POST":
        type_id = request.form.get("type")
        title = request.form.get("title")
        desc = request.form.get("desc")
        photo = request.files["img"]
        folder = lesson_folder()
        if photo and checkFile(photo.filename):
            photo_file = secure_filename(photo.filename)
            photo_url = "/" + folder + "/" + photo_file
            app.config['UPLOAD_FOLDER'] = folder
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
            add = Lesson(title=title, desc=desc, img=photo_url, level_id=level_id.id, subject_id=level_id.subject_id,
                         type_id=type_id)
            db.session.add(add)
            db.session.commit()
    return render_template("creat/lesson.html", level_id=level_id, types=types)


@app.route("/filter_list_subject", methods=["GET", "POST"])
def filter_list_subject():
    subjects = Subject.query.all()
    return render_template("creat/filter_list_subject.html", subjects=subjects)


@app.route("/filter_list_level/<int:subject_id>", methods=["GET", "POST"])
def filter_list_level(subject_id):
    levels = SubjectLevel.query.filter(SubjectLevel.subject_id == subject_id).order_by(SubjectLevel.id)
    return render_template("creat/filter_list_level.html", levels=levels)


@app.route("/filter_list/<int:level_id>", methods=["GET", "POST"])
def filter_list(level_id):
    lessons = Lesson.query.filter(Lesson.level_id == level_id).order_by(Lesson.id)
    return render_template("creat/filter_list.html", lessons=lessons)


@app.route('/student_question', methods=["GET", "POST"])
def student_question():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    subject = Subject.query.all()
    try:
        if request.method == "POST":
            question = request.form.get("question")
            sub_id = request.form.get("sub_id")
            photo = request.files['photo']
            date = datetime.now()
            folder = question_folder()
            if photo and checkFile(photo.filename):
                photo_file = secure_filename(photo.filename)
                photo_url = "/" + folder + "/" + photo_file
                app.config['UPLOAD_FOLDER'] = folder
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
                add = StudentQuestion(question=question, img=photo_url, date=date, student_id=student.id,
                                      subject_id=sub_id)
                db.session.add(add)
                db.session.commit()
            return redirect(url_for('student_question'))
    except AttributeError:
        return redirect(url_for("login"))

    student_questions = StudentQuestion.query.filter(StudentQuestion.student_id == student.id).order_by(
        StudentQuestion.id).all()
    questions = StudentQuestion.query.filter(StudentQuestion.student_id == student.id).order_by(StudentQuestion.id)
    return render_template("question_answer/student_question.html", student_questions=student_questions,
                           student=student, questions=questions, subject=subject)

    # if request.method == "POST":
    #     question = request.form.get("question")
    #     photo = request.files['photo']
    #     date = datetime.now()
    #     folder = question_folder()
    #     if photo and checkFile(photo.filename):
    #         photo_file = secure_filename(photo.filename)
    #         photo_url = "/" + folder + "/" + photo_file
    #         app.config['UPLOAD_FOLDER'] = folder
    #         photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
    #         add = StudentQuestion(question=question, img=photo_url, date=date)
    #         db.session.add(add)
    #         db.session.commit()
    #     return redirect(url_for('student_question'))
    # student = StudentQuestion.query.filter(StudentQuestion.student_id == student_id).order_by(StudentQuestion.id)
    # return render_template("question_answer/student_question.html", student=student)

    # try:
    #     user = get_current_user()
    #     student = Student.query.filter(Student.user_id == user.id).first()
    #
    #     if request.method == "POST":
    #         question = request.form.get("question")
    #         photo = request.files['photo']
    #         date = datetime.now()
    #         folder = question_folder()
    #         if photo and checkFile(photo.filename):
    #             photo_file = secure_filename(photo.filename)
    #             photo_url = "/" + folder + "/" + photo_file
    #             app.config['UPLOAD_FOLDER'] = folder
    #             photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
    #             add = StudentQuestion(question=question, img=photo_url, date=date)
    #             db.session.add(add)
    #             db.session.commit()
    #         return redirect(url_for('student_question'))
    # except AttributeError:
    #     return render_template("login.html")
    # student_questions = StudentQuestion.query.filter(StudentQuestion.student_id == student.id).order_by(
    #     StudentQuestion.id).all()
    # return render_template("question_answer/student_question.html", student_questions=student_questions,
    #                        student=student)


@app.route('/question_answer/<int:question_id>', methods=["GET", "POST"])
def question_answer(question_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    question = StudentQuestion.query.filter(StudentQuestion.id == question_id).first()
    if request.method == "POST":
        answer = request.form.get("answer")
        photo = request.files['photo']
        date = datetime.now()
        folder = answer_folder()
        if photo and checkFile(photo.filename):
            photo_file = secure_filename(photo.filename)
            photo_url = "/" + folder + "/" + photo_file
            app.config['UPLOAD_FOLDER'] = folder
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
            add = QuestionAnswers(answer=answer, img=photo_url, date=date, user_id=student.id, question_id=question_id,
                                  subject_id=question.subject_id)
            db.session.add(add)
            db.session.commit()
        return redirect(url_for('question_answer', question_id=question_id))
    return render_template('question_answer/question_answer.html', question_id=question_id)


@app.route('/question_list', methods=["GET"])
def question_list():
    questions = StudentQuestion.query.all()
    return render_template("question_answer/question_list.html", questions=questions)


@app.route('/answer_comment/<int:question_id>', methods=["GET", "POST"])
def answer_comment(question_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    answer = QuestionAnswers.query.filter(QuestionAnswers.question_id == question_id).all()
    return render_template('question_answer/answer_comment.html', student=student, question_id=question_id,
                           answer=answer)


@app.route('/all_question', methods=["GET", "POST"])
def all_question():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    questions = StudentQuestion.query.filter(StudentQuestion.student_id == student.id).order_by(StudentQuestion.id)
    return render_template("question_answer/all question.html", student=student, questions=questions)


@app.route('/create_comment/<int:answer_id>', methods=["GET", "POST"])
def create_comment(answer_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    answer = QuestionAnswers.query.filter(QuestionAnswers.id == answer_id).first()
    if request.method == "POST":
        comment = request.form.get("comment")
        date = datetime.now()
        add = AnswerComment(comment=comment, date=date, user_id=student.id,
                            subject_id=answer.subject_id, question_id=answer.question_id, answer_id=answer_id)

        db.session.add(add)
        db.session.commit()
        return redirect(url_for("create_comment", answer=answer, answer_id=answer_id))
    return render_template("question_answer/create_comment.html", student=student, answer_id=answer_id,
                           answer=answer)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  ishlamotti
@app.route('/my_question', methods=["GET", "POST"])
def my_question():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    # questions = StudentQuestion.query.filter(StudentQuestion.student_id == StudentQuestion.question).all() xato edi
    questions = StudentQuestion.query.filter(StudentQuestion.student_id == student.id).all()
    return render_template("my_question/my_question.html", user=user, questions=questions)
