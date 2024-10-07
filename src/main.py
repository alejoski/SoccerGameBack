from fastapi import FastAPI
from src.v1.setting.database import engine
from src.v1.setting import database
from src.v1.routers import usario_router
from src.v1.routers import Jugadas_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Soccer Game - API"
app.version = "0.0.1"


# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://localhost:4200", "https://cuponerapre.uniandes.edu.co", "https://cuponera.uniandes.edu.co"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(usario_router.router)
app.include_router(Jugadas_router.router)

database.Base.metadata.create_all(bind=engine)


     

@app.get("/")
async def root():
    return {"message":"Activo!"}
