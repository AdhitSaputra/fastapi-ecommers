from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from app.v1 import api

app = FastAPI()

# Database Middleware
app.add_middleware(SQLAlchemyMiddleware,
    db_url="sqlite:///db.sqlite",
    engine_args={
        "echo": False,
        "pool_pre_ping": True,
        "pool_size": 10,
        "max_overflow": 64
    }
)

# Cors Middleware
app.add_middleware(CORSMiddleware,
    allow_origins=["127.0.0.1"],
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*"
)

@app.get("/")
def Home():
    return {"message": "Hello World!."}

app.include_router(api.api_router)

