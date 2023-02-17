from app import *
from backend.basics.settings import *
from backend.basics.views import *
from backend.models.basic_model import *
from pprint import pprint


@app.route('/teacher_groups')
def teacher_groups():
    user = get_current_user()
    teacher = Teacher.query.filter(Teacher.user_id == user.id).first()
    return render_template('teacher groups/choose course.html', teacher=teacher)


@app.route('/students<int:group_id>', methods=['POST', 'GET'])
def students(group_id):
    group = Group.query.filter(Group.id == group_id).first()
    levels = SubjectLevel.query.filter(SubjectLevel.subject_id == group.subject_id).all()
    if request.method == "POST":
        level = request.form.get("level")
        Group.query.filter(Group.id == group_id).update({
            "course_id": level
        })
        db.session.commit()
        return redirect(url_for('students', group_id=group_id))
    return render_template('teacher groups/group students.html', group=group, levels=levels, group_id=group_id)
