from app import *
import json
from backend.basics.settings import *
from werkzeug.security import *
from gingerit.gingerit import GingerIt


# from english_words import get_english_words_set
# import enchant

# parser = GingerIt()
#
# web2lowerset = get_english_words_set(['web2'], lower=True)
# d = enchant.Dict("en_US")


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
        else:
            exist = False
            with open("apis/api_kundalik.json") as r:
                data = json.load(r)
                for school in data['schools']:
                    for student in school['students']:
                        if student['username'] == username and student['password'] == password:
                            exist = True
                            rate = round((student['attendance'] * 0.7) + (student['score'] * 0.3)) / 100
                            password = generate_password_hash(student['password'], method='sha256')
                            add = User(username=student['username'], name=student['name'], surname=student['surname'],
                                       password=password)
                            add.add()

                            category = LevelCategory.query.filter(
                                and_(LevelCategory.ot <= rate, LevelCategory.do >= rate)).first()

                            student = Student(user_id=add.id, level_category=category.id)
                            student.add()
                            session['username'] = add.username
            if exist:
                return redirect(url_for('view_subjects'))
            else:
                return redirect(url_for('login'))
    write_json(data=to_json)

    return render_template('login.html')


def write_json(data, filename='apis/api_kundalik.json'):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
