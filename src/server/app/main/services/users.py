from app.main.models.UserModel import UserModel
from app.main.utils.save_db import save_db


def user_registration(data):
    user = UserModel().query.filter(UserModel.email == data['email']).all()

    if len(user) == 0:

        new_user = UserModel(
            name=data['name'],
            email=data['email'],
            mobile=data['mobile'],
            password=data['password'],
            role=data['role'])

        save_db(new_user)
        return True, "Registration Successfull"
    else:
        return False, "User Already Exists"
