from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    id: int
    user_name: str
    email: str
    password: str
    team_name: str



    
class UsuarioLoginDTO(BaseModel):
    email: str
    password: str

    

