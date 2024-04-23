import mlflow
# below the basic structure is from "test-model.py"
# repalce the path as model_name from http://localhost:5004/#/models
model_name = 'prediction_RF'


# now there is no "staging" to set 
# see https://mlflow.org/docs/latest/model-registry.html#migrating-from-stages 


#Fetch a specific model version
model_version = 1
# set the tracking uri
mlflow.set_tracking_uri("http://0.0.0.0:5004") # so we can load the model from this port

#specify the model uri 
loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

# Predict on a Pandas DataFrame.
import pandas as pd
data = [[
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
            ]]
print(f"Prediction is : {loaded_model.predict(pd.DataFrame(data))}")