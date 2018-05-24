import numpy as np
from sklearn import linear_model
import pandas as pd

dates = []
prices = []
dates_final=[]

def get_data(filename):

    df = pd.read_csv(filename)

    for i in range(len(df)):
        dates.append(df["Date"][i])
        prices.append(df["Close"][i])

    for j in range(len(dates)):

        dates_final.append(int(dates[j][8:10]))

    prices.reverse()
    dates_final.reverse()

    return

def predict_price(dates,prices,x):
    linear_mod = linear_model.LinearRegression() #defining the linear regression model
    dates = np.reshape(dates,(len(dates),1)) # converting to matrix of n X 1
    prices = np.reshape(prices,(len(prices),1))
    linear_mod.fit(dates,prices) #fitting the data points in the model
    predicted_price =linear_mod.predict(x)
    return predicted_price[0][0],linear_mod.coef_[0][0] ,linear_mod.intercept_[0]
