from fastapi import FastAPI
from typing import Annotated

app = FastAPI()

"""
경로 매개변수

item_id 값이 함수의 item_id 인자로 전달됩니다.
"""
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

"""
타입이 있는 매개변수

함수가 받은 값은 문자열이 아니라 int 입니다.
즉, 타입 선언을 하면 FastAPI는 자동으로 요청을 파싱합니다.

경로에 foo, 4.2 같은 값을 넣는다면 http 오류가 발생합니다. 데이터검증을 하기 때문입니다

타입 선언의 다른 장점으로 API 문서에서도 정수형으로 명시가 되어서 보여집니다.
"""
@app.get("/items/{item_id2}")
async def read_item(item_id2: int):
    return {"item_id": item_id2}

"""
순서 문제

아래와 같은 경로가 있을 때 자기 자신의 정보를 가져오는 함수를 먼저 실행하려면
/users/{user_id} 이전에 먼저 선언해야합니다.
"""
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

"""
파일 경로 선언
"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

"""
Query 말고 이번엔 Path를 import 하여 비슷하게 할 수 잇습니다
"""
from fastapi import Path
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    return results


"""
Number Validation

1보다 크거나 같아야 하는경우
"""
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

"""
0 <= item_id <= 1000
gt: 보다 큼
ge: 크거나 같음
lt: 보다 작음
le: 작거나 같음
"""
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[
        int, 
        Path(title="The ID of the item to get",gt=0, le=1000)],
    q: str,
): pass

"""
나중에 보게 될 query, path 등 기타 클래스는 Param 클래스의 하위 클래스입니다.

Query, Path를 import 하면 실제로는 함수입니다. 호출시에 같은 이름의 클래스 인스턴스를
반환합니다. 

이것의 장점은 에디터에서 해당 유형에 대한 오류를 표시하지 않기 위해서입니다.
"""