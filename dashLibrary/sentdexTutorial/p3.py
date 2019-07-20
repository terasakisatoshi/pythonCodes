import datetime

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web

"""
start = datetime.datetime()
end = datetime.datetime()

stock = "TESLA"

df = web.DataReader(stock, "google", start, end)
"""

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(children="""symbol to graph"""),
        dcc.Input(id="input", value="", type="text"),
        html.Div(id="output_graph")
    ]
)


@app.callback(
    Output(component_id="output_graph", component_property="children"),
    [Input(component_id="input", component_property="value")],
)
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader('F', 'iex', start, end)
    graph = dcc.Graph(
        id="example_graph",
        figure={
            "data": [
                {
                    "x": df.index,
                    "y": df.close,
                    "type": "line",
                    "name": input_data
                }
            ],
            "layout": {
                "title": input_data
            }
        })
    return graph


if __name__ == '__main__':
    app.run_server(debug=True)
