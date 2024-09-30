from sqlalchemy import Boolean, Column, Integer, String
from src.v1.setting.database  import Base 

# (Base) Declara Usuario como una entidad de la BD 
class Usario(Base):
    __tablename__ = 'Usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), unique=True)


    



    