import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import os
from dash import html, dcc, callback, Input, Output, State

from general_data import projects_dict
from pages import not_found_404

dash.register_page(__name__, path_template="/works/<work_id>", name="Work Detail", title="Work Detail")


def layout(work_id):
    if work_id not in projects_dict:
        return not_found_404.layout
    project = projects_dict[work_id]

    collaborators = project["collaborators"]
    if collaborators:
        collaborators_component = html.Div([html.P("Collaborators:", className="me-3")] +
                                           [dcc.Link(collab["name"], href=collab["link"], target="_blank",
                                                     className="me-2")
                                            for collab in collaborators], className="d-inline-flex")
    else:
        collaborators_component = None

    general_info_component = html.Div([
        html.Center(html.H1("Project: " + project["name"], className="display-3 mt-5")),
        html.Br(),
        html.P(project["short_desc"], className="lead"),
        dbc.Row([
            dbc.Col(html.P(f"Related Exam: {project['related_exam']}")),
            dbc.Col(html.P(f"Year: {project['year']}"))
        ])
    ])

    links_component = [dcc.Link("Git Repository", href=project["git_repo_link"], target="_blank")]
    if project["dash_link"] is not None:
        links_component.append(dcc.Link("Dash App", href=project["dash_link"], target="_blank",
                                        className="ms-3"))

    if project["paper_it_path"] is not None or project["paper_en_path"] is not None:
        paper_component = html.Div([
            html.Hr(className="my-3"),
            html.Div(className="d-flex justify-content-end align-items-center mb-3", children=[
                dmc.Switch("Show Paper", checked=False, id="show_paper_switch", size="md", radius="lg"),
                dmc.Select(id="paper_language_select", value="en", data=[
                    {"label": "English", "value": "en"}, {"label": "Italian", "value": "it"}
                ], className="ms-3")
            ]),
            html.ObjectEl(type="application/pdf", data=project["paper_en_path"], id="paper_object",
                          width="100%", height="600px", style={"display": "none"}),
        ])
    else:
        paper_component = None

    return dbc.Container(className="fluid", children=[
        general_info_component,
        collaborators_component,
        html.Hr(),
        html.Center(html.H5("Description"), className="display-5 mt-5 mb-3"),
        html.P(project["long_desc"]),
        html.Center(html.H5("Links"), className="display-5 mt-5 mb-3"),
        html.Center(html.Span(links_component)),
        paper_component,

        dcc.Store(id="work_id", data=dict(work_id=work_id)),

    ])


@callback(Output("paper_object", "data"),
          State("work_id", "data"),
          Input("paper_language_select", "value"), prevent_initial_call=True)
def change_paper_language(work_id, language):
    work_id = work_id["work_id"]
    if language == "it":
        return projects_dict[work_id]["paper_it_path"]
    return projects_dict[work_id]["paper_en_path"]


@callback(Output("paper_object", "style"),
          Input("show_paper_switch", "checked"), prevent_initial_call=True)
def show_paper(checked):
    if checked:
        return {"display": "block"}
    return {"display": "none"}
