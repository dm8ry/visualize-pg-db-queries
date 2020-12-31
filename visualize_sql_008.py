import psycopg2
import pandas as pd
import plotly.graph_objects as go
import numpy as np

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

fig = go.Figure()

fig.add_trace(go.Scatter(x=df[df.columns[0]], y=df[df.columns[1]],
                    mode='markers+lines',
                    name='markers+lines',
                    marker=dict(
                        color=np.random.randn(len(df)),
                        colorscale='Viridis',
                        line_width=1
                    )))

fig.show()

con.close()


