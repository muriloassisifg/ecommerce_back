from repositories.subcategory_repository import SubCategoryRepository
from models.subcategory_model import SubCategoryCreate

class SubCategoryService:
    def __init__(self):
        self.repository = SubCategoryRepository()  # Instância do repositório de subcategorias

    # Retorna todas as subcategorias
    def get_all_subcategories(self):
        return self.repository.get_all()

    # Retorna uma subcategoria pelo ID
    def get_subcategory_by_id(self, subcategory_id: int):
        return self.repository.get_by_id(subcategory_id)

    # Cria uma nova subcategoria associada a uma categoria
    def create_subcategory(self, subcategory: SubCategoryCreate):
        return self.repository.create(subcategory)

    # Remove uma subcategoria pelo ID
    def delete_subcategory(self, subcategory_id: int):
        return self.repository.delete(subcategory_id)
