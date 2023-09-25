from fastapi import FastAPI

from user.router import router as router_user

app = FastAPI()

app.include_router(router_user)