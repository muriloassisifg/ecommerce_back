

from models.order_model import OrderCreate
from repositories.order_repository import OrderRepository


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()  # Instância do repositório de categorias

    # Retorna todas as categorias
    def get_all_categories(self):
        return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_order_by_id(self, order_id: int):
        return self.repository.get_by_id(order_id)

    # Cria uma nova categoria
    def create_order(self, order: OrderCreate):
        return self.repository.create(order)

    # Remove uma categoria pelo ID
    def delete_order(self, order_id: int):
        return self.repository.delete(order_id)
