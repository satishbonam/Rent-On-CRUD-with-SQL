from .. import db


class UserRequestModel(db.Model):

    __tablename__ = "user_request"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    message = db.Column(db.String(255), nullable=True)
