import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


def get_data(file_name):
    data = pd.read_csv(file_name)

    x_parameter = []
    y_parameter = []

    for squarefeet in (data['square_feet']):
           x_parameter.append([float(squarefeet)])

    for  pricevalue in (data['price']):
           y_parameter.append(float(pricevalue))

    return x_parameter, y_parameter
X=[]
Y=[]
X,Y = get_data('input_data.csv')
print X
print Y

###Function to fit our data to Linear Model ###

def linear_model_main(x_parameters, y_parameters, predict_val):
    ### Create Linear Regression object ###

    regr = linear_model.LinearRegression()
    regr.fit(x_parameters, y_parameters)
    # regr.fit(x_parameters[:, np.newaxis], y_parameters)

    predict_outcome = regr.predict(predict_val)
    predictions = {}
    ## output of slope , intercept and y-value ###
    predictions['intercept'] = regr.intercept_
    predictions['coefficient']= regr.coef_
    predictions['predicted_val'] = predict_outcome
    return predictions

 ### Function to show the results of linear fit model ###
def show_linear_line (x_parameters, y_parameters):
    ####  linear regression object ####
    regr = linear_model.LinearRegression()
    regr.fit(x_parameters, y_parameters)
    plt.scatter(x_parameters, y_parameters, color='blue')
    plt.plot(x_parameters, regr.predict(x_parameters), color='red', linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()


predictvalue = [[700]]
result = linear_model_main(X,Y,predictvalue)
print "Intercept value", result['intercept']
print "Coefficient value", result['coefficient']
print "Predicted value :", result['predicted_val']
show_linear_line(X,Y)



