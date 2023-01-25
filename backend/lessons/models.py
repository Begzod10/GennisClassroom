from backend.models.basic_model import *


# Create your models here.


class Lesson(db.Model):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    level_id = Column(Integer, ForeignKey("level_category.id"))
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
    subject_id = Column(Integer, ForeignKey('subject.id'))
    desc = Column(String)
    answer = Column(Boolean, default=False)


class Essay(db.Model):
    __tablename__ = "essay"
    id = Column(Integer, primary_key=True)
    essay_text = Column(Text)
    student_id = Column(Integer, ForeignKey('student.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))


class EssayError(db.Model):
    __tablename__ = "essay_error"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    comment = Column(String)
    error = Column(String)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
    answer = Column(String)


class EssayPeerResult(db.Model):
    __tablename__ = "essay_peer_result"
    id = Column(Integer, primary_key=True)
    error_id = Column(Integer, ForeignKey('essay_error.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
