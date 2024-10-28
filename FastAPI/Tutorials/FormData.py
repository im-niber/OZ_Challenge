from typing import Annotated
from fastapi import FastAPI, Form
app = FastAPI()
"""
JSON 형식 대신 Form Data를 요청으로 받을 수 있습니다.

pip install python-multipart fastapi
from fastapi import Form
"""
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

"""
예시에서는 사용자 이름과 비밀번호를 form field에 보내고 있습니다.

form 형식을 사용하려면 명시적으로 선언해야합니다. 선언이 없다면
매개변수가 쿼리 매개변수 또는 JSON으로 해석하기 때문입니다.

"""