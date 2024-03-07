import os

import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output


from general_data import projects

dash.register_page(__name__, path="/", name="Home", title="Home")






table_header = [
    html.Thead(html.Tr([html.Th("Name", id="table_title"),
                        html.Th("Short Description"), html.Th("Related Exam"), html.Th("Year")]), className="fs-4")
]

table_body = [html.Tbody([
    html.Tr([html.Td(dbc.NavLink(html.B(project["name"]), href=project["page_link"])),
             html.Td(project["short_desc"]), html.Td(project["related_exam"]), html.Td(project["year"])])
    for project in projects])]

layout = dbc.Container(className="fluid", children=[
    html.Center(html.H1("Home Page", className="my-3")),
    html.Center(html.P("Welcome to my LinkTree, a collection of my projects")),
    html.Center(html.H3("Projects:", className="my-5"),),

    # html.Center(html.H1("WIP: Work in Progress")),

    dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True,
              className="mb-2"),

    dbc.Tooltip("Click over a name to open details", target="table_title",
                placement="top"),
])