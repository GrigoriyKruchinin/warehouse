from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.product import ProductCreate, Product
from app.db.models.product import Product as ProductModel
from app.db.session import SessionLocal

router = APIRouter()


@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    db = SessionLocal()

    existing_product = (
        db.query(ProductModel).filter(ProductModel.name == product.name).first()
    )
    if existing_product:
        raise HTTPException(status_code=400, detail="Product already exists")

    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@router.get("/", response_model=List[Product])
def get_products():
    db = SessionLocal()
    products = db.query(ProductModel).all()
    return products


@router.get("/{id}", response_model=Product)
def get_product(id: int):
    db = SessionLocal()
    product = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{id}", response_model=Product)
def update_product(id: int, product: ProductCreate):
    db = SessionLocal()
    db_product = db.query(ProductModel).filter(ProductModel.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{id}", response_model=dict)
def delete_product(id: int):
    db = SessionLocal()
    db_product = db.query(ProductModel).filter(ProductModel.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}
