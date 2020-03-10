import pandas as pd
import numpy as np
from datetime import datetime

data_cab = pd.read_csv("./uber-lyft-cab-prices/cab_rides.csv",delimiter=',')
data_weather = pd.read_csv("./uber-lyft-cab-prices/weather.csv",delimiter=',')

#Remove id product_id columns
data_cab = data_cab.drop(columns=['id','product_id'])

#Convert date_time to Weekday and date
data_cab['date_time'] = [datetime.utcfromtimestamp(i/1000).strftime('%Y-%m-%d:%H') for i in data_cab['time_stamp']]
data_cab['date'] = [datetime.utcfromtimestamp(i/1000).strftime('%Y-%m-%d') for i in data_cab['time_stamp']]
data_cab['time'] = [datetime.utcfromtimestamp(i/1000).strftime('%H:%M') for i in data_cab['time_stamp']]
data_cab['weekday'] = [(pd.Timestamp(i)).dayofweek for i in data_cab['date']]
data_cab = data_cab.drop(columns=['time_stamp'])

data_weather['date_time'] = [datetime.utcfromtimestamp(i).strftime('%Y-%m-%d:%H') for i in data_weather['time_stamp']]
data_weather = data_weather.drop(columns=['time_stamp'])

#Join two dataset
data_cab['date-location'] = data_cab.source.astype(str)+","+data_cab.date_time.astype(str)
data_weather['date-location'] = data_weather.location.astype(str)+","+data_weather.date_time.astype(str)
data_weather.index = data_weather['date-location']
data_merged = data_cab.join(data_weather,on=['date-location'],rsuffix ='_copy')


data_merged = data_merged.drop(columns=['date_time_copy','date-location_copy'])
data_merged = data_merged.drop(columns=['date-location','location'])

#Save joint dataset as data_merge.csv
data_merged.to_csv("./data_merged.csv",index=False,sep=',')
