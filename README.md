# effective-guide-mlops
#### End-to-end machine learning pipeline with Sagemaker Python SDK

<p float="left">
<img src="https://looker.com/assets/img/images/logos/external/bricks/amazon_sagemaker.png" alt="Sagemaker" height="200"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python" height="200"/>
</p>

This repository provides an example end-to-end machine learning pipeline on AWS build using the Sagemaker Python SDK. It leans on other resources (e.g. [here](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.ipynb) and [here](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html)), however, it provides a unified end-to-end example in a notebook from data processing to deployment of a REST API. This not production ready, but it will give you a good primary intuition how to orchestrate the ml lifecycle on AWS via the Sagemaker SDK. 

The main ressource for this guid is the notebook `ml_pipeline.ipynb` in the folder `notebooks`. The easiest way to follow along the tutorial would be to launch a notebook instance on AWS Sagemaker and pull the repository into your jupyterlab environment. 


### 1. Data
The [Penguin Dataset](https://allisonhorst.github.io/palmerpenguins/articles/intro.html) from Alison Horst is an alternative to the famous iris dataset that can be used for demonstrating various ml tasks. 
Read more [here](https://allisonhorst.github.io/palmerpenguins/articles/intro.html).
![Penguins](https://allisonhorst.github.io/palmerpenguins/man/figures/lter_penguins.png)


|    | species   | island    |   bill_length_mm |   bill_depth_mm |   flipper_length_mm |   body_mass_g | sex    |   year |
|----|-----------|-----------|------------------|-----------------|---------------------|---------------|--------|--------|
|  1 | Adelie    | Torgersen |             39.1 |            18.7 |                 181 |          3750 | male   |   2007 |
|  2 | Adelie    | Torgersen |             39.5 |            17.4 |                 186 |          3800 | female |   2007 |
|  3 | Adelie    | Torgersen |             40.3 |            18   |                 195 |          3250 | female |   2007 |


### 2. Objective

The goal is to train a classifier that predicts the sex/gender of a penguin based on all other variables available.

### 3. Ressources

##### Notebooks:

- stored in `/notebooks`
- `eda.ipynb` visual exploration of the data
- `ml_pipeline.ipynb` orchestrates preprocessing of the data, model training and deployment of the model as endpoint

### 4 Tutorial Wolkthrough

- head over to `notebooks.ml_pipeline.ipynb` and follow the procedure
