from app import *


@app.route('/view_subjects')
def view_subjects():
    return render_template('subjects/subjects.html')


@app.route('/get_subjects')
def get_subjects():
    subjects = Subject.query.order_by(Subject.id).all()
    subject_list = []
    for sub in subjects:
        info = {
            "id": sub.id,
            "name": sub.name
        }
        subject_list.append(info)
    return jsonify({
        "subjects": subject_list
    })
