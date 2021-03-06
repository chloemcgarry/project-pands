# project-pands

This repository is for H. Dip in Computer Science (Data Analytics) project.

# Plan to Investigate the Data Set
1. Researching the data set
2. Use Python to investigate the mean, minimum, maximum and standard deviation of the data set and analyse the results.
3. Graphically represent the data set analysis using python.

# Introduction
Sir Ronald Fisher was a British statistican and biologist who investigated three species of Iris flower and published the results of his investigation in his paper "The use of multiple measurements in taxonomic problems" in 1936.
Fisher pioneered the application of statistics to the design of scientific experiments.
The data set contains 150 observations of the Iris flower. 
Three types of the Iris flower were analysed - Iris setosa, Iris Versicolor and Iris Virginica. 
Measurements were taken of the sepal length, sepal width, petal length and petal width of each of the three species of the Iris flower. The data was recorded in centimetres.
50 flowers of each species were analysed under those four catagories. This led to the data set appearing in the following manner - five columns of data (sepal length, sepal width, petal length, petal width and species) with 150 rows of the data. 
Two of the three species were collected from the Gaspé Peninsula, Quebec, Canada and it is noted that these species of the Iris flower were collected from "the same pasture, picked on the same day, measured at the same time and by the same person".

This data set is a high profile and was one of the first of its kind it is used frequently as a statistics teaching resource and for testing machine learning and visualisations.


![iris flower](https://cdn-images-1.medium.com/max/800/0*GVjzZeYrir0R_6-X.png)

# Python Libraries Used
Many python libraries were used to assist in this project. Some of these were recommended in the lecture videos for this module and through research and analysis of code available online, I discovered that the seaborn library would also be helpful in this project. 

Pandas - This is a Python Data Analysis Library. Pandas is an open source library and is free to use. It is a data analysis tool for the Python programming language. 

NumPy - This is used in scientific computing when using Python. NumPy integrates with data bases quickly and easily. It is an open source software which is readily available. 

Seaborn - This a python-based visualisation library based on Matplotlib. It is used to create visual representation for statistical analysis. 

Matplotlib - Similar to Seaborn, Matplotlib is a visualisation library, creating visual representations for statistical analysis. It is used in Python script creating visuals "with jsut a few line of code". Matplotlib is not a "high-level interface" unlike Seaborn. 

These four libraries were essential in the analysis of Fisher's Iris data set. 

# Analysis of the Iris Data Set
Scatter plots of data

![scatterplots](http://academic.bancey.com/wp-content/uploads/2016/08/iris_wm-768x639.png)

Table of results of sepal length, sepal width, petal length and petal width analysis


Analysis   | sepal_length | sepal_width | petal_length | petal_width |
---------- | ------------ | ----------- | ------------ | ----------- |
**mean**   | 5.843        | 3.054       | 3.75         | 1.987       |
**stdev**  | 0.828        | 0.433       | 1.764        | 0.763       |
**min**    | 4.3          | 2.0         | 1.0          | 0.1         |
**max**    | 7.9          | 4.4         | 6.9          | 2.5         |

Data Summary of each species:

Setosa

Summary   | sepal_length | sepal_width | petal_length | petal_width |
--------- | ------------ | ----------- | ------------ | ----------- |
**mean**  | 5.01         | 3.42        | 1.46         | 0.24        |
**stdev** | 0.35         | 0.38        | 0.17         | 0.11        |
**min**   | 4.3          | 2.3         | 1.0          | 0.1         |
**max**   | 5.8          | 4.4         | 1.9          | 0.6         |

Veriscolor

Summary   | sepal_length | sepal_width | petal_length | petal_width |
--------- | ------------ | ----------- | ------------ | ----------- |
**mean**  | 5.94         | 2.77        | 4.26         | 1.33        |
**stdev** | 0.51         | 0.31        | 0.47         | 0.2         |
**min**   | 4.9          | 2.0         | 3.0          | 1.0         |
**max**   | 7.0          | 3.4         | 5.1          | 1.8         |

Virginica

Summary   | sepal_length | sepal_width | petal_length | petal_width |
--------- | ------------ | ----------- | -------------| ----------- |
**mean**  | 6.59         | 2.97        | 5.55         | 2.03        |
**stdev** | 0.63         | 0.32        | 0.55         | 0.27        |
**min**   | 4.9          | 2.2         | 4.5          | 1.4         |
**max**   | 7.9          | 3.8         | 6.9          | 2.5         |



# Areas of Development
There are serveral areas and skills which I developed and learned through out this project. 
1. The use of python libraries.

Prior to this project I used matplotlib on a few occasions. In my research of the project I found that Seaborn would be important in the creation of visual representation of the data.

2. Github Flavoured Markdown

Throughout this project I understood the importance of using images, tables and url links in all aspects.
I inserted images of scatterplots, boxplots and the iris flowers.
Created tables to display data.

# Resources and References

1. Kaggle https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
2. Scikit Learn https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
3. Pandas https://pandas.pydata.org/
4. Seaborn https://seaborn.pydata.org/
5. NumPy https://www.numpy.org/
6. Matplotlib https://matplotlib.org/
7. Lecture videos for this module
8. http://academic.bancey.com/plotting-multivariate-data-with-matplotlibpylab-edgar-andersons-iris-flower-data-set/
9. UCI Machine Learning Repository https://archive.ics.uci.edu/ml/datasets/iris
10. https://en.wikipedia.org/wiki/Iris_flower_data_set
11. https://gist.github.com/curran/a08a1080b88344b0c8a7
12. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
