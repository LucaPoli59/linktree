import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from general_data import projects

dash.register_page(__name__, path="/", name="Home", title="Home")

table_header = [
    html.Thead(html.Tr([html.Th("Name", id="table_title"),
                        html.Th("Short Description"), html.Th("Related Exam"), html.Th("Year")]), className="fs-4")
]

table_body = [html.Tbody([
    html.Tr([html.Td(dcc.Link(project["name"], href=project["page_link"], className="fw-bold text-dark")),
             html.Td(project["short_desc"]), html.Td(project["related_exam"]), html.Td(project["year"])])
    for project in projects])]

layout = dbc.Container(className="fluid", children=[
    html.Center(html.H1("My Projects", className="pt-4 pb-3")),
    html.Center(html.P("Welcome to my LinkTree, a collection of my projects")),

    dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True,
              className="mt-3"),

    dbc.Tooltip("Click over a name to open details", target="table_title",
                placement="top"),
])
