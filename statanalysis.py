#To analyse Fisher's Iris Data Set
#Investigate the mean, median, mode, standard deviation, minumum value and maximum value of the Iris data set


#Importing pandas library
import pandas as pd 

data = pd.read_csv("iris_data_set.csv")

#Short hand for each variable in the data set
sl = 'sepal_length'
sw = 'sepal_width'
pl = 'petal_length'
pw = 'petal_width'

#Using stats to investigate mean, median, mode, standard deviation, minimum value and maximum value of the data set
from statistics import mean, median, mode, stdev

#Finding the mean of the each of the variables
avg1 = mean(data[0:150][sl])
avg2 = mean(data[0:150][sw])
avg3 = mean(data[0:150][pl])
avg4 = mean(data[0:150][pw])
#Printing the average(mean) of each of the variables in the data set
print(avg1, avg2, avg3, avg4)

#Finding the median of each of the variables in the data set
med1 = median(data[0:150][sl])
med2 = median(data[0:150][sw])
med3 = median(data[0:150][pl])
med4 = median(data[0:150][pw])
#Printing the median of each variable of the data set
print(med1, med2, med3, med4)

#Finding the mode of each variable in the data set
mode1 = mode(data[0:150][sl])
mode2 = mode(data[0:150][sw])
mode3 = mode(data[0:150][pl])
mode4 = mode(data[0:150][pw])
#Printing the mode of the variables in the data set
print(mode1, mode2, mode3, mode4)

#Finding the standard deviation of each variable in the data set
std1 = stdev(data[0:150][sl])
std2 = stdev(data[0:150][sw])
std3 = stdev(data[0:150][pl])
std4 = stdev(data[0:150][pw])
#Printing the standard deviation of the variables in the data set
print(std1, std2, std3. std4)

#Finding the Minimum Value of each variable in the data set
min1 = min(data[0:150][sl])
min2 = min(data[0:150][sw])
min3 = min(data[0:150][pl])
min4 = min(data[0:150][pw])
#Printing the minimum value of each variable in the data set

#Finding the maximum value of each variable in the data set
max1 = max(data[0:150][sl])
max2 = max(data[0:150][sw])
max3 = max(data[0:150][pl])
max4 = max(data[0:150][pw])
#Printing the maximum value of each variable in the data set

#To find the range [minumum, maximum] of each variable in the data set
print([min(data[0:150][sl]), max(data[0:150][sl])])
print([min(data[0:150][sw]), max(data[0:150][sw])])
print([min(data[0:150][pl]), max(data[0:150][pl])])
print([min(data[0:150][pw]), max(data[0:150][pw])])