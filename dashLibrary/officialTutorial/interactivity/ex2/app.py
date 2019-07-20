import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np

app = dash.Dash()
graph = dcc.Graph(id='graph-with-slider',
                  figure={'layout': dict(height=400, width=300)})
slider = dcc.Slider(id='slider', min=0, max=20, value=3, step=0.1)

app.layout = html.Div(children=[graph,
                                html.Label('power'),
                                slider],
                      style=dict(height=400, width=400))


@app.callback(
    dash.dependencies.Output(component_id='graph-with-slider',
                             component_property='figure'),
    [dash.dependencies.Input(component_id='slider',
                             component_property='value')])
def update_figure(power):
    xs = np.linspace(0, 1, 100)
    ys = pow(xs, power)
    data = [dict(x=xs, y=ys, type='line')]
    return dict(data=data)


def main():
    app.run_server()
if __name__ == '__main__':
    main()
