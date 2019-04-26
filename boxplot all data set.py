#Boxplot for data set

#Import pandas library
import pandas as pd 
#Import seaborn library
import seaborn as sns
#Import matplotlib
import matplotlib.pyplot as plt 

#Import Iris dataset with pandas
f = pd.read_csv("iris_data_set.csv")

#Setting the graph size
plt.figure(figsize= (10.8))

#Giving the plot a title
plt.title("Iris Species Boxplot")

#Setting the boxplot style
#Setting the background colour
sns.set(style="darkgrid", color_codes=True)

#Setting the data set to plot
sns.boxplot(data=f)

#Plotting the data set
plt.show()

