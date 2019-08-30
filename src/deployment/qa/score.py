import pickle
import json
import numpy as np
from azureml.core.model import Model
from azureml.monitoring import ModelDataCollector
import joblib


def init():
    # this call should return the path to the model.pkl file on the local disk.
    model_path = Model.get_model_path(model_name='model')
    
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)

# note you can pass in multiple rows for scoring
def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = np.array(data)
        result = model.predict(data)

        # you can return any data type as long as it is JSON-serializable
        return result.tolist()
    except Exception as e:
        result = str(e)
        return result

