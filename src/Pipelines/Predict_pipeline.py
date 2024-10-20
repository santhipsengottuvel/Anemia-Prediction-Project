import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import save_object
from src.utils import load_object
from dataclasses import dataclass


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path="artifacts/model.pkl"
            preprocessor_path="artifacts/preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        


class CustomData:
    def __init__(self,Gender:int,Hemoglobin:float,MCH:float,MCHC:float,MCV:float):
        self.Gender=Gender

        self.Hemoglobin=Hemoglobin

        self.MCH=MCH

        self.MCHC=MCHC

        self.MCV=MCV

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "Gender":[self.Gender],
                "Hemoglobin":[self.Hemoglobin],
                "MCH":[self.MCH],
                "MCHC":[self.MCHC],
                "MCV":[self.MCV]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)

