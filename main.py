from fastapi import FastAPI
from fastapi.params import Body
from typing import List
from fastapi import Depends
from .import models,schemas
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import post,user
from pydantic import BaseModel
from sqlalchemy import insert
from passlib.context import CryptContext
from random import randrange
from .database import get_db
from .routers import users,post
from .passcode import hash,verify
from .routers import authenticate



models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(post.router)
app.include_router(users.router)
app.include_router(authenticate.router)






#sending any api request we use this:db:session=depends(get_db)




