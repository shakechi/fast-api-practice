from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User, get_books_by_category
from datetime import datetime
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Event(BaseModel):
    name: str = "未定"
    start_datetime: datetime
    participants: list[str] = []
    
external_data = {
    "name": "FastAPI勉強会",
    # "start_datetime": "2023-07-07 07:00",
    "start_datetime": "abc",
    "participants": ["山田","鈴木","田中"]
}
try:
    event = Event(**external_data)
    print("イベント名：", event.name, type(event.name))
    print("開催日時：", event.start_datetime, type(event.start_datetime))
    print("参加者：", event.participants, type(event.participants))
except ValidationError as e:
    print("データのバリデーションエラーが発生しました：", e.errors())

@app.get("/")
async def get_hello():
    return {"message":"Hello World"}

# ユーザIDをパスパラメータとして受け取り、ユーザ情報を返すエンドポイント
# 引数：ユーザID (整数)
# 戻り値：辞書型
@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    # ユーザー情報の取得
    user: Optional[User] = get_user(user_id)
    if user is None:
        return HTTPException(status_code=404,detail="User not found")
    return {"user_id": user_id, "username": user.name}

# クエリパラメータでしてされたカテゴリに基づいて書籍情報を検索し、
# 結果をJSON形式で返す
@app.get("/books/")
async def read_books(
    category: Optional[str] = None
)-> list[dict[str, str]]:
    # クエリパラメータで指定されたカテゴリに基づいて書籍を検索する
    result = get_books_by_category(category)
    # 結果をリストとして返す
    return [{
        "id": book.id,
        "title": book.title,
        "category": book.category,
    }for book in result]