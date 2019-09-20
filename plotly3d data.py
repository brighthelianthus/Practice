########### This is about using figure_factory module instead of graph_objs module of plotly to plot a 2D density plot ################
import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as go
import plotly as py


pubg = pd.read_csv ('PUBG.csv')
df_pubg = pubg.apply(pd.to_numeric, errors="ignore")
df_bar_pubg = df_pubg.head(10)
x = df_bar_pubg['solo_Wins']
y = df_bar_pubg['solo_TimeSurvived']
z = df_bar_pubg['solo_RoundsPlayed']

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker = dict(
        size = 12,
        color = z,
        colorscale ='Viridis',
        opacity =0.8)
    )

data = [trace1]

layout = go.Layout(
    margin = dict(
        l=0,
        r=0,
        b=0,
        t=0)
        )

fig = go.Figure(data = data, layout = layout)
offline.plot(fig, filename='3d-pubg-plot.html')
