
from sqlalchemy.orm import Session

from app.models.reservation_models import ReservationORM
from app.repository.client_repository import get_client_by_id
from app.schemas.reservation import ReservationRequest
from datetime import date


def get_all_reservations(db: Session) -> list[ReservationORM]:
    return db.query(ReservationORM).all()

def add_reservation(db: Session, reservation: ReservationRequest) -> ReservationORM:
    today = date.today()  # Obtén la fecha actual
    if reservation.date <= today:
        raise Exception("Not enough date.")

    client_reservation = get_client_by_id(db, reservation.client_id)

    if len(client_reservation.reservations) >= 5:
        raise Exception("The client has more than 5 reservations.")

    db_reservation = ReservationORM(
        reservation_code=reservation.reservation_code,
        date=reservation.date,
        client_id=reservation.client_id,
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def delete_reservation(db: Session, reservation_id: int):
    reservation = get_reservation_by_id(db, reservation_id)

    if not reservation:
        raise Exception("Dont exist reservation.")

    db.delete(reservation)
    db.commit()
    return reservation

def get_reservation_by_id(db: Session, reservation_id: int) -> ReservationORM:
    return db.query(ReservationORM).filter(ReservationORM.id == reservation_id).first()