"""
python 3.10+, FastAPI 0.95 에서 권장하는
Annotated가 있습니다.

q: str | None = Non 이 코드를

q: Annotated[str | None] = None 이렇게 사용하세요
"""


from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
쿼리 매개변수

쿼리: URL에서 ? 후에 나오고, &으로 구분되는 키-값 쌍의 집합

경로 매개변수의 일부가 아닌 달느 함수 매개변수를 선언하면 "쿼리" 매개변수로 자동 해석합니다.

URL: http://127.0.0.1:8000/items/?skip=0&limit=10

에서 skip은 0을 가지고, limit는 10을 가집니다. url의 일부라서 문자열이됩니다.
하지만 타입선언을 하였기떄문에 해당 타입으로 변환 및 검증됩니다. 
"""
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""
쿼리 매개변수는 경로에서 고정된 부분이 아니기 떄문에 옵셔널일 수 있고, 기본값을 가질 수 있습니다.
위의 예시에서는 skip=0, limit=10 이라는 기본 값을 가집니다.

같은 방법으로 기본값을 None 으로 설정하여서 선택적 매개변수를 선언 가능합니다.

FastAPI는 item_id가 경로 매개변수이고 q는 경로 매개변수가 아닌 쿼리 매개변수라는 것을 알 정도로 충분히 똑똑합니다.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

"""
쿼리 매개변수 형변환
아래 함수의 경우
http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?short=true
http://127.0.0.1:8000/items/foo?short=on
http://127.0.0.1:8000/items/foo?short=yes

다 동일하게 true 값으로 함수에 전달되게 된다네요.
"""
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return 


"""
필수 쿼리 매개변수
필수로 받아야 하는 함수도 만들 수 있겠져
아래 함수는 needy를 무조건적으로 작성해야합니다.
http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
"""
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


"""
쿼리 매개변수 제한하는 여러 방식

q의 값이 주어질 때 50글자를 초과하지 않게 하려면
Query를 import해서 max_length=50 을 할당하면댐니다.
min_length 매개변수도 있습니당
pattern 매개변수에는 정규식을 정의할 수 있습니다.
"""
from fastapi import Query

@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

"""
쿼리 매개변수 리스트 / 다중 값

값들을 리스트나 다른 방법으로 여러 값을 받도록 선언할 수 있습니다.
http://localhost:8000/items/?q=foo&q=bar 가능.

주의할 점은 list 자료형으로 선언하려면 Query를 명시적으로 사용해야합니다. 그렇지 않다면
request body로 해석합니다. 
"""
from typing import List
@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items


"""
더 많은 메타데이터 선언
아래의 정보는 OpenAPI에 포함됩니다.
"""
@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    ),
):
    pass

"""
매개변수 별칭 (alias)
http://127.0.0.1:8000/items/?item-query=foobaritems

매개변수가 item-query로 하고 싶을때, python에서는 item_query 겠죠
이럴 경우에 alias를 사용하면 해결할 수 있슴니다.
"""
@app.get("/items/")
async def read_items(item_query: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if item_query:
        results.update({"item-query": item_query})
    return results


"""
Query 매개변수s
"""
@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

"""
Annotated 사용 예시
"""
from typing import Annotated
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
