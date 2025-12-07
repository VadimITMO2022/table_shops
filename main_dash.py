from dash import Dash, dcc, html, Input, Output, dash_table
from main_read import calculate_data
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.Label('data from:'),
    dcc.RadioItems(
        options=[
            {'label': 'SQLight DB', 'value': 1}, # 1 извлечь из БД SQLite
            {'label': 'SQLight DB with SQLAlchemy', 'value': 2}, # 2 извлечь из БД  SQLAlchemy 
      #      {'label': 'PastgreSQL DB', 'value': 3}, # 3 извлечь из БД PostgreSQL
      #      {'label': 'PostgreSQL DB with SQLAlchemy', 'value': 4}, # 4 извлечь из БД  SQLAlchemy 
            {'label': 'txt file', 'value': 5}, # 5 извлечь из текстового файла
            {'label': 'CSV file', 'value': 6}, # 6 извлечь из файла csv
        ],
        value=1,  # Default selected value
        id='radio-buttons-example',
   #     inline=True
    ),
    html.Div(dash_table.DataTable(id="my_table"), className="one column"),
], className="row")

@app.callback(
    Output('my_table', 'data'),
    Input('radio-buttons-example', 'value')
)
def display_value(value):
    data=calculate_data(value) # list of lists
    df = pd.DataFrame(data)  #dataframe
    df1=df.to_dict('records') # dictionary
    return df1

if __name__ == '__main__':
    app.run(debug=True)