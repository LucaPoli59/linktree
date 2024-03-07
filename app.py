import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import DiskcacheManager, html
from whitenoise import WhiteNoise

app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                suppress_callback_exceptions=True)
# server = app.server
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')


app.layout = html.Div(children=[
    html.Div(children=[
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
        )
    ]),

    dash.page_container,

    dmc.Footer("LinkTree",
               height=60,
               fixed=False,
               style={"background-color": "#333333", "color": "white"},
               className="d-flex justify-content-center align-items-center",
               )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
