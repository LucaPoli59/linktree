import os
import sys

import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output
from dash_ag_grid import AgGrid


dash.register_page(__name__, path="/", name="Home", title="Home", is_index=True, order=0, nav=True)


layout = dbc.Container(className="fluid", children=[
])