from backend.models.basic_model import *

from backend.basics.models import *


# Create your models here.


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


class ExerciseTypes(db.Model):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lesson = relationship("Lesson", backref="exercise_types", order_by="Lesson.id")


class Exercise(db.Model):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    desc = Column(String)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    type_id = Column(Integer, ForeignKey('exercise_types.id'))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    level_id = Column(Integer, ForeignKey("subject_level.id"))


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


class EssayTypes(db.Model):
    __tablename__ = "essay_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    img = Column(String)
    essay_title = relationship("EssayInfo", backref="essay_type", order_by="EssayInfo.id", lazy="select")


class EssayInfo(db.Model):
    __tablename__ = "essay_info"
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    type_id = Column(Integer, ForeignKey('essay_types.id'))
    img = Column(String)
    essays = relationship("Essay", backref="essay_info", order_by="Essay.id", lazy="select")


class Essay(db.Model):
    __tablename__ = "essay"
    id = Column(Integer, primary_key=True)
    essay_text = Column(Text)
    student_id = Column(Integer, ForeignKey('student.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    info_id = Column(Integer, ForeignKey('essay_info.id'))
    status = Column(Boolean)
    archive = relationship("EssayErrorArchive", backref="essay", lazy='select', order_by="EssayErrorArchive.id")

    def add(self):
        db.session.add(self)
        db.session.commit()


class EssayErrorType(db.Model):
    __tablename__ = "essay_error_type"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    errors = relationship("EssayError", backref="error_type", lazy="select", order_by="EssayError.id")


class EssayError(db.Model):
    __tablename__ = "essay_error"
    id = Column(Integer, primary_key=True)
    comment = Column(String)
    error = Column(String)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
    answer = Column(String)
    error_type_id = Column(Integer, ForeignKey('essay_error_type.id'))
    archive = relationship("EssayErrorArchive", backref="essay_error", lazy='select', order_by="EssayErrorArchive.id")


class EssayErrorArchive(db.Model):
    __tablename__ = "essay_error_archive"
    id = Column(Integer, primary_key=True)
    error_id = Column(Integer, ForeignKey("essay_error.id"))
    essay_id = Column(Integer, ForeignKey('essay.id'))

    def add(self):
        db.session.add(self)
        db.session.commit()


class EssayStudentChecks(db.Model):
    __tablename__ = "essay_student_checks"
    id = Column(Integer, primary_key=True)
    comment = Column(String)
    error = Column(String)
    student_id = Column(Integer, ForeignKey('student.id'))
    essay_id = Column(Integer, ForeignKey('essay.id'))
    answer = Column(String)
    error_type_id = Column(Integer, ForeignKey('essay_error_type.id'))
    committed = Column(Boolean)

    def add(self):
        db.session.add(self)
        db.session.commit()
