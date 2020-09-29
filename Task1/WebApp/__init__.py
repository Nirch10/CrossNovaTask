# In[]:
# Import required libraries
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Define the app
from Task1.WebApp.PSqlQuery import PSqlQuery

app = dash.Dash('')
server = app.server
app.config.suppress_callback_exceptions = False
app.scripts.config.serve_locally = True


class DashCallbackVariables:
    """Class to store information useful to callbacks"""

    def __init__(self):
        self.n_clicks = {1: 0, 2: 0}


def get_page_html():
    return [
        html.Div(
            id='chosen_drop',
            title='Welcome to the query graph maker'
        ),
        html.Div(
            [dcc.Dropdown(
                id='column1Drop',
                options=[{'label': 'column1Name', 'value': 'acceleration'}],
                placeholder="Select Column 1 Name(will be the y index)",
            )
            ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div(
            [dcc.Dropdown(
                id='column2Drop',
                options=[{'label': 'column2Name', 'value': 'mpg'}],
                placeholder="Select Column 2 Name(will be the y index)",
            )
            ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            html.Button(id="update-graph-btn", n_clicks=0, children="Update")
        ]),
        html.Div([
            dcc.Graph(
                id='example_graph',
            )
        ])

    ]


callbacks_vars = DashCallbackVariables()

root_layout = html.Div(
    id='main_page',
    children=get_page_html()
)

app.layout = root_layout


@app.callback(
    Output('example_graph', 'figure'),
    [Input('update-graph-btn', 'n_clicks')],
    [State('column1Drop', 'value'),
     State('column2Drop', 'value')]

)
def example_graph_callback(value, col1, col2):
    if col1 is None or col2 is None:
        return get_empty_graph_html()
    query = PSqlQuery("178.22.68.101", 5434, "auto", "candidato", "crossnova20")
    lst = query.get_2_numerical_columns(col1, col2)
    df = pd.DataFrame(lst)
    keys = []
    for key in lst:
        keys.append(key)
    fig = px.bar(df, x=keys[0], y=keys[1], barmode="group");
    return fig


def get_empty_graph_html():
    return {
        "layout": {
            "xaxis": {
                "visible": False
            },
            "yaxis": {
                "visible": False
            },
            "annotations": [
                {
                    "text": "No matching data found",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {
                        "size": 28
                    }
                }
            ]
        }
    }


# In[]:
# Main
if __name__ == '__main__':
    app.run_server(debug=True)
