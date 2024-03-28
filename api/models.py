from api.app import db
from decimal import Decimal
from sqlalchemy import Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class AdvertismentModel(db.Model):
    __tablename__ = "advertisments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[Decimal] = mapped_column(
        DECIMAL(precision=10, scale=2), default=Decimal(0.0)
    )
    photos: Mapped[str] = mapped_column(String()) # 'url1, url2, url3'
    created_at: Mapped[datetime] = mapped_column(DateTime, default=db.func.now())
