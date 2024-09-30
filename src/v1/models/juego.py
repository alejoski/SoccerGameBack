from sqlalchemy import Boolean, Column, Integer, String
from src.v1.setting.database  import Base 

    
class Jugadas(Base):
    __tablename__ = "jugadas"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50))
    descripcion = Column(String(300))
    posibilidades = Column(String(250))
    cambio_equipo = Boolean()
    jugada_contrario = Boolean()
    caract_aumentan = Column(String(250))
    caract_disminuyen = Column(String(250))
    caract_contrario_aumentan = Column(String(250))
    caract_contrario_disminuye = Column(String(250))



    