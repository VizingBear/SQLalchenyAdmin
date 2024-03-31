from fastapi import APIRouter, Depends, HTTPException
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette import status

from src.database import get_db

from .models import User as model_user
from .shemas import User_shema as shema_user

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: shema_user, db: Session = Depends(get_db)):
    new_products = model_user(**payload.dict())
    db.add(new_products)
    db.commit()
    db.refresh(new_products)
    return {"status": "success", "products": new_products}


@router.patch('/{product_id}')
def update_note(product_id: str, payload: shema_user, db: Session = Depends(get_db)):
    products_query = db.query(model_user).filter(model_user.id == product_id)
    db_products = products_query.first()

    if not db_products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {product_id} found')
    update_data = payload.dict(exclude_unset=True)
    products_query.filter(model_user.id == product_id).update(update_data,
                                                              synchronize_session=False)
    db.commit()
    db.refresh(db_products)
    return {"status": "success", "products": db_products}


@router.get('/{product_id}')
def get_post(product_id: str, db: Session = Depends(get_db)):
    products = db.query(model_user).filter(model_user.id == product_id).first()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "products": products}


@router.delete('/{product_id}')
def delete_post(product_id: str, db: Session = Depends(get_db)):
    products_query = db.query(model_user).filter(model_user.id == product_id)
    note = products_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {id} found')
    products_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
