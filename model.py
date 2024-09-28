from sqlalchemy import Boolean, Column, Integer, String
from database  import Base 

class Usario(Base):
    __tablename__ = 'Usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), unique=True)


    
# class Jugadas(Base):
#     __tablename__ = "jugadas"
    
#     id = Column(Integer, primary_key=True, index=True)
#     key = Column(String(50))
    