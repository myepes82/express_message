from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from modules import read_file_as_string as reader, FileType

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
async def get_home() -> None:
    file = reader(file_name="index", file_type=FileType.HTML)
    return file    

@app.get("/about", response_class=HTMLResponse)
async def get_home() -> None:
    file = reader(file_name="about", file_type=FileType.HTML)
    return file

@app.get("/contact", response_class=HTMLResponse)
async def get_home() -> None:
    file = reader(file_name="contact", file_type=FileType.HTML)
    return file      
    

if __name__ == "__main__":
    pass