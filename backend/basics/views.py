from app import *
import json
from backend.basics.settings import *
from werkzeug.security import *


# Create your views here.


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if user and check_password_hash(user.password, password):
                session['username'] = user.username
                return redirect(url_for('view_subjects'))
            else:
                return redirect(url_for('login'))
        else:
            exist = False
            with open("api_kundalik.json") as r:
                data = json.load(r)
                for school in data['schools']:
                    for student in school['students']:
                        if student['card_id'] == username and student['password'] == password:
                            exist = True
                            rate = round((student['attendance'] * 0.7) + (student['score'] * 0.3)) / 100
                            password = generate_password_hash(student['password'], method='sha256')
                            add = User(name=student['name'], surname=student['surname'], password=password)
                            add.add()

                            category = LevelCategory.query.filter(
                                and_(LevelCategory.ot <= rate, LevelCategory.do >= rate)).first()

                            student = Student(user_id=add.id, level_category=category.id)
                            student.add()
            if exist:
                return redirect(url_for('view_subjects'))
            else:
                return redirect(url_for('login'))
    write_json(data=to_json)
    return render_template('register.html')


def write_json(data, filename='api_kundalik.json'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
