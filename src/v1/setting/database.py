from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://root:r00t@localhost:3306/soccer_game_db'

engine = create_engine(URL_DATABASE,
                       pool_size=20,
                       max_overflow=10,
                       pool_timeout=30,
                       pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()        
    try:
        yield db
    finally:
        db.close()