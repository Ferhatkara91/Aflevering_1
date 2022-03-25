import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

Excel_file = 'my_shop_data.xlsx'
customers = pd.read_excel(Excel_file, "customers")
order = pd.read_excel(Excel_file, "order")
employee = pd.read_excel(Excel_file, "employee")
products = pd.read_excel(Excel_file, "products")

def sales():
    fig = px.bar(order, x='employee_id', y='quantity', title='Sales by employee')
    return fig

def products():
    fig = px.bar(order, x='product_id', y='quantity', title='Sales by products')
    return fig

app = dash.Dash()

app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

body_app = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'sales', figure = sales()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
         
        dbc.Col(
            dcc.Graph(id = 'products', figure = products()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6), 
    ]),

],fluid = True) 

topbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.NavbarBrand("Graphs", style = {'color':'black', 'fontSize':'25px','fontFamily':'Times New Roman'}
                    ),
                )
            ],
            align="center",
            className="g-10",
        ),
    ]
)

app.layout = html.Div(id = 'parent', children = [topbar, body_app])


if __name__ == "__main__":
    app.run_server()