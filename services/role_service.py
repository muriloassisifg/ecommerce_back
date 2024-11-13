from repositories.role_repository import RoleRepository
from models.role_model import RoleCreate

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()  # Instância do repositório de categorias

    # Retorna todas as categorias
    def get_all_roles(self):
        return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_role_by_id(self, role_id: int):
        return self.repository.get_by_id(role_id)

    # Cria uma nova categoria
    def create_role(self, role: RoleCreate):
        return self.repository.create(role)

    # Remove uma categoria pelo ID
    def delete_role(self, role_id: int):
        return self.repository.delete(role_id)
