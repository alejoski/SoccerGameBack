from math import exp
import time, datetime as datetime_d
from traceback import print_tb
from fastapi import Request, HTTPException, status
from jwt import encode, decode, InvalidTokenError
from datetime import datetime, timezone


def create_token(data: dict)->str:
    
    #calculo de la fecha e increcremento del tiempo de sesion 
    hora_actual = datetime.now(tz=timezone.utc)    
    #60 Segundos * 60 MInutos = 1 Hora 
    delta = datetime_d.timedelta(seconds=(60*60))        
    tiempo_exp = hora_actual+delta

    fecha_exp_UNIX= time.mktime( tiempo_exp.timetuple())

    token : str = encode({"email":data['email'], "exp":(fecha_exp_UNIX)}, key="my_secret_key_SG", algorithm="HS256")
    return token



# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)
    
#     async def __call__(self, request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             token = credentials.credentials
#             if not True: #self.validate_token(token):
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             return token
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")


 

def validate_token(token: str)-> dict:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print("Validatoken")
        print(token)

        data : dict =  decode(token, key="my_secret_key_SG", algorithms=["HS256"])
        print("Decodifica token")

    except InvalidTokenError:
        raise credentials_exception

    return data