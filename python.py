import csv
from typing import Dict 
import numpy as np
from numpy.core.numeric import correlate 
import plotly.express as px

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee"]))
            sleep.append(float(row["Sleep"]))

        return {
            "x" : coffee,
            "y" : sleep
        }

def correlationFinder(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Coffee consumed and sleep taken is\n", correlation[0,1])

def plot(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee", y = "Sleep")
        fig.show()
    

def setUp():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    correlationFinder(dataSource)
    plot(data_path)

setUp()
    