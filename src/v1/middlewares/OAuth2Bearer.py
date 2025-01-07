from fastapi import Request
import time, datetime as datetime_d
from jwt import encode, decode
from datetime import datetime, timezone

from fastapi.security import OAuth2PasswordBearer


class JWTOAuth2PasswordBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) :
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)


def create_access_token(data: dict)->str:
    
    #calculo de la fecha e increcremento del tiempo de sesion 
    hora_actual = datetime.now(tz=timezone.utc)    
    #60 Segundos * 60 MInutos = 1 Hora 
    delta = datetime_d.timedelta(seconds=(60*60))        
    tiempo_exp = hora_actual+delta

    fecha_exp_UNIX= time.mktime( tiempo_exp.timetuple())

    token : str = encode({"email":data['email'], "exp":(fecha_exp_UNIX)}, key="my_secret_key_SG", algorithm="HS256")
    return token

def validate_token(token: str)-> dict:
    data : dict = decode(token, key="my_secret_key_SG", algorithms=["HS256"])
    return data

#Ejemplo para mejorar la validacion
#tiene que validar que el token no este expirado

# def verify_jwt(self, jwtoken: str) -> bool:
#     is_token_valid: bool = False
#     try:
#         payload = decode(jwtoken, SECRET_KEY, algorithms=[ALGORITHM])
#     except JWTError:
#         payload = None
#     if payload:
#         is_token_valid = True
#     return is_token_valid
