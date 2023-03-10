from backend.models.basic_model import *


class Subject(db.Model):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    levels = relationship("SubjectLevel", backref="subject", order_by="SubjectLevel.id")
    answer = relationship('ExerciseAnswers', backref="subject", order_by="ExerciseAnswers.id")
    lesson = relationship('Lesson', backref="subject", order_by="Lesson.id")
    exercise = relationship('Exercise', backref="subject", order_by="Exercise.id")
    student_question = relationship("StudentQuestion", lazy="select", order_by="StudentQuestion.id")
    question_answers = relationship("QuestionAnswers", lazy="select", order_by="QuestionAnswers.id")
    answer_comment = relationship("QuestionAnswerComment", lazy="select", order_by="QuestionAnswerComment.id")
    donelessons = relationship('StudentExercise', backref="subject", order_by="StudentExercise.id")
    studentsubject = relationship('StudentSubject', backref="subject", order_by="StudentSubject.id")
    certificate = relationship('Certificate', backref="subject", order_by="Certificate.id")


class LevelCategory(db.Model):
    __tablename__ = "level_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ot = Column(Float)
    do = Column(Float)
    students = relationship("Student", backref="level", order_by="Student.id", lazy="select")


class SubjectLevel(db.Model):
    __tablename__ = "subject_level"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    lesson = relationship('Lesson', backref="subject_level", order_by="Lesson.id")
    exercise = relationship('Exercise', backref="subject_level", order_by="Exercise.id")
    donelessons = relationship("StudentExercise", backref="subject_level", order_by="StudentExercise.id")
    studentcourse = relationship('StudentCourse', backref="subject_level", order_by="StudentCourse.id")
    certificate = relationship('Certificate', backref="subject_level", order_by="Certificate.id")
