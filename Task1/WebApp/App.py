import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from Task1.WebApp.PSqlQuery import PSqlQuery

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


class Server:
    def __init__(self):
        self.df = []
        self.fig = None

    def start(self):
        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),

            html.Div(children='''
                    Dash: A web application framework for Python.
                '''),

            dcc.Graph(
                id='example-graph',
                figure=self.fig
            )
        ])
        app.run_server(debug=True)

    def update_data(self, values_to_show: dict) -> None:
        self.df = pd.DataFrame(values_to_show)
        keys = []
        for key in values_to_show:
            keys.append(key)
        self.fig = px.bar(self.df, x=keys[0], y=keys[1], barmode="group");


if __name__ == '__main__':
    query = PSqlQuery("178.22.68.101", 5434, "auto", "candidato", "crossnova20")
    lst = query.get_2_numerical_columns("acceleration", "mpg")
    server = Server()
    server.update_data(lst)
    server.start()
