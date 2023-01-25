from flask import *
from backend.models.basic_model import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


from backend.basics.views import *
from backend.creat_lesson.views import *
if __name__ == '__main__':
    app.run()
