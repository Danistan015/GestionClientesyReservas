from datetime import datetime

from pydantic import BaseModel, Field
from datetime import date


class ReservationRequest(BaseModel):
    reservation_code: str = Field(..., min_length=1)
    date: date
    client_id: int = Field(...)

class ReservationDTO(BaseModel):
    id: int
    reservation_code: str
    date: date
    client_id: int

    class Config:
        orm_mode = True