import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "TextSummarizer"

# Define the list of files in a set
list_of_files = {
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
}

# Iterate through the list of files and create the directories if they do not exist
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it does not exist
    if filedir != "":  # Check if there is a directory part
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file {filename}')

    # Check if the file exists or is empty and create an empty file if needed
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:  # Use 'w' to create a new file
            pass  # Creating an empty file
        logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'{filename} already exists')