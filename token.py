from jose import JWTError,jwt
from datetime import datetime,timedelta
from. import schemas
from fastapi import status,HTTPException,Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

oauth2_scheme = OAuth2AuthorizationCodeBearer(
   authorizationUrl="http://127.0.0.1:8000/authorise",
   tokenUrl="/login"
)


#secrete key
#algorithm
#expiration time

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

#creating the token
    token_generation=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token_generation 

def verify_access_token(token:str,credential_exception):
    try:
      token_verification=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
      id:str =token_verification.get("user_id")
      if id is None:
         raise credential_exception
      token_data=schemas.tokendata(id=id)
    except JWTError:
       raise credential_exception
    return token_data
    
#this function takes the token,extract the id in it,verify the token,
def get_current_user(token:str=Depends(oauth2_scheme)):
   credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers={"WWW-Authenticate":"Bearer"})

   return verify_access_token(token,credentials_exception)

 
