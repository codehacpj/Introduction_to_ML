from sklearn import datasets
import pandas as pd
import numpy as np


iris_dataset = datasets.load_iris()

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(iris_dataset.data,iris_dataset.target,random_state = 0)

X_train_df = pd.DataFrame(X_train)

#import plotly.plotly as py
#import plotly.graph_objs as go
#
#py.sign_in('prashantpkj01','T9ow4JHoN6QtzFrfj9kz') 
#
##df = pd.DataFrame(iris_dataset['data'],columns=iris_dataset.feature_names)
#X_train_df = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
#trace0 = go.Scatter(
#    x=X_train_df['sepal length (cm)'],
#    y=X_train_df['sepal width (cm)']
#)
#data = [trace0]
#
#py.iplot(data, filename = 'basic-line')



#Building model using KNN

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
