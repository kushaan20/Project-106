import plotly.express as px 
import csv 
import numpy as np
import pandas as pd

def getDataSource(data_path):
    present_days = []
    marks_percentage = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            present_days.append(float(row['Marks In Percentage']))
            marks_percentage.append(float(row['Days Present']))
    return{"y" : present_days, "x" : marks_percentage}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print('Correlation Coeeficient is:', correlation[0,1])

def plotGraph():
    df = pd.read_csv("Student Marks vs Days Present.csv")
    fig = px.scatter(df,x = 'Marks In Percentage',y = 'Days Present',color = 'Roll No')
    fig.show()
    
def setup():
    data_path = './Student Marks vs Days Present.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
plotGraph()
setup()

        