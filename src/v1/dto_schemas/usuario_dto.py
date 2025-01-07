from datetime import datetime
from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    id: int
    user_name: str
    password: str
    email: str
    team_name: str
    create_date: datetime


    
class UsuarioLoginDTO(BaseModel):
    email: str
    password: str

    

