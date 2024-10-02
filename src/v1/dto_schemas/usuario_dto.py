from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    id: int
    user_name: str
    correo: str
    password: str

    
class UsuarioLoginDTO(BaseModel):
    correo: str
    password: str

