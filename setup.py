from setuptools import setup, find_packages

setup(
    name="folder_manager_api",
    version="1.0.0",
    description="A FastAPI wrapper for the folder_manager package, providing a RESTful API for managing folders and files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Javer Valino",
    url="https://github.com/phintegrator/folder_manager_api",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "folder_manager",
    ],
    entry_points={
        "console_scripts": [
            "folder_manager_api=folder_manager_api.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
