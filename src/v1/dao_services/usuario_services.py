from unittest import result
from src.v1.models.usuario_model import Usuario as UsuarioModel
from src.v1.dto_schemas.usuario_dto import UsuarioDTO

class UsusarioServices():

    def __init__(self, db) -> None:
        self.db = db

    def create_usuario(self, usuario: UsuarioDTO):
        new_user = UsuarioModel(**usuario.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def get_usuarios(self):
        result = self.db.query(UsuarioModel).all()
        return result
        