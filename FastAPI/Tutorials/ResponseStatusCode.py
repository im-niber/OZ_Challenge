from fastapi import FastAPI
app = FastAPI()

"""
Response Status Code

데코레이터에 상태 코드를 추가할 수 있습니다.
숫자로 입력 받거나, 파이썬의 http.HTTPStauts 같은 IntEnum을 입력받을 수도 있습니다.

fastapi.status 도 사용 가능합니당.
"""
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

from fastapi import status

@app.get("/items", status_code=status.HTTP_200_OK)
async def read_items():
    return {"items": "items"}