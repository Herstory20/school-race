from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import students

# créer les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SchoolRace API")

# CORS (frontend Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en prod stricte plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)


@app.get("/")
def root():
    return {"status": "SchoolRace backend running"}
