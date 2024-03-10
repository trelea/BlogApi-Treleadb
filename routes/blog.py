from fastapi import APIRouter, Request, Response
from uuid import UUID
from .middleware import middlewareToken
from .models import Blog
from treleadb import TreleadbClient
import os


db = TreleadbClient(dbName='BlogApp', secretKey=os.getenv('sK'))


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/')
async def get_blogs(req: Request):
    middlewareToken(req)
    blogs = db.select('Blogs').get()
    return blogs.data



@router.get('/{blog_id}')
async def get_blog(req: Request, blog_id: str):
    middlewareToken(req)
    blog = db.select('Blogs').get().where({ '__id': blog_id })
    return blog.data[0]



@router.post('/')
async def post_blog(req: Request, res: Response, schema: Blog):
    middlewareToken(req)
    schema.user_id = str(req.cookies['__id'])
    blog = db.select('Blogs').insert(schema.dict())
    return blog



@router.put('/{blog_id}')
async def edit_blog(req: Request, blog_id: str, schema: Blog):
    middlewareToken(req)
    schema.user_id = str(req.cookies['__id'])
    blog = db.select('Blogs').update(schema.dict()).where({ '__id': blog_id })
    return blog.data[0]



@router.delete('/{blog_id}')
async def delete_blog(req: Request,blog_id: str):
    middlewareToken(req)
    blog = db.select('Blogs').delete({ '__id': blog_id })
    return blog.data
