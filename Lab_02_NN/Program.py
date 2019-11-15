import sklearn #1

import pandas #3

import matplotlib.pyplot as plt #4
import seaborn as sns # visualization #4

import numpy as np #5

from sklearn.utils import shuffle #8

from sklearn.neural_network import MLPClassifier #10

from sklearn.model_selection import cross_validate #14


data=pandas.read_csv("iris.data",header=None)#(place "header=None" into parenthesis to show header #3
print(data) #3

sns.pairplot( data=data,vars=(0,1,2,3), hue=4 ) #4
plt.show() #4

data=np.array(data) #5

X=data[:,0:4] #This gets all the rows and only the first 4 columns. #6
y=data[:,4] #Gets only the 4th row #6
print(X.shape) #(150,4) #6
print(y.shape) #(150,1) #6

X,y=shuffle(X,y,random_state=0) #8

trainX=X[:111] #9
trainy=y[:111] #9
testX=X[111:151] #9
testy=y[111:151] #9

# ~ for layerSize in range(1,12):
clf = MLPClassifier(hidden_layer_sizes=[3], random_state=2000,max_iter=2000) #10
clf.fit(trainX, trainy) #10
trainScore=clf.score(trainX,trainy)
testScore(clf.score(testX,testy)
print("%d,%f,%f"%(layerSize,trainScore,testScore))

#print(dir(clf))
print(clf.coefs_)#11

prediction=clf.predict(testX) #12

print(clf.score(trainX,trainy)) #13
print(clf.score(testX,testy)) #13

cv_results = cross_validate(clf, X, y, cv=4) #14
print(cv_results) #14

