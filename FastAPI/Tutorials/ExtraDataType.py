from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

"""
여러 데이터 타입을 지원합니다.
아래의 추가적인 데이터 자료형을 사용할 수 있습니다:

- UUID: 표준 "범용 고유 식별자"로, 많은 데이터베이스와 시스템에서 ID로 사용됩니다.
요청과 응답에서 str로 표현됩니다.

- datetime.datetime: 파이썬의 datetime.datetime.
요청과 응답에서 2008-09-15T15:53:00+05:00와 같은 ISO 8601 형식의 str로 표현됩니다.

- datetime.date: 파이썬의 datetime.date.
요청과 응답에서 2008-09-15와 같은 ISO 8601 형식의 str로 표현됩니다.

- datetime.time: 파이썬의 datetime.time.
요청과 응답에서 14:23:55.003와 같은 ISO 8601 형식의 str로 표현됩니다.

- datetime.timedelta: 파이썬의 datetime.timedelta.
요청과 응답에서 전체 초(seconds)의 float로 표현됩니다.
Pydantic은 "ISO 8601 시차 인코딩"으로 표현하는 것 또한 허용합니다. 더 많은 정보는 이 문서에서 확인하십시오..

- frozenset: 요청과 응답에서 set와 동일하게 취급됩니다:
요청 시, 리스트를 읽어 중복을 제거하고 set로 변환합니다.
응답 시, set는 list로 변환됩니다.
생성된 스키마는 (JSON 스키마의 uniqueItems를 이용해) set의 값이 고유함을 명시합니다.

- bytes: 표준 파이썬의 bytes.
요청과 응답에서 str로 취급됩니다.
생성된 스키마는 이것이 binary "형식"의 str임을 명시합니다.

- Decimal: 표준 파이썬의 Decimal.
요청과 응답에서 float와 동일하게 다뤄집니다.
여기에서 모든 유효한 pydantic 데이터 자료형을 확인할 수 있습니다: Pydantic 데이터 자료형.
"""


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }