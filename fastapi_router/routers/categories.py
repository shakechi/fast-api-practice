from fastapi import APIRouter
from schemas.category import Category

router = APIRouter()

@router.get("/categories/", response_model=dict)
async def read_categories():
    return {"message": "カテゴリ一覧を表示", "categoroies": []}

@router.post("/categories/", response_model=dict)
async def create_category(category: Category):
    return {"message": "カテゴリを作成", "category": category}

@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    return {"message": "カテゴリを削除", "category_id": category_id}