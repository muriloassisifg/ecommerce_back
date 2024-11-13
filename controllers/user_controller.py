# app/controllers/user_controller.py
from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from models.user_model import UserResponse, UserCreate

router = APIRouter()
service = UserService()

@router.get("/users", response_model=list[UserResponse])
def get_all_users():
    return service.get_all_users()

@router.get("/user/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/user/save", response_model=UserResponse)
def create_user(user: UserCreate):
    return service.create_user(user)

@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
