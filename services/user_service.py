from fastapi import Request
from fastapi.responses import JSONResponse
from repositories.user_repository import UserRepository
from models.user_model import UserCreate, UserLogin
from utils.settings import settings
from jose import jwt

class UserService:

    def __init__(self):
        self.repository = UserRepository()  # Instância do repositório de categorias

    def login(self, user: UserLogin, req: Request):

        user_db = self.get_user_by_username(username=user.username)

        if not user_db or user_db.password != user.password:
            return JSONResponse(
                status_code=401,
                content="usuário não encontrado!",
            )
            

        payload = {
            "username": user_db.username,
            "user_id": user_db.id,
        }

        access_token = jwt.encode(payload, settings.jwt_key, settings.jwt_algorithm)

        return access_token

    # Retorna todas as categorias
    def get_all_users(self):
        return self.repository.get_all()

    # Retorna uma categoria pelo ID
    def get_user_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    
    def get_user_by_username(self, username: int):
        return self.repository.get_by_username(username)

    # Cria uma nova categoria
    def create_user(self, user: UserCreate):
        return self.repository.create(user)

    # Remove uma categoria pelo ID
    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
