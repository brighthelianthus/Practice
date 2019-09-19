import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import plotly.offline as offline
N= 100
example_x = np.random.rand(N)
example_y = np.random.rand(N)
trace = go.Scatter(
    x = example_x, y = example_y, mode ='markers'
)
data = [trace]
fig = go.Figure(data)
offline.plot(fig)