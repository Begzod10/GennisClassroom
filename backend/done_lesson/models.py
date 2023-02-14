from backend.models.basic_model import *
from backend.lessons.models import *
from backend.basics.models import *


class DoneLesson(db.Model):
    __tablename__ = "donelesson"
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
    __tablename__ = "studentlesson"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer)
    finished = Column(Boolean)


class StudentCourse(db.Model):
    __tablename__ = "studentcourse"
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("subject_level.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer)
    finished = Column(Boolean)


class StudentSubject(db.Model):
    __tablename__ = "studentsubject"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    percentage = Column(Integer, default=0)
    finished = Column(Boolean, default=False)
