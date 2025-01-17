import pandas as pd
import csv
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

print("Loading Data...")
city = pd.read_csv("./data/City_time_series.csv")
prefilter_shape = city.shape[0]pip insta
print(city.columns)

# Begin filtering
# create subtable with just 3bedroom prices, cityID, and Date
# add new column for true if a 3bedroom price exists for that row (use isnull)
# group each cityId by number of true values (see last dsc10 lecture for how to do this)
cols = ["Date", "RegionName", "MedianListingPricePerSqft_1Bedroom", "MedianListingPricePerSqft_2Bedroom", "MedianListingPricePerSqft_3Bedroom", "MedianListingPricePerSqft_4Bedroom", "MedianListingPricePerSqft_5BedroomOrMore"]
city_filter1 = city.filter(cols)
for i in tqdm(range(1, 5)):
    city_filter1 = city_filter1[city_filter1["MedianListingPricePerSqft_" + str(i) + "Bedroom"].isnull() == False]
city_filter1 = city_filter1[city_filter1["MedianListingPricePerSqft_5BedroomOrMore"].isnull() == False]
cityList = np.unique(city_filter1['RegionName'].values)
postfilter_shape = city_filter1.shape[0]

print(city_filter1.head())
print(city_filter1.shape)
print(city_filter1.sort_values('Date', ascending=True).head())
print("Filtered", (prefilter_shape - postfilter_shape), "values")

city_filter2 = city_filter1.groupby('RegionName').count().sort_values('Date', ascending=False)
print(city_filter2.head())

city_filter3 = city_filter1[city_filter1['RegionName'] == 'yonkerswestchesterny']
print(city_filter3.sort_values('Date', ascending=False).head())

fig, ax = plt.subplots()
ax.plot(city_filter3['Date'], city_filter3['MedianListingPricePerSqft_5BedroomOrMore'], label='5 Bedrooms')
ax.plot(city_filter3['Date'], city_filter3['MedianListingPricePerSqft_4Bedroom'], label='4 Bedrooms')
ax.plot(city_filter3['Date'], city_filter3['MedianListingPricePerSqft_3Bedroom'], label='3 Bedrooms')
ax.plot(city_filter3['Date'], city_filter3['MedianListingPricePerSqft_2Bedroom'], label='2 Bedrooms')
ax.plot(city_filter3['Date'], city_filter3['MedianListingPricePerSqft_1Bedroom'], label='1 Bedroom')
ax.legend()

plt.show()
