# Folder Manager API

folder_manager_api is a FastAPI wrapper for the [folder_manager](https://pypi.org/project/folder-manager/) package, providing a RESTful API for managing folders and files.

## Features:

- Create and delete folders
- List files in a folder
- Count files in a folder
- Create and delete files
- Check if a folder or file exists
- List and count files with specific extensions
- Basic authentication
- Logging functionality

## Installation:

You can install folder_manager_api using pip:

```python
pip install folder_manager_api
```

## Usage:

To run the API server:

```python
folder_manager_api

or

python -m folder_manager_api
```

This will start the server on [http://localhost:8000](http://localhost:8000/).

### API Endpoints and Sample Requests:

1. GET /: Health check endpoint
    
    ```python
    curl -X GET http://localhost:8000/
    ```
    
2. POST /create_folder/: Create a new folder
    
    ```python
    curl -X POST http://localhost:8000/create_folder/ -H "Content-Type: application/json" -d '{"path": "/path/to/new/folder"}'
    ```
    
3. POST /list_files/: List files in a folder
    
    ```python
    curl -X POST http://localhost:8000/list_files/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder"}'
    ```
    
4. POST /list_files_with_extension/: List files with a specific extension
    
    ```python
    curl -X POST http://localhost:8000/list_files_with_extension/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder", "extension": ".txt"}'
    ```
    
5. POST /count_files/: Count files in a folder
    
    ```python
    curl -X POST http://localhost:8000/count_files/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder"}'
    ```
    
6. POST /count_files_with_extension/: Count files with a specific extension
    
    ```python
    curl -X POST http://localhost:8000/count_files_with_extension/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder", "extension": ".txt"}'
    ```
    
7. POST /create_file/: Create a new file
    
    ```python
    curl -X POST http://localhost:8000/create_file/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder", "file_name": "newfile.txt", "content": "Hello, World!"}'
    ```
    
8. POST /delete_file/: Delete a file
    
    ```python
    curl -X POST http://localhost:8000/delete_file/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder", "file_name": "file_to_delete.txt"}'
    ```
    
9. POST /delete_folder/: Delete a folder
    
    ```python
    curl -X POST http://localhost:8000/delete_folder/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder/to/delete"}'
    ```
    
10. POST /folder_exists/: Check if a folder exists
    
    ```python
    curl -X POST http://localhost:8000/folder_exists/ -H "Content-Type: application/json" -d '{"path": "/path/to/check"}'
    ```
    
11. POST /file_exists/: Check if a file exists
    
    ```python
    curl -X POST http://localhost:8000/file_exists/ -H "Content-Type: application/json" -d '{"path": "/path/to/folder", "file_name": "file_to_check.txt"}'
    ```
    

Note: All endpoints require basic authentication. Add -u username:password to your curl commands or use appropriate authentication in your HTTP client.

## Configuration:

The API can be configured using a folder_manager_api.config file. If not present, a default configuration will be created.

Sample configuration file (folder_manager_api.config):

```
[server]
port = 8000

[auth]
username = admin
password = password

[logging]
log_size = 1073741824
```

### Configuration details:

1. server section:
    - port: The port number on which the API server will run. Default is 8000.
2. auth section:
    - username: The username for basic authentication.
    - password: The password for basic authentication.
3. logging section:
    - log_size: Maximum size of the log file in bytes before it rotates. Default is 1073741824 (1GB).

You can modify these values to customize the API's behavior. If the configuration file is not present when the API starts, it will create a default one with these values.

## Logging:

The API logs all requests and responses to a file named folder_manager_api.log. The log file uses a rotating file handler, which means it will create new log files and archive old ones when the file size limit (specified in log_size) is reached.

## Dependencies:

- fastapi
- uvicorn
- pydantic
- folder_manager

## License:

This project is licensed under the MIT License.

## Author:

[Javer Valino](https://github.com/phintegrator)

## Links:

GitHub: https://github.com/phintegrator/folder_manager_api

## Contributing:

Contributions are welcome! Please feel free to submit a Pull Request.

## Support:

If you encounter any problems or have any questions, please open an issue on the GitHub repository.