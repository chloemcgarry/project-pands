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


# Resources and References

1. Kaggle
2. Scikit Learn
3. Pandas
4. Seaborn
5. NumPy
6. Matplotlib
7. Lecture videos for this module
8. http://academic.bancey.com/plotting-multivariate-data-with-matplotlibpylab-edgar-andersons-iris-flower-data-set/
