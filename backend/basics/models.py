from backend.models.basic_model import *


class Subject(db.Model):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class LevelCategory(db.Model):
    __tablename__ = "level_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ot = Column(Float)
    do = Column(Float)
    students = relationship("Student", backref="level", order_by="Student.id", lazy="select")
