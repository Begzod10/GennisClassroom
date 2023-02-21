from backend.models.basic_model import *


class Certificate(db.Model):
    __tablename__ = "certificate"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    certificate_id_number = Column(Integer)
    course_id = Column(Integer, ForeignKey("subject_level.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))
