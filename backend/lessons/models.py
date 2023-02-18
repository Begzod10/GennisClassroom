from backend.models.basic_model import *

from backend.basics.models import *


class Lesson(db.Model):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey("exercise_types.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    level_id = Column(Integer, ForeignKey("subject_level.id"))
    title = Column(String)
    desc = Column(String)
    img = Column(String)
    video = Column(String)
    exercise = relationship("Exercise", backref="lesson", order_by="Exercise.id")
    answers = relationship("ExerciseAnswers", backref="lesson", order_by="ExerciseAnswers.id")
    donelesson = relationship("StudentExercise", backref="lesson", order_by="StudentExercise.id")
    studentlesson = relationship("StudentLesson", backref="lesson", order_by="StudentLesson.id")


class ExerciseTypes(db.Model):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lesson = relationship("Lesson", backref="exercise_types", order_by="Lesson.id")
    donelessons = relationship("StudentExercise", backref="exercise_types", order_by="StudentExercise.id")


class Exercise(db.Model):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    desc = Column(String)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type_id = Column(Integer, ForeignKey('exercise_types.id'))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    level_id = Column(Integer, ForeignKey("subject_level.id"))
    exercise_variants = relationship("ExerciseAnswers", backref="exercise", order_by="ExerciseAnswers.id")
    donelessons = relationship("StudentExercise", backref="exercise", order_by="StudentExercise.id")


class ExerciseAnswers(db.Model):
    __tablename__ = "exercise_answers"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type_id = Column(Integer, ForeignKey('exercise_types.id'))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    level_id = Column(Integer, ForeignKey("subject_level.id"))
    desc = Column(String)
    answer = Column(Boolean, default=False)
    donelessons = relationship("StudentExercise", backref="exercise_answers", order_by="StudentExercise.id")


class StudentExercise(db.Model):
    __tablename__ = "student_exercise"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    level_id = Column(Integer, ForeignKey("subject_level.id"))
    type_id = Column(Integer, ForeignKey("exercise_types.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    exercise_id = Column(Integer, ForeignKey("exercise.id"))
    answer_id = Column(Integer, ForeignKey("exercise_answers.id"))
    boolean = Column(Boolean)


class StudentLesson(db.Model):
    __tablename__ = "student_lesson"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer)
    finished = Column(Boolean)


class StudentCourse(db.Model):
    __tablename__ = "student_course"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("subject_level.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer)
    finished = Column(Boolean)


class StudentSubject(db.Model):
    __tablename__ = "student_subject"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer, default=0)
    finished = Column(Boolean, default=False)


