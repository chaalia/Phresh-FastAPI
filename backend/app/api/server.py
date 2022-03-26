from ensurepip import version
from turtle import title
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title="Phresh", version="1.0.0")

    app.add_middleware(
        CORSMiddleware, 
        allow_origin=["*"],
        allow_credentials=True,
        allow__methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()