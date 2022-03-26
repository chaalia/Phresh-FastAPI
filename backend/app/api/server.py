from ensurepip import version
from turtle import title
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def get_application():
    app = FastAPI(title="Phresh", version="1.0.0")

    app.add_middleware(
        CORSMiddleware, 
        allow_origin=["*"],
        allow_credentials=True,
        allow__methods=["*"],
        allow_headers=["*"]
    )
    return app


app = get_application()