import pickle
import json
import numpy as np
from azureml.core.model import Model
from azureml.monitoring import ModelDataCollector
import joblib


def init():
    global model
    global inputs_dc, prediction_dc
    inputs_dc = ModelDataCollector("model", identifier="inputs", feature_names=["feat1", "feat2", "feat3"])
    prediction_dc = ModelDataCollector("model", identifier="predictions", feature_names=["prediction1"])
    # note here "best_model" is the name of the model registered under the workspace
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
        inputs_dc.collect(data) #this call is saving our input data into Azure Blob
        prediction_dc.collect(result) #this call is saving our prediction data into Azure Blob

        # you can return any data type as long as it is JSON-serializable
        return result.tolist()
    except Exception as e:
        result = str(e)
        return result

if __name__ == "__main__":
    init()
    run({"data": ""})
