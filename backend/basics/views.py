from app import *
import json
from backend.basics.settings import *
from werkzeug.security import *
from backend.models.basic_model import *
from backend.lessons.student_views import *

from backend.teacher.views import *


@app.route('/', methods=['POST', 'GET'])
def login():
    users = [
        {
            "id": 1,
            "name": "Shahzod",
            "surname": "Sobirov",
            "username": "Sob1rov",
            "father_name": "Sherzod",
            "password": 12345,
            "student": True,
            "teacher": False,
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
            "password": 12345,
            "student": True,
            "teacher": False,
            "group": [
                {
                    "id": 1,
                    "group_name": "A1",
                    "group_subject": "Ingliz tili"
                },
                {
                    "id": 2,
                    "group_name": "oqtoplam",
                    "group_subject": "Matematika"
                },
                {
                    "id": 3,
                    "group_name": "biologiya",
                    "group_subject": "Biologiya"
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
            "password": 12345,
            "teacher_id": 3,
            "student": True,
            "teacher": False,
            "group": [
                {
                    "id": 3,
                    "group_name": "B1",
                    "group_subject": "Ingliz tili"
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
            "password": 12345,
            "student": True,
            "teacher": False,
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
            "password": 12345,
            "student": True,
            "teacher": False,
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
            "password": 12345,
            "student": False,
            "teacher": True,
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
            "password": 12345,
            "student": True,
            "teacher": False,
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
            "id": 20,
            "name": "ismi yo",
            "surname": "yo",
            "username": "ismiyo",
            "father_name": "otasi yo",
            "password": 12345678,
            "student": False,
            "teacher": True,
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
            "id": 21,
            "name": "yetim",
            "surname": "yetim",
            "username": "yetim",
            "father_name": "yetim",
            "password": 12345678,
            "student": True,
            "teacher": False,
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
            "id": 70,
            "name": "cmo",
            "surname": "cmo",
            "username": "cmo",
            "father_name": "cmo",
            "password": 12345678,
            "student": True,
            "teacher": False,
            "group": [
                {
                    "id": 5,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 19,
            "name": "lox",
            "surname": "lox",
            "username": "lox",
            "father_name": "lox",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 5,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 13,
            "name": "latta",
            "surname": "latta",
            "username": "latta",
            "father_name": "latta",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 9,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 99,
            "name": "zaybal",
            "surname": "zaybal",
            "username": "zaybal",
            "father_name": "zaybal",
            "password": 12345678,
            "student": True,
            "teacher": False,
            "group": [
                {
                    "id": 9,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 100,
            "name": "kot",
            "surname": "kot",
            "username": "kot",
            "father_name": "kot",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 9,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 101,
            "name": "qotobow",
            "surname": "qotobow",
            "username": "qotobow",
            "father_name": "qotobow",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 9,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 103,
            "name": "qotobow",
            "surname": "qotobow",
            "username": "qotobow2",
            "father_name": "qotobow",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 9,
                    "group_name": "Tarix",
                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 55,
            "name": "qotobow",
            "surname": "qotobow",
            "username": "pidr",
            "father_name": "qotowbow",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 10,
                    "group_name": "Tarix",

                    "group_subject": "Tarix"
                }
            ],
            "photo_profile": "",
        },
        {
            "id": 97,
            "name": "qotobow",
            "surname": "qotobow",
            "username": "user",
            "father_name": "qotowbow",
            "password": 12345678,
            "student": False,
            "teacher": True,
            "group": [
                {
                    "id": 11,
                    "group_name": "ing",

                    "group_subject": "Ingliz tili"
                }
            ],
            "photo_profile": "",
        }
    ]
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        platform_user = User.query.filter(User.username == username).first()
        if not platform_user:
            for user in users:
                id = user["id"]
                nik = user["username"]
                name = user["name"]
                platform_password = str(user["password"])
                surname = user["surname"]
                teacher_id = user["teacher"]
                student_id = user["student"]
                hashed = generate_password_hash(password=platform_password, method="sha256")
                if username == nik:
                    if platform_user:
                        print("bu oquvchi bor")
                    else:
                        add = User(name=name, surname=surname, username=nik, password=hashed, platform_id=id)
                        db.session.add(add)
                        db.session.commit()
                        if student_id == True:
                            student = Student(user_id=add.id)
                            db.session.add(student)
                            db.session.commit()
                            for gr in user['group']:
                                exist_group = Group.query.filter(Group.platform_id == gr['id']).first()
                                if not exist_group:
                                    subject = Subject.query.filter(Subject.name == gr['group_subject']).first()
                                    group_add = Group(platform_id=gr['id'], name=gr['group_name'], subject_id=subject.id)
                                    db.session.add(group_add)
                                    db.session.commit()
                                    if group_add not in student.groups:
                                        student.groups.append(group_add)
                                        db.session.commit()
                                    else:
                                        if exist_group not in student.groups:
                                            student.groups.append(exist_group)
                                            db.session.commit()

                        else:
                            teacher = Teacher(user_id=add.id)
                            db.session.add(teacher)
                            db.session.commit()
                            for gr in user['group']:
                                exist_group = Group.query.filter(Group.platform_id == gr['id']).first()
                                if not exist_group:
                                    subject = Subject.query.filter(Subject.name == gr['group_subject']).first()
                                    group_add = Group(platform_id=gr['id'], name=gr['group_name'],
                                                      subject_id=subject.id)
                                    db.session.add(group_add)
                                    db.session.commit()
                                    if group_add not in teacher.groups:
                                        teacher.groups.append(group_add)
                                        db.session.commit()
                                else:
                                    if exist_group not in teacher.groups:
                                        teacher.groups.append(exist_group)
                                        db.session.commit()
        else:
            if platform_user and check_password_hash(platform_user.password, password):
                session['username'] = platform_user.username
                student = Student.query.filter(Student.user_id == platform_user.id).first()
                teacher = Teacher.query.filter(Teacher.user_id == platform_user.id).first()
                if student:
                    if student.studentsubject:
                        return redirect(url_for('my_subjects'))
                    else:
                        return redirect(url_for('view_subjects'))
                if teacher:
                    return redirect(url_for('teacher_groups'))
            else:
                print(False)
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
