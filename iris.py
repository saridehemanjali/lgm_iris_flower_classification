# -*- coding: utf-8 -*-
"""iris

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1atMFQFIWjoriyxu7i7N7Kf0bJSfNAVvz
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# %matplotlib inline

col=['sepal length','sepal width','petal length','petal width','class labels']
df=pd.read_csv('iris.data',names=col)
df.head(150)

df.describe()

sns.pairplot(df,hue='class labels')

data=df.values
x=data[:,0:4]
y=data[:,4]
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_test)

from sklearn.svm import SVC
model_svc=SVC()
model_svc.fit(x_train,y_train)

prediction1=model_svc.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,prediction1)*100)

#logistic Regression
from sklearn.linear_model import LogisticRegression
model_LR=LogisticRegression()
model_LR.fit(x_train,y_train)

prediction2=model_svc.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,prediction2)*100)
for i in range(len(prediction1)):
  print(y_test[i],prediction1[i])

#decision tree
from sklearn.tree import DecisionTreeClassifier
model_DTC=DecisionTreeClassifier()
model_DTC.fit(x_train,y_train)

prediction3=model_svc.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,prediction3))

from sklearn.metrics import classification_report
print(classification_report(y_test,prediction2))

x_new=np.array([[3,2,1,0.2],[4.9,2.2,3.8,1.1],[5.3,2.5,4.6,1.9]])
prediction=model_svc.predict(x_new)
print("prediction of species:{}".format(prediction))