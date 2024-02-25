import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

list_of_folders = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/data_validation.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py"  , 
    "src/constants/__init__.py",
    "src/config/__init__.py",
    "src/entity/__init__.py",
    "src/utils/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "requirements.txt",
    "requirements_dev.txt",
    "init_setup.sh",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "notebooks/experiment.ipynb",
   "github/workflows/.gitkeep"
]



for filepath in list_of_folders:
    filepath = Path(filepath)
    folders,filename = os.path.split(filepath)

    if folders != '':
        os.makedirs(folders,exist_ok=True)
        logging.info(f"Creating directory:{folders}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        logging.info(f"Creating file:{filename}")
        with open(file=filepath,mode='w') as file:
            pass
    else:
        logging.info(f"file :{filename} already exists")
    

