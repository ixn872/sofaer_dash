# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from pages import (
    overview,
    pricePerformance,
    # portfolioManagement,
    # feesMins,
    # distributions,
    # newsReviews,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],external_stylesheets=["https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" ,
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"],external_scripts=["https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"])

app.title = "Sofaer Technologies"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=True), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    # if pathname == "/dash-financial-report/price-performance":
    #     return pricePerformance.create_layout(app)
    # elif pathname == "/dash-financial-report/portfolio-management":
    #     return portfolioManagement.create_layout(app)
    # elif pathname == "/dash-financial-report/fees":
    #     return feesMins.create_layout(app)
    # elif pathname == "/dash-financial-report/distributions":
    #     return distributions.create_layout(app)
    # elif pathname == "/dash-financial-report/news-and-reviews":
    #     return newsReviews.create_layout(app)
    if pathname == "/dash-financial-report/":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            # portfolioManagement.create_layout(app),
            # feesMins.create_layout(app),
            # distributions.create_layout(app),
            # newsReviews.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    # app.run_server(debug=True,port=5000)
    app.run_server(debug=False,port=5000)
