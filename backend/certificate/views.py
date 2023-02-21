from app import *
from PyPDF2 import PdfReader
# pdf = PdfReader(str("certificate.pdf"))
# print(len(pdf.metadata.title))
# pdf.pages[0].extract_text()
from PyPDF2 import *
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFillColorRGB(0, 0, 0)
can.setFont("Times-Roman", 28)
can.drawString(70, 365, "OMONBOYEV SHAHZOD")
can.setFont("Times-Roman", 20)
can.drawString(70, 305, "HTML CSS Course")
can.setFont("Times-Roman", 15)
can.drawString(175, 273, "0000012")
can.setFont("Times-Roman", 15)
can.drawString(70, 100, "Shahzod Sobirjonov")
can.save()
packet.seek(0)
new_pdf = PdfReader(packet)
existing_pdf = PdfReader(open("backend/certificate/CERTIFICATE_WEB.pdf", "rb"))
output = PdfWriter()
page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)
outputStream = open("OMONBOYEV SHAHZOD.pdf", "wb")
output.write(outputStream)
outputStream.close()


@app.route("/certificate", methods=["GET", "POST"])
def certificate():
    user = get_current_user()
    # if request.method == "POST":

    return render_template("certificate/certificate.html")
