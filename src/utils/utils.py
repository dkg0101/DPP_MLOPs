import os,sys,pickle
import pandas as pd
import numpy as np
from logger import logging
from exception import CustomException
from sklearn.metrics import r2_score



def save_object(filepath:str,object):
    try:
        folder_name = os.path.dirname(filepath)

        os.makedirs(folder_name,exist_ok=True)

        with open(filepath,'wb') as file_obj:

            logging.info(f"Saving object at {filepath}")
            pickle.dump(obj=object,file=file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def numpy_array(filepath:str,array):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,'wb') as np_file:
            logging.info(f"saving numpy array at: {filepath}")
            np.save(np_file,array)
            
    except Exception as e:
        CustomException(e,sys)

        

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)



def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
    