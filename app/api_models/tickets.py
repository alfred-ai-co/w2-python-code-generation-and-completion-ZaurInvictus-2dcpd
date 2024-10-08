from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    project_id: int
    status: str
    priority: str

class TicketResponse(TicketCreate):
    id: int
    updated_at: datetime
    
    class Config:
        from_attributes = True