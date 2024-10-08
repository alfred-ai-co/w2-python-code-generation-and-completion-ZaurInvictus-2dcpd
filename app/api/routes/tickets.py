# Ticket Endpoints
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.tickets import TicketCreate, TicketResponse
from app.api.dependencies.sqldb import get_db


router = APIRouter()


@router.post('', response_model=TicketResponse)
async def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.create_ticket(
        db, 
        ticket.title, 
        ticket.description, 
        ticket.project_id, 
        ticket.status, 
        ticket.priority
        )
    return db_ticket

@router.get('/{ticket_id}', response_model=TicketResponse)
async def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    return db_ticket

@router.put('/{ticket_id}', response_model=TicketResponse)
async def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    if not ticket.project_id:
        raise HTTPException(status_code=422, detail="Field 'project_id' is required")
    db_ticket = crud.update_ticket(
        db, 
        ticket_id, 
        ticket.title, 
        ticket.description, 
        ticket.project_id, 
        ticket.status, 
        ticket.priority
        )
    return db_ticket

@router.delete('/{ticket_id}')
async def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    crud.delete_ticket(db, ticket_id)
    return {'message': f'Ticket with id {ticket_id} deleted'}


