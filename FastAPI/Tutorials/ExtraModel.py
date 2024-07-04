from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel, EmailStr
app = FastAPI()

"""
관련 모델은 보통 두 개 이상 있는것이 일반적입니다.

특히 사용자 모델의 경우 입력 모델에 비밀번호가 있어야하고
출력 모델에는 비밀번호가 없어야 하며 데이터베이스 모델에는 해시된 비밀번호가 필요할 수 있습니다.

** 사용자의 일반 텍스트 비밀번호를 저장하지 마십시오. 항상 확인할 수 있는 보안 해시를 저장하세요 ! **

다음은 일반적이 유저 모델의 경우입니다.
"""
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


"""
딕셔너리 언래핑

.model_dump: 딕셔너리로 만들어주는 pydantic 메서드. v1에서는 .dict()

user_dicr와 같은 딕셔너리를 **user_dict로 전달하면 이를 언래핑합니다.
key랑 value들을 전달한다고 보시면 됩니다.

UserInDB(**user_dict) ->
UserInDB(
    username="john",
    password="secret",
    email="john.doe@example.com",
    full_name=None,
)
"""
def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


"""
입력(요청)으로 UserIn 모델을, 출력(응답)으로 UserOut 모델을 사용하고 있습니다.
fake_save_user 함수에서는 받은 UserIn 모델을 사용해서 평문 비밀번호가 아닌 hashed_password를
DB에 저장합니다
"""
@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


"""
Reduce duplication

코드가 중복되면 버그, 보안, 코드 비동기 문제(한 곳에서는 업데이트하지만 다른 곳에서는
업데이트하지 않는경우)등이 발생할 가능성이 높습니다. 그리고 이러한 모델은 모두 많은 데이터를 공유하고
속성 이름과 유혀을 중복합니다.

이런 경우 다른 모델의 기반 역할을 하는 Base 모델을 선언할 수 있습니다.
그런 다음 해당 모델을 상속하는 하위클래스를 만들 수 있습니다.

메서드는 동일하고, 같은 동작을 합니다.
"""
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str

"""
Union을 사용할 때, 구체적인 모델이 앞에 와야합니다.
아래 예시에서는 더 구체적인 PlaneItem이 앞에오고, 좀 덜 구체적인 CarItem이
뒤에옵니다.

응답을 두 가지 유형으로 선언할 수 있습니다.

만약 타입 어노테이션이였다면, PlaneItem | CarItem 으로 가능합니다.
지금은 값으로 전달하기 때문에 Union을 사용해야합니다.
"""
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


"""
Recap

여러 개의 Pydantic 모델을 사용하고 각 경우에 대해 자유롭게
상속하세요. 엔티티가 서로 다른 '상태'를 가질 수 있어야 하는 경우 엔티티당 하나의 데이터
모델을 가질 필요는 없습니다.
"""