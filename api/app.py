from decimal import Decimal
from flask import Flask, jsonify, request
import os
from flask_sqlalchemy import SQLAlchemy

from decimal import Decimal
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime



from pydantic import ValidationError


from dotenv import load_dotenv

# from api.advertisment_service import create_advertisment_service

from .data import CreateAdvertismentDTO

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///db.sqlite")

db = SQLAlchemy(app)


class AdvertismentModel(db.Model):
    __tablename__ = "advertisments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column(
        Integer, default=0
    )
    photos: Mapped[str] = mapped_column(String()) # 'url1, url2, url3'
    created_at: Mapped[datetime] = mapped_column(DateTime, default=db.func.now())


with app.app_context():
    db.create_all()


def create_advertisment_service(db: SQLAlchemy, advertisment: CreateAdvertismentDTO):
    created_advertisment = AdvertismentModel(**advertisment.model_dump())
    db.session.add(created_advertisment)
    db.session.commit()
    return dict(id=created_advertisment.id, 
                name=created_advertisment.name, 
                description=created_advertisment.description, 
                price=created_advertisment.price, 
                photos=created_advertisment.photos, 
                created_at=created_advertisment.created_at)


@app.get('/do_something')
def index():
    return "Hello World"

@app.post('/advertisments')
def create_advertisment():
    body = request.json
    body['photos'] = ", ".join(body['photos'])
    try:
        body = CreateAdvertismentDTO(**body)
        
    except ValidationError as e:
        # errors = list(map(lambda err: dict(err), e.errors()))
        return e.json(), 400
    return jsonify(create_advertisment_service(db, body))

@app.get('/advertisments')
def get_advertisments():
    pass


@app.get('/advertisments/search')
def search_advertisments():
    pass


def main():
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 8888))
    app.config["DEBUG"] = True
    app.run(host, port)


if __name__ == '__main__':
    main()
