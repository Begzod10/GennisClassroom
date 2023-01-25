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


@app.route("/creat_question/<int:level>", methods=["GET", "POST"])
def creat_question(level):
    subject = Subject.query.all()
    levels = SubjectLevel.query.all()
    variants = ExerciseAnswers.query.all()
    types = ExerciseTypes.query.all()
    return render_template("creat/creat test.html", types=types, subject=subject, levels=levels, level=level,
                           variants=variants)


@app.route("/choose_subject", methods=["GET", "POST"])
def choose():
    subject = Subject.query.all()
    if request.method == "POST":
        return redirect(url_for("choose_levels"))
    return render_template("creat/choose subject.html", subject=subject)


@app.route("/choose_levels", methods=["GET", "POST"])
def choose_levels():
    levels = SubjectLevel.query.all()
    if request.method == "POST":
        level = request.form.get("level")
        return redirect(url_for("exercise", level=level))
    return render_template("creat/choose levels.html", levels=levels)


@app.route("/lesson", methods=["GET", "POST"])
def lesson():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")
        photo = request.files["img"]
        folder = lesson_folder()
        if photo and checkFile(photo.filename):
            photo_file = secure_filename(photo.filename)
            photo_url = "/" + folder + "/" + photo_file
            app.config['UPLOAD_FOLDER'] = folder
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
            add = Lesson(title=title, desc=desc, img=photo_url)
            db.session.add(add)
            db.session.commit()
    return render_template("creat/lesson.html")


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
    return render_template("creat/choose_lesson.html", lesson=lesson)


@app.route("/exercise/<int:level>", methods=["GET", "POST"])
def exercise(level):
    types = ExerciseTypes.query.all()
    return render_template("creat/exercise.html", types=types)


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
