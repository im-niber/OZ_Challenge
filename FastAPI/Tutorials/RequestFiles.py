from typing import Annotated
from fastapi import FastAPI, File, UploadFile
app = FastAPI()

"""
업로드된 파일을 받으려면 먼저 python-multipart를 설치해야합니다.
업로드된 파일은 'form data'로 전송되기 때문입니다.

file은 Form에서 직접 상속되는 클래스입니다.

Form 형식을 받을려고 선언한 것처럼 File을 선언해야합니다.
선언하지 않는다면 쿼리 매개변수, JSON으로 해석하기 때문입니다.

file은 form-data 로 업로드 됩니다. 경로 함수 파라미터의 유형을 bytes 로 선언하면
fastapi가 파일을 읽고 내용을 바이트로 받게 됩니다. 이것의 의미는 전체 내용이 메모리에 
저장된다는 것을 의미합니다. 이 방법은 작은 파일에 적합합니다.
"""
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

"""
Uploadfile의 장점

- 매개변수의 기본값으로 file()을 사용할 필요가 없습니다.
- 'spooled'file: 최대 크기 제한까지 메모리에 저장되고 제한을 넘으면 디스크에 저장되는 파일을 사용합니다.
- 이미지, 동영상, 대용량 파일 등과 같은 파일에 대해 모든 메모리를 소모하지 않고 잘 작동합니다.
- 업로드 파일에서 메타데이터를 가져올 수 있습니다.
- file 과 유사한 비동기 인터페이스가 있습니다.
- 파일과 유사한 객체를 기대하는 다른 라이브러리에 전달할 수 있는 객체(SpooledTemporaryFile)를 노출합니다.

속성

- filename : 업로드된 원본 파일 이름이 포함된 문자열 (e.g. myimage.jpg)
- content_type: 콘텐츠유형(MIME, media 타입)이 포함된 문자열 (e.g. image/jpeg)
- file: SpooledTemporaryfile(파일형 객체) 다른 라이브러리, 함수 등에 직접 전달할 수 있는 파이썬 파일

비동기 메서드

- write(data): 파일에 데이터(str or bytes)를 씁니다.
- read(size): 파일의 크기(int) 바이트/문자를 읽습니다.
- seek(offset): 파일의 바이트 위치 오프셋(int)로 이동합니다. 
    - 예를 들어, await myfile.seek(0)는 파일의 시작부분으로 이동합니다.
    - 이 함수는 특히 await myfile.read()를 한 번 실행 후에 내용을 다시 읽어야 할 때 유용합니다.
- close(): 파일을 닫습니다.
"""
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

"""
메타데이터 추가
"""
@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}


"""
여러 파일 업로드
"""
from fastapi.responses import HTMLResponse
@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
