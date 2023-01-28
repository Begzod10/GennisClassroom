from app import *
from backend.models.basic_model import *
from backend.basics.settings import *


@app.route('/write_essay/', methods=['GET', 'POST'])
def write_essay():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user).first()
    if request.method == "POST":
        essay = request.form.get('essay')
        add = Essay(essay_text=essay, student_id=student.id, info_id=1)
        add.add()
        return redirect(url_for('write_essay'))
    return render_template('writing/wirtingStudent/writingStudent.html')


@app.route('/check_essay/<int:essay_id>', methods=['POST', 'GET'])
def check_essay(essay_id):
    # essay = Essay.query.filter(Essay.id == essay_id).first()
    # essay_errors = EssayError.query.order_by(EssayError.id).all()
    # error_top = "xato topmadi"
    #
    # for error in essay_errors:
    #     if error.error in essay.essay_text:
    #         error_top = "xato topdi"
    error_types = EssayErrorType.query.order_by(EssayErrorType.id).all()
    return render_template('writing/insideWriting/insideWriting.html', error_types=error_types)


@app.route("/creat_task", methods=["GET", "POST"])
def creat_task():
    if request.method == "POST":
    # name = request.form.get("name")
    # add = Task(name=name)
    # db.session.add(add)
    # db.session.commit()
    return render_template("creat/create_task.html")


@app.route("/creat_essay", methods=["GET", "POST"])
def creat_essay():
    if request.method == "POST":
    # name = request.form.get("name")
    # task_id = request.form.get("name")
    # add = Essay(name=name, task_id=task_id)
    # db.session.add(add)
    # db.session.commit()
    return render_template("creat/esse_type (2).html")
