# app/models/role.py
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from connection.database import Base

# Definição do modelo SQLAlchemy
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Definição dos schemas Pydantic
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int
