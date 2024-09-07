from fastapi import FastAPI
from app.routes import client_routes, reservation_routes

app = FastAPI()


app.include_router(client_routes.router,
                   prefix="/clients",
                   tags=["clients"])

app.include_router(reservation_routes.router,
                   prefix="/reservations",
                   tags=["reservations"])

@app.get("/")
async def root():
    return {"message": "Hello DANI"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
