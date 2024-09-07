from typing import List
from sqlalchemy.orm import Session
from app.config.config import get_db
from fastapi import APIRouter, HTTPException, Depends

from app.schemas.reservation import ReservationDTO, ReservationRequest
from app.services.reservation_service import get_reservations_services, create_reservations_services, \
    delete_reservation_services

router = APIRouter()

@router.get('/', response_model=List[ReservationDTO])
def get_reservations(db: Session = Depends(get_db)):
    reservations = get_reservations_services(db)
    if(not reservations):
        raise HTTPException(status_code=404, detail='dont have reservations')
    return reservations

@router.post('/', response_model=ReservationDTO)
def create_reservation(reservation: ReservationRequest, db: Session = Depends(get_db)):
    try:
        created_reservation = create_reservations_services(db, reservation)
        return created_reservation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete('/{reservation_id}', response_model=ReservationDTO)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    try:
        deleted_reservation = delete_reservation_services(db, reservation_id)
        return deleted_reservation
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))