from typing import List
from decimal import Decimal
from pydantic import BaseModel, BeforeValidator, field_validator
from typing_extensions import Annotated
from api.validation import validate_fixed_length




class CreateAdvertismentDTO(BaseModel):
    name: str
    description: str
    price: Decimal
    price: float
    photos: str

    @field_validator('photos')
    @classmethod
    def validate_fixed_length(cls, v):

        v = v.split(', ')

        assert validate_fixed_length(3)(v), \
            "Maximum number of photos should be 3"
        
        return ', '.join(v)
    

class CreatedAdvertismentDTO(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    photos: str
     