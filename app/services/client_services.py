from sqlalchemy.orm import Session

from app.repository.client_repository import get_all_clients, add_client, delete_client
from app.schemas.clients import ClientRequest


def get_clients_services(db: Session):
    return get_all_clients(db)

def create_clients_services(db: Session, client: ClientRequest):
    return add_client(db, client)

def delete_client_services(db: Session, client_id: int):
    return delete_client(db, client_id)