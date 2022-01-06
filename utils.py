import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def Header(app):
    return html.Div([get_header(app), html.Br([])])


def get_header(app):
    header = html.Div(
        [
            # html.Div(
            #     [
            #         html.A(
            #             html.H6(
            #                 "Sofaer Technologies",className="seven columns main-title"
            #             ),
            #         ),

            #     ],
            # ),
            # html.Div(
            #     [
            #         html.Div(
            #             [html.H5("Combined Strategy Backtest Report")],
            #             className="seven columns main-title",
            #         ),

            #     ],
     
            # ),

            dbc.Row(
                [
                    html.Div(
                        html.H6(
                            "Sofaer Technologies",className="seven columns main-title",style = {"padding-left":"20px"}
                        ),
                    ),
                    html.Div(
                        html.H5("Combined Strategy Backtest Report"),
                        className="seven columns main-title",
                    ),

                ], style = {"padding-bottom":"35px","padding-left": "0px"}
            ),
            # dbc.Row(
            #     [
            #         html.Div(
            #             [html.H5("Combined Strategy Backtest Report")],
            #             className="seven columns main-title",
            #         ),

            #     ],
     
            # ),



        ],
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Price Performance",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Portfolio & Management",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Fees & Minimums", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Distributions",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
