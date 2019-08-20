
template for ML projects requiring DevOps practices.

# Setup
## Azure Service Connection:
In the "Register model with AzureML" Build [task](https://dev.azure.com/clmccarthy/mlopstemplate/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=3), select your azure subscription and authroize
- If you do not have permissions to authorize, ask somebody who does to create a service connection

# Notebooks
Some options for making code reviews / source control / PRs easier with jupyter notebooks:
1) manually clear all outputs before pushing to repo
2) utilize [this](https://marketplace.visualstudio.com/items?itemName=ms-air-aiagility.ipynb-renderer) extension for rendering in repo (does not render in PRs)

# Workflow
## Data Ingestion
**fill in**

## Experimentation
Experiment in jupyter notebooks 
Save your experiment notebook in the experiment_nbs directory with your alias as a prefix.
Once you get to a place with your experimentation notebook where you would like to save the model, export the notebook as a .py file and modify it so that it can run as an independent script that outputs a .pkl file.
![image guide for exporting](materials/exportaspy.png)

*Note: make sure to update requirements.txt with any dependencies