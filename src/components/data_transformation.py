from logger import logging
from exception import CustomException
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer
from utils.utils import save_object
from dataclasses import dataclass
import numpy as np
import pandas as pd
import os,sys,pickle

@dataclass
class DataTransformationConfig:
    preprocessor_object_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:

    def __init__(self):
            self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
            try:
                logging.info('Data Transformation initiated...')

                # Define numerical and categorical columns
                categorical_cols = ['cut','color','clarity']
                numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']



                # Define custom ranking for each categorical feature
                cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
                color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
                clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']


                logging.info("Pipeline Initiated")

                num_pipeline = Pipeline(
                    steps=[
                        ('Imputer',SimpleImputer(strategy='median')),
                        ('Scaling',StandardScaler())
                    ]
                )


                cat_pipeline=Pipeline(
                    steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                    ]
                )

                preprocessor = ColumnTransformer(
                    [
                    ('num_pipeline',num_pipeline,numerical_cols),
                    ('cat_pipeline',cat_pipeline,categorical_cols)
                    ],
                    remainder='passthrough'
                )


                return preprocessor
            
            except Exception as e:
                  raise CustomException(e,sys)
    


    def initialize_data_transformation(self,train_path,test_path):
          try:
                logging.info('Reading train and test df')
                train_df= pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)

                logging.info('splitting input and target fetures..')

                target_feature = 'price'
                drop_columns = ['id','price']


                input_feature_train_df = train_df.drop(columns=drop_columns)
                target_feature_train_df = train_df[target_feature]


                input_feature_test_df = test_df.drop(columns=drop_columns)
                target_feature_test_df = test_df[target_feature]


                logging.info('Applying transformations..')

                preprocessor = self.get_data_transformation()

                input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
                input_feature_test_arr = preprocessor.transform(input_feature_test_df)


                train_arr = np.c_[input_feature_train_arr,target_feature_train_df]
                test_arr = np.c_[input_feature_test_arr,target_feature_test_df]

                logging.info('Saving preprocessor object')

                save_object(filepath=self.data_transformation_config.preprocessor_object_path,object=preprocessor)


                return (train_arr,test_arr)
          
          except Exception as e:
                raise CustomException(e,sys)


