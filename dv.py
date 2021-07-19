import pandas as pd 
import plotly.express as px
dataFile=pd.read_csv("line_chart.csv")
graph=px.line(dataFile,x="Year",y="Per capital income",title="incomeChart")
graph.show()