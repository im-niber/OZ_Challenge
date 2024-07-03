from typing import Annotated
from fastapi import Cookie, FastAPI, Header
app = FastAPI()

"""
쿠키 매개변수를 Query, Path 같은 방식으로 정의할 수 있습니다
"""
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

"""
헤더 매개변수를 Query, Path 같은 방식으로 정의가능
"""
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


"""
자동변환

대부분의 표준 헤더는 하이픈(-) 문자로 구분됩니다. 하지만 python에서는 이런 변수는 유효하지 x

따라서 헤더는 기본적으로 매개변수 이름을 언더스코어에서 하이픈으로 변환하여 헤더를 추출하고 기록합니다.
또한 헤더는 대소문자 구분하지 않으므로, snake_case로 선언 가능합니다.
User-Agent 같이 대문자화할 필요가 x
만약 언더스코어를 하이픈으로 자동 변환을 비활성화 해야하는 이유가 있다면 아래 
convert_underscore를 false로 선언하십시오
"""
@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}

"""
중복 헤더

동일 헤더에 여러 값이 포함될 수 있습니다. 이런 경우 리스트로 받을 수 있씀니다

X-Token: foo
X-Token: bar
의 경우, 아래 응답으로 반환됩니다
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
"""
@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}