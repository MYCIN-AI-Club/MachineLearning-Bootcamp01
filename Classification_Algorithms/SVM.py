import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_name = str(input("Enter the Dataset Name: "))

dataset = pd.read_csv(dataset_name)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Spliting into training and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# importing our model

from sklearn.svm import SVC
model = SVC(kernel = 'linear', random_state=0)
model.fit(X_train,y_train)

print("The model is ready to predict")
print("Did the person bought the SUV? : ",model.predict(sc.transform([[30,87000]])))

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy of this model is: ",accuracy_score(y_test,y_pred)*100,'%')