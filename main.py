import uvicorn
from fastapi import Body, FastAPI, Depends
from app.auth.jwt_handler import signJWT
from app.models import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_bearer import get_current_user, jwtBearer

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


@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["Posts"])
def create_post(post:PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return{
        "message": "Post created successfully",
        "data": post
    }
    
@app.get("/users", tags=["Users"])
def get_all_users():
    return {
        "data": users
    }

# Function for creating a user
@app.post("/users", tags=["Users"])
def user_signup(user: UserSchema = Body(default=None)):
    user.id = len(users) + 1
    users.append(user)
    return {
        "message": "User created successfully",
        "data": user
    }
    
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["Users"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid email or password"
        }

@app.get("/me", tags=["Users"])
def get_logged_in_user(user: dict = Depends(get_current_user)):
    return {"message": "This is the current user", "user": user}

# This is a test comment

# Second comment for testing purposes

