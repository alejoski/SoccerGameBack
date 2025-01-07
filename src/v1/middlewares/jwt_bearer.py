from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException, status
from src.v1.setting.jwt_manager import  validate_token
from jwt import InvalidTokenError, encode, decode


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) :

        print("Llego a CALL")
        print(request)
        auth = await super().__call__(request)
        print("Rewuest")
        print (auth)
        data = validate_token(auth.credentials)
        print("DATA")
        print(data)
        print(data['email'])
        
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImljYXJvbmlAZ21haWwuY29tIiwiZXhwIjoxNzI5MzEwNzg2LjB9.17fOlZ9AxZylCUV9aQ11q1o0APUTjKA_pwwo2En1U6M
        #eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImljYXJvbmlAZ21haWwuY29tIiwiZXhwIjoxNzI5NDk0NjYwLjB9.QYNBA_ce8LqOifwRzReglEKl7IuHhNLIIoW5ROAC7rI
        if data['email'] != data['email']:
            raise HTTPException(status_code=403, detail="Credenciales Invalidas")
        
        return data


       


