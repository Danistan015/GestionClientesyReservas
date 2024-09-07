from pydantic import BaseModel, Field, EmailStr


class ClientRequest(BaseModel):
    full_name: str = Field(..., min_length=1)
    phone_number: str = Field(..., min_length=10)
    email: EmailStr

class ClientDTO(BaseModel):
    id: int
    full_name: str
    phone_number: str
    email: EmailStr

    class Config:
        orm_mode = True