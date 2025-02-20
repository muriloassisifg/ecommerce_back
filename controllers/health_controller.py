# controllers/cart_controller.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()
@router.get("/health")
def health():
    return HTMLResponse('OK')


