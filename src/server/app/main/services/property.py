from app.main.models.PropertyModel import PropertyModel
from app.main.models.AmenitiesModel import AmenitiesModel
from app.main.utils.save_db import save_db
from app.main import db


def create_property(data):
    new_property = PropertyModel(
        owner_id=data['owner_id'],
        area=data['area'],
        bedrooms=data['bedrooms'],
        furnishing=data.get('furnishing'),
        locality=data['locality'],
    )

    flag_property = save_db(new_property)

    amenitines = AmenitiesModel(
        property_id=new_property.id,
        power_backup=data['amenitines']['power_backup'],
        parking=data['amenitines']['parking'],
        water_supply=data['amenitines']['water_supply']
    )

    flag_amenities = save_db(amenitines)

    if flag_property and flag_amenities:
        return True
    else:
        return False


def get_properties_all():
    all_amenities = ['power_backup', 'parking', 'water_supply']
    query = "select * from property as p join amenities as a on p.id=a.property_id;"
    data_raw = db.engine.execute(query)
    data = []
    for item in data_raw:
        temp = {}
        temp['property_id'] = item['property_id']
        temp['area'] = item['area']
        temp['bedrooms'] = item['bedrooms']
        temp['furnishing'] = item['furnishing']
        temp['locality'] = item['locality']
        temp['isRented'] = item['isRented']
        temp['amenities'] = []
        for x in all_amenities:
            if item[x]:
                temp['amenities'].append(x)
        data.append(temp)

    return True, data


def edit_property(data, user_id):
    prop = PropertyModel().query.filter(PropertyModel.owner_id ==
                                        user_id and PropertyModel.id == data['property_id']).first()

    if prop:
        db.session.query(PropertyModel).filter(
            PropertyModel.owner_id == user_id and PropertyModel.id == data['property_id']).update({
                PropertyModel.area: data['area'],
                PropertyModel.bedrooms: data['bedrooms'],
                PropertyModel.furnishing: data['furnishing'],
                PropertyModel.isRented: data['isRented'],
                PropertyModel.locality: data['locality']
            })
        db.session.commit()

        db.session.query(AmenitiesModel).filter(AmenitiesModel.property_id == data['property_id']).update({
            AmenitiesModel.power_backup: data['amenitines']['power_backup'],
            AmenitiesModel.parking: data['amenitines']['parking'],
            AmenitiesModel.water_supply: data['amenitines']['water_supply']
        })
        db.session.commit()
        return True
    else:
        return False


def delete_property(data, user_id):
    prop = PropertyModel().query.filter(PropertyModel.owner_id ==
                                        user_id and PropertyModel.id == data['property_id']).first()

    if prop:
        db.session.query(AmenitiesModel).filter(
            AmenitiesModel.property_id == data['property_id']).delete()
        db.session.commit()

        db.session.query(PropertyModel).filter(
            PropertyModel.id == data['property_id']).delete()
        db.session.commit()

        return True
    else:
        return False
