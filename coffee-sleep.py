import plotly.express as px 
import csv 
import numpy as np
import pandas as pd

def getDataSource(data_path):
    coffee_amount = []
    amount_sleep = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            coffee_amount.append(float(row['Coffee in ml']))
            amount_sleep.append(float(row['sleep in hours']))
    return{"x" : coffee_amount, "y" : amount_sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print('Correlation Coeeficient is:', correlation[0,1])
    
def plotGraph():
    df = pd.read_csv("cups of coffee vs hours of sleep.csv")
    fig = px.scatter(df,x = 'Coffee in ml',y = 'sleep in hours',color = 'week')
    fig.show()

def setup():
    data_path = './cups of coffee vs hours of sleep.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
setup()
plotGraph()

        