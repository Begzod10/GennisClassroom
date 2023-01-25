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
        info = {
            "id": 0,
            "name": "",
            "surname": "",
            "age": 0,
            "attendance": 0,
            "score": 0,
            "card_id": "",
            "password": ""
        }
        with open("api_kundalik.json") as r:
            data = json.load(r)
            for school in data['schools']:
                for student in school['students']:
                    if student['card_id'] == username and student['password'] == password:
                        rate = round((student['attendance'] * 0.7) + (student['score'] * 0.3))
                        # password = generate_password_hash(info['password'], method='sha256')
                        # add = User(name=student['name'], surname=student['surname'], password=password)
                        # add.add()
                        # student = Student(user_id=add.id)
                        print(rate)
    write_json(data=to_json)
    return render_template('register.html')


def write_json(data, filename='api_kundalik.json'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
