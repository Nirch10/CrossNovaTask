import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from Task1.AppConfig.Config import Config
from Task1.WebApp.PSqlQuery import PSqlQuery

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


class Server:
    def __init__(self):
        self.df = []
        self.fig = None

    def start(self, dropdown_list: list):
        app.layout = html.Div(
            id='main_page',
            children=self.__get_page_html(dropdown_list)
        )
        app.run_server(debug=True)

    def update_graph_data(self, values_to_show: dict) -> None:
        self.df = pd.DataFrame(values_to_show)
        keys = []
        for key in values_to_show:
            keys.append(key)
        self.fig = px.bar(self.df, x=keys[0], y=keys[1], barmode="group")
        return self.fig

    @staticmethod
    def __get_page_html(dropdown_data: list):
        return [
            html.Div(
                id='chosen_drop',
                title='Welcome to the query graph maker'
            ),
            html.Div(
                [dcc.Dropdown(
                    id='column1Drop',
                    options=[{'label': i, 'value': i} for i in dropdown_data],
                    placeholder="Select Column 1 Name(will be the y index)",
                )
                ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div(
                [dcc.Dropdown(
                    id='column2Drop',
                    options=[{'label': i, 'value': i} for i in dropdown_data],
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


@app.callback(
    Output('example_graph', 'figure'),
    [Input('update-graph-btn', 'n_clicks')],
    [State('column1Drop', 'value'),
     State('column2Drop', 'value')]
)
def example_graph_callback(value, col1, col2):
    if col1 is None or col2 is None or col1 == col2:
        return get_empty_graph_html()
    query_result_list = query.get_2_numerical_columns(col1, col2)
    return server.update_graph_data(query_result_list)


def start_web_app(app_config: Config):
    global query
    global server
    query = PSqlQuery(app_config.dbHost, app_config.dbPort, app_config.dbTable, app_config.dbUserName, app_config.dbPassword)
    lst = query.get_table_columns(['numeric'])
    server = Server()
    server.start(lst)