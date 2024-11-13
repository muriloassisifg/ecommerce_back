# app/repositories/order_repository.py
from models.order_model import Order
from connection.database import database
from models.product_model import Product

class OrderRepository:
    
    def get_all(self):
        with database.get_session() as session:
            return session.query(Order).all()

    def get_by_id(self, order_id: int):
        with database.get_session() as session:
            return session.query(Order).filter(Order.id == order_id).first()

    def create(self, description: str, product_ids: list[int]):
        with database.get_session() as session:
            # Cria uma nova ordem
            db_order = Order(description=description)
            session.add(db_order)
            session.commit()
            session.refresh(db_order)

            # Associa os produtos à ordem
            for product_id in product_ids:
                product = session.query(Product).filter(Product.id == product_id).first()
                if product:
                    db_order.products.append(product)

            session.commit()
            return db_order

    def delete(self, order_id: int):
        with database.get_session() as session:
            order = session.query(Order).filter(Order.id == order_id).first()
            if order:
                session.delete(order)
                session.commit()
                return True
            return False
