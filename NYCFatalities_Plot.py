#-------------------------------------------------------------------------------
# Name:        verma_priyanka_04
# Purpose:     Script reads JSON data for Fatalities on NYC Roads from 2009-2015
#              Creates a Plot for deaths by year
#              Data Source: NYC Department of Transportation
# Author:      pverma
# Created:     08/10/2015
# Copyright:   (c) pverma 2015
#-------------------------------------------------------------------------------

import json
import matplotlib.pyplot as plt

'''Read and Extract data from JSON'''
with open('C:\\Users\\pverma\\Desktop\\fatality_yearly.json') as f: #Path to data
    data = json.load(f)
l =[]
m = []
for feature in data['features']:
    Fat = feature['properties']['Fatalities']
    Year = feature['properties']['YR']
    l.append(Fat) # list of fatalities
    m.append(Year) #list of year


#initialize variables
y1 = y2 = y3 = y4 = y5 = y6 = y7 = 0
#Calculate number of yearly fatalities
for pos in range(1419):
    if m[pos] == '2009':
        y1 = y1 + l[i]
    elif m[pos] == '2010':
        y2 = y2 + l[i]
    elif m[pos] == '2011':
        y3 = y3 + l[i]
    elif m[pos] == '2012':
        y4 = y4 + l[i]
    elif m[pos] == '2013':
        y5 = y5 + l[i]
    elif m[pos] == '2014':
        y6 = y6 + l[i]
    else:
        y7 = y7 + l[i]


'''Final Lists'''
years =[2009,2010,2011,2012,2013,2014,2015] # years
list2 = [] #fatalities by year
list2.append(y1)
list2.append(y2)
list2.append(y3)
list2.append(y4)
list2.append(y5)
list2.append(y6)
list2.append(y7)


'''Plot Fatalities by Year'''
plot = plt.plot(years,list2)
plt.setp(plot, color='g', linewidth=2.0,marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Fatalities')
plt.title('NYC Road Fatalities By Year')
plt.margins(0.35)
plt.show() #plot

