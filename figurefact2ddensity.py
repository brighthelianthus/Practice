########### This is about using figure_factory module instead of graph_objs module of plotly to plot a 2D density plot ################

import plotly.offline as offline
import plotly.figure_factory as ff

pubg = pd.read_csv ('PUBG.csv')
df_pubg = pubg.apply(pd.to_numeric, errors="ignore")
df_bar_pubg = df_pubg.head(10)
x = df_bar_pubg['solo_Wins']
y = df_bar_pubg['solo_TimeSurvived']
#z = df_bar_pubg['squad_Heals']

colorscale = ['#C09055','#1B5709','#FF8237','#FF65A4','#C8B4FF']

fig = ff.create_2d_density(
    x,y,colorscale=colorscale, hist_color= 'rgb(255,237,222)', point_size = '3'
        )

offline.plot(fig, filename ='histogram_subplots')