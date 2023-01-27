from flask import *
from backend.models.basic_model import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)

from backend.basics.views import *
from backend.creat_lesson.views import *
from backend.lessons.views import *
from backend.lessons.essay_route import *

if __name__ == '__main__':
    app.run()
