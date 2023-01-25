from backend.models.basic_model import *


# Create your models here.

class Lesson(db.Model):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    desc = Column(String)
    img = Column(String)
    video = Column(String)


class ExerciseTypes(db.Model):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Exercise(db.Model):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    desc = Column(String)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type_id = Column(Integer, ForeignKey('exercise_types.id'))


class ExerciseAnswers(db.Model):
    __tablename__ = "exercise_answers"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type_id = Column(Integer, ForeignKey('exercise_types.id'))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    desc = Column(String)
    answer = Column(Boolean, default=False)
