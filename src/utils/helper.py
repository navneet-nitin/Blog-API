from fastapi import Request, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.utils.settings import settings
from src.user.model import UserModel
from jwt import InvalidTokenError,ExpiredSignatureError
import jwt


def is_authenticated(request:Request,db:Session=Depends(get_db)):
    try:
        token=request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized!!")
        token=token.split(" ")[-1]
        print(token)
        body=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        user_id=body.get("id")     #user_id is the variable assigned in payload while encoding
        valid=db.query(UserModel).filter(UserModel.id==user_id).first()
        if not valid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized")
        return valid
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

def is_admin(user: UserModel = Depends(is_authenticated)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="You are not allowed!")
    return user