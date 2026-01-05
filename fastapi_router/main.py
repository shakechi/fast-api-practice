from fastapi import FastAPI
from routers.categories import router as categories_router
from routers.items import router as items_router

app = FastAPI()

app.include_router(categories_router)
app.include_router(items_router)