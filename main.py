# 19.09.2023 21:39:45
# Тут был Хлеб

# 25.09.2023 18:42:54
# Я снова здесь ...

from fastapi import FastAPI

from src.user.router import router as router_user
from src.booking.router import router as router_booking

app = FastAPI()
print("DSSSD")
app.include_router(router_user)
app.include_router(router_booking)