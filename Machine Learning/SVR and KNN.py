#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Naresh IT\emp_sal.csv")

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# simple linear regression model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# linear regression visualization
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('linear regression model (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

lin_model_pred = lin_reg.predict([[6]])
lin_model_pred

# polynomial regression model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(x)

poly_reg.fit(x_poly, y)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# polynomial regression visualization.
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('polymodel (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred

# if we do hyper parameter tunning that means when we will add a parameter in polynomial features which is degree = 3/4/5, upon increasing the degree the more accurate the results will be and the loss will decrease.

# Support vector regression model.
from sklearn.svm import SVR
svr_reg = SVR()
svr_reg.fit(x, y)

svr_pred = svr_reg.predict([[6]])
print(svr_pred)

# to do hyperparameter tunning in svr we should add kernel and degree the code is given below demonstrating the topic.
from sklearn.svm import SVR
svr_reg = SVR(kernel = 'poly', degree = 5)
svr_reg.fit(x, y)

svr_pred = svr_reg.predict([[6]])
print(svr_pred)

# knn K Nearest Neighbour Regressor.
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor()
knn_reg.fit(x, y)

knn_pred = knn_reg.predict([[6]])
print(knn_pred)

# the hyperparameter tunning in knn regressor 
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors= 3)
knn_reg.fit(x, y)

knn_pred = knn_reg.predict([[6]])
print(knn_pred)