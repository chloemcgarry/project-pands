#Importing pandas library
import pandas as pd 
#Importing seaborn library
import seaborn as sns
#Importing matplotlib library
import matplotlib.pyplot as plt

dataset = pd.read_csv('iris_data_set.csv')

#Creating scatter plot of sepal length vs sepal width
f, axes = plt.subplot(1,2, sharey=True, figsize=(6,4))
sns.scatterplot(x="sepal_length", y="sepal_width", data=dataset, ax=axes[0], hue="species")
#Display scatter plot
plt.show()

#Creating scatter plot of petal length vs petal width
sns.scatterplot(x="petal_length", y="petal_width", data=dataset, ax=axes[1], hue="species")
#Display scatter plot
plt.show()