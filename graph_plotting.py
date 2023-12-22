import matplotlib.pyplot as plt
import pandas as pd

class plot_data(pd.DataFrame):
    def __init__(self, data):
        self.Data = data

    def __getitems__(self):
        self.Data.plot(x='timestamp', y= 'price')
