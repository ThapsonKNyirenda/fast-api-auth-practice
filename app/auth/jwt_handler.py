# This file is responsible for signing, decoding, encoding, returning JWT tokens, and verifying them.


import time
import jwt
from decouple import config

JWT_SECRET= config("secret")
JWT_ALGORITHM = config("algorithm")