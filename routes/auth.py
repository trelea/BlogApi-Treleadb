from fastapi import APIRouter, Request, Response
from .models import User, UserAuth
from treleadb import TreleadbClient
from .middleware import middlewareToken
from cryptography.fernet import Fernet
import os
import jwt
import hashlib
import time
from dotenv import load_dotenv
load_dotenv()


db = TreleadbClient(dbName='BlogApp', secretKey=os.getenv('sK'))


router = APIRouter(
    prefix='/auth',
    tags=['authetication']
)



@router.post('/signup')
async def signup(schema: User):
    SHA256 = hashlib.sha256()
    SHA256.update(str(schema.user_password).encode())
    schema.user_password = SHA256.hexdigest()
    schema.user_gender = str(schema.user_gender.value)

    if db.select('Users').get().where(schema.dict()).data:
        return { 'msg': 'this user already exists' }
    if db.select('Users').get().where({ "user_email": schema.user_email }).data:
        return { 'msg': 'this email is already used' }
    if db.select('Users').get().where({ "user_name": schema.user_name }).data:
        return { 'msg': 'this user already exists' }

    user = db.select('Users').insert(schema.dict())
    return { 'created_at': user['created_at'], 'updated_at': user['updated_at'] }



@router.post('/signin')
async def signup(schema: UserAuth, res: Response):
    SHA256 = hashlib.sha256()
    SHA256.update(str(schema.user_password).encode())
    schema.user_password = SHA256.hexdigest()

    user = db.select('Users').get(__id=True, user_name=True).where(schema.dict()).data

    if not user:
        return { 'msg': 'Wrong Credentials' }
    
    t = str(time.time())
    user[0]['time'] = t

    jwtToken = jwt.encode(payload=user[0], key=os.getenv('sK'), algorithm='HS256')
    fernet = Fernet(str(os.getenv('encK')).encode())
    jwtToken = fernet.encrypt(jwtToken.encode())

    res.set_cookie(key='__token', value=f'{t}:{jwtToken.decode()}')
    res.set_cookie(key='__id', value=user[0]['__id'])

    return { 'msg': 'Successfully Signed-In' }



@router.post('/signout')
async def signup(req: Request, res: Response):
    middlewareToken(req)
    res.delete_cookie(key='__token')
    res.delete_cookie(key='__id')
    return { 'msg': 'Successfully Signed-Out' } 
