import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df1 = 'my_shop_data.xlsx'
df2= pd.read_excel(df1, "customers")
df3 = pd.read_excel(df1, "order")
df4 = pd.read_excel(df1, "employee")
df5 = pd.read_excel(df1, "products")


def sales():
    fig = px.pie(df3, names='employee_id', values='quantity', title='Sales by Employee') 
    fig.update_layout({
        'plot_bgcolor':'rgb(175,153,153)',
        'paper_bgcolor': 'rgb(175,153,153)',})
    
    return fig

def products():
    fig = px.pie(df3, names='product_id', values='quantity', title='Sales by Products')
    fig.update_layout({
        'plot_bgcolor':'rgb(175,153,153)',
        'paper_bgcolor': 'rgb(175,153,153)',})
    return fig

app = dash.Dash()

app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],
)


body_app = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'sales', figure = sales()),
            style = {'height':'750px', 'background-color':'rgb(175,153,153)' },xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
         
        dbc.Col(
            dcc.Graph(id = 'products', figure = products()),
            style = {'height':'750px', 'background-color':'rgb(175,153,153)'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6), 
    ]),

],fluid = True) 

topbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.NavbarBrand("Pie-charts of excel spreadsheet", style = {'color':'#460101', 'fontSize':'100px','fontFamily':'Times New Roman'}
                    ),
                )
            ],
            align="right",
            className="g-10",
        ),
    ]
)

app.layout = html.Div(id = 'parent', children = [topbar, body_app]

)


if __name__ == "__main__":
    app.run_server()