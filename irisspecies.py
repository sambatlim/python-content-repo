# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:55:14 2020
@author: ISHIKA
"""
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.metrics import confusion_matrix
from sklearn import neighbors
sets=[]
ssets=[]
#from kaggle.competitions import twosigmanews
data = pd.read_csv(r"C:\Users\ISHIKA\Downloads\iris.data",delimiter=',',names=['slen','swid','plen','pwid','name'])
print(data.head())
from sklearn.model_selection import LeaveOneOut 
X = data.drop(['name'],axis=1)
y = data[['name']]
from sklearn.model_selection import KFold 

kf = KFold(n_splits=2, random_state=None, shuffle=True) # Define the split - into 2 folds 
kf.get_n_splits(X) # returns the number of splitting iterations in the cross-validator
print(kf.split(X)) 
for train_index, test_index in kf.split(X):
    traini=np.array(train_index)
    testi=np.array(test_index)
    
    sets.append(traini.flatten())
    ssets.append(testi.flatten())
def knn(data,ssets,sets):
    s1=pd.DataFrame()
    s2=pd.DataFrame()
    testx=pd.DataFrame()
    testy=pd.DataFrame()
    #inp=sets[0].ravel()
    for i in range(0,len(sets[0])):
        s1=pd.concat([s1,X.iloc[[sets[0][i]]]])
        s2=pd.concat([s2,y.iloc[[sets[0][i]]]])
    for i in range(0,len(ssets[0])):
        testx=pd.concat([testx,X.iloc[[ssets[0][i]]]])
        testy=pd.concat([testy,y.iloc[[ssets[0][i]]]])
    
    #testx=X.iloc[[ssets[0]]]
    
    #testy=y.iloc[[ssets[0]]]
    clf=neighbors.KNeighborsClassifier(15)
    clf.fit(s1,s2)
    z=clf.predict(testx)
    z=z.reshape(testy.shape)
    cm1=confusion_matrix(testy,z)
    speci=cm1[0,0]/(cm1[0,0]+cm1[0,1])
    sensi=cm1[0,0]/(cm1[1,0]+cm1[0,0])
    f1=2*(speci*sensi)/(speci+sensi)
    print(f1)
    print(z)
    for i in range(0,len(sets[1])):
        s1=pd.concat([s1,X.iloc[[sets[1][i]]]])
        s2=pd.concat([s2,y.iloc[[sets[1][i]]]])
    
    for i in range(0,len(ssets[0])):
        testx=pd.concat([testx,X.iloc[[ssets[1][i]]]])
        testy=pd.concat([testy,y.iloc[[ssets[1][i]]]])
    clf.fit(s1,s2)
    z1=clf.predict(testx)
    z1=z1.reshape(testy.shape)
    cm1=confusion_matrix(testy,z1)
    speci=cm1[0,0]/(cm1[0,0]+cm1[0,1])
    sensi=cm1[0,0]/(cm1[1,0]+cm1[0,0])
    f1=2*(speci*sensi)/(speci+sensi)
    print(f1)
    print(z1)
    
    
   

knn(data,sets,ssets)
    
    
'''
loo = LeaveOneOut()
loo.get_n_splits(X)
for train_index, test_index in loo.split(X):
   print("TRAIN:", train_index, "TEST:", test_index)
   X_train, X_test = X[train_index], X[test_index]
   y_train, y_test = y[train_index], y[test_index]
   print(X_train, X_test, y_train, y_test)
'''   
