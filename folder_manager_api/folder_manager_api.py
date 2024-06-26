import os
import configparser
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
from folder_manager import Folder, FolderError
import secrets

# Read configuration file
config = configparser.ConfigParser()
config_file = 'folder_manager_api.config'

# Create a default configuration file if it doesn't exist
if not os.path.exists(config_file):
    config['server'] = {'port': '8000'}
    config['auth'] = {'username': 'admin', 'password': 'password'}
    with open(config_file, 'w') as configfile:
        config.write(configfile)

# Read the configuration file
config.read(config_file)
port = int(config['server']['port'])
username = config['auth']['username']
password = config['auth']['password']

# Initialize the FastAPI app with metadata
app = FastAPI(
    title="Folder Manager API",
    description="This API allows managing folders and files, including creating, listing, counting, and deleting files and folders.",
    version="1.0.0",
)

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, username)
    correct_password = secrets.compare_digest(credentials.password, password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

class CreateFileRequest(BaseModel):
    file_name: str
    content: Optional[str] = ""

class PathOperation(BaseModel):
    path: str

class FileOperation(BaseModel):
    path: str
    file_name: str

@app.post("/create_folder/")
def create_folder(operation: PathOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        if folder.create_folder():
            return {"message": "Folder created successfully"}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/list_files/")
def list_files(operation: PathOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        files = folder.list_files()
        return {"files": files}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/count_files/")
def count_files(operation: PathOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        count = folder.count_files()
        return {"file_count": count}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/create_file/")
def create_file(operation: PathOperation, request: CreateFileRequest, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        if folder.create_file(request.file_name, request.content):
            return {"message": f"File '{request.file_name}' created successfully"}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/delete_file/")
def delete_file(operation: FileOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        if folder.delete_file(operation.file_name):
            return {"message": f"File '{operation.file_name}' deleted successfully"}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/delete_folder/")
def delete_folder(operation: PathOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    try:
        if folder.delete_folder():
            return {"message": f"Folder '{operation.path}' deleted successfully"}
    except FolderError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/folder_exists/")
def folder_exists(operation: PathOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    return {"exists": folder.folder_exists()}

@app.post("/file_exists/")
def file_exists(operation: FileOperation, username: str = Depends(get_current_username)):
    folder = Folder(operation.path)
    return {"exists": folder.file_exists(operation.file_name)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
