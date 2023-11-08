from fastapi import FastAPI,Depends,APIRouter
from ..database import SessionLocal, engine
from ..import models,schemas
from sqlalchemy.orm import Session
from ..database import get_db
from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")





router=APIRouter()

@router.post("/users",response_model=schemas.userout)
def create_user(user:schemas.usercreate,db:Session=Depends(get_db)):

    hashed_password=pwd_context.hash(user.password)#hashing a password
    user.password=hashed_password
    
    new_user= models.user(id=user.id,email=user.email,password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{id}",response_model=schemas.userout)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.id==id).first()
    return user