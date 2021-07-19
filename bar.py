import pandas as pd 
import plotly.express as px
dataFile=pd.read_csv("data.csv")
graph=px.bar(dataFile,x="Country",y="InternetUsers",title="incomeChart")
graph.show()