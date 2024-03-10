# About Project

### Authetication and CRUD Apis build with __FastAPI__ and __Treleadb__ for a simple blog platform

### Treleadb is a object database build by me trelea :) You can install my db using pip command, check repo pls: https://github.com/trelea/TreleaDB

## Installation Dependencies
```bash
pip3 install -r requirements.txt
```

## Run Application
```bash
uvicorn main:app --reload
```

## API Routes

### Authetication Routes
```javascript
POST    /api/v1/auth/signup
POST    /api/v1/auth/signin
POST    /api/v1/auth/signout
```

### CRUD Blog Routes
```javascript
GET     /api/v1/blog/
GET     /api/v1/blog/{blog_id}
POST    /api/v1/blog/
PUT     /api/v1/blog/{blog_id}
DELETE  /api/v1/blog/{blog_id}
```