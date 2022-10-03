
# Breast_Cancer Extent Prediction


This poject predicts the livelihood of the breast cancer as benign or malignant.
The project can be made using various algorithms such as RandomForest Classification ,etc. 
Here we use the sklearn library to import all the methods of classification.
We use the Logistic Regression for training our model.


## Problem Statement
Breast_Cancer prediction model deals wheather the cancer growing in a human is benign or malignant.This is a classification problem like the cancer can only be either benign(0) or malignant(1).We have been provided with dataset with all the diagnosis information to train our model.


## About Dataset

The dataset we are using is taing from the sklearn itself.
Sklearn have various datasets which can be loaded from importing sklearn directy.




To load the dataset,use the following code:
```bash
  sklearn.datasets.load_breast_cancer()
```

The dataset contains 2 classes. The size of dataset is 569 rows*30 columns.It contains the diagnosis information of the patient.
## Logistic Regression 

Logistic regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables.

Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.
## Libraries used

NUMPY: It provide strong object like array to deal with numeric data.

PANDAS:-It is used to analyse the data using tabular method.

MATPLOTLIB & SEABORN: They are the major tool for the data representation and visualisation.

SKLEARN: This library is used to import the dataset and the classifier logistic regression .
## Result:
The model was tested for testing data of 144 rows .The accuracy score was imported from sklearn metrices to calculate the accuracy of the model.


The recieved score was 97.3% which was pretty good to train our model.
Our model predicted accurately about the livelihood of the cancer i.e. it's benign(0) or malignant(1).


