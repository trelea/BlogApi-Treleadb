from fastapi import FastAPI
from routes import auth, blog

app = FastAPI(openapi_prefix='/api/v1')

# Authetication Routes
app.include_router(auth.router)

# CRUD Blog Routes
app.include_router(blog.router)