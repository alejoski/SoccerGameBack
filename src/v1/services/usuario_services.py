from unittest import result
from src.v1.models.usuario_model import Usuario as UsuarioModel

class UsusarioServices():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_usuarios(self):
        result = self.db.query(UsuarioModel).all()
        return result
        