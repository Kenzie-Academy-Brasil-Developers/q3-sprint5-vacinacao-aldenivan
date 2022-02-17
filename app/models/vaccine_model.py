from app.configs.database import db
from sqlalchemy import Column, String, DateTime
from dataclasses import dataclass
from datetime import datetime

@dataclass
class VaccineModel(db.Model):

    __tablename__ = "vaccine_cads"

    cpf: str = Column(String(11), primary_key=True)
    name: str = Column(String(100), nullable=False)
    first_shot_date: str = Column(DateTime, default = datetime.now())
    second_shot_date: str = Column(DateTime, default = datetime.fromordinal(datetime.now().toordinal()+90))    
    vaccine_name: str = Column(String(50), nullable=False)
    health_unit_name: str = Column(String(100))

