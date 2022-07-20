#objective is to preprocess the data and get the data in those terms that we could use to apply our Ml algorithm on

import csv
import matplotlib.pyplot as plt

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
Volume_array=[]
with open('TATAMOTORS.NS.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        Date_array+=[row[0]]
        Open_price_array+=[row[1]]
        Highs_array+=[row[2]]
        Lows_array+=[row[3]]
        Close_price_array+=[row[4]]
        Volume_array+=[row[6]]



# removing the first row that doesnt have numbers
Date_array.pop(0)
Open_price_array.pop(0)
Highs_array.pop(0)
Lows_array.pop(0)
Close_price_array.pop(0)
Volume_array.pop(0)


#converting all to numpy arrays

num_Date=np.array(Date_array)
num_Open=np.array(Open_price_array)
num_High=np.array(Highs_array)
num_Low=np.array(Lows_array)
num_Close=np.array(Close_price_array)
num_Volume=np.array(Volume_array)

num_difference=np.subtract(num_Open,num_Close)

#Firsty utilizing the data that a candlestick plot tells us

#the green or red that implies and up or down can be represented by a boolean numpy array
#green implies 1 and red implies 0
green_red=[]
for i in range(len(num_difference)):
    if num_difference[i]>=0:
        green_red+=[1]
    else:
        green_red+=[0]
num_green_red=np.array(green_red)

#Finding the mean price of each day to then use it for scaling operations
#mean taken wrt open and close ie centre of each candlestick

num_mean=(np.add(num_Close,num_Open))/2

#finding the candlewick part for each day

candlewick_top=[]
candlewick_bottom=[]
for i in range(len(num_green_red)):
    if num_green_red[i]==0:
        candlewick_top+=[Highs_array[i]-Open_price_array[i]]
        candlewick_bottom+=[Close_price_array[i]-Lows_array[i]]
    else:
        candlewick_top+=[Highs_array[i]-Close_price_array[i]]
        candlewick_bottom+=[Open_price_array[i]-Lows_array[i]]

num_candlewick_top=np.array(candlewick_top)
num_candlewick_bottom=np.array(candlewick_bottom)

#scaling the candle size and the candlewick sizes in terms of the mean of each day so that they are
#independent of the price and are related more to the percentage change

num_scaled_diff=num_difference/num_mean
num_scaled_candlewick_top=num_candlewick_top/num_mean
num_scaled_candlewick_bottom=num_candlewick_bottom/num_mean

#next we could include the difference between each days closing and the next days opening
#however the way this is calculated in the actual sctock market
#there doesnt seem that much of a co relation between this and the other parameters
diff_2_days=[]
for i in range(len(Close_price_array)):
    if i==len(Close_price_array)-1:
        break
    diff_2_days+=[Open_price_array[i+1]-Close_price_array[i]]
num_diff_2_days=np.array(diff_2_days)
#note lenght of this array is one less than the others

#another factor that we could use would be the total value of the stock traded per day 
# as simply the product of the volume and candlestick size/ difference

num_product=num_difference*num_Volume




