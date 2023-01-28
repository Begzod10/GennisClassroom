from app import *
from backend.models.basic_model import *
from backend.basics.settings import *
import requests


@app.route('/write_essay/', methods=['GET', 'POST'])
def write_essay():
    # google translate
    # url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    #
    # payload = "q=bye&target=uz&source=en"
    # headers = {
    #     "content-type": "application/x-www-form-urlencoded",
    #     "Accept-Encoding": "application/gzip",
    #     "X-RapidAPI-Key": "1973d60fb8mshece0ce163f66024p1f4d12jsn70ad27675fdf",
    #     "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    # }
    #
    # response = requests.request("POST", url, data=payload, headers=headers)

    # speech to text
    # url = "https://speech-to-text13.p.rapidapi.com/transcript"

    # payload = "audio_url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fb%2Fbb%2FAmerican%2527s_Choice_and_Opportunity_%2528Newton_D._Baker%2529.ogg"
    # headers = {
    #     "content-type": "application/x-www-form-urlencoded",
    #     "X-RapidAPI-Key": "1973d60fb8mshece0ce163f66024p1f4d12jsn70ad27675fdf",
    #     "X-RapidAPI-Host": "speech-to-text13.p.rapidapi.com"
    # }
    #
    # response = requests.request("POST", url, data=payload, headers=headers)

    # plagarism
    # url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
    #
    # payload = {
    #     "text": "This is a test with a minimum of 40 characters to check plagiarism for.",
    #     "language": "en",
    #     "includeCitations": False,
    #     "scrapeSources": False
    # }
    # headers = {
    #     "content-type": "application/json",
    #     "X-RapidAPI-Key": "1973d60fb8mshece0ce163f66024p1f4d12jsn70ad27675fdf",
    #     "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
    # }
    #
    # response = requests.request("POST", url, json=payload, headers=headers)

    # print(response.text)


    user = get_current_user()
    student = Student.query.filter(Student.user_id == user).first()
    if request.method == "POST":
        essay = request.form.get('essay')
        add = Essay(essay_text=essay, student_id=student.id, info_id=1)
        add.add()
        return redirect(url_for('write_essay'))
    return render_template('writing/wirtingStudent/writingStudent.html')


@app.route('/essays_list')
def essays_list():
    essays = Essay.query.order_by(Essay.id).all()
    return render_template('writing/wrintgList/writingList.html', essays=essays)


@app.route('/check_essay/<int:essay_id>', methods=['POST', 'GET'])
def check_essay(essay_id):
    # essay = Essay.query.filter(Essay.id == essay_id).first()
    # essay_errors = EssayError.query.order_by(EssayError.id).all()
    # error_top = "xato topmadi"
    #
    # for error in essay_errors:
    #     if error.error in essay.essay_text:
    #         error_top = "xato topdi"
    essay = Essay.query.filter(Essay.id == essay_id).first()
    error_types = EssayErrorType.query.order_by(EssayErrorType.id).all()
    essay_errors = EssayError.query.order_by(EssayError.id).all()
    error_list = []
    for error in essay_errors:
        if error.error in essay.essay_text:
            archive = EssayErrorArchive.query.filter(EssayErrorArchive.error_id == error.id,
                                                     EssayErrorArchive.essay_id == essay_id).first()
            if not archive:
                add = EssayErrorArchive(error_id=error.id, essay_id=essay_id)
                add.add()
    archive_errors = EssayErrorArchive.query.filter(EssayErrorArchive.essay_id == essay_id).all()
    for error in archive_errors:
        info = {
            "error": error.essay_error.error,
            "error_type": error.essay_error.error_type.name,
            "answer": error.essay_error.answer,
            "comment": error.essay_error.comment
        }
        error_list.append(info)

    return render_template('writing/insideWriting/insideWriting.html', error_types=error_types, essay=essay,
                           error_list=error_list)

# @app.route("/creat_task", methods=["GET", "POST"])
# def creat_task():
#     if request.method == "POST":
#     # name = request.form.get("name")
#     # add = Task(name=name)
#     # db.session.add(add)
#     # db.session.commit()
#     return render_template("creat/create_task.html")
#
#
# @app.route("/creat_essay", methods=["GET", "POST"])
# def creat_essay():
#     if request.method == "POST":
#     # name = request.form.get("name")
#     # task_id = request.form.get("name")
#     # add = Essay(name=name, task_id=task_id)
#     # db.session.add(add)
#     # db.session.commit()
#     return render_template("creat/esse_type (2).html")
