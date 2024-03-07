import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from whitenoise import WhiteNoise
from dash import html

app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                suppress_callback_exceptions=True)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')


app.layout = html.Div(children=[
    dbc.NavbarSimple(
        brand="LinkTree",
        brand_href="/",
        color="dark",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/LucaPoli59",
                                    external_link=True, target="_blank")),
            dbc.NavItem(dbc.NavLink("GitLab", href="https://gitlab.com/Luca599",
                                    external_link=True, target="_blank")),
            dbc.NavItem(dbc.NavLink("LinkedIn", href="https://www.linkedin.com/in/luca-poli-cs",
                                    external_link=True, target="_blank")),
        ],
    ),

    html.Div(dash.page_container, style={"min-height": "calc(100vh - 60px - 56px)"}, className="pb-3"),

    dmc.Footer([
        html.Div("Luca Poli", className="me-3"),
        html.Div("+39 3455164670", className="me-3"),
        html.Div("poli.luca.marconi@gmail.com")
    ],
               height=60,
               fixed=False,
               style={"background-color": "#333333", "color": "white"},
               className="d-flex justify-content-center align-items-center",
               )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
