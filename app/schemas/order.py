from typing import List
from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.order_item import OrderItemBase, OrderItem


class OrderBase(BaseModel):
    status: str = Field(default="in_process")


class OrderCreate(OrderBase):
    items: List[OrderItemBase]


class Order(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItem]

    class ConfigDict:
        from_attributes = True
