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

    user = get_current_user()
    student = Student.query.filter(Student.user_id == user.id).first()
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
    url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
    essay = Essay.query.filter(Essay.id == essay_id).first()
    # payload = {
    #     "text": essay.essay_text,
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
    #
    # print(response.text)
    # if response:
    #     for source in response.json()['sources']:
    #         Essay.query.filter(Essay.id == essay_id).update({
    #             "plagiarism_link": source['url']
    #         })
    #         db.session.commit()

    error_types = EssayErrorType.query.order_by(EssayErrorType.id).all()
    essay_errors = EssayError.query.order_by(EssayError.id).all()

    for error in essay_errors:
        if error.error in essay.essay_text:
            archive = EssayErrorArchive.query.filter(EssayErrorArchive.error_id == error.id,
                                                     EssayErrorArchive.essay_id == essay_id).first()
            if not archive:
                add = EssayErrorArchive(error_id=error.id, essay_id=essay_id)
                add.add()

    return render_template('writing/insideWriting/insideWriting.html', error_types=error_types, essay=essay,
                           essay_id=essay_id)


@app.route('/get_essay_errors/<int:essay_id>')
def get_essay_errors(essay_id):
    error_list = []
    archive_errors = EssayErrorArchive.query.filter(EssayErrorArchive.essay_id == essay_id).all()
    for error in archive_errors:
        info = {
            "id": error.id,
            "mistake": error.essay_error.error,
            "error_type": error.essay_error.error_type.name,
            "answer": error.essay_error.answer,
            "comment": error.essay_error.comment
        }
        error_list.append(info)
    return jsonify({
        "error_list": error_list
    })


@app.route('/send_errors/<int:essay_id>', methods=['POST'])
def send_errors(essay_id):
    mistake = request.get_json()['mistake']['mistake']
    answer = request.get_json()['mistake']['answer']
    comment = request.get_json()['mistake']['comment']
    error_type = request.get_json()['mistake']['mistake_type']

    error_add = EssayError(error=mistake, essay_id=essay_id, answer=answer,
                           comment=comment, error_type_id=error_type)
    db.session.add(error_add)
    db.session.commit()
    add = EssayErrorArchive(error_id=error_add.id, essay_id=essay_id)
    add.add()
    return jsonify({'success': True})

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
