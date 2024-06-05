import os
import shutil
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Upload a file</title>
        </head>
        <body>
            <h1>Upload a file</h1>
            <form action="/uploadfile/" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return content

@app.get('/hello')#decorator function (concepto de python avanzado, funcion q genera funciones)
def hello(): 
    return "Hellooo"

@app.get('/bye')#decorator function (concepto de python avanzado, funcion q genera funciones)
def hello(): 
    return "Bye...."

@app.get('/led/{led_number}/{status}')
def change_led_state(led_number:str, status:int):
    '''TBD logic to turn led on'''
    str_status = 'ON' if status >0 else 'OFF'
    return f"led {led_number} turned {str_status}"


@app.post('/uploadfile')
def upload_file(file:UploadFile = File(...)):
    try:
        uploads_folders = os.getcwd() + '/uploads/'
        os.makedirs(upload_file, exist_ok=True)


        with open(uploads_folders+file.filename,"wb+") as f:
            shutil.copyfileobj(file, f)
        return "file created"
    
    except Exception as e: 
        return f"Could not submit file error {e}"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)