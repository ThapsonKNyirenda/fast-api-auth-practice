import uvicorn
from fastapi import FastAPI
from app.models import PostSchema

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Sample Post",
        "content": "This is a sample post content."
    },
    {
        "id": 2,
        "title": "Another Post",
        "content": "This is another post content."
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post."
    }
]

users = []

@app.get("/", tags=["Test"])
def greet():
    return {"message": "Hello, World!"}


@app.get("/posts",tags=["Posts"])
def get_posts():
    return {"data": posts}


@app.get("/posts/{post_id}", tags=["Posts"])
def get_one_post(post_id:int):
    if post_id > len(posts):
        return {"error": "Post not found"}
    
    for post in posts:
        if post['id'] == post_id:
            return {"data": post}


@app.post("/posts", tags=["Posts"])
def create_post(post:PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return{
        "message": "Post created successfully",
        "data": post
    }
