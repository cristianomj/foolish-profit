import datetime

import plotly.graph_objects as go
import plotly
from kaleido.scopes.plotly import PlotlyScope

def generate(data, title: str, format: str = "svg") -> go.Figure:
    datetimes = []
    prices = []
    for kp in data:
        if kp['price'] is not None and kp['date'] is not None:
            if type(kp['date']) != 'datetime':
                dt = datetime.datetime.strptime(kp['date'], "%Y-%m-%d")
                datetimes.append(dt)
            else:
                datetimes.append(kp['date'])
            prices.append(kp['price'])
        
    fig = go.Figure(
        data = go.Scatter(x=datetimes, y=prices), 
        layout = dict( 
            title = dict(
                text=title
            )
        )
    )

    scope = PlotlyScope()
    img = scope.transform(fig, format=format)
    # img = plotly.io.to_image(fig=fig, format=format)
    return img
