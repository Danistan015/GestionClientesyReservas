from sqlalchemy.orm import Session

from app.repository.reservation_repository import get_all_reservations, add_reservation, delete_reservation
from app.schemas.reservation import ReservationRequest


def get_reservations_services(db: Session):
    return get_all_reservations(db)

def create_reservations_services(db: Session, reservation: ReservationRequest):
    return add_reservation(db, reservation)

def delete_reservation_services(db: Session, reservation_id: int):
    return delete_reservation(db, reservation_id)