from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return { "Hello World" }

@app.get("/hello")
def hello():
    return {"message": "hi"}