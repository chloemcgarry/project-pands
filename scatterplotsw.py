#Importing pandas library
import pandas as pd 
#Importing matplolib library
import matplotlib.pyplot as plt 

#Read csv file and call it data
data = pd.read_csv('iris_data_set.csv')

#labelling x axis and y axis
x = data.species
y = data.sepal_width 

plt.scatter(x,y)

#Naming the scatter plot of the sepal width data
title = ("Sepal Width Comparison Plot")
#Plotting the sepal width data on a scatter plot
plt.show()