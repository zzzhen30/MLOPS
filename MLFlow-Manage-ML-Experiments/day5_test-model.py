# below code is from http://127.0.0.1:5000/#/experiments/313923835210507997/runs/714922e1862c4e5a882f15909a1cfd0a/artifacts
# in "make prediction" section 

import mlflow
logged_model = 'runs:/714922e1862c4e5a882f15909a1cfd0a/RandomForestClassifier' 
# 1. it will load the model which has been trained 

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
data =       [[
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]]  # data is from "README.md", it is usded for test to generate prediction
# 2. then the loaded model will generate prediction 

print(f"prediction is:{ loaded_model.predict(pd.DataFrame(data))}")