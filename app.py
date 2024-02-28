import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import DiskcacheManager, html
from whitenoise import WhiteNoise


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}],
                suppress_callback_exceptions=True)
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')


app.layout = html.Div([
    html.Div([
        dbc.NavbarSimple(
            brand="Disambiguation LinkTree",
            brand_href="/",
            color="dark",
            dark=True,
        )
    ]),


    dash.page_container,


    dmc.Footer(
        children=[
            html.P("Disambiguation LinkTree"),
        ],
        height=60,
        fixed=False,
        style={"background-color": "#333333", "color": "white", "text-align": "center", "padding-top": "20px",
               "margin-top": "20px"}
    )
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)