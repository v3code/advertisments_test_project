from flask_sqlalchemy import SQLAlchemy
from api.data import CreateAdvertismentDTO
from api.models import AdvertismentModel


def create_advertisment_service(db: SQLAlchemy, advertisment: CreateAdvertismentDTO):
    created_advertisment = AdvertismentModel(**advertisment.model_dump())
    db.session.add(created_advertisment)
    db.session.commit()
    return created_advertisment