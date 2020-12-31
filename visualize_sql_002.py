import psycopg2
import pandas as pd
import plotly.graph_objects as go

db_name="postgres"
db_user="postgres"
db_port="15436"
db_host="localhost"
db_pwd="123456"

sql="""
SELECT datname, count(1) num_of_connections 
from pg_stat_activity 
group by datname 
order by 2 desc
limit 15
"""

sql_desc="Connections number by datname"

con=psycopg2.connect(database=db_name, user=db_user, password=db_pwd, host=db_host, port=db_port)

df = pd.read_sql_query(sql,con)

print("SQL:")

print (sql)

print ("\n")

print ("Dataset:")

print(df)

print ("\n")

fig = go.Figure(data=[go.Bar(x=df[df.columns[0]], y=df[df.columns[1]])])

fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text=sql_desc)

fig.show()

con.close()

