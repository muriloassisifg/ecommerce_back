# app/models/order.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection.database import Base
from models.order_product_model import order_product_table

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)

    # Relacionamento com Product usando a tabela intermediária
    products = relationship("Product", secondary=order_product_table, back_populates="orders")

# Definição dos schemas Pydantic
class OrderBase(BaseModel):
    name: str

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
