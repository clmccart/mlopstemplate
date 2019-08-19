
template for ML projects requiring DevOps practices.


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