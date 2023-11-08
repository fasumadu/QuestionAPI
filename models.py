from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String, nullable=False)
    content=Column(String, nullable=False)
    hashed_password = Column(String)
    published= Column(Boolean, server_default="True",nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class user(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)






