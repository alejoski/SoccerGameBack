from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from src.v1.setting.jwt_manager import  validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) :
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['correo'] != "aa":
            raise HTTPException(status_code=403, detail="Credenciales Invalidas")