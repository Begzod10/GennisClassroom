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
