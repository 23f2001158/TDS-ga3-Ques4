from fastapi import FastAPI
from mailroom import router

app = FastAPI()
app.include_router(router)
