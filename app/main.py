from typing import Union

from fastapi import FastAPI

from database.database import Base, engine
from router.main_router import main_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(main_router)
