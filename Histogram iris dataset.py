#Histogram Iris Data Set

#Import Pandas library
import pandas as pd 
#Import Seaborn library
import seaborn as sns
#Import Matplotlib library
import matplotlib.pyplot as plt 

#Import iris data set with pandas
f = pd.read_csv("iris_data_set.csv")

#Creating histogram of sepal lengths
sns.distplot(f["sepal_length"], color= "red")
#Giving the histogram a title and labelling the x axis and y axis
plt.title('Sepal Length of All Species Histogram')
plt.xlabel('sepal_length')
plt.ylabel('count')
#Plotting the Histogram
plt.show()

#Creating Histogram of Sepal Widths 
sns.distplot(f["sepal_width"], color= "blue")
#Giving the histpgram a title and labelling the x axis and y axis
plt.title('Sepal Width of All Species Histogram')
plt.xlabel('sepal_width')
plt.ylabel('count')
plt.show()

#Creating the histogram for petal length
sns.distplot(f["petal_length"], color= "green")
#Giving the histogram a title and labelling x axis and y axis
plt.title('Petal Length of All Species Histogram')
plt.xlabel('petal_length')
plt.ylabel('count')
plt.show()

#Creating the histogram for petal width
sns.distplot(f["petal_width"], color= "orange")
#Giving the histogram a title and labelling the x axis and y axis
plt.title('Petal Width of All Species Histogram')
plt.xlabel('petal_width')
plt.ylabel('count')
plt.show()
