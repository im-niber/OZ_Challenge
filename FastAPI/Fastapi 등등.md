## FastAPI

파이썬의 웹 프레임워크. pydantic과 Starlette로 만들어진 프레임워크라고 한다.

타입 검증 라이브러리인 pydantic을 사용하여 스키마로 엔드포인트의 반환 타입을 정의할 수 있다. 타입 힌트 기능을 많이 사용하고 있어서, 버그의 위험이 줄었다고 볼 수 있음

또 되게 간단하게 비동기 함수를 생성하고 호출할 수 있다. 장고보다 훨씬 쉬움.

uvicorn -> asyncio -> FastAPI (middleware layer -> router -> function)으로 이어진다.

> https://rumbarum.oopy.io/post/examine-fastapi-handling-request-line-by-line-with-comment
>
> 요기 설명이 잘 되어 있다..!

### get 메소드 만드는 코드

get 메소드 코드와 반환 형태를 살펴보겠슴니다.

```python
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    ...
    return db_user  # <-- instance of `models.User`
```

간단하게 데코레이터의 get 붙이면 만들 수 있고. 리턴 타입은 models.User이지만, 데코레이터 내부에서 가로채어진(response_model 인자가 있기 때문에)다음 schemas.User로 변하고 이를 반환합니다.

## Pydantic

Python에서 가장 널리 사용되는 데이터 검증 라이브러리. 얘를 사용해서 보통 FastAPI의 스키마를 구성함. DTO와 거의 같다고 보면된다.

예시 코드

```python
from datetime import datetime
from typing import Tuple

from pydantic import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)
```

장점으로는, 타입 힌트기능, 속도(Rust 사용), JSON 스키마 생성가능, 8천개 패키지가 Pydantic을 사용하는 등의 장점이 있다.

### 모델과 스키마

모델은 실제 데이터베이스 테이블에 매핑되는 클래스라고 보면된다.

스키마는 데이터베이스와는 아무 관련이 없으며, 이러한 스키마 중 일부는 요청이 유효한 것으로 간주되기 위해 특정 API 엔드포인트에서 수신할 것으로 예상되는 데이터를 정의합니다. 다른 스키마는 특정 엔드포인트에서 반환되는 데이터를 정의합니다.

### 에러 로그

데이터가 유효하지 않은 에러라면 아래의 로그가 발생한다.

```python
try:
    User(**external_data)  
except ValidationError as e:
    print(e.errors())
    """
    [
        {
            'type': 'int_parsing',
            'loc': ('id',),
            'msg': 'Input should be a valid integer, unable to parse string as an integer',
            'input': 'not an int',
            'url': 'https://errors.pydantic.dev/2/v/int_parsing',
        },
        {
            'type': 'missing',
            'loc': ('signup_ts',),
            'msg': 'Field required',
            'input': {'id': 'not an int', 'tastes': {}},
            'url': 'https://errors.pydantic.dev/2/v/missing',
        },
    ]
    """

```

## SQL Alchemy

개발자에게 SQL의 모든 기능과 유연성을 제공하는 Python SQL 툴 및 ORM 이다. 효율적이고 고성능의 데이터베이스 액세스를 위해 설계된 잘 알려진 엔터프라이즈급 제품군을 간단한 Python 언어로 적용하여 제공함.

### 테이블 설정

항상 metadata_obj는 필수이다. 이 객체는 기본적으로 문자열 이름으로 키가 젖장된 일련의 테이블 객체를 저장하는 facade임니다.

facade pattern: 복잡한 구조 코드를 가리고, 사용하기 편하게 간편한 인터페이스를 구성하기 위한 구조 패턴.

```python
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
metadata_obj = MetaData()
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)
```

### Raw SQL문 사용한 쿼리

execute 사용하고 SQL문을 삽입해서 하는 방법으로 select 가능함 

```python
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
```

### Insert ORM

```python
from sqlalchemy import insert
stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
print(stmt) # INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)
result = conn.execute(stmt)
``` 

### Select ORM

```python
from sqlalchemy import select
stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
WHERE user_account.name = :name_1
```

### Update, Delete ORM

```python
from sqlalchemy import update
stmt = (
    update(user_table)
    .where(user_table.c.name == "patrick")
    .values(fullname="Patrick the Star")
)
print(stmt) # UPDATE user_account SET fullname=:fullname WHERE user_account.name = :name_1

from sqlalchemy import delete
stmt = delete(user_table).where(user_table.c.name == "patrick")
print(stmt) # DELETE FROM user_account WHERE user_account.name = :name_1
```