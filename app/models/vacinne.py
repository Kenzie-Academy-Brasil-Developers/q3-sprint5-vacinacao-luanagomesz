
import datetime
from sqlalchemy import Column, DateTime, Integer,String
from sqlalchemy.orm import validates
from app.configs.database import db
from dataclasses import dataclass

from app.exc.vaccine_exc import CpfInvalid

@dataclass
class Vacinne(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str
    __tablename__= "vaccine_cards"


    cpf = Column(String(length=11), primary_key = True)
    name = Column(String, nullable=False)
    first_shot_date= Column(DateTime, nullable=False)
    second_shot_date = Column(DateTime, nullable=False)
    vaccine_name = Column(String, nullable =False)
    health_unit_name = Column(String,nullable=False)

    @staticmethod
    def createdate():
        dates = {"first_shot_date": datetime.datetime.now(), "second_shot_date": datetime.datetime.now() + datetime.timedelta(days=90) }
        return dates
   
    @validates("cpf")
    def validate_cpf(self, key, cpf):
        if len(cpf) != 11:
            raise CpfInvalid
        return cpf