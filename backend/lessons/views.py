from app import *
from backend.basics.settings import *
from backend.models.basic_model import *


@app.route('/view_subjects')
def view_subjects():
    user = get_current_user()
    return render_template('subjects/subjects.html')


@app.route('/get_subjects/')
def get_subjects():
    subjects = Subject.query.order_by(Subject.id).all()
    subject_list = []
    for sub in subjects:
        info = {
            "id": sub.id,
            "title": sub.name,
            "img": sub.img
        }
        subject_list.append(info)
    return jsonify({
        "subjects": subject_list
    })


@app.route('/receive_subjects/', methods=['POST'])
def receive_subjects():
    user = get_current_user()
    subjects = request.get_json()['subjects']
    student = Student.query.filter(Student.user_id == user.id).first()
    for sub in subjects:
        subject = Subject.query.filter(Subject.id == sub['id']).first()
        if subject not in student.subjects:
            student.subjects.append(subject)
            db.session.commit()
    return redirect(url_for('my_subjects'))


@app.route('/my_subjects/')
def my_subjects():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    return render_template('mySubjects/mySubjects.html', student=student)


@app.route('/my_lesson/<int:sub_id>')
def my_lesson(sub_id):
    subject = Subject.query.filter(Subject.id == sub_id).first()

    pass
