import os
from box.exceptions import BoxValueError
import yaml
from src.DeepLearningClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



# FUNCTION TO READ YAML FILES
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file: {} loaded successfully".format(path_to_yaml))
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e



# FUNCTION TO CREATE DIRECTORIES AT GIVEN PATH
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info("created directory at: {}".format(path))



#SAVING FILES AS JSON AT THE PATH GIVEN
@ensure_annotations
def save_json(path: Path, data: dict):
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info("json file saved at: {}".format(path))


# LOADING THE JSON FILE FROM THE PATH GIVEN
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    
    with open(path) as f:
        content = json.load(f)

    logger.info("json file loaded succesfully from: {}".format(path))
    return ConfigBox(content)


# FUNCTION TO SAVE BINARY FILES
@ensure_annotations
def save_binary_file(data: Any, path: Path):
    
    joblib.dump(value=data, filename=path)
    logger.info("Binary file saved at : {}".format(path))


# FUNCTION TO LOAD BINARY FILE FROM PATH GIVEN
@ensure_annotations
def load_binary_file(path: Path) -> Any:
    
    data = joblib.load(path)
    logger.info("Loaded binary file from : {}".format(path))
    return data


# FUNCTION TO GET SIZE OF FILE IN KB
@ensure_annotations
def get_size(path: Path) -> str:
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return "The file size is ~{} KB".format(size_in_kb)



# FUNCTION TO DECODING IMAGES FROM GIVEN PATH
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


# FUNCTION TO ENCODING IAMGE TO BASE64
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())