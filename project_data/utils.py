import os
import numpy as np
import pickle 
import json
#import sys
#sys.path.insert(0, "H:\Python Data sceience class\VS code\API\Medi_insurance")
import config


class MediInsurance():
    def __init__(self,age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.smoker = smoker
        self.children = children
        self.region = "region_" + region

    def LoadModel(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)
    def Predict_Charges(self):
        self.LoadModel()

        region_index = self.json_data["columns"].index(self.region)

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        test_array[region_index] = 1

        print("Predicting charges for values:", test_array)
        

        predicted_charges = np.around(self.model.predict([test_array])[0], 2)
        print("charges are:", predicted_charges)


        return predicted_charges



if "__name__" == "main":

    age = 26
    sex = "male"
    bmi = 25.5
    children = 0
    smoker = "no"
    region = "southwest"
    medi_insu = MediInsurance(age, sex, bmi, children, smoker, region)
    medi_insu.Predict_Charges()