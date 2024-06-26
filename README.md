
# Folder Manager

Folder Manager is a simple Python package for managing folders and files. It provides methods to create folders, list files, count files, create files, delete files, move files, and copy files with optional verbose output.

## Installation

You can install the package via pip:

```python
pip install folder_manager
```

## Usage

### Importing the Folder class

First, import the `Folder` class from the `folder_manager` package:

```python
from folder_manager import Folder
```

### Creating a Folder Instance

Create an instance of the `Folder` class by specifying the folder path and an optional verbose flag:

```python
folder = Folder('C:\\path\\to\\folder', verbose=True)
```

### Creating a Folder

To create the specified folder, use the `create_folder` method:

```python
if folder.create_folder():
    print("Folder created successfully.")
else:
    print("Failed to create folder.")
```

### Checking if a Folder Exists

To check if the folder exists, use the `folder_exists` method:

```python
if folder.folder_exists():
    print("Folder exists.")
else:
    print("Folder does not exist.")
```

### Listing Files in a Folder

To list all files in the folder, use the `list_files` method:

```python
files = folder.list_files()
print(f"Files: {files}")
```

### Counting Files in a Folder

To count the number of files in the folder, use the `count_files` method:

```python
file_count = folder.count_files()
print(f"Number of files: {file_count}")
```

### Creating a File

To create a file in the folder, use the `create_file` method:

```python
if folder.create_file('example.txt', 'Hello, world!'):
    print("File created successfully.")
else:
    print("Failed to create file.")
```

### Deleting a File

To delete a file from the folder, use the `delete_file` method:

```python
if folder.delete_file('example.txt'):
    print("File deleted successfully.")
else:
    print("Failed to delete file.")
```

### Moving a File

To move a file within the file system, use the `move_file` method:

```python
if folder.move_file('C:\\path\\to\\folder\\example.txt', 'C:\\new\\path\\example.txt'):
    print("File moved successfully.")
else:
    print("Failed to move file.")
```

### Copying a File

To copy a file within the file system, use the `copy_file` method:

```python
if folder.copy_file('C:\\path\\to\\folder\\example.txt', 'C:\\new\\path\\example.txt'):
    print("File copied successfully.")
else:
    print("Failed to copy file.")
```

### Deleting a Folder

To delete the folder and all its contents, use the `delete_folder` method:

```python
if folder.delete_folder():
    print("Folder deleted successfully.")
else:
    print("Failed to delete folder.")
```

## CLI Usage

You can also use the Folder Manager via the command line:

```bash
# Create a folder
folder-manager create_folder "C:\path\to\folder"

# Check if a folder exists
folder-manager folder_exists "C:\path\to\folder"

# List files in a folder
folder-manager list_files "C:\path\to\folder"

# Count files in a folder
folder-manager count_files "C:\path\to\folder"

# Create a file in a folder
folder-manager create_file "C:\path\to\folder" --file_name example.txt --content "Hello, world!"

# Delete a file from a folder
folder-manager delete_file "C:\path\to\folder" --file_name example.txt

# Move a file
folder-manager move_file "C:\path\to\folder" --file_name example.txt --dest "C:\new\path\example.txt"

# Copy a file
folder-manager copy_file "C:\path\to\folder" --file_name example.txt --dest "C:\new\path\example.txt"

# Delete a folder
folder-manager delete_folder "C:\path\to\folder"
```

## Example Script

Here is a complete example script demonstrating how to use the `Folder` class:

```python
from folder_manager import Folder

def main():
    # Create an instance of Folder with verbose=True to enable printing
    folder = Folder('C:\\path\\to\\folder', verbose=True)

    # Create a folder
    if folder.create_folder():
        print("Folder created successfully.")
    else:
        print("Failed to create folder.")

    # Check if the folder exists
    if folder.folder_exists():
        print("Folder exists.")
    else:
        print("Folder does not exist.")

    # List files in the folder
    files = folder.list_files()
    print(f"Files: {files}")

    # Count files in the folder
    file_count = folder.count_files()
    print(f"Number of files: {file_count}")

    # Create a new file in the folder
    if folder.create_file('example.txt', 'Hello, world!'):
        print("File created successfully.")
    else:
        print("Failed to create file.")

    # List files again to see the new file
    files = folder.list_files()
    print(f"Files after creation: {files}")

    # Delete the file
    if folder.delete_file('example.txt'):
        print("File deleted successfully.")
    else:
        print("Failed to delete file.")

    # List files again to confirm deletion
    files = folder.list_files()
    print(f"Files after deletion: {files}")

    # Delete the folder and its contents
    if folder.delete_folder():
        print("Folder deleted successfully.")
    else:
        print("Failed to delete folder.")

    # Create another instance of Folder with verbose=False to disable printing
    folder_silent = Folder('C:\\path\\to\\folder', verbose=False)

    # Create a folder silently (no print output)
    if folder_silent.create_folder():
        print("Folder created successfully (silent).")
    else:
        print("Failed to create folder (silent).")

    # Check if the folder exists silently (no print output)
    if folder_silent.folder_exists():
        print("Folder exists (silent).")
    else:
        print("Folder does not exist (silent).")

if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

[Javer Valino](https://github.com/phintegrator)

## Acknowledgements

- Python's `os`, `shutil` and `argparse` libraries