# app/models/subrole.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from connection.database import Base
from models.role_model import RoleResponse

# Definição do modelo SQLAlchemy
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))  # Chave estrangeira para Category
    role = relationship("Role")

# Definição dos schemas Pydantic
class UserBase(BaseModel):
    name: str
    role_id: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    role: RoleResponse
