from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
app = FastAPI()


"""
리스트 필드 선언

만약 set으로 선언하게 된다면, 중복된 데이터를 포함된 요청을 받더라도
고유한 항목 집합으로 변환됩니다. 또 그에 따라 주석이 달리고 문서화됩니다
"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = [] 
    # typing 모듈내의 List 사용해도 ㄱㅊ
    # 3.9 이전에서는 위 typing 모듈을 사용해야만함

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

"""
중첩 모델
예상 body
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
"""
class Image(BaseModel):
    url: str # 아래 둘 중 하나 사용하믄 댐
    url2: HttpUrl # 유효한 url 확인하고, OpenAPI에 문서화된다
    name: str
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

"""
딕셔너리 바디

딕셔너리 형태로도 받을 수 있슴니다. 키를 아직 모르는 경우에 유용하빈다.
3.8버전 이전에서는 typing의 Dict 클래스를 사용해야합니당
"""
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights