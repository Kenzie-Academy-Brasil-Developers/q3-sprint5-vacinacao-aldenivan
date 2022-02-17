from flask import jsonify, request, current_app
from app.models.vaccine_model import VaccineModel
from app.services.vaccine_service import validation_cpf, validation_keys, validation_types
from http import HTTPStatus

def create_vaccine_card():
    
    data = request.get_json()

    format_data= validation_keys(**data)

    vaccine = VaccineModel(**format_data)

    try:
        validation_cpf(vaccine.cpf)
        validation_types(vaccine)
        current_app.db.session.add(vaccine)
        current_app.db.session.commit()

    except ValueError:
        return {"msg": "The CPF is incorrect, your length is wrong. Use eleven numbers"}, HTTPStatus.BAD_REQUEST
    
    except TypeError:
        return {"msg": "The values is not strings or the CPF is incorrect, use only numbers"},  HTTPStatus.BAD_REQUEST

    except:
        return {"msg": "The CPF alredy exists. Try again"},  HTTPStatus.CONFLICT


    return jsonify(vaccine), HTTPStatus.CREATED


def get_vaccine_cards():
    
    vaccines = (VaccineModel.query.all())

    return jsonify(vaccines), HTTPStatus.OK