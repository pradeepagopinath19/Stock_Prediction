import csv
import numpy as np
from sklearn.svm import SVR
import requests
import datetime

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)	# skipping column names
        c=0
        for row in csvFileReader:
            if c>25:
                break
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[2]))
            c+=1
        return

def predict_price(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1
    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
    svr_rbf.fit(dates, prices) # fitting the data points in the models
    return svr_rbf.predict(x)[0]

def get_historical(quote):
    url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+quote+'&output=csv'
    r = requests.get(url, stream=True)
    if r.status_code != 400:
        with open(quote+".csv", 'wb') as f:
            for chunk in r:
                f.write(chunk)
    return True

get_historical("mchp")
get_data("mchp"+".csv") # calling get_data method by passing the csv file to it
print(predict_price(dates, prices, (datetime.datetime.now() + datetime.timedelta(days=1)).day
))
