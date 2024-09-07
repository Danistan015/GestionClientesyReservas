from sqlalchemy.orm import Session

from app.models.client_models import ClientORM
from app.schemas.clients import ClientRequest


def get_all_clients(db: Session) -> list[ClientORM]:
    return db.query(ClientORM).all()

def add_client(db: Session, client: ClientRequest) -> ClientORM:
    db_client = ClientORM(
        full_name=client.full_name,
        email=client.email,
        phone_number=client.phone_number,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def delete_client(db: Session, client_id: int):
    client = db.query(ClientORM).filter(ClientORM.id == client_id).first()

    if not client:
        raise Exception("dont found client.")

    if client.reservations:
        raise Exception("the client has reservations.")

    db.delete(client)
    db.commit()
    return client
def get_client_by_id(db: Session, client_id: int) -> ClientORM:
    return db.query(ClientORM).filter(ClientORM.id == client_id).first()