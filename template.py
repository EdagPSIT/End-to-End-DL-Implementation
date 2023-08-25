import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "DeepLearningClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath) # Getting WindowsPath object
    filedir, filename = os.path.split(filepath) #Splitting the windowspath into folder name and file name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {} for file: {}".format(filedir,filename))

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #creating an empty file only
            logging.info("Creating empty file: {}".format(filepath))
    
    else:
        logging.info("{} is already exists".format(filename))