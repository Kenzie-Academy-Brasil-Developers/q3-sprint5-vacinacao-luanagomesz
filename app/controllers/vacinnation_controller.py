
from http import HTTPStatus
import psycopg2
import sqlalchemy
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from flask import current_app, jsonify, request
from app.exc.vaccine_exc import CpfInvalid
from app.models.vacinne import Vacinne

def get_vaccination():
    data = (Vacinne.query.all())
    serializer = [{"cpf":vacina.cpf, "first_shot_date": vacina.first_shot_date,
    "second_shot_date": vacina.second_shot_date, "health_unit_name": vacina.health_unit_name,
    "name": vacina.name,"vaccine_name": vacina.name
    } for vacina in data]
    return {"data": serializer}

def post_vaccination():
    data = request.get_json()
    
    
    data["first_shot_date"] = Vacinne.createdate()["first_shot_date"]
    data["second_shot_date"] = Vacinne.createdate()["second_shot_date"]
    for i in data:
        data[i] = str(data[i]).lower()
    
    try:
        vacinnation = Vacinne(**data)
    except CpfInvalid:
        return { "err": "CPF precisa ter o tamanho de 11 caracteres"}, HTTPStatus.BAD_REQUEST
    except TypeError:
        return {"err": "Campos invalidos adicionados"}, HTTPStatus.BAD_REQUEST
    try:
        current_app.db.session.add(vacinnation)
        current_app.db.session.commit()
    except IntegrityError as e:
        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            return {"err": "CPF já cadastrado"}, HTTPStatus.CONFLICT
        else:
            return {"err": "Preencha todos valores"}, HTTPStatus.BAD_REQUEST

    print(vacinnation)
    return jsonify(vacinnation), HTTPStatus.CREATED