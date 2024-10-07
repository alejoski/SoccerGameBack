from math import exp
import time, datetime as datetime_d
from jwt import encode, decode
from datetime import datetime, timezone

def create_token()->str:
    
    tiempo_exp = datetime.now(tz=timezone.utc)
    print(tiempo_exp)
    delta = datetime_d.timedelta(seconds=(60*60))
    print("delta", delta)

    print("Tiemop Final", (tiempo_exp+delta))
    return ""


create_token()
