       #Expenses in Pie Chart
import plotly.offline as offline
import plotly.graph_objs as go

groups = ['rent', 'food', 'bills', 'miscellaneous']
amount = [ 6000, 3000, 1000, 2000]
colours = ['#e0a80d','#b1f22e','#b4b4ed','#598217']

trace = go.Pie( labels = groups, values = amount, hoverinfo='label+percent', textinfo='value', textfont=dict(size=25), marker = dict(colors = colours, line = dict(color='#000000',width=3)))

                #plot

offline.plot([trace])