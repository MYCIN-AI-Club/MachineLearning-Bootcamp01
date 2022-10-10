import pandas as pd
import numpy as np
dataset_name = str(input("Enter the Dataset Name: "))

dataset = pd.read_csv(dataset_name)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
y = y.reshape(len(y),1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25,random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train.ravel())
print("The Model is Ready to predict!")

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("The accuracy of this model: ",accuracy_score(y_test,y_pred)*100,'%')