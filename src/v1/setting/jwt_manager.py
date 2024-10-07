from math import exp
import time, datetime as datetime_d
from jwt import encode, decode
from datetime import datetime, timezone

def create_token(data: dict)->str:
    
    #calculo de la fecha e increcremento del tiempo de sesion 
    hora_actual = datetime.now(tz=timezone.utc)    
    #60 Segundos * 60 MInutos = 1 Hora 
    delta = datetime_d.timedelta(seconds=(60*60))        
    tiempo_exp = hora_actual+delta

    fecha_exp_UNIX= time.mktime( tiempo_exp.timetuple())

    token : str = encode({"correo":data['correo'], "exp":(fecha_exp_UNIX)}, key="my_secret_key_SG", algorithm="HS256")
    return token


def validate_token(token: str)-> dict:
    data : dict = decode(token, key="my_secret_key_SG", algorithms=["HS256"])
    return data

