import pandas as pd 
import plotly.express as px
dataFile=pd.read_csv("data2.csv")
graph=px.scatter(dataFile,x="date",y="cases",color="country",title="CovidCases")
graph.show()