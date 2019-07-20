"""
app.py
"""

"""
Generating HTML with Dash
Dash apps are composed of two parts.
The first part is "layout" of the app and it
describes what the application looks like.
The second part describes the interactivity of 
the application.

Dash provides Python classes for all of the visual components of
the application. We mention a set of components in the dash_core_components
and the ```dash_html_components``` and ```dash_core_components```
library but you can also build your own with JavaScript and
React.js
"""

"""
To get started, create a file named app.py with the following code:
"""

import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                dict(x=[1,2,3],y=[4,1,2],type='line',name='something'),
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


def main():
    app.run_server(debug=True)

if __name__ == '__main__':
    main()


