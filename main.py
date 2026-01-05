from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema, BookResponseSchema
from pydantic import BaseModel, Field

app = FastAPI()

class BookSchema(BaseModel):
    title: str = Field(..., description="タイトルの指定：必須", example="コイノボリが如く")
    category: str = Field(..., description="カテゴリの指定：必須", example="comics")
    publish_year: int = Field(default=None, description="出版年の指定：任意", example=2023)
    price: float = Field(..., gt=0, le=5000, description="価格の指定：0 < 価格 <=10000：必須", example=2500)

books: list[BookResponseSchema] = [
    BookResponseSchema(id=1, title="Python入門", category="technical"),
    BookResponseSchema(id=2, title="はじめてのプログラミング", category="technical"),
    BookResponseSchema(id=3, title="すすむ巨人", category="comics"),
    BookResponseSchema(id=4, title="DBおやじ", category="comics"),
    BookResponseSchema(id=5, title="週刊ダイヤモンド", category="magazine"),
    BookResponseSchema(id=6, title="ザ・社長", category="magazine")
]

# ----------------------------------------------------
# 書籍を追加するためのエンドポイント
# 引数：BookSchema
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book

# ----------------------------------------------------
# 書籍情報を全件取得するエンドポイント
# 引数：なし
# 戻り値：BookResponseSchemaのリスト
# ----------------------------------------------------
@app.get("/books/", response_model=list[BookResponseSchema])
def read_books():
    return books

# ----------------------------------------------------
# 書籍情報をidによって1件取得するエンドポイント
# 引数：書籍ID
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@app.get("/books/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# ----------------------------------------------------
# idに対応する書籍情報を更新するエンドポイント
# 引数：
#   書籍ID
#   BookSchema
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            update_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = update_book
            return update_book
    raise HTTPException(status_code=404, detail="Book not found")

# ----------------------------------------------------
# idに対応する書籍情報を削除するエンドポイント
# 引数：書籍ID
# 戻り値：BookResponseSchema
# ----------------------------------------------------
@app.delete("/books/{book_id}", response_model=BookResponseSchema)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
        raise HTTPException(status_code=4040, detail="Book not found")