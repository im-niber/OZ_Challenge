from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

"""
반환 타입을 선언할 수 있습니다.
Pydantic의 모델, 리스트, 딕셔너리 등등 사용가능합니다

반환 데이터 유효성 검사, OpenAPI 경로의 응답에 대한 JSON 스키마 추가 하는 작업을 하고,
가장 중요한 점은 출력 데이터를 반환 유형에 정의된 것으로 제한하고 필터링 하는 점입니다.
"""
@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

"""
response_model 파라미터

데코레이터 메소드의 매개변수입니다.

만약 위의 반환유형도 같이 선언한다면 이 응답모델이 우선순위를 가집니다. 
"""

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

"""
동일 입력데이터 반환
"""
# EmailStr 사용시에는 email_valiator를 설치하세요
# E.g. pip install email-validator or pip install pydantic[email]
from pydantic import EmailStr

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

# 요렇게 하시믄 안됩니다. 비밀번호가 보이기떄문에,,
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user

"""
출력 모델 추가

출력용 모델을 만들고, response_model에 선언해주면
비밀번호는 안보이겠져

만약 반환 타입도 UserOut으로 하면 에디터에서는 잘못된 반환이라고
경고를 줄것입니다. 그래서 지금 예제는 response_model로 선언해줘야합니다.
이를 극복한 에제는 아래에서 살펴보겠슴니당
"""
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


"""
Return Type and Data Filtering

이전 예제에서는 클래스가 다르기 때문에 response_model 매개변수를 사용해야했지만
이는 편집기와 도구의 지원을 받지 못하는것을 의미합니다.

보통 이 작업들은 데이터 필터링, 제거 정도의 작업이기 때문에 클래스의 상속을 사용한다면
자동완성 같은 기능을 지원받으면서도 기존 기능을 수행할 수 있습니다.
-> 상속으로 해결하겠다~
"""
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str
    
@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

"""
직접 반환하는 방식
Response 클래스(또는 하위클래스)이기 때문에 FastAPI에서 자동으로 처리됨니다
RedirectRes,JSONRes또한 Respone의 하위클래스이므로 타입에러x
"""
from fastapi import Response
from fastapi.responses import JSONResponse, RedirectResponse

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

"""
Pydantic 응답 모델 만들기 실패하는 경우
type annotation이 Pydantic type이 아니라서 실패합니다.
"""
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

"""
응답 모델 비활성화

만약 FastAPI에서 수행하는 데이터 유효성 검사, 문서화, 필터링을 원하지 않고, 편집기나 타입 검사기
지원을 받으려면 함수에 리턴 타입을 유지해야 하는 경우도 있습니다.

이런 경우에는 response_model=None을 수행하면됩니다.
응답 모델 생성을 건너뛰고, FastAPI 앱의 영향을 주지않습니다.
"""
@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

"""
응답 모델 파라미터
"""