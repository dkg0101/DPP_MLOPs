from logger import logging
from exception import CustomException
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
import pandas as pd
import os,sys


obj = DataIngestion()


train_data_path,test_data_path = obj.initiate_data_ingestion()

data_transformation_obj = DataTransformation()

train_arr,test_arr = data_transformation_obj.initialize_data_transformation(train_path=train_data_path,test_path=test_data_path)


model_trainer_obj = ModelTrainer()
model_trainer_obj.initate_model_training(train_array=train_arr,test_array=test_arr)