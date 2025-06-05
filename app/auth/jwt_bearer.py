from fastapi import Depends, Request, HTTPException
from fastapi import security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import decodeJWT
bearer_scheme = HTTPBearer()

class jwtBearer(HTTPBearer):
    
    def __init__(self,auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)
        
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme.lower() == "bearer":
                raise HTTPException(
                    status_code=403,
                    detail="Invalid authentication scheme. Use 'Bearer'."
                )
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403,
                detail="Invalid authorization code."
            )
    
    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False
        payload = decodeJWT(jwtoken)
        if payload:
            isTokenValid = True
        return isTokenValid
        
        
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    payload = decodeJWT(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload 