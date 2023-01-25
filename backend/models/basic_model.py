from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import *
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, functions

db = SQLAlchemy()


# app.config['SQLALCHEMY_ECO'] = True
# lazy = "dynamic" -> bu relationship bugan table lani 2 tarafdan , filter, order  qb beradi va misol uchun child table orqali parentni ozgartirsa boladi yoki teskarisi
# lazy = "select" -> bu relationship bugan table lani aloxida query qb beradi
# lazy = "joined" -> bu relationship bugan table lani bittada hammasini query qb beradi
# lazy = "subquery" -> "joined" ga oxshidi test qlib iwltib koriw kere farqi tezligida bolishi mumkin
def db_setup(app):
    app.config.from_object('backend.models.config')
    db.app = app
    db.init_app(app)
    Migrate(app, db)
    return db


from backend.basics.models import *
from backend.lessons.models import *


class User(db.Model):
    id = Column(Integer, primary_key=True)
    __tablename__ = "user"
    username = Column(String)
    name = Column(String)
    surname = Column(String)
    image = Column(String)
    balance = Column(Integer)
    password = Column(String)
    student = relationship('Student', backref='user', order_by="Student.id", lazy="dynamic")

    def add(self):
        db.session.add(self)
        db.session.commit()


class Student(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    level_category = Column(Integer, ForeignKey('level_category.id'))
    subjects = relationship("Subject", secondary="student_subject", lazy="select", order_by="Subject.id")

    def add(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit(self)


db.Table('student_subject',
         db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
         db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
         )

db.Table('teacher_subject',
         db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')),
         db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
         )


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
