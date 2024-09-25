from typing import Optional
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int = Field(default=0, ge=0)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class ConfigDict:
        from_attributes = True
