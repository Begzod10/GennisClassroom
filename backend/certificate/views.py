from app import *
from backend.models.basic_model import *
from PyPDF2 import *
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import shutil


@app.route("/certificate", methods=["GET", "POST"])
def certificate():
    user = get_current_user()
    courses = SubjectLevel.query.order_by(SubjectLevel.id).all()
    folder = 'certificates'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    if request.method == "POST":
        course_id = int(request.form.get('course_id'))
        student = Student.query.filter(Student.user_id == user.id).first()
        group = db.session.query(Group).join(Group.student).options(contains_eager(Group.student)).filter(
            Student.id == student.id, Group.course_id == course_id).first()
        teacher = db.session.query(Teacher).join(Teacher.groups).options(contains_eager(Teacher.groups)).filter(
            Group.id == group.id).first()
        course = SubjectLevel.query.filter(SubjectLevel.id == course_id).first()
        get_certificate = Certificate.query.filter(Certificate.course_id == course.id).order_by(
            desc(Certificate.id)).first()
        if get_certificate:
            certificate_id = get_certificate.certificate_id_number + 1
        else:
            certificate_id = 1
        max_number = 8
        number_of_0 = max_number - len(str(certificate_id))
        number_of_0 = number_of_0 * "0"
        print(number_of_0)
        add = Certificate(user_id=user.id, certificate_id_number=certificate_id, course_id=course.id,
                          subject_id=course.subject_id)
        db.session.add(add)
        db.session.commit()
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFillColorRGB(0, 0, 0)
        can.setFont("Times-Roman", 28)
        can.drawString(70, 365, f"{user.name.upper()} {user.surname.upper()}")
        can.setFont("Times-Roman", 20)
        can.drawString(70, 305, f"{course.name.upper()} Course")
        can.setFont("Times-Roman", 15)
        can.drawString(175, 273, f"{number_of_0}{certificate_id}")
        can.setFont("Times-Roman", 15)
        can.drawString(70, 100, f"{teacher.user.name.upper()} {teacher.user.surname.upper()}")
        can.save()
        packet.seek(0)
        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(open("backend/certificate/web_certificate.pdf", "rb"))
        output = PdfWriter()
        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
        output_stream = open(f"certificates/{user.name.upper()} {user.surname.upper()} {course.name}.pdf", "wb")
        output.write(output_stream)
        output_stream.close()
        return send_file(f"{user.name.upper()} {user.surname.upper()} {course.name}.pdf", as_attachment=True)
    return render_template("certificate/certificate.html", courses=courses, user=user)
