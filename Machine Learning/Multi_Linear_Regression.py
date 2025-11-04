
#----------------------------REGRESSION MODELS---------------------------#

# MULTI LINEAR REGRESSION

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_03_MultiLinearRegression\Investment.csv")

X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,4]

X = pd.get_dummies(X,dtype = int)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

# Bias
bias = regressor.score(X_train,Y_train)
print(bias)

# Variance
variance = regressor.score(X_test,Y_test)
print(variance)

m_slope= regressor.coef_
print(m_slope)

c_intercept= regressor.intercept_
print(c_intercept)

X = np.append(arr= np.ones((50,1)).astype(int), values= X, axis=1)

#-------------Recursive Feature Eliminaion---------

import statsmodels.api as sm

# OLS= Ordinary Least Squares
# Now, whichever index has p-value greater than 0.05, we reject them
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
                      # endog= input, exog= output
regressor_OLS.summary()
# Here, index with p-value greater than 0.05 --> x4==4

X_opt = X[:,[0,1,2,3,5]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
regressor_OLS.summary()
# Here, index with p-value greater than 0.05 --> x4==5

X_opt = X[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
regressor_OLS.summary()
# Here, index with p-value greater than 0.05 --> x2==2

X_opt = X[:,[0,1,3]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
regressor_OLS.summary()
# Here, index with p-value greater than 0.05 --> x2==3


#--------------------------------------------------------------------------

# So based on the model the firm should invest in 'Research'.

















