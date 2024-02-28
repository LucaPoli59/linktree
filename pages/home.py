import os

import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path="/", name="Home", title="Home", is_index=True, order=0, nav=True)

sarcasm_desc = "Creation of a Deep Learning model to detect sarcasm in reddit comments"
trnet_desc = "Analysis of the structure and vulnerabilities of the Transportation Network: Deutsche Bahn"
fma_desc = "Creation of multiple portfolios strategies based on factor models, inspired by QEPM"
emb_1_desc = ""
emb_2_desc = ""



table_header = [
    html.Thead(html.Tr([html.Th("Name"), html.Th("Short Description"), html.Th("Related Exam"), html.Th("Year")]))
]

table_body = [html.Tbody([
    html.Tr([html.Td(dbc.NavLink(children=["Sarcasm Detection"], href="/")),
             html.Td(sarcasm_desc), html.Td("Data Analytics"), html.Td("2023")]),
    html.Tr([html.Td(dbc.NavLink(children=["Transportation Network Analysis"], href="/")),
                html.Td(trnet_desc), html.Td("Data Analytics"), html.Td("2024")]),
    html.Tr([html.Td(dbc.NavLink(children=["Factor Models Strategies"], href="/")),
                html.Td(fma_desc), html.Td("Financial Market Analytics"), html.Td("2023")]),

])]

layout = dbc.Container(className="fluid", children=[
    html.Center(html.H1("Home Page", className="my-3")),
    html.Center(html.P("Welcome to the Disambiguation LinkTree, a collection of my projects")),
    html.Center(html.H3("Projects:", className="my-5"),),

    html.Center(html.H1("WIP: Work in Progress")),

    # dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True,
    #           className="mb-2"),
])