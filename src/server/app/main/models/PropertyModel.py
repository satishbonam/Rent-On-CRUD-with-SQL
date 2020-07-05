from .. import db


class PropertyModel(db.Model):

    __tablename__ = "property"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    furnishing = db.Column(db.Boolean, nullable=False, default=False)
    locality = db.Column(db.String(255), nullable=False)
    isRented = db.Column(db.Boolean, nullable=False, default=False)
