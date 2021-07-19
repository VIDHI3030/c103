import pandas as pd 
import plotly.express as px
dataFile=pd.read_csv("data.csv")
graph=px.scatter(dataFile,x="Population",y="Per capita",size="Percentage",color="Country",title="incomeChart")
graph.show()