from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

# --- Users ---
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    preferred_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    photo: Optional[str] = None

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

# --- Shows ---
class ShowBase(BaseModel):
    title: str
    theatre: Optional[str] = None
    description: Optional[str] = None
    status: bool = True
    show_time: Optional[str] = None

class ShowResponse(ShowBase):
    id: int
    created_at: datetime
    updated_at: datetime

# --- Assignments ---
class AssignmentBase(BaseModel):
    user_id: UUID
    show_id: int
    is_clover: bool = False
    location: Optional[str] = None
    status: bool = True

class AssignmentResponse(AssignmentBase):
    id: int
    created_at: datetime
    updated_at: datetime