from backend.models.basic_model import *


class StudentQuestion(db.Model):
    __tablename__ = "student_question"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    question = Column(String)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    date = Column(DateTime)
    img = Column(Text)
    question_answers = relationship("QuestionAnswers", lazy="select", order_by="QuestionAnswers.id")
    question_answer_comment = relationship("QuestionAnswerComment", lazy="select", order_by="QuestionAnswerComment.id")


class QuestionAnswers(db.Model):
    __tablename__ = "question_answers"
    id = Column(Integer, primary_key=True)
    answer = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    checked = Column(Boolean)
    date = Column(Date)
    img = Column(Text)
    subject_id = Column(Integer, ForeignKey("subject.id"))
    question_id = Column(Integer, ForeignKey("student_question.id"))
    question_answer_comment = relationship("QuestionAnswerComment", lazy="select", order_by="QuestionAnswerComment.id")


class QuestionAnswerComment(db.Model):
    __tablename__ = "question_answer_comment"
    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey("question_answers.id"))
    user_id = Column(Integer, ForeignKey('user.id'))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    question_id = Column(Integer, ForeignKey("student_question.id"))
    comment = Column(Text)
    date = Column(Date)
    check = Column(Boolean)
