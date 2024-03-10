from treleadb import Database
import os
import json
from dotenv import load_dotenv
load_dotenv()

db = Database(dbName='BlogApp', secretKey=os.getenv('sK'))

Users = db.setupCollection('Users').modelSchema({
    "user_name": str,
    "user_email": str,
    "user_gender": str,
    "user_password": str
}).migrate()

Todos = db.setupCollection('Blogs').modelSchema({
    "user_id": str,
    "blog_title": str,
    "blog_description": str
}).migrate()


print(json.dumps(Users, indent=4, default=str))
print(json.dumps(Todos, indent=4, default=str))