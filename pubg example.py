import pandas as pd
import plotly.graph_objs as go
import plotly.offline as offline
pubg = pd.read_csv ('PUBG.csv')
desired_width = 800
pd.set_option('display.width',desired_width)
pd.set_option('display.max_columns',100)
# print pubg
pubg.head(10)

        ######## Scatter Plot ##########
df_pubg = pubg.apply(pd.to_numeric, errors="ignore")
df_new_pubg = df_pubg.head(10)

print df_new_pubg.head(10)

trace = go.Scatter ( x = df_new_pubg ['solo_RoundsPlayed'], y = df_new_pubg['solo_Wins'],name = 'Rounds Won')

layout = go.Layout (title='PUBG Player Wwins vs Rounds Played',
                    plot_bgcolor = 'rgb(230,230,200)', showlegend = True)

fig = go.Figure(data=[trace], layout=layout)

# offline.plot(fig,filename = 'scatter plot')

           ############### Bar Chart ###############

df_bar_pubg = df_pubg.head(10)

trace1 = go.Bar( x = df_bar_pubg['player_name'], y = df_bar_pubg['solo_RoundsPlayed'], name = 'Rounds Played')

trace2 = go.Bar( x = df_bar_pubg['player_name'], y = df_bar_pubg['solo_Wins'], name = 'Rounds Won')

data1 = [trace1, trace2]
layout1 = go.Layout(barmode ='group')

fig1 = go.Figure(data=data1,layout=layout1)

offline.plot(fig1, filename ='grouped bar chart')