
import pandas as pd
import numpy as np
import matplotlib as plt
dataset_name = str(input("Enter the Dataset Name: "))

dataset = pd.read_csv(dataset_name)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
model.fit(X_train, y_train)
print('The model is ready to predict')

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy: ",accuracy_score(y_test,y_pred)*100,'%')