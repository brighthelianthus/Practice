## pakages ##
import csv
import sys
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
from sklearn import  linear_model
import plotly.offline as offline

## function to get data ##
def get_data (filename):
    data = pd.read_csv(filename)
    flash_x = []
    flash_y = []
    arrow_x = []
    arrow_y = []

    for x1,y1,x2,y2 in zip(data['flash_episode_number'], data['flash_us_viewers'],data['arrow_episode_number'], data['arrow_us_viewers']):
        flash_x.append([float(x1)])
        flash_y.append(float(y1))
        arrow_x.append([float(x2)])
        arrow_y.append(float(y2))
    return flash_x,flash_y, arrow_x,arrow_y

## function to know which TV show will have more viewers in the next episode ##

def more_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1,y1)
    predicted_val1 = regr1.predict([[9]])
    print predicted_val1
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)
    predicted_val2 = regr2.predict([[9]])
    print predicted_val2
    if predicted_val1 > predicted_val2:
        print "The Flash will have more viewers for next week"
    else:
        print "The Arrow will have more viewers for the next week"

### Function to show the results of linear fit model ###
def show_linear_line (x1, y1,x2,y2):
    ####  linear regression object ####
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1, y1)
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2, y2)

    plt.scatter(x1, y1, color='violet')
    plt.scatter(x2, y2, color='yellow')

    # plt.plot(x_parameters, regr.predict(x_parameters), color='red', linewidth=3)
    # plt.xticks(range(0,7,1))
    # plt.yticks(range(0,7,1))
    # plt.show()

    plt.plot(x1, regr1.predict(x1), color='purple', linewidth=2)
    plt.plot(x2, regr2.predict(x2), color='orange', linewidth=2)
    plt.show()
    # data1 = [trace1, trace2]
    # layout1 = go.Layout(title='Flash vs Arrow viewers', plot_bgcolor= '#000000', showlegend=True)
    # fig1 = go.Figure(data=data1,layout=layout1)
    #
    # offline.plot(fig1, filename='comparison plot')
## Operation ##
x1,y1,x2,y2 = get_data('tvshowdata.csv')
more_viewers(x1,y1,x2,y2)
show_linear_line(x1,y1,x2,y2)




