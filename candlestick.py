import csv
import matplotlib.pyplot as plt
#from mpl_finance import candlestick_ohlc
#use this second one instead of the previous line of code then everything works fine

from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import numpy as np
import datetime

#initialising arrays to store the date the open price close price high and low
Date_array=[]
Open_price_array=[]
Close_price_array=[]
Highs_array=[]
Lows_array=[]
with open('TATAMOTORS.NS.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        Date_array+=[row[0]]
        Open_price_array+=[row[1]]
        Highs_array+=[row[2]]
        Lows_array+=[row[3]]
        Close_price_array+=[row[4]]

#splitting the data into period of 20 days so that we could plot in groups of 20 and then save that data as images locally
#setting the period here in case we want to change the period for which we want to take images of the candlestick data
period=20
#using a while loop that will break out once there are less than 20 days to put in a graph
iterator=0
while(True):
    if (iterator+1)*period>len(Date_array):
        break
    
    # Defining a dataframe showing stock prices 
    # of a week
    stock_prices = pd.DataFrame({'date': np.array([datetime.datetime.strptime(Date_array[iterator*period+i+1], '%Y-%m-%d') for i in range(period)]),
                                'open': Open_price_array[1+iterator*period:period+1+iterator*period],
                                'close': Close_price_array[1+iterator*period:period+1+iterator*period],
                                'high': Highs_array[1+iterator*period:period+1+iterator*period],
                                'low': Lows_array[1+iterator*period:period+1+iterator*period]})
    
    ohlc = stock_prices.loc[:, ['date', 'open', 'high', 'low', 'close']]
    ohlc['date'] = pd.to_datetime(ohlc['date'])
    ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)
    
    # Creating Subplots
    fig, ax = plt.subplots()
    
    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green',
                    colordown='red', alpha=0.8)
    
    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Stock Prices of a week')
    
    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    
    fig.tight_layout()

    #path_of_file='/Users/ruchir/Documents/Playgrounds/tutorial/Candle_TATA/Plot.png'
    path_of_file="/Users/ruchir/Documents/Playgrounds/tutorial/Candle_TATA/Plot" + str(iterator+1)+ ".png"

    plt.savefig(path_of_file)
    plt.close()
    iterator+=1