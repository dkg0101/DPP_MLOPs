from logger import logging
from exception import CustomException
from sklearn.model_selection import train_test_split
from pathlib import Path
from dataclasses import dataclass
from utils.utils import read_sql_data
import pandas as pd
import sys,os



@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("data ingestion started...")
        try:
            logging.info('Reading data from mysql')
            df = read_sql_data()

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" Saved the raw dataset in artifact folder")
            
            logging.info("Performing train test split...")
            train_data,test_data=train_test_split(df,test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

                       
            logging.info(f"data ingestion part completed. \n train_data_path:{self.ingestion_config.train_data_path},\n test_data_path: {self.ingestion_config.test_data_path}")
            
            return (
                               
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )

        except Exception as e:
            logging.info(f'{e}')
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()





