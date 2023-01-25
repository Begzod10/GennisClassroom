from app import *
from backend.basics.models import *
from backend.lessons.models import *
from werkzeug.utils import secure_filename
from backend.basics.settings import *


def subject_folder():
    upload_folder = 'static/img/subject_img'
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
    levels = QuizLevels.query.all()
    variants = ExerciseAnswers.query.all()
    types = ExerciseTypes.query.all()
    return render_template("creat/creat test.html", types=types, subject=subject, levels=levels, level=level,
                           variants=variants)


# @app.route("/test/<int:level_id>", methods=["POST"])
# def test(level_id):
#     test = request.get_json()['list']
#     level_id = QuizLevels.query.filter(QuizLevels.id == level_id).first()
#     for item in test:
#         question = item["question"]
#         variants = item["variants"]
#         type = item["type"]
#         addquestions = Questions(question=question, levels_id=level_id.id,
#                                  subject_id=level_id.subject_id, type_id=type)
#         db.session.add(addquestions)
#         db.session.commit()
#         for var in variants:
#             variant = var["value"]
#             checked = var["checked"]
#             addvariants = Variants(variants=variant, answer=checked, levels_id=level_id.id,
#                                    subject_id=level_id.subject_id, question_id=addquestions.id)
#             db.session.add(addvariants)
#             db.session.commit()
#     pprint(test)
#     return jsonify({
#         'success': True
#     })
