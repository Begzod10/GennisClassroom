from app import *
from backend.basics.models import *
from backend.lessons.models import *
from werkzeug.utils import secure_filename
from backend.basics.settings import *


def subject_folder():
    upload_folder = 'static/img/subject_img'
    return upload_folder


def lesson_folder():
    upload_folder = 'static/img/lesson_img'
    return upload_folder


def checkFile(filename):
    value = '.' in filename
    type_file = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    return value and type_file


@app.route("/subject", methods=["GET", "POST"])
def subject():
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
    print(result)
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
    print(test)
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
    print(test)
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


# @app.route("/creat_task", methods=["GET", "POST"])
# def creat_task():
#     if request.method == "POST":
#         # name = request.form.get("name")
#         # add = Task(name=name)
#         # db.session.add(add)
#         # db.session.commit()
#     return render_template("creat/create_task.html")


# @app.route("/creat_essay", methods=["GET", "POST"])
# def creat_essay():
#     if request.method == "POST":
#         # name = request.form.get("name")
#         # task_id = request.form.get("name")
#         # add = Essay(name=name, task_id=task_id)
#         # db.session.add(add)
#         # db.session.commit()
#     return render_template("creat/esse_type (2).html")
