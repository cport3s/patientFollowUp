import dash
import dash_html_components as html
import dash_core_components as dcc
import followUpStyles
import dash_bootstrap_components as dbc

tabStyles = followUpStyles.bottomTabbedMenuStyles()

# Define the app
app = dash.Dash(__name__, title='Follow Up', external_stylesheets=[dbc.themes.MORPH])
server = app.server

app.layout = html.Div(
    children=[
        html.H1(children='Follow Up'),
        html.Div(children='This is a test'),
        # Setup a tabbed menu
        html.Div(
            style = tabStyles.tabbedMenuContainerStyle,
            children = [
                #dcc.Tabs(
                #    id='tabbedBottomMenu',
                #    value='tab-1',
                #    children = [
                #        dcc.Tab(
                #            label='Tab 1',
                #            value='tab-1',
                #            style = tabStyles.tabDefaultStyle,
                #            selected_style = tabStyles.tabSelectedStyle
                #        ),
                #        dcc.Tab(
                #            label='Tab 2',
                #            value='tab-2',
                #            style = tabStyles.tabDefaultStyle,
                #            selected_style = tabStyles.tabSelectedStyle
                #        ),
                #        dcc.Tab(
                #            label='Tab 3',
                #            value='tab-3',
                #            style = tabStyles.tabDefaultStyle,
                #            selected_style = tabStyles.tabSelectedStyle
                #        ),
                #        dcc.Tab(
                #            label='Tab 4',
                #            value='tab-4',
                #            style = tabStyles.tabDefaultStyle,
                #            selected_style = tabStyles.tabSelectedStyle
                #        ),
                #        dcc.Tab(
                #            label='Tab 5',
                #            value='tab-5',
                #            style = tabStyles.tabDefaultStyle,
                #            selected_style = tabStyles.tabSelectedStyle
                #        )
                #    ]
                #)
                dbc.ButtonGroup(
                    children = [
                        dbc.Button("Dashboard"),
                        dbc.Button("Patients"), 
                        dbc.Button("Finances")
                    ],
                    size="md"
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port='5000', dev_tools_silence_routes_logging=False)