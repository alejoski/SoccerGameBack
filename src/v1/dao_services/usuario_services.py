from traceback import print_tb
from unittest import result
from src.v1.models.usuario_model import Usuario as UsuarioModel
from src.v1.dto_schemas.usuario_dto import UsuarioDTO

class UsusarioServices():

    def __init__(self, db) -> None:
        self.db = db

    def create_usuario(self, usuario: UsuarioDTO):
        print(usuario)
        new_user = UsuarioModel(**usuario.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def get_usuarios(self):
        result = self.db.query(UsuarioModel).all()
        return result
    
    def get_usuario_by_email(self, email):
        print("Llego al servicio get_usuario_by_email()", email)
        result = self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        return result
        