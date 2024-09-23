from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.order import OrderBase, OrderCreate, Order
from app.db.models.order import Order as OrderModel
from app.db.models.order_item import OrderItem as OrderItemModel
from app.db.models.product import Product as ProductModel
from app.db.session import SessionLocal

router = APIRouter()


@router.post("/", response_model=Order)
def create_order(order: OrderCreate):
    db = SessionLocal()

    for item in order.items:
        product = (
            db.query(ProductModel).filter(ProductModel.id == item.product_id).first()
        )
        if not product or product.quantity_in_stock < item.quantity:
            db.close()
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient quantity for product ID {item.product_id}",
            )

    db_order = OrderModel()
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_order_item = OrderItemModel(
            order_id=db_order.id, product_id=item.product_id, quantity=item.quantity
        )
        db.add(db_order_item)

        product.quantity_in_stock -= item.quantity

    db.commit()

    items = (
        db.query(OrderItemModel).filter(OrderItemModel.order_id == db_order.id).all()
    )

    order_response = {**db_order.__dict__, "items": items}

    return order_response


@router.get("/", response_model=List[Order])
def get_orders():
    db = SessionLocal()
    orders = db.query(OrderModel).all()

    orders_with_items = []
    for order in orders:
        items = (
            db.query(OrderItemModel).filter(OrderItemModel.order_id == order.id).all()
        )
        order_data = order.__dict__
        order_data["items"] = items
        orders_with_items.append(order_data)

    return orders_with_items


@router.get("/{id}", response_model=Order)
def get_order(id: int):
    db = SessionLocal()
    order = db.query(OrderModel).filter(OrderModel.id == id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    items = db.query(OrderItemModel).filter(OrderItemModel.order_id == order.id).all()
    order_data = order.__dict__
    order_data["items"] = items

    return order_data


@router.patch("/{id}/status")
def update_order_status(id: int, status_update: OrderBase):
    db = SessionLocal()
    db_order = db.query(OrderModel).filter(OrderModel.id == id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    db_order.status = status_update.status
    db.commit()

    return {"message": f"Статус заказа id={id} изменен на '{status_update.status}'"}
