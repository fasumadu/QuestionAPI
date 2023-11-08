from fastapi import FastAPI,Depends,APIRouter
from ..database import SessionLocal, engine
from .. import models,schemas
from sqlalchemy.orm import Session
from ..database import get_db
from .. import token




router=APIRouter()


@router.get("/posts")
def root(db:Session=Depends(get_db)):
    posts=db.query(models.post).all()
    return posts


@router.post("/posts",response_model=schemas.Postresponse)
def create_post(post:schemas.Postcreate, db:Session=Depends(get_db),user_id :int=Depends(token.get_current_user)):
   print(user_id)
   new_posts= models.post(id=post.id,title=post.title,content=post.content,hashed_password=post.hashed_password,published=post.published)
   db.add(new_posts)
   db.commit()
   db.refresh(new_posts)
   return {"status":new_posts}


@router.get("/posts/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.post).filter(models.post.id==id).first()
    return {"message":post}