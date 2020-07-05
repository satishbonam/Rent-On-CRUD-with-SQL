from app.main.models.PropertyModel import PropertyModel
from app.main.models.RentedModel import RentedModel
from app.main.utils.save_db import save_db
from app.main import db


def property_rented(property_data, u_id):
    prop = PropertyModel().query.filter(PropertyModel.id ==
                                        property_data['property_id'] and PropertyModel.isRented == False).first()

    if prop:
        data = RentedModel(
            property_id=property_data['property_id'],
            user_id=u_id
        )
        save_db(data)

        db.session.query(PropertyModel).filter(PropertyModel.id == property_data['property_id']).update({
            PropertyModel.isRented: 1
        })
        db.session.commit()
        return True
    else:
        return False
