import dash 
from dash.dependencies import Input, Output
import dash_html_components as html 
import dash_core_components as dcc 

app = dash.Dash()

app.layout=html.Div([
    dcc.Input(id='my-id',value='init value',type='text'),
    html.Div(id='my-div')])

@app.callback(
    Output(component_id='my-div',component_property='children'),
    [Input(component_id='my-id', component_property='value')])

def update_output_div(input_value):
    return 'you\'ve entered "{}"'.format(input_value)

def main():
    app.run_server()
if __name__ == '__main__':
    main()