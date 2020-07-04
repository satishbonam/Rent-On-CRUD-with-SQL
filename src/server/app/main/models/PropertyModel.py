from .. import db


class PropertyModel(db.Model):

    __tablename__ = "property"

    id = db.Column(db.Interger, primary_key=True)
    owner_id = db.Column(db.Interger, db.ForeignKey('user.id'), nullable=False)
    area = db.Column(db.Interger, nullable=False)
    bedrooms = db.Column(db.Interger, nullable=False)
    furnishing = db.Column(db.Boolean, nullable=False, default=False)
    locality = db.Column(db.String(255), nullable=False)
    isRented = db.Column(db.Boolean, nullable=False, default=False)
