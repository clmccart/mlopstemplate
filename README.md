
# Abstract
This project serves as a potential template for ML projects that require DevOps practices. The project is currently in dev. Desired end-state is as follows:
- Data scientists are able to experiment in notebooks in the "experiment_nbs" directory.
- Once they have completed experimentation and are ready to operationalize their code, they can convert their notebooks to pyfiles under the "src" directory.
    - Within the notebooks and the pyfiles, they can leverage the DataIngestor and DataPreprocessor classes which handle data ingestion and data preprocessing (duh) and are covered by tests. They can also add methods to these classes and the accompanying tests.
- Any commits under the src directory in master will trigger a Build pipeline which will run all the tests. If the tests all pass, it will also build the model using the operationalized .py file and register it with AzureML.
- The Build pipeline will produce the registered model as an artifact which will automatically trigger a Release pipeline which will include manual gates, QA in ACI, and Prod in AKS.
- This project will also contain a .yml file for easy and consistent environment setup. 
    

# Setup
## Azure Service Connection:
1) In the "Register model with AzureML" Build [task](https://dev.azure.com/clmccarthy/mlopstemplate/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=3), select your azure subscription and authroize
    - If you do not have permissions to authorize, ask somebody who does to create a service connection

2) You will need to recreate the secrets.json file. This file will be saved in the root directory and have the following format:

    ![secrets.json image](materials/secrets.png)
    - You will also need to put these secrets in as protected variables in the Build pipeline as well as the Release pipeline.
3) In the release pipeline, fill in the "aksComputeTarget" variable. Make sure you also fill in the same value in  the prod_deploy.json file.
    - Note: this can either be the name of a pre-existing compute target that you would like to deploy to or the name you would like to give to the one that will be created.

# Notebooks
Some options for making code reviews / source control / PRs easier with jupyter notebooks:
1) manually clear all outputs before pushing to repo
2) utilize [this](https://marketplace.visualstudio.com/items?itemName=ms-air-aiagility.ipynb-renderer) extension for rendering in repo (does not render in PRs)

# Workflow
## Data Ingestion
The DataIngestor class serves to abstract away the process of pulling data into a dataframe. Adjust the DataIngestor class as needed depending on where your data lives. The interface that this class follows is that it takes in a filename and a json of secrets and it returns a dataframe. The default DataIngestor class pulls from blob store. The DataIngestor class will look for the secrets.json file that you pass in. If it is not present, it will pull the secrets from environment variables.

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
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from helpers.data_ingestion.data_ingestion import DataIngestor
```

## Data Preprocessing
In order to add preprocessing steps, add functions to the DataProcessor class. Make sure these functions are covered with tests. 
To use the DataPreprocessor, just call the constructor and then the steps in sequential order that you would like to apply. Like so:
```python
from src.data_preprocessing.data_preprocessor import DataPreprocessor

dp = DataPreprocessor(df)
dp.drop_columns(['sepal_length'])
dp.remove_rows_based_on_value(column_name='sepal_width', 
                            bad_values=[3.5])
df = dp.get_df()
```
## Experimentation
Experiment in jupyter notebooks 
Save your experiment notebook in the experiment_nbs directory with your alias as a prefix.

## Operationalize
Once you get to a place with your experimentation notebook where you would like to save the model, export the notebook as a .py file and modify it so that it can run as an independent script that outputs a .pkl file.

![image guide for exporting](materials/exportaspy.png)

*Note: make sure to update requirements.txt with any dependencies
Whenever there is an update to the code on the master branch outside of the experiments_nb folder, a CI build will be triggered that will run all tests and fail if the new code has broken anything.
Whenever there is an update on the master branch to the "src/model_building" folder, a model build will be triggered in addition to the regular build which will register the model with AzureML. Once the build is complete, that will trigger a release.

*Note: any code in the src folder is expected to be covered by tests.

## Deployment
When a build artifact is published, that will automatically queue a Release pipeline. There are two stages in this Release: QA and Prod.
Beofre the QA stage begins, you will need to approve the stage. Once approved, the QA stage will use the Build artifact to deploy to ACI. It will also make a POST Request to the deployed endpoint using the data contained in .azureml/test.json. If the response back is abnormal, the Release pipeline will fail. If not, it will continue on to the Prod stage.
Before approving the Prod stage, check the output from the QA POST Request task to make sure that the repsonse back is what you would like. Once approved, the Prod stage will deploy the model to AKS and do a similar testing to the QA stage.
The Release pipeline deploys using AzureML and requires the developer to write the score.py file and ensure that the .azureml/conda_dependencies.yml file is update with any packages that score.py will need.
If you make a change to score.py and want to update your deployment, you will have to manually queue a release and point it to the most recent build artifact that contains a model_metadata file. A model_metadata build artifact will only be produced if there was a change made to a file in the src/model_build folder. Therefore, you will have to go back to the most recent build that contained a change to a file in that folder and select it as the build artifact when manually queuing a new release with the updated score.py

# TODO:
1) Integration tests for data_ingestion.py
2) Documentation for all py files
3) Secret handling for data_ingestion.py
4) Create yml file for easy environment setup
5) Lock down master branch
6) Documentation for data preprocessor
7) Dynamically configure conda dependencies based on requirements.txt
9) Figure out how to specify modelname or score.py
11) Research reusability of AzDO projects
12) Scratch to CI/CD from new project
13) Add linter
14) Export pipelines as templates

Note: pkl files are git ignored. This makes it so that the only way a model can be registered is if it successfully completes the build.
To change this, remove the .pkl line in the gitignore.
