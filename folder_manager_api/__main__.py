# __main__.py

import uvicorn
from .folder_manager_api import app

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
