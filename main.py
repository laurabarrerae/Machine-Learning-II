from typing import Union
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
