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
    print(subjects)
    student = Student.query.filter(Student.user_id == user.id).first()
    for sub in subjects:
        if 'checked' in sub:
            subject = Subject.query.filter(Subject.id == sub['id']).first()
            add = StudentSubject(student_id=student.id, subject_id=subject.id)
            db.session.add(add)
            db.session.commit()
            return redirect(url_for('my_subjects'))
    return redirect(url_for('my_subjects'))


@app.route('/my_subjects/')
def my_subjects():
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    student_subjects = StudentSubject.query.filter(StudentSubject.student_id == student.id).order_by(
        StudentSubject.id).all()
    subject_list = []
    for subject in student_subjects:
        info = {
            "id": subject.subject.id,
            "name": subject.subject.name,
            "img": subject.subject.img
        }
        subject_list.append(info)

    return render_template('mySubjects/mySubjects.html', student=student, subject_list=subject_list)


@app.route('/my_lesson/<int:sub_id>')
def my_lesson(sub_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    subject = Subject.query.filter(Subject.id == sub_id).first()
    questions = Exercise.query.filter(Exercise.subject_id == sub_id).all()
    lesson = Lesson.query.filter(Lesson.subject_id == sub_id).first()
    print(sub_id)
    group = Group.query.filter(Group.subject_id == sub_id).first()
    lesson_list = Lesson.query.filter(Lesson.subject_id == sub_id, Lesson.level_id == group.course_id).all()
    level = SubjectLevel.query.filter(SubjectLevel.subject_id == sub_id).order_by(SubjectLevel.id).all()
    done = StudentExercise.query.first()
    info = {
        "id": lesson.id,
        "title": lesson.title,
        "desc": lesson.desc,
        "img": lesson.img,
        "exercises": []
    }
    course = SubjectLevel.query.filter(SubjectLevel.subject_id == sub_id).count()
    done_course = StudentCourse.query.filter(StudentCourse.student_id == student.id,
                                             StudentCourse.percentage == 100).count()
    result = round((done_course / course) * 100)

    filter = StudentSubject.query.filter(StudentSubject.student_id == student.id,
                                         StudentSubject.subject_id == sub_id).first()
    if filter:
        StudentSubject.query.filter(StudentSubject.student_id == student.id,
                                    StudentSubject.subject_id == sub_id).update(
            {
                "percentage": result
            })

        db.session.commit()
    else:
        student_lessons = StudentSubject(subject_id=sub_id, student_id=student.id)
        db.session.add(student_lessons)
        db.session.commit()
    return render_template('subject/subject.html', subject=subject, lesson=lesson, questions=questions,
                           level=level,
                           lesson_list=lesson_list, info=info)


@app.route('/my_lesson_level/<int:level_id>')
def my_lesson_level(level_id):
    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
    done = StudentExercise.query.first()
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
    done_lesson = StudentLesson.query.filter(StudentLesson.student_id == student.id,
                                             StudentLesson.percentage == 100).count()
    lessons = Lesson.query.filter(Lesson.level_id == level_id).count()
    print(done_lesson)
    result = round((done_lesson / lessons) * 100)

    filter = StudentCourse.query.filter(StudentCourse.student_id == student.id,
                                        StudentCourse.course_id == level_id).first()
    if filter:
        StudentCourse.query.filter(StudentCourse.student_id == student.id,
                                   StudentCourse.course_id == level_id).update(
            {
                "percentage": result
            })

        db.session.commit()
    else:
        student_lessons = StudentCourse(course_id=level_id, student_id=student.id)
        db.session.add(student_lessons)
        db.session.commit()
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
    done_lesson = StudentExercise.query.filter(StudentExercise.student_id == student.id,
                                               StudentExercise.lesson_id == lesson_id).all()
    done_lessons = StudentExercise.query.filter(StudentExercise.student_id == student.id,
                                                StudentExercise.lesson_id == lesson_id).count()
    exercise = Exercise.query.filter(Exercise.lesson_id == lesson_id).count()

    result = round((done_lessons / exercise) * 100)

    filter = StudentLesson.query.filter(StudentLesson.student_id == student.id,
                                        StudentLesson.lesson_id == lesson_id).first()
    # finished = StudentLesson.query.filter(StudentLesson.student_id == student.id,
    #                                       StudentLesson.lesson_id == lesson_id, StudentLesson.percentage == 100).first()
    #
    # if finished:
    #     StudentLesson.query.filter(StudentLesson.student_id == student.id,
    #                                StudentLesson.lesson_id == lesson_id, StudentLesson.percentage == 100).update(
    #         {
    #             "finished": True
    #         })
    #     db.session.commit()
    if filter:
        StudentLesson.query.filter(StudentLesson.student_id == student.id, StudentLesson.lesson_id == lesson_id).update(
            {
                "percentage": result
            })
        db.session.commit()
    else:
        student_lessons = StudentLesson(lesson_id=lesson_id, student_id=student.id)
        db.session.add(student_lessons)
        db.session.commit()

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
        finished_exercise = StudentExercise.query.filter(StudentExercise.lesson_id == lesson_id,
                                                         StudentExercise.student_id == student.id,
                                                         StudentExercise.exercise_id == les.id).first()
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
        add = StudentExercise(lesson_id=answer.lesson_id, student_id=student.id, subject_id=answer.subject_id,
                              level_id=answer.level_id,
                              type_id=answer.type_id, exercise_id=answer.exercise_id, answer_id=answer.id, boolean=False)
        db.session.add(add)
        db.session.commit()
        if answer.answer == True:
            add = StudentExercise(lesson_id=answer.lesson_id, student_id=student.id, subject_id=answer.subject_id,
                                  level_id=answer.level_id,
                                  type_id=answer.type_id, exercise_id=answer.exercise_id, answer_id=answer.id,
                                  boolean=True)
            db.session.add(add)
            db.session.commit()

        return redirect(url_for('lesson_info', lesson_id=lesson_id))
    return render_template('subject/subject.html', lesson=lesson, subject=subject, lesson_list=lesson_list,
                           student=student, info=info)
