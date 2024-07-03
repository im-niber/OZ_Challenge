from fastapi import FastAPI, Query
from typing import Union

"""
app 변수는 FastAPI 클래스의 인스턴스가 됩니다.
모든 API를 생성하기 위한 상호작용의 주요지점이 될 것입니다.
uvicron 이 찾모하는 app과 동일합니다.

만약 이름을 바꾼다면 my_awesome_api
uvicron main:my_awesome_api --reload 명령어를 실행해야 fastapi가 실행됩니다
"""
app = FastAPI()

"""
경로 설정, "/" 에 대한 GET 작동을 사용하는 요청을 받을때마다
FastAPI에 의해 호출됩니다.
"""
@app.get("/")
async def root():
    return {"message": "Hello World"}