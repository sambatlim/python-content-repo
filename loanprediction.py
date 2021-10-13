# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:13:31 2020
@author: ISHIKA
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")
data=pd.read_csv(r"C:\Users\ISHIKA\ml\loan-prediction-problem-dataset\train_u6lujuX_CVtuZ9i.csv")
testdata=pd.read_csv(r"C:\Users\ISHIKA\ml\loan-prediction-problem-dataset\test_Y3wMUE5_7gLdaTN.csv")
dummy=pd.get_dummies(data["Gender"])
#print(dummy.head())
data=pd.concat([dummy,data],axis=1)
data.drop(["Gender"],axis=1,inplace=True)
data.Married.replace(['Yes',"No"],[1,0],inplace=True)
data.Education.replace(['Graduate',"Not Graduate"],[1,0],inplace=True)
data.Self_Employed.replace(['Yes',"No"],[1,0],inplace=True)
dummy2=pd.get_dummies(data["Property_Area"])
#print(dummy2.head())
data=pd.concat([data,dummy2],axis=1)
data.drop(["Property_Area"],axis=1,inplace=True)
data.Loan_Status.replace(["Y","N"],[1,0],inplace=True)
data=data.fillna(data.mean())
df=data[["ApplicantIncome","CoapplicantIncome","LoanAmount"]]
normalize=(df-df.mean())/df.std()
data.drop(["ApplicantIncome","CoapplicantIncome","LoanAmount"],axis=1,inplace=True)
#dummy=pd.get_dummies(data["Gender"])
data=pd.concat([data,normalize],axis=1)
#data=pd.read_csv(r"C:\Users\ISHIKA\ml\loan-prediction-problem-dataset\train_u6lujuX_CVtuZ9i.csv")
dummy=pd.get_dummies(testdata["Gender"])
#print(dummy.head())
testdata=pd.concat([dummy,testdata],axis=1)
testdata.drop(['Gender'],axis=1,inplace=True)
testdata.Married.replace(['Yes',"No"],[1,0],inplace=True)
testdata.Education.replace(['Graduate',"Not Graduate"],[1,0],inplace=True)
testdata.Self_Employed.replace(['Yes',"No"],[1,0],inplace=True)
dummy2=pd.get_dummies(testdata["Property_Area"])
#print(dummy2.head())
testdata=pd.concat([testdata,dummy2],axis=1)
testdata.drop(["Property_Area"],axis=1,inplace=True)
#testdata.Loan_Status.replace(["Y","N"],[1,0],inplace=True)
testdata=testdata.fillna(testdata.mean())
df=testdata[["ApplicantIncome","CoapplicantIncome","LoanAmount"]]
normalize=(df-df.mean())/df.std()
testdata.drop(["ApplicantIncome","CoapplicantIncome","LoanAmount"],axis=1,inplace=True)
testdata=pd.concat([testdata,normalize],axis=1)
from sklearn.model_selection import train_test_split as tts
x_train=data.drop(["Loan_ID","Loan_Status"],axis=1)
y_train=data[["Loan_Status"]]
#x_train,x_test,y_train,y_test=tts(x,y)
#print(data.head())
'''
import seaborn as sns
plt.figure(figsize=(10,10))
sns.heatmap(data.corr(),annot=True)
plt.show()
'''

x_test=testdata.drop(["Loan_ID"],axis=1)
#y_test=testdata[["Loan_Status"]]

import statsmodels.api as sm
x_trainm1=np.array(x_train,dtype="float64")
y_trainm1=np.array(y_train,dtype="float64")
x_testm1=np.array(x_test,dtype="float64")
#y_testm1=np.array(y_test,dtype="float64")
'''
print(x_trainm1,y_trainm1)
model1=sm.GLM(y_trainm1,(sm.add_constant(x_trainm1)),family=sm.families.Binomial())
model1.fit()
print(model1.fit().summary())
'''
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
lr=LogisticRegression()
lr.fit(x_trainm1,y_trainm1)
h=lr.predict(x_testm1)
preddf=pd.DataFrame(h)
#y_test_df=pd.DataFrame(y_test)
#y_test_df["Loan_ID"]=y_test.index
preddf = preddf.iloc[:,[0]]
preddf[0] = preddf[0].map( lambda x: "Y" if x == 1 else "N")
preddf=preddf.rename(columns={0:"Loan_Status"})
#y_test_df.reset_index(drop=True,inplace=True)
#preddf.reset_index(drop=True,inplace=True)
#op=pd.concat([y_test_df,preddf],axis=1)
print(preddf.head())

#print(h)
