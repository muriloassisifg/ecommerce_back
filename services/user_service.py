from repositories.user_repository import UserRepository
from models.user_model import UserCreate

class UserService:
    def __init__(self):
        self.repository = UserRepository()  # Instância do repositório de categorias

    # Retorna todas as categorias
    def get_all_users(self):
        return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)

    # Cria uma nova categoria
    def create_user(self, user: UserCreate):
        return self.repository.create(user)

    # Remove uma categoria pelo ID
    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
