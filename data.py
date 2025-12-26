from typing import Optional

# Userクラス
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
user_list = [
    User(id=1, name="内藤"),
    User(id=2, name="辻"),
    User(id=3, name="鷹木")
]

# 指定されたユーザIDに鯛尾するユーザを
# user_listから検索する関数
# 引数：ユーザID（整数）
# 戻り値：UserオブジェクトまたはNone（見つからない場合）
def get_user(user_id: int) -> Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user
    return None


class Book:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category
        
# ダミーの書籍情報リスト
# category"technical:技術書、comics:コミック、magazine:雑誌"
books = [
    Book(id="1", title="Python入門", category="technical"),
    Book(id="2", title="はじめてのプログラミング", category="technical"),
    Book(id="3", title="すすむ巨人", category="comics"),
    Book(id="4", title="DBおやじ", category="comics"),
    Book(id="5", title="週刊ダイヤモンド", category="magazine"),
    Book(id="6", title="ザ・社長", category="magazine")
]

# カテゴリに基づいて書籍を検索する関数
# もしcategoryがNoneなら、すべての書籍を返す
def get_books_by_category(
    category: Optional[str] = None
)-> list[Book]:
    if category is None:
        # カテゴリーの指定がない場合は全ての書籍を返す
        return books
    else:
        return [book for book in books if book.category == category]