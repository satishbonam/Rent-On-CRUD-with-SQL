from .. import db


class AmenitiesModel(db.Model):

    __tablename__ = "amenities"

    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey(
        'property.id'), nullable=False)
    power_backup = db.Column(db.Boolean, nullable=False, default=False)
    parking = db.Column(db.Boolean, nullable=False, default=False)
    water_supply = db.Column(db.Boolean, nullable=False, default=False)
