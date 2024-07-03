from fastapi import FastAPI, Path, Query, Body
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

"""
위의 선언한 Pydantic의 BaseModel로 만든 모델을
요청할 때 넘겨줄 수 있습니다.

위 모델에선 description, tax는 옵셔널이라 name, price만 넘겨주면 되겠져

그리고 GET 메소드는 본문이 없다는 점을 알아둬야합니다
"""
@app.post("/items/")
async def create_item(item: Item):
    return item

"""
결과 FastAPI는 다음과 같이 동작합니다.

- 요청의 본문을 JSON으로 읽습니다.
- 필요하다면 대응되는 타입으로 변환합니다
- 데이터를 검증합니다
    - 만약 유효하지 않다면 정확히 에러를 반환합니다
- 매개변수 item 에 포함된 수신 데이터를 제공합니다.
    - 함수 내에서 매개변수를 Item 타입으로 선언하였기 때문에 그에 대한 어트리뷰트, 
    자동완성 기능등을 받을 수 있습니다
- 모델을 위한 JSON 스키마 정의를 생성합니다.
- 이러한 스키마는 생성된 OpenAPI 스키마 일부가 될것이며, 자동 문서화 UI에 사용됩니다.
"""

"""
Request Body + Path Parameter + Query Parameter

FastAPI는 경로 매개변수와 일치하는 매개변수는 url에서 가져와야 하는 것을 알고있고,
Pydantic 모델로 선언된 매개변수는 request body 에서 가져와야 하는것을 알고있습니다 !

그러면, Query Parameter도 같이 사용가능하겠져 ? yes

인지하는 방식은, path에 item_id가 있으니까 얘는 경로 매개변수로 인지합니다.
쿼리 매개변수는 단일 유형, raw type?(itn, float, str, bool) 같은 경우 쿼리 매개변수로 해석합니다.
Pydantic모델 타입이면 request body로 해석됩니다
"""
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

"""
Pydantic 없이도 가능합니다. Body 매개변수를 사용하면됩니다. 요건 차차 살펴보겠습니다
"""

"""
Path, Query 같이 사용
"""
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None, # 옵셔널
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


"""
여러 개의 Body Parameter

예상하는 Body, key 값이 있어야함니다 !
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
"""
class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


"""
단일 타입을 body로 받는 방법, 0보다 커야함
예상 body
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

"""
body parameter embed

하나의 바디 파라미터에서도 키값을 통한 요청이 가능하다. 예상 body
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
} 또는
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


"""
Field.

Pydantic의 Field를 사용하여 모델 내 검증 및 메타데이터를 선언할 수 있습니다.
"""
from pydantic import Field
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results