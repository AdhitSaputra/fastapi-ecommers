from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from app.v1 import api

app = FastAPI(
    title="fastapi-ecommers",
    version="v1",
    openapi_url=f"/api/v1/openapi.json"
)

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
    allow_methods=["*"],
    allow_headers=["*"],
)

class CustomException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(self, http_code: int = None, code: str = None, message: str = None):
        self.http_code = http_code if http_code else 500
        self.code = code if code else str(self.http_code)
        self.message = message

@app.get("/")
def Home():
    return {"message": "Hello World!."}

app.include_router(api.api_router, prefix="/api/v1")

