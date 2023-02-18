from flask import *
from backend.models.basic_model import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)

from backend.basics.views import *
from backend.create_lesson.views import *
from backend.essay_funtions.views import *
from backend.lessons.views import *
from backend.question_answer.views import *
from backend.teacher.views import *

if __name__ == '__main__':
    app.run()
