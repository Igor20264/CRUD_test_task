# 19.09.2023 21:39:45
# Тут был Хлеб

# 25.09.2023 18:42:54
# Я снова здесь ...

from fastapi import FastAPI

from user.router import router as router_user
from booking.router import router as router_booking
app = FastAPI()

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(router_user)
app.include_router(router_booking)