from backend.models.basic_model import *


class Subject(db.Model):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    levels = relationship("QuizLevels", backref="subject", order_by="QuizLevels.id")
    answer = relationship('ExerciseAnswers', backref="subject", order_by="ExerciseAnswers.id")


class LevelCategory(db.Model):
    __tablename__ = "level_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ot = Column(Float)
    do = Column(Float)
    students = relationship("Student", backref="level", order_by="Student.id", lazy="select")


class QuizLevels(db.Model):
    __tablename__ = "quiz_levels"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    levels = Column(String)
    # questions = db.relationship("Questions", backref="quiz_levels", order_by="Questions.id")
