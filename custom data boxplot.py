# https://plot.ly/box-plots/

            ########## This is about plotting box-plots ##########
import plotly.offline as offline
import plotly.graph_objs as go
import  numpy as np

xdata = [ 'Carmelo', 'Dwane', 'Brook', 'David', 'Williams','Deron']

y0 = np.random.rand(50)-1
y1 = np.random.rand(50)+1
y2 = np.random.rand(50)
y3 = np.random.rand(50)+2
y4 = np.random.rand(50)-2
y5 = np.random.rand(50)+3

ydata=[y0,y1,y2,y3,y4,y5]

colors = ['rgba(93,164,214,0.5)','rgba(90,160,214,0.5)','rgba(93,100,214,0.5)','rgba(76,164,288,0.5)','rgba(93,164,290,0.5)','rgba(93,145,125,0.5)']

traces =[]

for xd, yd, clr in zip(xdata,ydata,colors):
    traces.append(go.Box(y=yd,
                         name=xd,
                         boxpoints='all',
                         jitter =0.5,
                         whiskerwidth =0.2,
                         fillcolor=clr,
                         marker=dict(size=2),
                         line = dict(width=1)
                         )
                  )
    layout = go.Layout(
        title = 'Points Scored by the Top 6 scoring NBA players in 2019',
        yaxis=  dict  (
            autorange = True,
            showgrid = True,
            zeroline = True,
            dtick =5,
            gridcolor = 'rgb(255,255,255)',
            gridwidth = 1,
            zerolinecolor='rgb(255,255,255)',
            zerolinewidth=2
                        ),
        margin = dict(l=40,r=30,b=80,t=100),
        paper_bgcolor ='rgb(243,243,243)',
        plot_bgcolor ='rgb(243,243,243)',
        showlegend = True
    )


fig = go.Figure(data = traces, layout = layout)
offline.plot(fig, filename ='Box-plot.html')
