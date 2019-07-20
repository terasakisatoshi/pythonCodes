"""
The dash_core_components include a set a higher-level components
like dropdowns, graphs, markdown blocks, and more...
Like all Dash components, they are described entirely declaratively.
Every option that is configurable is available as a keyword argument of the
component.
"""

import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

dropdown = [html.Label('Dropdown'),
            dcc.Dropdown(options=[
                {'label': 'A', 'value': 'a'},
                {'label': 'B', 'value': 'b'},
                {'label': 'C', 'value': 'c'}],
            value='b')]

multi_select_dropdown = [html.Label('Multi-Select Dropdown'),
                         dcc.Dropdown(options=[
                             {'label': 'P', 'value': 'p'},
                             {'label': 'Q', 'value': 'q'},
                             {'label': 'R', 'value': 'r'}],
                         value=['q', 'r'],
                         multi=True)]

radio_item = [html.Label('Radio Items'),
              dcc.RadioItems(options=[
                  {'label': 'X', 'value': 'x'},
                  {'label': 'Y', 'value': 'y'},
                  {'label': 'Z', 'value': 'z'}],
              value='z')]

check_box = [html.Label('Checkbox'),
             dcc.Checklist(options=[
                 {'label': 'S', 'value': 's'},
                 {'label': 'T', 'value': 't'},
                 {'label': 'U', 'value': 'u'}],
             values=['s', 'u'])]

slider = [html.Label('Slider'),
          dcc.Slider(min=0,
                     max=5,
                     marks={i:i for i in range(5)},
                     value=3)]

text_input=html.Div([html.Label('Text input'),
                    html.Br(),
                    dcc.Input(value='input here',type='text'),
                    html.Br()])

app.layout = html.Div([
    *dropdown,
    *multi_select_dropdown,
    *radio_item,
    *check_box,
    text_input,
    *slider,
], style={'columnCount': 2})


def main():
    app.run_server(debug=True, port=8800)

if __name__ == '__main__':
    main()
