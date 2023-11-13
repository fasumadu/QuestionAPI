#validation
from pydantic import BaseModel,EmailStr
from typing import Optional

class Postcreate(BaseModel):
    id:int
    title: str
    content: str
    published:bool =True
    hashed_password:str


class Postresponse(BaseModel):
    id:int
    title: str
    content: str
    hashed_password:str
    published:bool
    
   

class usercreate(BaseModel):
    id:int
    email:EmailStr
    password:str

class userout(BaseModel):
    id:int
    email:EmailStr
    class configure:
        orm_mode=True

class userlogin(BaseModel):
    email:EmailStr
    password:str

class token(BaseModel):
    access_token:str
    token_type:str

#what need to be in the token   
class tokendata(BaseModel):
    id:Optional[str]=None

