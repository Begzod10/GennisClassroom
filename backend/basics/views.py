from app import *
import json
from backend.basics.settings import *
from werkzeug.security import *
from gingerit.gingerit import GingerIt
from backend.models.basic_model import *


@app.route('/', methods=['POST', 'GET'])
def login():
    users = [
        {
            "id": 1,
            "name": "Shahzod",
            "surname": "Sobirov",
            "username": "Sob1rov",
            "father_name": "Sherzod",
            "teacher_id": 1,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "A1",
                    "group_subject": "English"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 2,
            "name": "Aybek",
            "surname": "Abdusamatov",
            "username": "Aybek",
            "father_name": "Baxtjan",
            "teacher_id": 2,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "A1",
                    "group_subject": "English"
                },
                {
                    "id": 2,
                    "group_name": "oqtoplam",
                    "group_subject": "Matematika"
                },
                {
                    "id": 3,
                    "group_name": "biologiya",
                    "group_subject": "biologiya"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 3,
            "name": "Begzod",
            "surname": "Jumaniyozov",
            "username": "rimefara",
            "father_name": "Jumaniyoz",
            "teacher_id": 3,
            "password": 12345,
            "group": [
                {
                    "id": 3,
                    "group_name": "B1",
                    "group_subject": "English"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 4,
            "name": "Asad",
            "surname": "Nimatilloyev",
            "username": "Asad",
            "father_name": "Nimat",
            "teacher_id": 3,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 5,
            "name": "Shoxjaxon",
            "surname": "Xudoyberganov",
            "username": "Shox",
            "father_name": "Xudoyberg",
            "teacher_id": 5,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 6,
            "name": "Ulugbek",
            "surname": "Fatxullayev",
            "username": "Monster",
            "father_name": "Fatxulla",
            "teacher_id": 6,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 7,
            "name": "Asliddin",
            "surname": "Mirmuhsinov",
            "username": "Asi",
            "father_name": "Mirmuhsin",
            "teacher_id": 6,
            "password": 12345,
            "group": [
                {
                    "id": 1,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        }
    ]
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # user = User.query.filter(User.username == username).first()
        platform_user = User.query.filter(User.username == username).first()
        if not platform_user:
            for user in users:
                id = user["id"]
                nik = user["username"]
                name = user["name"]
                platform_password = str(user["password"])
                surname = user["surname"]
                hashed = generate_password_hash(password=platform_password, method="sha256")
                if username == nik:
                    print("ishladi")
                    if platform_user:
                        print("bu oquvchi bor")
                    else:
                        add = User(name=name, surname=surname, username=nik, password=hashed, platform_id=id)
                        db.session.add(add)
                        db.session.commit()
                        student = Student(user_id=add.id)
                        db.session.add(student)
                        db.session.commit()
        else:
            if platform_user and check_password_hash(platform_user.password, password):
                session['username'] = platform_user.username
                student = Student.query.filter(Student.user_id == platform_user.id).first()
                teacher = Teacher.query.filter(Teacher.user_id == platform_user.id).first()
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


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        surname = request.form.get("surname")
        password = request.form.get("password")
        hashed = generate_password_hash(password=password, method="sha256")
        add = User(name=name, username=username, surname=surname, password=hashed)
        db.session.add(add)
        db.session.commit()
        student = Student(user_id=add.id)
        db.session.add(student)
        db.session.commit()
    return render_template('register.html')

