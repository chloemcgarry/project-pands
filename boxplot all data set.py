#Boxplot for data set

#Import pandas library
import pandas as pd 
#Import seaborn library
import seaborn as sns
#Import matplotlib
import matplotlib.pyplot as plt 

data_set = pd.read_csv('iris_data_set.csv')

#To create boxplot of the Sepal Length column
sns.boxplot(x="species", y=("sepal_length"), data=data_set).set_title('Sepal Length Comparison Plot')
plt.show()

#To create a boxplot of the Sepal Width column
sns.boxplot(x="species", y=("sepal_width"), data=data_set).set_title('Sepal Width Comparison Plot')
plt.show()

#To create a boxplot of the Petal Length column
sns.boxplot(x="species", y=("petal_length"), data=data_set).set_title('Petal Length Comparison Plot')
plt.show()

#To create a boxplot of the Petal Width column
sns.boxplot(x="species", y=("petal_width"), data=data_set).set_title('Petal Width Comparison Plot')
plt.show()