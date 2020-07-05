from app.main.models.UserModel import UserModel
import datetime
import jwt
from app.main.settings import key


def user_login(data):
    user = UserModel().query.filter(UserModel.email ==
                                    data['email'] and UserModel.password == data['password']).first()

    if user != None:
        token_data = {
            "id": user.id,
            "expire": str(datetime.datetime.utcnow() + datetime.timedelta(days=1)),
            "role": user.role
        }
        token = jwt.encode(token_data, key)
        return True, token
    else:
        return False, ""
