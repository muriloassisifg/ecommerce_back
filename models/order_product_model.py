# app/models/order_product.py
from sqlalchemy import Table, Column, ForeignKey
from connection.database import Base

# Tabela intermediária que associa `Order` e `Product`
order_product_table = Table(
    "order_product",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)
