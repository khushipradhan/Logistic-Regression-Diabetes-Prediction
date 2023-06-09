# -*- coding: utf-8 -*-
"""Diabetes_Prediction_Logistic_Regression (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cjUblajPoGr7PEIT679eeNTVb8AzY3OD
"""

# Diabetes Prediction using Logistic Regression

import pandas as obj 
mydf=obj.read_csv('diabetes.csv')
print(mydf)

import pandas as pd

X= mydf.loc[:,['Pregnancies', 'Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
Y=mydf.loc[:,'Outcome'].values
print(X)
print(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.40,random_state=2)
display (X_train.shape,y_train.shape,X_test.shape,y_test.shape)

X_train

y_train

X_test

y_test

from sklearn.linear_model import LogisticRegression
mylr = LogisticRegression()
mylr.fit(X_train,y_train)
print ("Logistic Regression model is built !!")

y_pred=mylr.predict(X_test)

y_pred

print ("Actual testing data of diabetes prediction status:", y_test)
print ("Predicted data of diabetes prediction status:",y_pred)

from sklearn import metrics
print('Accuracy of the model: ',metrics.accuracy_score(y_test, y_pred)*100,'%')

new_application = {'Pregnancies':[12],
  'Glucose' :[143],
  'BloodPressure':[79],
  'SkinThickness':[0],
  'Insulin':[411],
  'BMI':[40],
  'DiabetesPedigreeFunction':[0.123],
   'Age':[28]}

df2 = pd.DataFrame(new_application,columns= ['Pregnancies','Glucose', 'BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
df2

new_pred=mylr.predict(df2)

print("Diabetic Status : ", new_pred)
# 1 -Diabetic
# 0 - Not Diabetic

# we are calculating the “Area Under the Curve” (AUC) of “Receiver Characteristic Operator” (ROC).
# The Receiver Operator Characteristic (ROC) curve is an evaluation metric for binary classification problems. 
# It is a probability curve that plots the TPR against FPR at various threshold values and essentially 
# separates the ‘signal’ from the ‘noise’. The Area Under the Curve (AUC) is the measure of the ability of a 
# classifier to distinguish between classes and is used as a summary of the ROC curve.
# The higher the AUC, the better the performance of the model at distinguishing between the positive and negative classes.

# FPR = False Positive Rate
# TPR = True Positive Rate

#for visualization and plotting
import matplotlib.pyplot as plt
import seaborn as sns

#ROC curve and AUC value
y_pred_proba = mylr.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba) # _ for threshold value
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()