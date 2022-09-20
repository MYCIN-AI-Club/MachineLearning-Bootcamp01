Aim – To predict the sales of the Big Market .

Dataset Description --
We have two csv files form kaggle related to Big market 
sales -
	1-file.csv (8523 * 12)
	2-Predict.csv (5681 * 11)
file.csv  file contain both input and output variable(s). We need to predict the sales for the predict.csv data set.

ItemOutletSales(only contain by file.csv file) ---- Sales of the product in the particular store. This is the outcome variable to be predicted.
(we have to predict this column for predict.csv)
 
Libraries Used --

1. Numpy is used as np for linear algebra in our dataset.
2. Pandas is used as pd for data processing.
3. OrdinalEncoder from sklearn.preprocessing is used to interpret the ordinal datatypes.
4. train_test_split from sklearn.model is used for spliting the csv file into two different parts for training and testing and this traing and testing file is further divided into into two parts x and y value i.e. input and output values . 
5. LinearRegression from sklearn.linear_model is used as model for our data prediction.
6. mean_absolute_error, mean_squared_error from sklearn.metrics is used to find absolute and mean square error for our model to estimate the model accuracy.
7. sns is imported from seaborn to see the relationship between different column with outcome variable at a same time.
Footer
8.Extreme Gradient Boosting (XGBoost) is an open-source library that provides an efficient
 and effective implementation of the gradient boosting algorithm.z
