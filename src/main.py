from fastapi import FastAPI
from src.v1.setting.database import engine
from src.v1.setting import database
from src.v1.routers import usario_router
from src.v1.routers import Jugadas_router

app = FastAPI()
app.title = "Soccer Game - API"
app.version = "0.0.1"


#Routers
app.include_router(usario_router.router)
app.include_router(Jugadas_router.router)

database.Base.metadata.create_all(bind=engine)


     

@app.get("/")
async def root():
    return {"message":"Activo!"}
