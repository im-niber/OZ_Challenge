from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

"""
Use HTTPException

HTTPException을 사용하여 에러를 리턴하는 방식

이는 일반적인 파이썬의 예외입니다. 반환하지 않고, raise 합니다.
즉, 경로 함수내부에서 HTTPException을 발생시키면 나머지 코드가 실행되지
않고 해당 요청을 바로 종료하고 클라이언트로 전송합니다.

값 보다 예외를 반환하는것의 이점은 종속성 및 보안 섹션에서 살펴보겠슴니당

HTTPException이 발생하면 str 뿐만 아니라 JSON으로 변환할 수 있는
모든 타입을 detail 파라미터로 전달할 수 있습니다. list, dict ...
FastAPI에 의해 처리됩니다.
"""
items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

"""
Add Custom headers

HTTP 오류에 사용자 정의 헤더를 추가하는 것이 유용한 상황이 있습니다.
예를들어 일부 보안 유형의 경우 코드에서 직접 사용할 필요는 없지만
고급 시나리오에 필요한 경우 사용자 정의 헤더를 추가할 수 있습니다.
"""
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

"""
Install Custom Exception Handlers

예외 처리기를 만들어서 처리할 수 있습니다.
사용자 지정예외를 만들고, FastAPI로 전역적으로 처리하고자한다면, 
@app.exception_handler() 데코레이터를 추가하면 됩니다.

아래 코드에서, yolo 를 요청하게되면 저희가 정의한 UnicronException이 발생하고,
이를 처리하는 핸들러도 우리가 만든 핸들러가 담당하게됩니다.
"""

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


"""
Override the default Exception handler

FastAPI에는 몇 가지 기본 예외 처리기가 있습니다. 이러한 처리기는
HTTPException을 발생시킬 때와 요청에 잘못된 데이터가 있을 때 기본
JSON 응답 반환하는 역할을 담당합니다. 이를 재정의하여 커스텀이 가능합니다
"""
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}

"""
RequestValidationError vs ValidationError

RequsetValidationError는 Pydantic의 ValidationError의 하위클래스입니다.
FastAPI는 이를 사용하여 response_model 에서 Pydantic 모데을 사용하고 데이터에 오류가
있는 경우 로그에 표시합니다. 그러나 클라이언트는 볼 수 없고, 대신 HTTP 상태코드 500 내부 서버 오류를
받게됩니다. 이렇게 해야하는 이유는 응답이나 코드의 어느 곳에 Pydantic ValidationError는 실제 코드버그이기
때문입니다. 그리고 오류를 수정하는 동안 클라이언트는 보안 취약점을 노출할 수 있으므로 내부 정보에 액세스해서는 x
"""
from fastapi import status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item

"""
위 코드에서

{
 "title": "towel",
 "size": "XL"
}
size에 대한 오류를 발생하는 json을 요청으로 보내면, 아래와 같은 응답을 받게됩니다.

{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "towel",
    "size": "XL"
  }
}
"""

"""
Starlette HTTPException

FastAPI에는 자체 HTTP 예외가 있습니다. Starlette과 달리 세부필드에
JSON을 허용합니다.

하지만 예외 핸들러를 등록할 때는 Starlette의 HTTPExcetpion에 등록해야합니다. 이렇게하면
Starlette 내부 코드의 일부 또는 Starlette 확장 프로그램이나 플러그인에서 
Starlette HTTP 예외가 발생하면 핸들러가 이를 포착하여 처리할 수 있습니다.
"""