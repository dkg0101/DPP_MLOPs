import os,sys
import pandas as pd
from exception import CustomException
from logger import logging
from utils.utils import load_object



class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity


    def get_data_as_dataframe(self):
        
        try:

            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')

            return df
        
        except Exception as e:
            raise CustomException(e,sys)
        

class PredictionPipeline:
    

    def __init__(self) :

        self.preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
        self.model_path = os.path.join('artifacts','model.pkl')


    def predict(self,data):
        try:
            preprocessor = load_object(file_path=self.preprocessor_path)
            model = load_object(file_path=self.model_path)


            logging.info('Transforming input data..')
            transformed_data = preprocessor.transform(data)
            
            logging.info('Making prediction')
            prediction = model.predict(transformed_data)

            return prediction
        
        except Exception as e:
            raise CustomException(e,sys)
        

