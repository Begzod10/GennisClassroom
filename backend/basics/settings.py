from app import *

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_current_user():
    user_result = None
    if 'username' in session:
        username = session['username']
        user = User.query.filter(User.username == username).first()
        user_result = user

    return user_result


to_json = {
    "schools": [
        {
            "school_num": 52,

            "students": [

                {
                    "id": 1,
                    "name": "Begzod",
                    "surname": "Jumaniyozov",
                    "age": 21,
                    "attendance": 90,
                    "score": 90,
                    "card_id": "asd21wedsd",
                    "password": "12345678"
                },
                {
                    "id": 2,
                    "name": "Ulug'bek",
                    "surname": "Fatxullayev",
                    "age": 19,
                    "attendance": 80,
                    "score": 90,
                    "card_id": "fdsfseqe221e",
                    "password": "12345678"
                },
                {
                    "id": 3,
                    "name": "Asliddin",
                    "surname": "Mirmuhsinov",
                    "age": 19,
                    "attendance": 80,
                    "score": 80,
                    "card_id": "sadad231sdqw",
                    "password": "12345678"
                },
                {
                    "id": 4,
                    "name": "Mehroj",
                    "surname": "Ibodov",
                    "age": 27,
                    "attendance": 50,
                    "score": 50,
                    "card_id": "qwds21w12ssd",
                    "password": "12345678"
                }
            ]
        }
    ]
}
