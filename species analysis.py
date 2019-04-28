#Importing pandas library
import pandas as pd

data = pd.read_csv("iris_data_set.csv")

#Short hand for ech variable in the data set
sl = 'sepal_length'
sw = 'sepal_width'
pl = 'petal_length'
pw = 'petal_width'

#Using statistics to investigate the mean, median and standard deviation
from statistics import mean, stdev

#Finding the mean, standard deviation, minimum and maximum of the setosa species
setosa_sl_mean = mean(data[0:50][sl])
setosa_sl_std = stdev(data[0:50][sl])
setosa_sl_min = min(data[0:50][sl])
setosa_sl_max = max(data[0:50][sl])
print(setosa_sl_mean, setosa_sl_std, setosa_sl_min, setosa_sl_max)

setosa_sw_mean = mean(data[0:50][sw])
setosa_sw_std = stdev(data[0:50][sw])
setosa_sw_min = min(data[0:50][sw])
setosa_sw_max = max(data[0:50][sw])
print(setosa_sw_mean, setosa_sw_std, setosa_sw_min, setosa_sw_max)

setosa_pl_mean = mean(data[0:50][pl])
setosa_pl_std = stdev(data[0:50][pl])
setosa_pl_min = min(data[0:50][pl])
setosa_pl_max = max(data[0:50][pl])
print(setosa_pl_mean, setosa_pl_std, setosa_pl_min, setosa_pl_max)\

setosa_pw_mean = mean(data[0:50][pw])
setosa_pw_std = stdev(data[0:50][pw])
setosa_pw_min = min(data[0:50][pw])
setosa_pw_max = max(data[0:50][pw])
print(setosa_pw_mean, setosa_pw_std, setosa_pw_min, setosa_pw_max)

#Finding the mean, standard deviation, minimum and maximum values of the veriscolor species.
veriscolor_sl_mean = mean(data[50:100][sl])
veriscolor_sl_std = stdev(data[50:100][sl])
veriscolor_sl_min = min(data[50:100][sl])
veriscolor_sl_max = max(data[50:100][sl])
print(veriscolor_sl_mean, veriscolor_sl_std, veriscolor_sl_min, veriscolor_sl_max)

veriscolor_sw_mean = mean(data[50:100][sw])
veriscolor_sw_std = stdev(data[50:100][sw])
veriscolor_sw_min = min(data[50:100][sw])
veriscolor_sw_max = max(data[50:100][sw])
print(veriscolor_sw_mean, veriscolor_sw_std, veriscolor_sw_min, veriscolor_sw_max)

veriscolor_pl_mean = mean(data[50:100][pl])
veriscolor_pl_std = stdev(data[50:100][pl])
veriscolor_pl_min = min(data[50:100][pl])
veriscolor_pl_max = max(data[50:100][pl])
print(veriscolor_pl_mean, veriscolor_pl_std, veriscolor_pl_min, veriscolor_pl_max)

veriscolor_pw_mean = mean(data[50:100][pw])
veriscolor_pw_std = stdev(data[50:100][pw])
veriscolor_pw_min = min(data[50:100][pw])
veriscolor_pw_max = max(data[50:100][pw])
print(veriscolor_pw_mean, veriscolor_pw_std, veriscolor_pw_min, veriscolor_pw_max)

#Finding the mean, standard deviation, minimum and maximum values of the virginica species
virginica_sl_mean = mean(data[100:150][sl])
virginica_sl_std = stdev(data[100:150][sl])
virginica_sl_min = min(data[100:150][sl])
virginica_sl_max = max(data[100:150][sl])
print(virginica_sl_mean, virginica_sl_std, virginica_sl_min, virginica_sl_max)

virginica_sw_mean = mean(data[100:150][sw])
virginica_sw_std = stdev(data[100:150][sw])
virginica_sw_min = min(data[100:150][sw])
virginica_sw_max = max(data[100:150][sw])
print(virginica_sw_mean, virginica_sw_std, virginica_sw_min, virginica_sw_max)

virginica_pl_mean = mean(data[100:150][pl])
virginica_pl_std = stdev(data[100:150][pl])
virginica_pl_min = min(data[100:150][pl])
virginica_pl_max = max(data[100:150][pl])
print(virginica_pl_mean, virginica_pl_std, virginica_pl_min, virginica_pl_max)

virginica_pw_mean = mean(data[100:150][pw])
virginica_pw_std = stdev(data[100:150][pw])
virginica_pw_min = min(data[100:150][pw])
virginica_pw_max = max(data[100:150][pw])
print(virginica_pw_mean, virginica_pw_std, virginica_pw_min, virginica_pw_max)

