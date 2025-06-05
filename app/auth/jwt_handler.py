import time
import jwt
from decouple import config

JWT_SECRET= config("secret")
JWT_ALGORITHM = config("algorithm")

# Function to return the generated token
def token_response(token:str):
    return{
        "access_token": token,
        "token_type": "bearer"
    }

# Function for Signing the JWT token
def signJWT(user_id: str):
    payload={
        "user_id": user_id,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded_token=jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {
            "error": "Invalid token or expired token"
        }

