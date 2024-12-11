# app/models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from connection.database import Base
from models.subcategory_model import SubCategoryResponse

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    sub_category_id = Column(Integer, ForeignKey("subcategories.id"))
    sub_category = relationship("SubCategory")

# Schemas Pydantic para `Product`
class ProductBase(BaseModel):
    name: str
    price: float
    sub_category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    sub_category: SubCategoryResponse
