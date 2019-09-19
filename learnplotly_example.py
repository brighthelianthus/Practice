import plotly.graph_objs as go
import plotly.offline as offline

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],

)
offline.plot(fig)
