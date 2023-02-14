from app import *
from backend.basics.settings import *
from backend.models.basic_model import *
from pprint import pprint


# from dnevnikru import Dnevnik


@app.route('/view_subjects')
def view_subjects():
    # dairy = Dnevnik("asadbeknimatilloyev", "asadbek2021!")
    # birthdays = dairy.birthdays(day=9, month=5)
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
        if 'checked' in sub:
            subject = Subject.query.filter(Subject.id == sub['id']).first()
            if subject not in student.subjects:
                student.subjects.append(subject)
                db.session.commit()
    return redirect(url_for('my_subjects'))


@app.route('/my_subjects/')
def my_subjects():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    subject_list = []
    for subject in student.subjects:
        info = {
            "id": subject.id,
            "name": subject.name,
            "img": subject.img
        }
        subject_list.append(info)

    return render_template('mySubjects/mySubjects.html', student=student, subject_list=subject_list)


@app.route('/my_lesson/<int:sub_id>')
def my_lesson(sub_id):
    subject = Subject.query.filter(Subject.id == sub_id).first()
    questions = Exercise.query.filter(Exercise.subject_id == sub_id).all()
    lesson = Lesson.query.filter(Lesson.subject_id == sub_id).first()
    lesson_list = Lesson.query.filter(Lesson.subject_id == sub_id).all()
    level = SubjectLevel.query.filter(SubjectLevel.subject_id == sub_id).order_by(SubjectLevel.id).all()
    done = DoneLesson.query.first()
    info = {
        "id": lesson.id,
        "title": lesson.title,
        "desc": lesson.desc,
        "img": lesson.img,
        "exercises": []
    }
    return render_template('subject/subject.html', subject=subject, lesson=lesson, questions=questions,
                           level=level,
                           lesson_list=lesson_list, info=info)


@app.route('/my_lesson_level/<int:level_id>')
def my_lesson_level(level_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    done = DoneLesson.query.first()
    lesson = Lesson.query.first()
    info = {
        "id": lesson.id,
        "title": lesson.title,
        "desc": lesson.desc,
        "img": lesson.img,
        "exercises": []
    }
    level = SubjectLevel.query.filter(SubjectLevel.id == level_id).first()
    subject = Subject.query.filter(Subject.id == level.subject_id).first()
    lesson = Lesson.query.filter(Lesson.level_id == level_id).order_by(Lesson.id).first()
    level = SubjectLevel.query.filter(SubjectLevel.id == level_id).order_by(SubjectLevel.id).all()
    lesson_list = Lesson.query.filter(Lesson.level_id == level_id).all()

    return render_template('subject/subject.html', level_id=level_id, lesson=lesson, subject=subject, level=level,
                           lesson_list=lesson_list, student=student, info=info)


@app.route('/lesson_info/<int:lesson_id>', methods=['POST', 'GET'])
def lesson_info(lesson_id):
    # user = get_current_user()
    student = Student.query.filter(Student.user_id == 2).first()
    lesson = Lesson.query.filter(Lesson.id == lesson_id).first()
    subject = Subject.query.filter(Subject.id == lesson.subject_id).first()
    lesson = Lesson.query.filter(Lesson.id == lesson_id).order_by(Lesson.id).first()
    lesson_list = Lesson.query.filter(Lesson.id == lesson_id).all()
    done_lesson = DoneLesson.query.filter(DoneLesson.student_id == student.id,
                                          DoneLesson.lesson_id == lesson_id).all()
    done_lessons = DoneLesson.query.filter(DoneLesson.student_id == student.id,
                                           DoneLesson.lesson_id == lesson_id).count()
    exercise = Exercise.query.filter(Exercise.lesson_id == lesson_id).count()
    print(done_lessons)
    print(exercise)
    result = round((done_lessons / exercise) * 100)
    print(result)
    info = {
        "id": lesson.id,
        "title": lesson.title,
        "desc": lesson.desc,
        "img": lesson.img,
        "exercises": []
    }

    for les in lesson.exercise:
        new_info = {
            "id": les.id,
            "desc": les.desc,
            "exercises_variants": [],
            "finished": False
        }
        finished_exercise = DoneLesson.query.filter(DoneLesson.lesson_id == lesson_id,
                                                    DoneLesson.student_id == student.id,
                                                    DoneLesson.exercise_id == les.id).first()
        if finished_exercise:
            new_info['finished'] = True
        for exer in les.exercise_variants:
            exercise_info = {
                "id": exer.id,
                "desc": exer.desc
            }
            new_info["exercises_variants"].append(exercise_info)
        info['exercises'].append(new_info)

    if request.method == "POST":
        var_id = request.form.get("id")
        answer = ExerciseAnswers.query.filter(ExerciseAnswers.id == var_id).first()
        add = DoneLesson(lesson_id=answer.lesson_id, student_id=student.id, subject_id=answer.subject_id,
                         level_id=answer.level_id,
                         type_id=answer.type_id, exercise_id=answer.exercise_id, answer_id=answer.id, boolean=False)
        db.session.add(add)
        db.session.commit()
        if answer.answer == True:
            add = DoneLesson(lesson_id=answer.lesson_id, student_id=student.id, subject_id=answer.subject_id,
                             level_id=answer.level_id,
                             type_id=answer.type_id, exercise_id=answer.exercise_id, answer_id=answer.id,
                             boolean=True)
            db.session.add(add)
            db.session.commit()
            pprint("hello")
        return redirect(url_for('lesson_info', lesson_id=lesson_id))
    return render_template('subject/subject.html', lesson=lesson, subject=subject, lesson_list=lesson_list,
                           student=student, info=info)
