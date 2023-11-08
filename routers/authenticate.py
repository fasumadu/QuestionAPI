from fastapi import APIRouter,Depends,HTTPException,Response
from sqlalchemy.orm import Session
from ..import models , schemas 
from ..database import get_db
from ..import passcode,token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=["Authentication"])

@router.post("/login",response_model=schemas.token)
def login(credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.email==credentials.username).first()
    if not user:
        raise HTTPException
    if not passcode.verify(credentials.password,user.password):
        raise HTTPException
    access_token=token.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}








