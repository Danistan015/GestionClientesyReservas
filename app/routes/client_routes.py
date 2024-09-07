from typing import List
from sqlalchemy.orm import Session
from app.config.config import get_db
from fastapi import APIRouter, HTTPException, Depends

from app.schemas.clients import ClientDTO, ClientRequest
from app.services.client_services import get_clients_services, create_clients_services, delete_client_services

router = APIRouter()

@router.get('/', response_model=List[ClientDTO])
def get_clients(db: Session = Depends(get_db)):
    clients = get_clients_services(db)
    if(not clients):
        raise HTTPException(status_code=404, detail='Dont clients')
    return clients

@router.post('/', response_model=ClientDTO)
def create_client(client: ClientRequest, db: Session = Depends(get_db)):
    created_client = create_clients_services(db, client)
    return created_client

@router.delete('/{client_id}', response_model=ClientDTO)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    try:
        deleted_client = delete_client_services(db, client_id)
        return deleted_client
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))