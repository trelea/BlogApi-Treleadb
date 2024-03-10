from fastapi import Request, HTTPException
from cryptography.fernet import Fernet
import jwt
import os


def middlewareToken(request: Request):
    if not request.cookies:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    _time = request.cookies['__token'].split(':')[0]
    _token = request.cookies['__token'].split(':')[1]

    try:
        fernet = Fernet(str(os.getenv('encK')).encode())
        _token = fernet.decrypt(_token.encode()).decode()
    except:
        raise HTTPException(status_code=498, detail="Invalid Token")

    try:
        _jwt = jwt.decode(_token, key=os.getenv('sK'), algorithms="HS256")

        if _jwt['time'] != _time:
            raise HTTPException(status_code=498, detail="Invalid Token")
        if _jwt['__id'] != request.cookies['__id']:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
    except Exception as e:
        raise HTTPException(status_code=498, detail="Invalid Token")
    