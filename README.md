# effective-guide-mlops
Example end-to-end ml pipeline build with the Sagemaker Python SDK

![Sagemaker](https://looker.com/assets/img/images/logos/external/bricks/amazon_sagemaker.png) ![Python](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)



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
