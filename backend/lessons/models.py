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


class EssayTypes(db.Model):
    __tablename__ = "essay_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)


class EssayInfo(db.Model):
    __tablename__ = "essay_info"
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    type_id = Column(Integer, ForeignKey('essay_types.id'))
    img = Column(String)


class Essay(db.Model):
    __tablename__ = "essay"
    id = Column(Integer, primary_key=True)
    essay_text = Column(Text)
    student_id = Column(Integer, ForeignKey('student.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    info_id = Column(Integer, ForeignKey('essay_info.id'))
    status = Column(Boolean)

    def add(self):
        db.session.add(self)
        db.session.commit()


class EssayErrorType(db.Model):
    __tablename__ = "essay_error_type"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class EssayError(db.Model):
    __tablename__ = "essay_error"
    id = Column(Integer, primary_key=True)
    comment = Column(String)
    error = Column(String)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
    answer = Column(String)
    error_type = Column(Integer, ForeignKey('essay_error_type.id'))


class EssayPeerResult(db.Model):
    __tablename__ = "essay_peer_result"
    id = Column(Integer, primary_key=True)
    error_id = Column(Integer, ForeignKey('essay_error.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
