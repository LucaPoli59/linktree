
import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, callback, Input, Output


from general_data import projects_dict

dash.register_page(__name__, path_template="/works/<work_id>", name="Work Detail", title="Work Detail")


def layout(work_id):
    project = projects_dict[work_id]

    collaborators = project["collaborators"]
    if collaborators:
        collaborators = [html.Li(html.A(collab["name"], href=collab["link"])) for collab in collaborators]
    else:
        collaborators = ""

    return dbc.Container(className="fluid", children=[
        html.Center(html.H1(project["name"], className="my-3")),
        html.Center(html.H3(project["long_desc"], className="my-5")),
        html.Center(html.P(f"Related Exam: {project['related_exam']}")),
        html.Center(html.P(f"Year: {project['year']}")),
        html.Center(children=[html.P("Collaborators:"), html.Ul(collaborators)]),
    ])
