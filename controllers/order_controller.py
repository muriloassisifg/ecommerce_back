# app/controllers/order_controller.py
from fastapi import APIRouter, HTTPException
from services.order_service import OrderService
from models.order_model import OrderResponse, OrderCreate

router = APIRouter()
service = OrderService()

@router.get("/categories", response_model=list[OrderResponse])
def get_all_categories():
    return service.get_all_categories()

@router.get("/order/{order_id}", response_model=OrderResponse)
def get_order_by_id(order_id: int):
    order = service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/order/save", response_model=OrderResponse)
def create_order(order: OrderCreate):
    return service.create_order(order)

@router.delete("/order/{order_id}")
def delete_order(order_id: int):
    deleted = service.delete_order(order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
