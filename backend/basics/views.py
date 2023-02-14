from app import *
import json
from backend.basics.settings import *
from werkzeug.security import *
from gingerit.gingerit import GingerIt


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if user and check_password_hash(user.password, password):
                session['username'] = user.username
                student = Student.query.filter(Student.user_id == user.id).first()
                teacher = Teacher.query.filter(Teacher.user_id == user.id).first()
                if student:
                    if student.subjects:
                        return redirect(url_for('my_subjects'))
                    else:
                        return redirect(url_for('view_subjects'))
                if teacher:
                    return redirect(url_for('essays_list'))
            else:
                return redirect(url_for('login'))

    return render_template('login.html')
