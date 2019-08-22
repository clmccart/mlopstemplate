
template for ML projects requiring DevOps practices.

# Setup
## Azure Service Connection:
1) In the "Register model with AzureML" Build [task](https://dev.azure.com/clmccarthy/mlopstemplate/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=3), select your azure subscription and authroize
    - If you do not have permissions to authorize, ask somebody who does to create a service connection

2) You will need to recreate the secrets.json file. This file will be saved in the root directory and have the following format:

    ![secrets.json image](materials/secrets.png)
    - You will also need to put these secrets in as protected variables in the Model Build pipeline.
# Notebooks
Some options for making code reviews / source control / PRs easier with jupyter notebooks:
1) manually clear all outputs before pushing to repo
2) utilize [this](https://marketplace.visualstudio.com/items?itemName=ms-air-aiagility.ipynb-renderer) extension for rendering in repo (does not render in PRs)

# Workflow
## Data Ingestion
Use the DataIngestor class in a notebook as so: 
```python
import sys
sys.path.append("..")
from helpers.data_ingestion.data_ingestion import DataIngestor

ingestor = DataIngestor(<file name you want in your df>)
df = ingestor.get_df()
```
Import the DataIngestor class in a python script as so:
```python
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from helpers.data_ingestion.data_ingestion import DataIngestor
```
**fill in**

## Experimentation
Experiment in jupyter notebooks 
Save your experiment notebook in the experiment_nbs directory with your alias as a prefix.

## Operationalize
Once you get to a place with your experimentation notebook where you would like to save the model, export the notebook as a .py file and modify it so that it can run as an independent script that outputs a .pkl file.

![image guide for exporting](materials/exportaspy.png)

*Note: make sure to update requirements.txt with any dependencies

Whenever there is an update on the master branch to the "src" folder, a build will be triggered which will register the model with AzureML. Once the build is complete, that will trigger a release.


# TODO:
1) Integration tests for data_ingestion.py
2) Documentation to data_ingestion.py
3) Secret handling for data_ingestion.py
4) Data preprocessing script
5) Create yml file for easy environment setup


Note: pkl files are git ignored. This makes it so that the only way a model can be registered is if it successfully completes the build.
To change this, remove the .pkl line in the gitignore.
