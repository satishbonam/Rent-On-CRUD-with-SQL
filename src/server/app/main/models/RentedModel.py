from .. import db


class RentedModel(db.Model):

    __tablename__ = "rented"

    id = db.Column(db.Interger, primary_key=True)
    property_id = db.Column(db.Interger, db.ForeignKey(
        'property.id'), nullable=False)
    user_id = db.Column(db.Interger, db.ForeignKey(
        'user.id'), nullable=False)
