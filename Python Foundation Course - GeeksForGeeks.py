# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # [Python Programming Foundation Course](https://practice.geeksforgeeks.org/courses/Python-Foundation?utm_source=geeksforgeeks&utm_medium=article&utm_campaign=GFG_Article_Bottom_Python_Foundation) <a class="tocSkip">

# by GeeksForGeeks 

# + [markdown] heading_collapsed=true
# # [Python | Pandas DataFrame](https://www.geeksforgeeks.org/python-pandas-dataframe/)

# + [markdown] hidden=true
# **Pandas DataFrame** is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the **data**, **rows**, and **columns**.

# + [markdown] hidden=true
# <img src="https://media.geeksforgeeks.org/wp-content/uploads/finallpandas.png" />

# + [markdown] hidden=true
# We will get a brief insight on all these basic operation which can be performed on Pandas DataFrame :
#
# * [Creating a DataFrame](#Creating-a-Pandas-DataFrame)
# * [Dealing with Rows and Columns](#Dealing-with-Rows-and-Columns)
# * [Indexing and Selecting Data](#Indexing-and-Selecting-Data)
# * [Working with Missing Data](#Selecting-a-single-columns)
# * [Iterating over rows and columns](#Iterating-over-rows-and-columns)

# + [markdown] heading_collapsed=true hidden=true
# ## Creating a DataFrame

# + [markdown] hidden=true
# In the real world, a Pandas DataFrame will be created by loading the datasets from existing storage, storage can be SQL Database, CSV file, and Excel file. Pandas DataFrame can be created from the lists, dictionary, and from a list of dictionary etc. Dataframe can be created in different ways here are some ways by which we create a dataframe:

# + [markdown] hidden=true
# **Creating a dataframe using List:** DataFrame can be created using a single list or a list of lists.

# + hidden=true
# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

# + [markdown] hidden=true
# **Creating DataFrame from dict of ndarray/lists:** To create DataFrame from dict of narray/list, all the narray must be of same length. If index is passed then the length index should be equal to the length of arrays. If no index is passed, then by default, index will be range(n) where n is the array length.

# + hidden=true
# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses.
 
import pandas as pd
 
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)

# + [markdown] heading_collapsed=true hidden=true
# ## Dealing with Rows and Columns

# + [markdown] hidden=true
# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. We can perform basic operations on rows/columns like selecting, deleting, adding, and renaming.

# + [markdown] hidden=true
# **Column Selection:** In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.

# + hidden=true
# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])

# + [markdown] hidden=true
# **Row Selection:** Pandas provide a unique method to retrieve rows from a Data frame.[DataFrame.loc\[\]](https://www.geeksforgeeks.org/python-pandas-extracting-rows-using-loc/) method is used to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to an [iloc\[\]](https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/) function.

# + [markdown] hidden=true
# **Note:** We’ll be using [nba.csv](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv) file in below examples.

# + hidden=true
# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", index_col ="Name")
 
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)

# + [markdown] hidden=true
# For more Details refer to [Dealing with Rows and Columns](https://www.geeksforgeeks.org/dealing-with-rows-and-columns-in-pandas-dataframe/)

# + [markdown] heading_collapsed=true hidden=true
# ## Indexing and Selecting Data

# + [markdown] hidden=true
# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame. Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. Indexing can also be known as **Subset Selection**.

# + [markdown] heading_collapsed=true hidden=true
# #### Indexing a Dataframe using indexing operator [] : <a class="tocSkip">

# + [markdown] hidden=true
# Indexing operator is used to refer to the square brackets following an object. The [.loc](https://www.geeksforgeeks.org/python-pandas-extracting-rows-using-loc/) and [.iloc](https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/) indexers also use the indexing operator to make selections. In this indexing operator to refer to `df[]`.

# + [markdown] heading_collapsed=true hidden=true
# ### Selecting a single columns

# + [markdown] hidden=true
# In order to select a single column, we simply put the name of the column in-between the brackets

# + hidden=true
# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", index_col ="Name")
 
# retrieving columns by indexing operator
first = data["Age"]

print(first)

# + [markdown] heading_collapsed=true hidden=true
# #### Indexing a DataFrame using [.loc\[\]](https://www.geeksforgeeks.org/python-pandas-extracting-rows-using-loc/) :  <a class="tocSkip">

# + [markdown] hidden=true
# This function selects data by the **label** of the rows and columns. The `df.loc` indexer selects data in a different way than just the indexing operator. It can select subsets of rows or columns. It can also simultaneously select subsets of rows and columns.

# + [markdown] heading_collapsed=true hidden=true
# ### Selecting a single row

# + [markdown] hidden=true
# In order to select a single row using `.loc[]`, we put a single row label in a `.loc` function.

# + hidden=true
# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", index_col ="Name")
 
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
 
 
print(first, "\n\n\n", second)

# + [markdown] heading_collapsed=true hidden=true
# #### Indexing a DataFrame using [.iloc\[\]](https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/) :  <a class="tocSkip">

# + [markdown] hidden=true
# This function allows us to retrieve rows and columns by position. In order to do that, we’ll need to specify the positions of the rows that we want, and the positions of the columns that we want as well. The `df.iloc` indexer is very similar to `df.loc` but only uses integer locations to make its selections.

# + [markdown] hidden=true
# In order to select a single row using `.iloc[]`, we can pass a single integer to `.iloc[]` function.

# + hidden=true
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", index_col ="Name")

# retrieving rows by iloc method 
row2 = data.iloc[3] 

print(row2)

# + [markdown] hidden=true
# For more Details refer
#
# * [Indexing and Selecting Data with Pandas](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
# * [Boolean Indexing in Pandas](https://www.geeksforgeeks.org/boolean-indexing-in-pandas/)

# + [markdown] heading_collapsed=true hidden=true
# ## Working with Missing Data

# + [markdown] hidden=true
# Missing Data can occur when no information is provided for one or more items or for a whole unit. Missing Data is a very big problem in real life scenario. Missing Data can also refer to as NA(Not Available) values in pandas.

# + [markdown] heading_collapsed=true hidden=true
# #### Checking for missing values using isnull() and notnull() : <a class="tocSkip">

# + [markdown] hidden=true
# In order to check missing values in Pandas DataFrame, we use a function `isnull()` and `notnull()`. Both function help in checking whether a value is `NaN` or not. These function can also be used in Pandas Series in order to find null values in a series.

# + hidden=true
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function  
df.isnull()

# + [markdown] heading_collapsed=true hidden=true
# #### Filling missing values using `fillna()`, `replace()` and `interpolate()` : <a class="tocSkip">

# + [markdown] hidden=true
# In order to fill null values in a datasets, we use `fillna()`, `replace()` and `interpolate()` function these function replace NaN values with some value of their own. All these function help in filling a null values in datasets of a DataFrame. Interpolate() function is basically used to fill NA values in the dataframe but it uses various interpolation technique to fill the missing values rather than hard-coding the value.

# + hidden=true
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# filling missing value using fillna()  
df.fillna(0)

# + [markdown] heading_collapsed=true hidden=true
# #### Dropping missing values using `dropna()` : <a class="tocSkip">

# + [markdown] hidden=true
# In order to drop a null values from a dataframe, we used `dropna()` function this fuction drop Rows/Columns of datasets with Null values in different ways.

# + hidden=true
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
   
df

# + [markdown] hidden=true
# Now we drop rows with at least one Nan value (Null value)

# + hidden=true
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# using dropna() function  
df.dropna()

# + [markdown] hidden=true
# For more Details refer to [Working with Missing Data in Pandas](https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/)

# + [markdown] heading_collapsed=true hidden=true
# ## Iterating over rows and columns

# + [markdown] hidden=true
# Iteration is a general term for taking each item of something, one after another. Pandas DataFrame consists of rows and columns so, in order to iterate over dataframe, we have to iterate a dataframe like a dictionary.

# + [markdown] heading_collapsed=true hidden=true
# #### Iterating over rows : <a class="tocSkip">

# + [markdown] hidden=true
# In order to iterate over rows, we can use three function `iteritems()`, `iterrows()`, `itertuples()`. These three function will help in iteration over rows.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
print(df)

# + [markdown] hidden=true
# Now we apply `iterrows()` function in order to get a each element of rows.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
# iterating over rows using iterrows() function 
for i, j in df.iterrows():
    print(i, j)
    print()

# + [markdown] heading_collapsed=true hidden=true
# #### Iterating over Columns : <a class="tocSkip">

# + [markdown] hidden=true
# In order to iterate over columns, we need to create a list of dataframe columns and then iterating through that list to pull out the dataframe columns.

# + hidden=true
# importing pandas as pd
import pandas as pd
   
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
  
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
 
print(df)

# + [markdown] hidden=true
# Now we iterate through columns in order to iterate through columns we first create a list of dataframe columns and then iterate through list.

# + hidden=true
# creating a list of dataframe columns
columns = list(df)
 
for i in columns:
 
    # printing the third element of the column
    print (df[i][2])

# + [markdown] hidden=true
# For more Details refer to [Iterating over rows and columns in Pandas DataFrame](https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/)

# + [markdown] heading_collapsed=true hidden=true
# #### DataFrame Methods:  <a class="tocSkip">

# + [markdown] hidden=true
# | FUNCTION | DESCRIPTION |
# | --- | --- |
# | index() | Method returns index (row labels) of the DataFrame |
# | insert() | Method inserts a column into a DataFrame |
# | add() | Method returns addition of dataframe and other, element-wise (binary operator add) |
# | sub() | Method returns subtraction of dataframe and other, element-wise (binary operator sub) |
# | mul() | Method returns multiplication of dataframe and other, element-wise (binary operator mul) |
# | div() | Method returns floating division of dataframe and other, element-wise (binary operator truediv) |
# | unique() | Method extracts the unique values in the dataframe |
# | nunique() | Method returns count of the unique values in the dataframe |
# | value_counts() | Method counts the number of times each unique value occurs within the Series |
# | columns() | Method returns the column labels of the DataFrame |
# | axes() | Method returns a list representing the axes of the DataFrame |
# | isnull() | Method creates a Boolean Series for extracting rows with null values |
# | notnull() | Method creates a Boolean Series for extracting rows with non-null values |
# | between() | Method extracts rows where a column value falls in between a predefined range |
# | isin() | Method extracts rows from a DataFrame where a column value exists in a predefined collection |
# | dtypes() | Method returns a Series with the data type of each column. The result’s index is the original DataFrame’s columns |
# | astype() | Method converts the data types in a Series |
# | values() | Method returns a Numpy representation of the DataFrame i.e. only the values in the DataFrame will be returned, the axes labels will be removed |
# | sort_values() | Set1, Set2	Method sorts a data frame in Ascending or Descending order of passed Column |
# | sort_index() | Method sorts the values in a DataFrame based on their index positions or labels instead of their values but  sometimes a data frame is made out of two or more data frames and hence later index can be changed using this method |
# | loc[] | Method retrieves rows based on index label |
# | iloc[] | Method retrieves rows based on index position |
# | ix[] | Method retrieves DataFrame rows based on either index label or index position. This method combines the best features of the .loc[] and .iloc[] methods |
# | rename() | Method is called on a DataFrame to change the names of the index labels or column names |
# | columns() | Method is an alternative attribute to change the coloumn name |
# | drop() | Method is used to delete rows or columns from a DataFrame |
# | pop() | Method is used to delete rows or columns from a DataFrame |
# | sample() | Method pulls out a random sample of rows or columns from a DataFrame |
# | nsmallest() | Method pulls out the rows with the smallest values in a column |
# | nlargest() | Method pulls out the rows with the largest values in a column |
# | shape() | Method returns a tuple representing the dimensionality of the DataFrame |
# | ndim() | Method returns an ‘int’ representing the number of axes / array dimensions.
# Returns 1 if Series, otherwise returns 2 if DataFrame |
# | dropna() | Method allows the user to analyze and drop Rows/Columns with Null values in different ways |
# | fillna() | Method manages and let the user replace NaN values with some value of their own |
# | rank() | Values in a Series can be ranked in order with this method |
# | query() | Method is an alternate string-based syntax for extracting a subset from a DataFrame |
# | copy() | Method creates an independent copy of a pandas object |
# | duplicated() | Method creates a Boolean Series and uses it to extract rows that have duplicate values |
# | drop_duplicates() | Method is an alternative option to identifying duplicate rows and removing them through filtering |
# | set_index() | Method sets the DataFrame index (row labels) using one or more existing columns |
# | reset_index() | Method resets index of a Data Frame. This method sets a list of integer ranging from 0 to length of data as index |
# | where() | Method is used to check a Data Frame for one or more condition and return the result accordingly. By default, the rows not satisfying the condition are filled with NaN value |
#  

# + [markdown] heading_collapsed=true hidden=true
# #### More on Pandas:  <a class="tocSkip">

# + [markdown] hidden=true
# * [Python | Pandas Series](https://www.geeksforgeeks.org/python-pandas-series/)
# * [Python | Pandas Working With Text Data](https://www.geeksforgeeks.org/python-pandas-working-with-text-data/)
# * [Python | Pandas Working with Dates and Times](https://www.geeksforgeeks.org/python-pandas-working-with-dates-and-times/)
# * [Python | Pandas Merging, Joining, and Concatenating](https://www.geeksforgeeks.org/python-pandas-merging-joining-and-concatenating/)
#

# + [markdown] heading_collapsed=true
# # [Python | Pandas dataframe.aggregate()](https://www.geeksforgeeks.org/python-pandas-dataframe-aggregate/)

# + [markdown] hidden=true
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier.
#
# Dataframe.aggregate() function is used to apply some aggregation across one or more column. Aggregate using callable, string, dict, or list of string/callables. Most frequently used aggregations are:
#
# | | |
# | --- | --- |
# | **sum:** | Return the sum of the values for the requested axis |
# | **min:** | Return the minimum of the values for the requested axis |
# | **max:** | Return the maximum of the values for the requested axis |
#
#
#
# | **Syntax:** | `DataFrame.aggregate(func, axis=0, *args, **kwargs)`  |
# | --- | --- |
# | **Parameters :** | |
# | **func :** | callable, string, dictionary, or list of string/callables. Function to use for aggregating the data. |
# | | If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. |
# | | For a DataFrame, can pass a dict, if the keys are DataFrame column names. |
# | **axis :** {0 or ‘index’ (default), 1 or ‘columns’} | 0 or ‘index’:   apply function to each column. |
# |                                                     | 1 or ‘columns’: apply function to each row.    |
# | **Returns :** | Aggregated DataFrame |
#
#
#

# + [markdown] hidden=true
# For link to CSV file Used in Code, click [here](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv)
#
# **Example #1:** Aggregate ‘sum’ and ‘min’ function across all the columns in data frame.

# + hidden=true
# importing pandas package
import pandas as pd
  
# making data frame from csv file
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
# printing the first 10 rows of the dataframe
df[:10]

# + [markdown] hidden=true
# Aggregation works with only numeric type columns.
#
# **Output of following code:**
#
# For each column which are having numeric values, minimum and sum of all values has been found. For dataframe df , we have four such columns Number, Age, Weight, Salary.

# + hidden=true
# Applying aggregation across all the columns 
# sum and min will be found for each 
# numeric type column in df dataframe
  
df.aggregate(['sum', 'min'])

# + [markdown] hidden=true
# **Example #2:** 
#
# In Pandas, we can also apply different aggregation functions across different columns. For that, we need to pass a dictionary with key containing the column names and values containing the list of aggregation functions for any specific column.
#
# **Output of following code:**
#
# Separate aggregation has been applied to each column, if any specific aggregation is not applied on a column then it has NaN value corresponding to it.

# + hidden=true
# importing pandas package
import pandas as pd
  
# making data frame from csv file
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
# We are going to find aggregation for these columns
df.aggregate({"Number":['sum', 'min'],
              "Age":['max', 'min'],
              "Weight":['min', 'sum'], 
              "Salary":['sum']})

# + [markdown] heading_collapsed=true
# # [Pandas GroupBy](https://www.geeksforgeeks.org/pandas-groupby/?ref=lbp)

# + [markdown] hidden=true
# Groupby is a pretty simple concept. We can create a grouping of categories and apply a function to the categories. It’s a simple concept but it’s an extremely valuable technique that’s widely used in data science. In real data science projects, you’ll be dealing with large amounts of data and trying things over and over, so for efficiency, we use Groupby concept. Groupby concept is really important because it’s ability to aggregate data efficiently, both in performance and the amount code is magnificent. Groupby mainly refers to a process involving one or more of the following steps they are:
#
# * Splitting : It is a process in which we split data into group by applying some conditions on datasets.
# * Applying : It is a process in which we apply a function to each group independently
# * Combining : It is a process in which we combine different datasets after applying groupby and results into a data structure

# + [markdown] hidden=true
# The following image will help in understanding a process involve in Groupby concept.
# 1. Group the unique values from the Team column <img src="https://media.geeksforgeeks.org/wp-content/uploads/groupby1.png" alt="" width="1000" height="484" class="alignnone size-full wp-image-873011">
# 1. Now there’s a bucket for each group <img src="https://media.geeksforgeeks.org/wp-content/uploads/groupby3.png" alt="" width="1000" height="717" class="alignnone size-full wp-image-873014">
# 1. Toss the other data into the buckets <img src="https://media.geeksforgeeks.org/wp-content/uploads/groupby2.png" alt="" width="1000" height="458" class="alignnone size-full wp-image-873013">
# 1.  Apply a function on the weight column of each bucket. <img src="https://media.geeksforgeeks.org/wp-content/uploads/groupby4.png" alt="" width="1000" height="779" class="alignnone size-full wp-image-873021">

# + [markdown] heading_collapsed=true hidden=true
# ## Splitting Data into Groups

# + [markdown] hidden=true
# Splitting is a process in which we split data into a group by applying some conditions on datasets. In order to split the data, we apply certain conditions on datasets. In order to split the data, we use `groupby()` function this function is used to split the data into groups based on some criteria. Pandas objects can be split on any of their axes. The abstract definition of grouping is to provide a mapping of labels to group names. Pandas datasets can be split into any of their objects. There are multiple ways to split data like:
#
# * `obj.groupby(key)`
# * `obj.groupby(key, axis=1)`
# * `obj.groupby([key1, key2])`
#
# **Note :** In this we refer to the grouping objects as the keys.

# + [markdown] heading_collapsed=true hidden=true
# ## Grouping data with one key:
#

# + [markdown] hidden=true
# In order to group data with one key, we pass only one key as an argument in groupby function.

# + hidden=true
# importing pandas module
import pandas as pd 
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we group a data of `Name` using `groupby()` function.

# + hidden=true
# using groupby function
# with one key
  
df.groupby('Name')
print(df.groupby('Name').groups)

# + [markdown] hidden=true
# **Output :**
#
# <img src="https://media.geeksforgeeks.org/wp-content/uploads/ser23.jpg" alt="" width="982" height="41" class="alignnone size-full wp-image-840328">

# + [markdown] hidden=true
# Now we print the first entries in all the groups formed.

# + hidden=true
# applying groupby() function to 
# group the data on Name value. 
gk = df.groupby('Name') 
    
# Let's print the first entries 
# in all the groups formed. 
gk.first() 

# + [markdown] heading_collapsed=true hidden=true
# ## Grouping data with multiple keys :

# + [markdown] hidden=true
# In order to group data with multiple keys, we pass multiple keys in `groupby` function.

# + hidden=true
# importing pandas module
import pandas as pd 
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we group a data of “Name” and “Qualification” together using multiple keys in groupby function.

# + hidden=true
# Using multiple keys in
# groupby() function
df.groupby(['Name', 'Qualification'])

print(df.groupby(['Name', 'Qualification']).groups)

# + [markdown] heading_collapsed=true hidden=true
# ## Grouping data by sorting keys :

# + [markdown] hidden=true
# Group keys are sorted by default uring the groupby operation. User can pass `sort=False` for potential speedups.

# + hidden=true
# importing pandas module
import pandas as pd 

# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], } 


# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)

print(df) 

# + [markdown] hidden=true
# Now we apply `groupby()` without `sort`

# + hidden=true
# using groupby function
# without using sort
  
df.groupby(['Name']).sum()

# + [markdown] hidden=true
# Now we apply `groupby()` using sort in order to attain potential speedups

# + hidden=true
# using groupby function
# with sort
  
df.groupby(['Name'], sort = False).sum()

# + [markdown] heading_collapsed=true hidden=true
# ## Grouping data with object attributes :

# + [markdown] hidden=true
# Groups attribute is like dictionary whose keys are the computed unique groups and corresponding values being the axis labels belonging to each group.

# + hidden=true
# importing pandas module
import pandas as pd 
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we group data like we do in a dictionary using keys.

# + hidden=true
# using keys for grouping
# data
  
df.groupby('Name').groups

# + [markdown] heading_collapsed=true hidden=true
# ## Iterating through groups

# + [markdown] hidden=true
# In order to iterate an element of groups, we can iterate through the object similar to `itertools.obj`.

# + hidden=true
# importing pandas module
import pandas as pd 
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we iterate an element of group in a similar way we do in itertools.obj.

# + hidden=true
# iterating an element
# of group
  
grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()

# + [markdown] hidden=true
# Now we iterate an element of group containing multiple keys

# + hidden=true
# iterating an element
# of group containing 
# multiple keys
  
grp = df.groupby(['Name', 'Qualification'])
for name, group in grp:
    print(name)
    print(group)
    print()

# + [markdown] heading_collapsed=true hidden=true
# ## Selecting a groups

# + [markdown] hidden=true
# In order to select a group, we can select group using `GroupBy.get_group()`. We can select a group by applying a function `GroupBy.get_group` this function select a single group.

# + hidden=true
# importing pandas module
import pandas as pd 
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df)

# + [markdown] hidden=true
# Now we select a single group using `Groupby.get_group`.

# + hidden=true
# selecting a single group
  
grp = df.groupby('Name')
grp.get_group('Jai')

# + [markdown] hidden=true
# Now we select an object grouped on multiple columns

# + hidden=true
# selecting object grouped
# on multiple columns
  
grp = df.groupby(['Name', 'Qualification'])
grp.get_group(('Jai', 'Msc'))

# + [markdown] heading_collapsed=true hidden=true
# ## Applying function to group

# + [markdown] hidden=true
# After splitting a data into a group, we apply a function to each group in order to do that we perform some operation they are:
#
# * **Aggregation :** It is a process in which we compute a summary statistic (or statistics) about each group. For Example, Compute group sums ormeans
# * **Transformation :** It is a process in which we perform some group-specific computations and return a like-indexed. For Example, Filling NAs within groups with a value derived from each group
# * **Filtration :** It is a process in which we discard some groups, according to a group-wise computation that evaluates True or False. For Example, Filtering out data based on the group sum or mean

# + [markdown] hidden=true
# **Aggregation :**
#
# Aggregation is a process in which we compute a summary statistic about each group. Aggregated function returns a single aggregated value for each group. After splitting a data into groups using `groupby` function, several aggregation operations can be performed on the grouped data.
#
# **Code #1:** Using aggregation via the aggregate method

# + hidden=true
# importing pandas module
import pandas as pd 
  
# importing numpy as np
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we perform aggregation using aggregate method

# + hidden=true
# performing aggregation using
# aggregate method
  
grp1 = df.groupby('Name')
  
grp1.aggregate(np.sum)

# + [markdown] hidden=true
# Now we perform aggregation on agroup containing multiple keys

# + hidden=true
# performing aggregation on
# group containing multiple
# keys
grp1 = df.groupby(['Name', 'Qualification'])
  
grp1.aggregate(np.sum)

# + [markdown] heading_collapsed=true hidden=true
# ## Applying multiple functions at once :

# + [markdown] hidden=true
# We can apply a multiple functions at once by passing a list or dictionary of functions to do aggregation with, outputting a DataFrame.

# + hidden=true

# importing pandas module
import pandas as pd 
  
# importing numpy as np
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we apply a multiple functions by passing a list of functions.

# + hidden=true
# applying a function by passing
# a list of functions
  
grp = df.groupby('Name')
  
grp['Age'].agg([np.sum, np.mean, np.std])

# + [markdown] heading_collapsed=true hidden=true
# ## Applying different functions to DataFrame columns :

# + [markdown] hidden=true
# In order to apply a different aggregation to the columns of a DataFrame, we can pass a dictionary to aggregate .

# + hidden=true
# importing pandas module
import pandas as pd 
  
# importing numpy as np
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score': [23, 34, 35, 45, 47, 50, 52, 53]} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we apply a different aggregation to the columns of a dataframe.

# + hidden=true
# using different aggregation
# function by passing dictionary
# to aggregate
grp = df.groupby('Name')
  
grp.agg({'Age' : 'sum', 'Score' : 'std'})

# + [markdown] heading_collapsed=true hidden=true
# ## Transformation :

# + [markdown] hidden=true
# Transformation is a process in which we perform some group-specific computations and return a like-indexed. Transform method returns an object that is indexed the same (same size) as the one being grouped. The transform function must:
#
# * Return a result that is either the same size as the group chunk
# * Operate column-by-column on the group chunk
# * Not perform in-place operations on the group chunk.

# + hidden=true

# importing pandas module
import pandas as pd 
  
# importing numpy as np
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score': [23, 34, 35, 45, 47, 50, 52, 53]} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we perform some group-specific computations and return a like-indexed.

# + hidden=true
## using transform function
grp = df.groupby('Name')
sc = lambda x: (x - x.mean()) / x.std()*10
grp.transform(sc)

# + [markdown] heading_collapsed=true hidden=true
# ## Filtration :

# + [markdown] hidden=true
# Filtration is a process in which we discard some groups, according to a group-wise computation that evaluates `True` or `False`. In order to filter a group, we use filter method and apply some condition by which we filter group.

# + hidden=true
# importing pandas module
import pandas as pd 
  
# importing numpy as np
import numpy as np
   
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score': [23, 34, 35, 45, 47, 50, 52, 53]} 
     
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
   
print(df) 

# + [markdown] hidden=true
# Now we filter data that to return the Name which have lived two or more times .

# + hidden=true
# filtering data using
# filter data
grp = df.groupby('Name')
grp.filter(lambda x: len(x) >= 2)


# + [markdown] heading_collapsed=true
# # [Combining multiple columns in Pandas groupby with dictionary](https://www.geeksforgeeks.org/combining-multiple-columns-in-pandas-groupby-with-dictionary/?ref=lbp)

# + [markdown] hidden=true
# Let’ see how to combine multiple columns in Pandas using groupby with dictionary with the help of different examples.
#
# **Example #1:**

# + hidden=true
# importing pandas as pd 
import pandas as pd 
  
# Creating a dictionary 
d = {'id':['1', '2', '3'],
     'Column 1.1':[14, 15, 16],
     'Column 1.2':[10, 10, 10],
     'Column 1.3':[1, 4, 5],
     'Column 2.1':[1, 2, 3],
     'Column 2.2':[10, 10, 10], }
  
# Converting dictionary into a data-frame 
df = pd.DataFrame(d)
print(df)

# + hidden=true
# Creating the groupby dictionary 
groupby_dict = {'Column 1.1':'Column 1',
                'Column 1.2':'Column 1',
                'Column 1.3':'Column 1',
                'Column 2.1':'Column 2',
                'Column 2.2':'Column 2' }
  
# Set the index of df as Column 'id'
df = df.set_index('id')
  
# Groupby the groupby_dict created above 
df = df.groupby(groupby_dict, axis = 1).min()
print(df)

# + [markdown] hidden=true
# **Explanation**
#
# Here we have grouped Column 1.1, Column 1.2 and Column 1.3 into Column 1 and Column 2.1, Column 2.2 into Column 2.
# Notice that the output in each column is the min value of each row of the columns grouped together. i.e in Column 1, value of first row is the minimum value of Column 1.1 Row 1, Column 1.2 Row 1 and Column 1.3 Row 1.
#  
# **Example #2:**

# + hidden=true
# importing pandas as pd 
import pandas as pd 
  
# Create dictionary with data 
dict = {
    "ID":[1, 2, 3],
    "Movies":["The Godfather", "Fight Club", "Casablanca"],
    "Week_1_Viewers":[30, 30, 40],
    "Week_2_Viewers":[60, 40, 80],
    "Week_3_Viewers":[40, 20, 20] };
  
# Convert dictionary to dataframe
df = pd.DataFrame(dict);
print(df)

# + hidden=true
# Create the groupby_dict 
groupby_dict = {
    "Week_1_Viewers":"Total_Viewers",
    "Week_2_Viewers":"Total_Viewers",
    "Week_3_Viewers":"Total_Viewers",
    "Movies":"Movies"
}
  
df = df.set_index('ID')
df = df.groupby(groupby_dict, axis = 1).sum()
print(df)

# + [markdown] hidden=true
# **Explanation**
#
# Explanation:
#
# * Here, notice that even though ‘Movies’ isn’t being merged into another column it still has to be present in the groupby_dict, else it won’t be in the final dataframe.
# * To calculate the Total_Viewers we have used the .sum() function which sums up all the values of the respective rows.
#
#

# + [markdown] heading_collapsed=true
# # [How to combine Groupby and Multiple Aggregate Functions in Pandas?](https://www.geeksforgeeks.org/how-to-combine-groupby-and-multiple-aggregate-functions-in-pandas/?ref=lbp)

# + [markdown] hidden=true
# Pandas is a Python package that offers various data structures and operations for manipulating numerical data and time series. It is mainly popular for importing and analyzing data much easier. It is an open-source library that is built on top of NumPy library.
#
# **Groupby()**
#
# Pandas [`dataframe.groupby()`](#section1) function is used to split the data in dataframe into groups based on a given condition.
#
# **Example 1:**

# + hidden=true
# import library
import pandas as pd
  
# import csv file
df = pd.read_csv("https://bit.ly/drinksbycountry")
  
df.head()

# + [markdown] hidden=true
#
# **Example 2:**

# + hidden=true
# Find the average of each continent
# by grouping the data  
# based on the "continent".
df.groupby(["continent"]).mean()

# + [markdown] hidden=true
# **`Aggregate()`**
#
# Pandas `dataframe.agg()` function is used to do one or more operations on data based on specified axis
#
# **Example:**

# + hidden=true
# here sum, minimum and maximum of column 
# beer_servings is calculatad
df.beer_servings.agg(["sum", "min", "max"])

# + [markdown] hidden=true
# **Using These two functions together:**
#
# We can find multiple aggregation functions of a particular column grouped by another column
#
# **Example:**

# + hidden=true
# find an aggregation of column "beer_servings"
# by grouping the "continent" column.
df.groupby(df["continent"]).beer_servings.agg(["min",
                                               "max",
                                               "sum",
                                               "count",
                                               "mean"])

# + [markdown] heading_collapsed=true
# # [Pandas – Groupby multiple values and plotting results](https://www.geeksforgeeks.org/pandas-groupby-multiple-values-and-plotting-results/?ref=lbp)

# + [markdown] hidden=true
# In this article, we will learn how to groupby multiple values and plotting the results in one go. Here, we take “excercise.csv” file of a dataset from [seaborn](https://www.geeksforgeeks.org/introduction-to-seaborn-python/) library then formed different groupby data and visualize the result. 
#
# For this procedure, the steps required are given below:
#
# * Import libraries for data and its visualization.
# * Create and import the data with multiple columns.
# * Form a grouby object by grouping multiple values.
# * Visualize the grouped data.
#
# Below is the implementation with some examples : 
#
# **Example 1 :**
#
# In this example, we take the “excercise.csv” file of a dataset from the seaborn library then formed groupby data by grouping two columns “pulse” and “diet” together on the basis of a column “time” and at last visualize the result.

# + hidden=true
# importing packages
import seaborn
import matplotlib.pyplot as plt
  
# load dataset and view
data = seaborn.load_dataset('exercise')
print(data)
  
# multiple groupby (pulse and diet both)
df = data.groupby(['pulse', 'diet']).count()['time']
print(df)
  
# plot the result
df.plot()
plt.xticks(rotation=45)
plt.show()

# + [markdown] hidden=true
# **Example 2:**
#
# This example is the modification of the above example for better visualization.

# + hidden=true
# importing packages
import seaborn
import matplotlib.pyplot as plt
  
# load dataset
data = seaborn.load_dataset('exercise')
  
# multiple groupby (pulse and diet both)
df = data.groupby(['pulse', 'diet']).count()['time']

print(df)

# plot the result
df.unstack().plot()
plt.xticks(rotation=45)
plt.show()

# + [markdown] hidden=true
# **Example 3:**
#
# In this example, we take “excercise.csv” file of a dataset from seaborn library then formed groupby data by grouping three columns “pulse”, “diet” , and “time” together on the basis of a column “kind” and at last visualize the result.

# + hidden=true
# importing packages
import seaborn
import matplotlib.pyplot as plt

# load dataset and view
data = seaborn.load_dataset('exercise')
print(data)
  
# multiple groupby (pulse, diet and time)
df = data.groupby(['pulse', 'diet', 'time']).count()['kind']
print(df)
  
# plot the result
df.plot()
plt.xticks(rotation=30)
plt.show()

# + [markdown] hidden=true
#
# **Example 4:**
#
# This example is the modification of the above example for better visualization.

# + hidden=true
# importing packages
import seaborn
import matplotlib.pyplot as plt

# load dataset
data = seaborn.load_dataset('exercise')
  
# multiple groupby (pulse, diet, and time)
df = data.groupby(['pulse', 'diet', 'time']).count()['kind']

print(df)

# plot the result
df.unstack().plot()
plt.xticks(rotation=30)
plt.show()

# + [markdown] heading_collapsed=true
# # [Pandas – GroupBy One Column and Get Mean, Min, and Max values](https://www.geeksforgeeks.org/pandas-groupby-one-column-and-get-mean-min-and-max-values/?ref=lbp)

# + [markdown] hidden=true
# We can use Groupby function to split dataframe into groups and apply different operations on it. One of them is Aggregation. Aggregation i.e. computing statistical parameters for each group created example – mean, min, max, or sums.
#
# Let’s have a look at how we can group a dataframe by one column and get their mean, min, and max values.
#
# **Example 1 :**

# + hidden=true
import pandas as pd
  
  
# creating a dataframe
df = pd.DataFrame([('Bike', 'Kawasaki', 186),
                   ('Bike', 'Ducati Panigale', 202),
                   ('Car', 'Bugatti Chiron', 304), 
                   ('Car', 'Jaguar XJ220', 210),
                   ('Bike', 'Lightning LS-218', 218), 
                   ('Car', 'Hennessey Venom GT', 270),
                   ('Bike', 'BMW S1000RR', 188)],
                  columns =('Type', 'Name', 'top_speed(mph)'))
  
df

# + [markdown] hidden=true
# Finding `mean`, `min` and `max` values.

# + hidden=true
# using groupby function with aggregation
# to get mean, min and max values
result = df.groupby('Type').agg({'top_speed(mph)': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Top Speed grouped by Vehicle Type")
print(result)

# + [markdown] hidden=true
# **Example 2 :**

# + hidden=true
import pandas as pd
  
  
# creating a dataframe
sales_data = pd.DataFrame({
'customer_id':[3005, 3001, 3002, 3009, 3005, 3007,
               3002, 3004, 3009, 3008, 3003, 3002],
      
'salesman_id': [102, 105, 101, 103, 102, 101, 101,
                106, 103, 102, 107, 101],
  
'purchase_amt':[1500, 2700, 1525, 1100, 948, 2400,
                5700, 2000, 1280, 2500, 750, 5050]})
  
sales_data

# + [markdown] hidden=true
# Finding `mean`, `min` and `max` values.

# + hidden=true
# using groupby function with aggregation 
# to get mean, min and max values
result = sales_data.groupby('salesman_id').agg({'purchase_amt': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Purchase Amount grouped by Salesman id")
print(result)

# + [markdown] hidden=true
# **Example 3 :**

# + hidden=true
import pandas as pd
  
  
# creating a dataframe
df = pd.DataFrame({"Team": ["Radisson", "Radisson", "Gladiators",
                            "Blues", "Gladiators", "Blues", 
                            "Gladiators", "Gladiators", "Blues", 
                            "Blues", "Radisson", "Radisson"],
                     
        "Position": ["Player", "Extras", "Player", "Extras",
                     "Extras", "Player", "Player", "Player",
                     "Extras", "Player", "Player", "Extras"],
                     
        "Age": [22, 24, 21, 29, 32, 20, 21, 23, 30, 26, 20, 31]})
df

# + [markdown] hidden=true
# Finding `mean`, `min` and `max` values.

# + hidden=true
# using groupby function with aggregation 
# to get mean, min and max values
result = df.groupby('Team').agg({'Age': ['mean', 'min', 'max']})
  
print("Mean, min, and max values of Age grouped by Team")
print(result)

# + [markdown] heading_collapsed=true
# # [Select row with maximum and minimum value in Pandas dataframe](https://www.geeksforgeeks.org/select-row-with-maximum-and-minimum-value-in-pandas-dataframe/?ref=lbp)

# + [markdown] hidden=true
# Let’s see how can we select row with maximum and minimum value in Pandas dataframe with help of different examples.
#
# Consider this dataset.

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
print(df.head(10))

# + [markdown] hidden=true
# **Using `max` on Dataframe –**
#
# **Code #1:** Shows max on Driver, Points, Age columns.

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# the result shows max on
# Driver, Points, Age columns.
print(df.max())

# + [markdown] hidden=true
# **Code #2:** Who scored max points

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# Who scored more points ?
print(df[df.Points == df.Points.max()])

# + [markdown] hidden=true
# **Code #3:**  What is the maximum age

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# what is the maximum age ?
print(df.Age.max())

# + [markdown] hidden=true
# **Code #4:**  Which row has maximum age in the dataframe | who is the oldest driver ?
#

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# Which row has maximum age |
# who is the oldest driver ?
print(df[df.Age == df.Age.max()])

# + [markdown] hidden=true
# **Using max on Dataframe –**
#
# **Code #1:** Shows min on Driver, Points, Age columns.

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# the result shows min on 
# Driver, Points, Age columns.
print(df.min())

# + [markdown] hidden=true
# **Code #2:** Who scored less points

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# Who scored less points ?
print(df[df.Points == df.Points.min()])

# + [markdown] hidden=true
# **Code #3:** Which row has minimum age in the dataframe | who is the youngest driver

# + hidden=true
# importing pandas and numpy
import pandas as pd
import numpy as np
  
# data of 2018 drivers world championship
dict1 ={'Driver':['Hamilton', 'Vettel', 'Raikkonen',
                  'Verstappen', 'Bottas', 'Ricciardo',
                  'Hulkenberg', 'Perez', 'Magnussen', 
                  'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                  'Grosjean', 'Gasly', 'Vandoorne',
                  'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
                    
        'Points':[408, 320, 251, 249, 247, 170, 69, 62, 56,
                   53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
                     
        'Age':[33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                      22, 21, 32, 22, 26, 28, 20, 29, 23]}
                        
# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
  
# Which row has maximum age | 
# who is the youngest driver ?
print(df[df.Age == df.Age.min()])

# + [markdown] heading_collapsed=true
# # [Find maximum values & position in columns and rows of a Dataframe in Pandas](https://www.geeksforgeeks.org/find-maximum-values-position-in-columns-and-rows-of-a-dataframe-in-pandas/)

# + [markdown] hidden=true
# In this article, we are going to discuss how to find maximum value and its index position in columns and rows of a Dataframe.
#
# **DataFrame.max()**
#
# Pandas `dataframe.max()` method finds the maximum of the values in the object and returns it. If the input is a series, the method will return a scalar which will be the maximum of the values in the series. If the input is a dataframe, then the method will return a series with maximum of values over the specified axis in the dataframe. The index axis is the default axis taken by this method.
#
# | **Syntax:** | `DataFrame.max(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)`  |
# | --- | --- |
# | **Parameters :** | |
# | **axis :** | { index (0), columns (1) }  |
# | **skipna :** | Exclude NA/null values when computing the result  |
# | **level :** | If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series  |
# | **numeric_only :** | Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series. |
# | **Returns :** | max : Series or DataFrame (if level specified) |
#
#
# Let’s take an example of how to use this function. Let’s suppose we have a Dataframe 

# + hidden=true
import numpy as np
import pandas as pd

# List of Tuples
matrix = [(10, 56, 17),
          (np.NaN, 23, 11),
          (49, 36, 55),
          (75, np.NaN, 34),
          (89, 21, 44)
          ]

# Create a DataFrame
abc = pd.DataFrame(matrix, index = list('abcde'), columns = list('xyz'))
 
# output
abc

# + [markdown] heading_collapsed=true hidden=true
# ## How to find Maximum values of every column?

# + [markdown] hidden=true
# To find the maximum value of each column, call max() method on the Dataframe object without taking any argument. 

# + hidden=true
# find the maximum of each column
maxValues = abc.max()
 
print(maxValues)

# + [markdown] hidden=true
# We can see that it returned a series of maximum values where the index is column name and values are the maxima from each column.

# + [markdown] heading_collapsed=true hidden=true
# ## How to find maximum values of every row? 

# + [markdown] hidden=true
# To find the maximum value of each row, call max() method on the Dataframe object with an argument axis = 1.  

# + hidden=true
# find the maximum values of each row
maxValues = abc.max(axis = 1)
print(maxValues)

# + [markdown] hidden=true
#
# We can see that it returned a series of maximum values where the index is row name and values are the maxima from each row. We can see that in the above examples NaN values are skipped while finding the maximum values in any axis. We can include NaN values as well if we want.
#
#

# + [markdown] heading_collapsed=true hidden=true
# ##  How to find maximum values of every column without skipping NaN?

# + hidden=true
# find maximum value of each
# column without skipping NaN
maxValues = abc.max(skipna = False)
 
print(maxValues)

# + [markdown] hidden=true
# By putting skipna=False we can include NaN values also. If any NaN value exists it will be considered as the maximum value.

# + [markdown] heading_collapsed=true hidden=true
# ## How to find maximum values of a single column or selected columns?

# + [markdown] hidden=true
# To get the maximum value of a single column see the following example 

# + hidden=true
# find maximum value of a
# single column 'x'
maxClm = abc['x'].max()
 
print("Maximum value in column 'x': " )
print(maxClm)

# + [markdown] hidden=true
# We have another way to find maximum value of a column : 

# + hidden=true
# find maximum value of a
# single column 'x'
maxClm = abc.max()['x']
maxClm

# + [markdown] hidden=true
#
# The result will be same as above. 

# + [markdown] hidden=true
# A list of columns can also be passed instead of a single column to find the maximum values of specified columns 

# + hidden=true
maxValues = abc[['x', 'z']].max()
 
print("Maximum value in column 'x' & 'z': ")
print(maxValues)

# + [markdown] heading_collapsed=true hidden=true
# ## How to get position of maximum values of every column?

# + [markdown] hidden=true
# **DataFrame.idxmax()**: Pandas **dataframe.idxmax()** method returns index of first occurrence of maximum over requested axis. While finding the index of the maximum value across any index, all NA/null values are excluded. 
#
# | Syntax | DataFrame.idxmax(axis=0, skipna=True) |
# | --- | --- |
# | **Parameters :** |  |
# | **axis :** | **0** or `‘index’` for **row-wise**, **1** or `‘columns’` for **column-wise**  |
# | **skipna :** | Exclude NA/null values. If an entire row/column is NA, the result will be NA |
# | **Returns :** | idxmax : Series |
#  
#
# Let’s take some examples to understand how to use it :

# + [markdown] heading_collapsed=true hidden=true
# ## How to get row index label of Maximum value in every column 

# + hidden=true
# find the index position of maximum
# values in every column
maxValueIndex = abc.idxmax()
 
print("Maximum values of columns are at row index position :")
print(maxValueIndex)

# + [markdown] hidden=true
# It returns a series containing the column names as index and row as index labels where the maximum value exists in that column.

# + [markdown] heading_collapsed=true hidden=true
# ## How to find Column names of Maximum value in every row?

# + hidden=true
# find the column name of maximum
# values in every row
maxValueIndex = abc.idxmax(axis = 1)
 
print("Max values of row are at following columns :")
print(maxValueIndex)

# + [markdown] hidden=true
# It returns a series containing the rows index labels as index and column names as values where the maximum value exists in that row.

# + [markdown] heading_collapsed=true
# # [Python | Pandas dataframe.max()](https://www.geeksforgeeks.org/python-pandas-dataframe-max/?ref=lbp)

# + [markdown] hidden=true
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric python packages. _**Pandas**_ is one of those packages and makes importing and analyzing data much easier.
#
# Pandas **dataframe.max()** function returns the maximum of the values in the given object. If the input is a series, the method will return a scalar which will be the maximum of the values in the series. If the input is a dataframe, then the method will return a series with maximum of values over the specified axis in the dataframe. By default the axis is the index axis.

# + [markdown] hidden=true
#
# | **Syntax:** | `DataFrame.max(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)`  |
# | --- | --- |
# | **Parameters :** | |
# | **axis :** | { index (0), columns (1) }  |
# | **skipna :** | Exclude NA/null values when computing the result  |
# | **level :** | If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series  |
# | **numeric_only :** | Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data. Not implemented for Series. |
# | **Returns :** | max : Series or DataFrame (if level specified) |
#

# + [markdown] hidden=true
# **Example #1:** Use `max()` function to find the maximum value over the index axis.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, 44, 1],
                   "B":[5, 2, 54, 3, 2],
                   "C":[20, 16, 7, 3, 8], 
                   "D":[14, 3, 17, 2, 6]})
  
# Print the dataframe
df

# + [markdown] hidden=true
# Let’s use the `dataframe.max()` function to find the maximum value over the index axis

# + hidden=true
# Even if we do not specify axis = 0, 
# the method will return the max over
# the index axis by default
df.max(axis = 0)

# + [markdown] hidden=true
# **Example #2:** Use `max()` function on a dataframe which has Na values. Also find the maximum over the column axis.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, None, 1], 
                   "B":[7, 2, 54, 3, None],
                   "C":[20, 16, 11, 3, 8],
                   "D":[14, 3, None, 2, 6]})
  
# skip the Na values while finding the maximum
df.max(axis = 1, skipna = True)

# + [markdown] heading_collapsed=true
# # [Python | Pandas dataframe.idxmax()](https://www.geeksforgeeks.org/python-pandas-dataframe-idxmax/?ref=lbp)

# + [markdown] hidden=true
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric python packages. _**Pandas**_ is one of those packages and makes importing and analyzing data much easier.
#
# Pandas **dataframe.idxmax()** function returns index of first occurrence of maximum over requested axis. While finding the index of the maximum value across any index, all NA/null values are excluded.

# + [markdown] hidden=true
#
# | **Syntax:** | `DataFrame.idmax(axis=0, skipna=True)`  |
# | --- | --- |
# | **Parameters :** | |
# | **axis :** | 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise  |
# | **skipna :** | Exclude NA/null values. If an entire row/column is NA, the result will be NA |
# | **Returns :** | idxmax : Series |
#

# + [markdown] hidden=true
# **Example #1:** Use idxmax() function to function to find the index of the maximum value along the index axis.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[4, 5, 2, 6], 
                   "B":[11, 2, 5, 8],
                   "C":[1, 8, 66, 4]})
  
# Print the dataframe
df

# + [markdown] hidden=true
# Now apply the `idxmax()` function along the index axis.

# + hidden=true
# applying idxmax() function.
df.idxmax(axis = 0)

# + [markdown] hidden=true
# If we look at the values in the dataframe, we can verify the result returned by the function. The function returned a pandas series object containing the index of maximum value in each column.
#  
#
# **Example #2:** Use `idxmax()` function to find the index of the maximum value along the column axis. The dataframe contains NA values.

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.DataFrame({"A":[4, 5, 2, None],
                   "B":[11, 2, None, 8], 
                   "C":[1, 8, 66, 4]})
  
# Skipna = True will skip all the Na values
# find maximum along column axis
df.idxmax(axis = 1, skipna = True)

# + [markdown] hidden=true
# The output is a pandas series containing the column label for each row which has the maximum value.

# + [markdown] heading_collapsed=true
# # [Get the index of maximum value in DataFrame column](https://www.geeksforgeeks.org/get-the-index-of-maximum-value-in-dataframe-column/?ref=lbp)

# + [markdown] hidden=true
# [Pandas DataFrame](#Python-|-Pandas-DataFrame) is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). 
#
# Let’s see how can we get the index of maximum value in DataFrame column.
# Observe this dataset first. We’ll use ‘Weight’ and ‘Salary’ columns of this data in order to get the index of maximum values from a particular column in Pandas DataFrame.

# + hidden=true
# importing pandas module
import pandas as pd
   
# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
 
df.head(10)

# + [markdown] hidden=true
# **Code #1:** Check the index at which maximum weight value is present. 

# + hidden=true
# importing pandas module
import pandas as pd
   
# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
 
# Returns index of maximum weight
df[['Weight']].idxmax()

# + [markdown] hidden=true
# We can verify whether the maximum value is present in index or not. 

# + hidden=true
# importing pandas module
import pandas as pd
    
# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
# from index 400 to 409
df.iloc[400:410]

# + [markdown] hidden=true
# **Code #2:** Let’s insert a new row at index 0, having maximum salary and then verify. 

# + hidden=true
# importing pandas module
import pandas as pd
    
# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':999999999}
                         , index=[0])
  
df = pd.concat([new_row, df]).reset_index(drop=True)
df.head(5)

# + [markdown] hidden=true
# Now, let’s check if the maximum salary is present at index 0 or not. 

# + hidden=true
# Returns index of minimum salary
df[['Salary']].idxmax()

# + [markdown] heading_collapsed=true
# # [How to get rows/index names in Pandas dataframe](https://www.geeksforgeeks.org/how-to-get-rows-index-names-in-pandas-dataframe/?ref=lbp)

# + [markdown] hidden=true
# While analyzing the real datasets which are often very huge in size, we might need to get the rows or index names in order to perform some certain operations.
#
# Let’s discuss how to get row names in [Pandas dataframe](#Python-|-Pandas-DataFrame).
#
# First, let’s create a simple dataframe with [nba.csv](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv).

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
    
# calling head() method  
# storing in new variable 
data_top = data.head(10) 
    
# display 
data_top 

# + [markdown] hidden=true
# Now let’s try to get the row name from above dataset.
#
# **Method #1:** Simply iterate over indices

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
    
# calling head() method  
# storing in new variable 
data_top = data.head(10) 
    
# iterating the columns
for row in data_top.index:
    print(row, end = " ")

# + [markdown] hidden=true
# **Method #2:** Using rows with dataframe object

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
  
# calling head() method  
# storing in new variable 
data_top = data.head(10) 
    
# list(data_top) or
list(data_top.index)

# + [markdown] hidden=true
#
# **Method #3:** `index.values` method returns an array of index.

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
  
# calling head() method  
# storing in new variable 
data_top = data.head(10) 
    
list(data_top.index.values)

# + [markdown] hidden=true
# **Method #4:** Using `tolist()` method with values with given the list of index.

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
  
# calling head() method  
# storing in new variable 
data_top = data.head(10) 
    
list(data_top.index.values.tolist())

# + [markdown] hidden=true
# **Method #5:** Count number of rows in dataframe
#
# Since we have loaded only 10 top rows of dataframe using head() method, let’s verify total number of rows first.

# + hidden=true
# iterate the indices and print each one
for row in data.index:
    print(row, end= " ")

# + [markdown] hidden=true
# Now, let’s print the total count of index.

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
  
row_count = 0
  
# iterating over indices
for col in data.index:
    row_count += 1
  
# print the row count
print(row_count)

# + [markdown] heading_collapsed=true
# # [Decimal Functions in Python | Set 2 (logical_and(), normalize(), quantize(), rotate() … )](https://www.geeksforgeeks.org/decimal-functions-in-python-set-2-logical_and-normalize-quantize-rotate/?ref=lbp)

# + [markdown] heading_collapsed=true hidden=true
# ## Logical Functions <a class="tocSkip">

# + [markdown] hidden=true
# 1. **logical_and()** :- This function computes digit-wise **logical “and”** operation of the number. Digits can only have the values 0 or 1.
# 1. **logical_or()** :- This function computes digit-wise **logical “or”** operation of the number. Digits can only have the values 0 or 1.
# 1. **logical_xor()** :- This function computes digit-wise **logical “xor”** operation of the number. Digits can only have the values 0 or 1.
# 1. **logical_invert()** :- This function computes digit-wise **logical “invert”** operation of the number. Digits can only have the values 0 or 1.

# + hidden=true
# Python code to demonstrate the working of
# logical_and(), logical_or(), logical_xor()
# and logical_invert()
 
# importing "decimal" module to use decimal functions
import decimal
 
# Initializing decimal number
a = decimal.Decimal(1000)
 
# Initializing decimal number
b = decimal.Decimal(1110)
 
# printing logical_and of two numbers
print ("The logical_and() of two numbers is : ",end="")
print (a.logical_and(b))
 
# printing logical_or of two numbers
print ("The logical_or() of two numbers is : ",end="")
print (a.logical_or(b))
 
# printing exclusive or of two numbers
print ("The exclusive or of two numbers is : ",end="")
print (a.logical_xor(b))
 
# printing logical inversion of number
print ("The logical inversion of number is : ",end="")
print (a.logical_invert())

# + [markdown] heading_collapsed=true hidden=true
# ## Greatest Lower and Least Upper Bound <a class="tocSkip">

# + [markdown] hidden=true
# 5. **next_plus()** :- This function returns the **smallest number** that can be represented, **larger than the given number**.
#
# 6. **next_minus()** :- This function returns the **largest number** that can be represented, **smaller than the given number**. 

# + hidden=true
# Python code to demonstrate the working of
# next_plus() and next_minus()
 
# importing "decimal" module to use decimal functions
import decimal
 
# Initializing decimal number
a = decimal.Decimal(101.34)
 
# printing the actual decimal number
print ("The original number is : ",end="")
print (a)
 
# printing number after using next_plus()
print ("The smallest number larger than current number : ",end="")
print (a.next_plus())
 
# printing number after using next_minus()
print ("The largest number smaller than current number : ",end="")
print (a.next_minus())

# + [markdown] heading_collapsed=true hidden=true
# ## Rounding <a class="tocSkip">

# + [markdown] hidden=true
# 7. **next_toward()** :- This function returns the **number nearest to the 1st argument in the direction of the second argument.** In case Both the numbers are equal, returns the **2nd number with the sign of first number**.
#
# 8. **normalize()** :- This function prints the number after **erasing all the rightmost trailing zeroes** in the number. 

# + hidden=true
# Python code to demonstrate the working of
# next_toward() and normalize()
 
# importing "decimal" module to use decimal functions
import decimal
 
# Initializing decimal number
a = decimal.Decimal(101.34)
 
# Initializing decimal number
b = decimal.Decimal(-101.34)
 
# Initializing decimal number
c = decimal.Decimal(-58.68)
 
# Initializing decimal number
d = decimal.Decimal(14.010000000)
 
# printing the number using next_toward()
print ("The number closest to 1st number in direction of second number : ")
print (a.next_toward(c))
 
# printing the number using next_toward()
# when equal
print ("The second number with sign of first number is : ",end="")
print (b.next_toward(a))
 
# printing number after erasing rightmost trailing zeroes
print ("Number after erasing rightmost trailing zeroes : ",end="")
print (d.normalize())

# + [markdown] heading_collapsed=true hidden=true
# ## Digits <a class="tocSkip">

# + [markdown] hidden=true
# 9. **quantize()** :- This function returns the 1st argument with the number of **digits in decimal part(exponent) shortened** by the **number of digits** in **decimal part(exponent) of 2nd argument**.
#
# 10. **same_quantum()** :- This function **returns 0 if both the numbers have different exponent and 1 if both numbers have same exponent**. 

# + hidden=true
# Python code to demonstrate the working of
# quantize() and same_quantum()
  
# importing "decimal" module to use decimal functions
import decimal
  
# Initializing decimal number
a = decimal.Decimal(20.76548)
  
# Initializing decimal number
b = decimal.Decimal(12.25)
 
# Initializing decimal number
c = decimal.Decimal(6.25)
 
# printing quantized first number
print ("The quantized first number is : ",end="")
print (a.quantize(b))
  
# checking if both number have same exponent
if (b.same_quantum(c)):
       print ("Both the numbers have same exponent")
else : print ("Both numbers have different exponent") 

# + [markdown] hidden=true
# 11. **rotate()** :- This function **rotates** the first argument by the **amount mentioned in the second argument**. If the sign of second argument is **positive, rotation is towards left, else the rotation is towards right**. The sign of first argument is unchanged.
#
# 12. **shift()** :- This function **shifts** the first argument by the **amount mentioned in the second argument**. If the sign of second argument is **positive, shifting is towards left, else the shifting is towards right**. The sign of first argument is unchanged. Digit shifted are **replaced by 0**.

# + hidden=true
# Python code to demonstrate the working of
# rotate() and shift()
  
# importing "decimal" module to use decimal functions
import decimal
  
# Initializing decimal number
a = decimal.Decimal(2343509394029424234334563465)
 
# using rotate() to rotate the first argument
# rotates to right by 2 positions
print ("The rotated value is : ",end="")
print (a.rotate(-2))
  
# using shift() to shift the first argument
# rotates to left by 2 positions
print ("The shifted value is : ",end="")
print (a.shift(2))

# + [markdown] heading_collapsed=true hidden=true
# ## Divisibility <a class="tocSkip">

# + [markdown] hidden=true
# 13. **remainder_near()** :- Returns the value “**1st – (n*2nd)**” where **n is the integer value nearest to the result of 1st/2nd**. If 2 integers have **exactly similar proximity, even one is chosen**.
#
# 14. **scaleb()** :- This function **shifts the exponent** of 1st number by the **value of second argument**. 

# + hidden=true
# Python code to demonstrate the working of
# remainder_near() and scaleb()
  
# importing "decimal" module to use decimal functions
import decimal
  
# Initializing decimal number
a = decimal.Decimal(23.765)
 
# Initializing decimal number
b = decimal.Decimal(12)
 
# Initializing decimal number
c = decimal.Decimal(8)
 
# using remainder_near to compute value
print ("The computed value using remainder_near() is : ",end="")
print (b.remainder_near(c))
  
# using scaleb() to shift exponont
print ("The value after shifting exponent : ",end="")
print (a.scaleb(2))

# + [markdown] hidden=true
#
# This article is contributed by [Manjeet Singh](https://auth.geeksforgeeks.org/profile.php?user=manjeet_04&list=practice). If you like GeeksforGeeks and would like to contribute, you can also write an article using [write.geeksforgeeks.org](http://www.write.geeksforgeeks.org/) or mail your article to [review-team@geeksforgeeks.org](mailto:review-team@geeksforgeeks.org). See your article appearing on the GeeksforGeeks main page and help other Geeks.
#
# Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

# + [markdown] heading_collapsed=true
# # [NetworkX : Python software package for study of complex networks](https://www.geeksforgeeks.org/networkx-python-software-package-study-complex-networks/?ref=lbp)

# + [markdown] hidden=true
# [NetworkX](https://networkx.org/documentation/stable/reference/introduction.html#)
# is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks. It is used to study large complex networks represented in form of graphs with nodes and edges. Using networkx we can load and store complex networks. We can generate many types of random and classic networks, analyze network structure, build network models, design new network algorithms and draw networks. 

# + [markdown] heading_collapsed=true hidden=true
# ## Installation of the package

# + hidden=true
# # !pip install networkx
# # !pip show networkx

# + [markdown] heading_collapsed=true hidden=true
# ## Creating Nodes

# + [markdown] hidden=true
# Add one node at a time: 

# + hidden=true
import networkx as nx
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
nx.shortest_path(G, 'A', 'D', weight='weight')

# + hidden=true
G = nx.Graph()

G.add_node(1)

# + [markdown] hidden=true
# Add a list of nodes: 

# + hidden=true
G.add_nodes_from([2,3])
G

# + [markdown] hidden=true
# Let us create nodes in the graph G. After adding nodes 1, 2, 3, 4, 7, 9 

# + [markdown] heading_collapsed=true hidden=true
# ## Creating Edges

# + [markdown] hidden=true
# Adding one edge at a time: 

# + hidden=true
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(2,4)
G.add_edge(4,1)
G.add_edge(9,1)

# + [markdown] hidden=true
# Adding a list of edges: 

# + hidden=true
G.add_edges_from([(1,2),(1,3)])

# + [markdown] hidden=true
# After adding edges (1,2), (3,1), (2,4), (4,1), (9,1), (1,7), (2,9) 

# + [markdown] heading_collapsed=true hidden=true
# ## Removing Nodes and Edges

# + [markdown] hidden=true
# One can demolish the graph using any of these functions: 
# ```
# Graph.remove_node()
# Graph.remove_nodes_from()
# Graph.remove_edge()
# ```
# and
# ```
# Graph.remove_edges_from()
# ```

# + [markdown] hidden=true
# After removing node 3 

# + [markdown] hidden=true
# After removing edge (1,2) 

# + hidden=true
# Python program to create an undirected
# graph and add nodes and edges to a graph
 
# To import package
import networkx
  
# To create an empty undirected graph
G = networkx.Graph()
  
# To add a node
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(7)
G.add_node(9)
  
# To add an edge
# Note graph is undirected
# Hence order of nodes in edge doesn't matter
G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(2,4)
G.add_edge(4,1)
G.add_edge(9,1)
G.add_edge(1,7)
G.add_edge(2,9)
  
# To get all the nodes of a graph
node_list = G.nodes()
print("#1: G.nodes()")
print(node_list)
  
# To get all the edges of a graph
edge_list = G.edges()
print("#2: G.edges()")
print(edge_list)
  
# To remove a node of a graph
G.remove_node(3)
node_list = G.nodes()
print("#3: G.nodes()")
print(node_list)
  
# To remove an edge of a graph
G.remove_edge(1,2)
edge_list = G.edges()
print("#4: G.edges()")
print(edge_list)
  
# To find number of nodes
n = G.number_of_nodes()
print("#5: G.number_of_nodes()")
print(n)
  
# To find number of edges
m = G.number_of_edges()
print("#6: G.number_of_edges()")
print(m)
  
# To find degree of a node
# d will store degree of node 2
d = G.degree(2)
print("#7: G.degree(2)")
print(d)
 
# To find all the neighbor of a node
neighbor_list = G.neighbors(2)
print("#8: G.neighbors(2)")
print(neighbor_list)
 
#To delete all the nodes and edges
G.clear()

# + [markdown] hidden=true
# In the next post, we’ll be discussing how to create weighted graphs, directed graphs, multi graphs. How to draw graphs. In later posts we’ll see how to use inbuilt functions like Depth first search aka dfs, breadth first search aka BFS, dijkstra’s shortest path algorithm. 
#
# Reference: [Networxx at Github](https://networkx.github.io/documentation/networkx-1.10/overview.html)

# + [markdown] heading_collapsed=true
# # [Directed Graphs, Multigraphs and Visualization in Networkx](https://www.geeksforgeeks.org/directed-graphs-multigraphs-and-visualization-in-networkx/?ref=lbp)

# + [markdown] hidden=true
# In the [previous article](#section14), we have leaned about the basics of Networkx module and how to create an undirected graph. Note that Networkx module easily outputs the various Graph parameters easily, as shown below with an example.

# + hidden=true
import networkx as nx

# To create an empty undirected graph
G = nx.Graph()

# To add a node
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)

# To add all edges with one command
edges = [(1, 2), (1, 6), (2, 3), (2, 4), (2, 6), 
         (3, 4), (3, 5), (4, 8), (4, 9), (6, 7)]
  
G.add_edges_from(edges)
nx.draw_networkx(G, with_labels = True)
  
print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges(data = True)))
print("Degree for all nodes: ", dict(G.degree()))
  
print("Total number of self-loops: ", int(G.number_of_selfloops()))
print("List of all nodes with self-loops: ",
             list(G.nodes_with_selfloops()))
  
print("List of all nodes we can go to in a single step from node 2: ",
                                                 list(G.neighbors(2)))

# + [markdown] hidden=true
# [networkx shows random_state_index is incorrect](https://stackoverflow.com/questions/66920533/networkx-shows-random-state-index-is-incorrect)
#
# > It looks like the issue MAY be due to a new release of the decorator module. See here: 
# > [Error in random_state decorator with decorator 5.0.0 version #4718](https://github.com/networkx/networkx/issues/4718)
#
# > This worked for me:
# > ```
# > pip install --user decorator==4.3.0 # (ignore waring for availability of newer version)
# > 
# > pip install --user networkx==2.3
# > ```
#
# The problem is resolved if you update the latest decorator 5.0.9 version (June 2021)

# + hidden=true
# !pip install --user decorator==4.3.0

# !pip install --user networkx==2.3

# + [markdown] heading_collapsed=true hidden=true
# ## Creating Weighted undirected Graph –
#
# Add list of all edges along with assorted weights –

# + hidden=true
import networkx as nx
G = nx.Graph()
  
edges = [(1, 2, 19), (1, 6, 15), (2, 3, 6), (2, 4, 10), 
         (2, 6, 22), (3, 4, 51), (3, 5, 14), (4, 8, 20),
         (4, 9, 42), (6, 7, 30)]
  
G.add_weighted_edges_from(edges)
nx.draw_networkx(G, with_labels = True)

# + [markdown] hidden=true
# We can load the edges from an Edge List, which needs to be saved in a `.txt` format (eg. `edge_list.txt`),
# rf. [networkx.readwrite.edgelist.read_edgelist](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.edgelist.read_edgelist.html).
#
# First, export the edges:

# + hidden=true
nx.write_edgelist(G, "test.edgelist")

# + hidden=true
fh = open("test.edgelist", "rb")
Gread = nx.read_edgelist(fh)
fh.close()
nx.draw_networkx(Gread, with_labels = True)

# + hidden=true
Gread = nx.read_edgelist("test.edgelist", nodetype=int)
nx.draw_networkx(Gread, with_labels = True)

# + hidden=true
Gread = nx.read_edgelist("test.edgelist", create_using=nx.DiGraph)
nx.draw_networkx(Gread, with_labels = True)

# + [markdown] heading_collapsed=true hidden=true
# ## Edge list can also be read via a Pandas Dataframe –

# + hidden=true
edge_list="""\
Kolkata Mumbai 2031
Mumbai Pune 155
Mumbai Goa 571
Kolkata Delhi 1492
Kolkata Bhubaneshwar 444
Mumbai Delhi 1424
Delhi Chandigarh 243
Delhi Surat 1208
Kolkata Hyderabad 1495
Hyderabad Chennai 626
Chennai Thiruvananthapuram 773
Thiruvananthapuram Hyderabad 1299
Kolkata Varanasi 679
Delhi Varanasi 821
Mumbai Bangalore 984
Chennai Bangalore 347
Hyderabad Bangalore 575
Kolkata Guwahati 1031
"""
# print(edge_list)
with open('edge_list.txt', 'a') as f:
    f.write(edge_list)

# + [markdown] hidden=true
# Now, we can add the edges via an Edge List, which needs to be saved in a `.txt` format (eg. `edge_list.txt`)

# + hidden=true
import pandas as pd
  
df = pd.read_csv('edge_list.txt', delim_whitespace = True, 
                   header = None, names =['n1', 'n2', 'weight'])
  
G = nx.from_pandas_edgelist(df, 'n1', 'n2', edge_attr ='weight')
  
# The Graph diagram does not show the edge weights. 
# However, we can get the weights by printing all the
# edges along with the weights by the command below
print(list(G.edges(data = True)))

# + [markdown] hidden=true
# We would now explore the different visualization techniques of a Graph.
#
# For this, We’ve created a Dataset of various Indian cities and the distances between them and saved it in a `.txt` file, `edge_list.txt`.

# + [markdown] hidden=true
# Now, we will make a Graph by the following code. We will also add a node attribute to all the cities which will be the population of each city.

# + hidden=true
import networkx as nx
  
G = nx.read_weighted_edgelist('edge_list.txt', delimiter =" ")
  
population = {
        'Kolkata' : 4486679,
        'Delhi' : 11007835,
        'Mumbai' : 12442373,
        'Guwahati' : 957352,
        'Bangalore' : 8436675,
        'Pune' : 3124458,
        'Hyderabad' : 6809970,
        'Chennai' : 4681087,
        'Thiruvananthapuram' : 460468,
        'Bhubaneshwar' : 837737,
        'Varanasi' : 1198491,
        'Surat' : 4467797,
        'Goa' : 40017,
        'Chandigarh' : 961587
        }
  
# We have to set the population attribute for each of the 14 nodes
for i in list(G.nodes()):
    G.nodes[i]['population'] = population[i]
  
nx.draw_networkx(G, with_label = True)
# This line allows us to visualize the Graph

# + [markdown] hidden=true
# But, we can customize the Network to provide more information visually by following these steps:
#
# 1. The size of the node is proportional to the population of the city.
# 1. The intensity of colour of the node is directly proportional to the degree of the node.
# 1. The width of the edge is directly proportional to the weight of the edge, in this case, the distance between the cities.

# + hidden=true
# fixing the size of the figure
plt.figure(figsize =(10, 7))
  
node_color = [G.degree(v) for v in G]
# node colour is a list of degrees of nodes
  
node_size = [0.0005 * nx.get_node_attributes(G, 'population')[v] for v in G]
# size of node is a list of population of cities
  
edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()]
# width of edge is a list of weight of edges
  
nx.draw_networkx(G, node_size = node_size, 
                 node_color = node_color, alpha = 0.7,
                 with_labels = True, width = edge_width,
                 edge_color ='.4', cmap = plt.cm.Blues)
  
plt.axis('off')
plt.tight_layout();

# + [markdown] hidden=true
# We can see in the above code, we have specified the layout type as tight. You can find the different layout techniques and try a few of them as shown in the code below:

# + hidden=true
print("The various layout options are:")
print([x for x in nx.__dir__() if x.endswith('_layout')])
# prints out list of all different layout options
  
node_color = [G.degree(v) for v in G]
node_size = [0.0005 * nx.get_node_attributes(G, 'population')[v] for v in G]
edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()]
  
plt.figure(figsize =(10, 9))
pos = nx.random_layout(G)
print("Random Layout:")
  
# demonstrating random layout
nx.draw_networkx(G, pos, node_size = node_size, 
                 node_color = node_color, alpha = 0.7, 
                 with_labels = True, width = edge_width,
                 edge_color ='.4', cmap = plt.cm.Blues)
  
  
plt.figure(figsize =(10, 9))
pos = nx.circular_layout(G)
print("Circular Layout")
  
# demonstrating circular layout
nx.draw_networkx(G, pos, node_size = node_size, 
                 node_color = node_color, alpha = 0.7, 
                 with_labels = True, width = edge_width, 
                 edge_color ='.4', cmap = plt.cm.Blues)

# + [markdown] hidden=true
# Networkx allows us to create a Path Graph, i.e. a straight line connecting a number of nodes in the following manner:

# + hidden=true
G2 = nx.path_graph(5)
nx.draw_networkx(G2, with_labels = True)

# + [markdown] hidden=true
# We can rename the nodes –

# + hidden=true
G2 = nx.path_graph(5)
  
new = {0:"Germany", 1:"Austria", 2:"France", 3:"Poland", 4:"Italy"}
G2 = nx.relabel_nodes(G2, new)
nx.draw_networkx(G2, with_labels = True)

# + [markdown] heading_collapsed=true hidden=true
# ## Creating Directed Graph –

# + [markdown] hidden=true
# Networkx allows us to work with Directed Graphs. Their creation, adding of nodes, edges etc. are exactly similar to that of an undirected graph as discussed [here](#NetworkX-:-Python-software-package-for-study-of-complex-networks).
#
# The following code shows the basic operations on a Directed graph.

# + hidden=true
import networkx as nx
G = nx.DiGraph()
G.add_edges_from([(1, 1), (1, 7), (2, 1), (2, 2), (2, 3), 
                  (2, 6), (3, 5), (4, 3), (5, 4), (5, 8),
                  (5, 9), (6, 4), (7, 2), (7, 6), (8, 7)])
  
plt.figure(figsize =(9, 9))
nx.draw_networkx(G, with_label = True, node_color ='green')
  
# getting different graph attributes
print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges()))
print("In-degree for all nodes: ", dict(G.in_degree()))
print("Out degree for all nodes: ", dict(G.out_degree))
  
print("Total number of self-loops: ", int(G.number_of_selfloops()))
print("List of all nodes with self-loops: ",
             list(G.nodes_with_selfloops()))
  
print("List of all nodes we can go to in a single step from node 2: ",
                                                list(G.successors(2)))
  
print("List of all nodes from which we can go to node 2 in a single step: ",
                                                    list(G.predecessors(2)))

# + [markdown] hidden=true
# Now, we will show the basic operations for a MultiGraph. Networkx allows us to create both directed and undirected Multigraphs. A Multigraph is a Graph where multiple parallel edges can connect the same nodes.
# For example, let us create a network of 10 people, A, B, C, D, E, F, G, H, I and J. They have four different relations among them namely Friend, Co-worker, Family and Neighbour. A relation between two people isn’t restricted to a single kind.
#
# But the visualization of Multigraph in Networkx is not clear. It fails to show multiple edges separately and these edges overlap.

# + hidden=true
import networkx as nx
import matplotlib.pyplot as plt
  
G = nx.MultiGraph()
relations = [('A', 'B', 'neighbour'), ('A', 'B', 'friend'), ('B', 'C', 'coworker'),
             ('C', 'F', 'coworker'), ('C', 'F', 'friend'), ('F', 'G', 'coworker'),
             ('F', 'G', 'family'), ('C', 'E', 'friend'), ('E', 'D', 'family'),
             ('E', 'I', 'coworker'), ('E', 'I', 'neighbour'), ('I', 'J', 'coworker'),
             ('E', 'J', 'friend'), ('E', 'H', 'coworker')]
  
for i in relations:
    G.add_edge(i[0], i[1], relation = i[2])
      
plt.figure(figsize =(9, 9))
nx.draw_networkx(G, with_label = True)
  
# getting various graph properties
print("Total number of nodes: ", int(G.number_of_nodes()))
print("Total number of edges: ", int(G.number_of_edges()))
print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges(data = True)))
print("Degree for all nodes: ", dict(G.degree()))
print("Total number of self-loops: ", int(G.number_of_selfloops()))
print("List of all nodes with self-loops: ", list(G.nodes_with_selfloops()))
print("List of all nodes we can go to in a single step from node E: ", list(G.neighbors("E")))

# + [markdown] hidden=true
# Similarly, a Multi Directed Graph can be created by using

# + hidden=true
G = nx.MultiDiGraph()

# + [markdown] heading_collapsed=true
# # [Python | Visualize graphs generated in NetworkX using Matplotlib](https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/?ref=lbp)

# + [markdown] hidden=true
# Prerequisites: Generating Graph using Network X, Matplotlib Intro
# In this article, we will be discussing how to plot a graph generated by NetworkX in Python using Matplotlib.
# **NetworkX** is not a graph visualizing package but basic drawing with Matplotlib is included in the software package.
#
# **Step 1 :** Import networkx and matplotlib.pyplot in the project file. 

# + hidden=true
# importing networkx
import networkx as nx
 
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

# + [markdown] hidden=true
# **Step 2 :** Generate a graph using networkx. 
#
# **Step 3 :** Now use draw() function of networkx.drawing to draw the graph. 
#
# **Step 4 :** Use savefig(“filename.png”) function of matplotlib.pyplot to save the drawing of graph in filename.png file.
#
# Below is the Python code:  

# + hidden=true
# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
g = nx.Graph()
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
 
nx.draw(g)
plt.savefig("filename.png")

# + [markdown] hidden=true
# To add numbering in the node add one argument `with_labels=True` in `draw()` function.  

# + hidden=true
# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
g = nx.Graph()
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
 
nx.draw(g, with_labels = True)
plt.savefig("filename.png")

# + [markdown] hidden=true
# Different graph types and plotting can be done using networkx drawing and matplotlib. 

# + [markdown] hidden=true
# **Note\*\* :** Here **keywords** is referred to optional keywords that we can mention use to format the graph plotting. Some of the general graph layouts are :  
#
# 1. **draw_circular(G, keywords)** : This gives circular layout of the graph G.
# 1. **draw_planar(G, keywords)** :] This gives a planar layout of a planar networkx graph G.
# 1. **draw_random(G, keywords)** : This gives a random layout of the graph G.
# 1. **draw_spectral(G, keywords)** : This gives a spectral 2D layout of the graph G.
# 1. **draw_spring(G, keywords)** : This gives a spring layout of the graph G.
# 1. **draw_shell(G, keywords)** : This gives a shell layout of the graph G. 

# + [markdown] hidden=true
# **Example :**

# + hidden=true
# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
g = nx.Graph()
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(4, 8)
g.add_edge(3, 8)
 
# drawing in circular layout
nx.draw_circular(g, with_labels = True)
plt.savefig("filename1.png")
 
# clearing the current plot
plt.clf()
 
# drawing in planar layout
nx.draw_planar(g, with_labels = True)
plt.savefig("filename2.png")
 
# clearing the current plot
plt.clf()
 
# drawing in random layout
nx.draw_random(g, with_labels = True)
plt.savefig("filename3.png")
 
# clearing the current plot
plt.clf()
 
# drawing in spectral layout
nx.draw_spectral(g, with_labels = True)
plt.savefig("filename4.png")
 
# clearing the current plot
plt.clf()
 
# drawing in spring layout
nx.draw_spring(g, with_labels = True)
plt.savefig("filename5.png")
 
# clearing the current plot
plt.clf()
 
# drawing in shell layout
nx.draw_shell(g, with_labels = True)
plt.savefig("filename6.png")
 
# clearing the current plot
plt.clf()

# + [markdown] heading_collapsed=true
# # [Visualize Graphs in Python](https://www.geeksforgeeks.org/visualize-graphs-in-python/?ref=lbp)

# + [markdown] hidden=true
# **Prerequisites:** [Graph Data Structure And Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
#
# A [Graph](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/) is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.
#
# In this tutorial we are going to visualize undirected Graphs in Python with the help of **networkx** library.

# + [markdown] hidden=true
# **Installation:**
#
# To install this module type the below command in the terminal.

# + hidden=true
# pip install networkx

# + [markdown] hidden=true
# Below is the implementation.

# + hidden=true
# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
   
  
# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
  
# Driver code
G = GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()

# + [markdown] heading_collapsed=true
# # [Graph Plotting in Python | Set 1](https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/?ref=lbp)

# + [markdown] hidden=true
# This series will introduce you to graphing in python with [Matplotlib](https://matplotlib.org/), which is arguably the most popular graphing and data visualization library for Python.
#
# **Installation**
#
# The easiest way to install matplotlib is to use pip. Type following command in terminal: 

# + hidden=true
# pip install matplotlib

# + [markdown] hidden=true
# OR, you can download it from here and install it manually. 

# + [markdown] heading_collapsed=true hidden=true
# ## Getting started (Plotting a line)

# + hidden=true
# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# The code seems self-explanatory. Following steps were followed: 
#
# * Define the x-axis and corresponding y-axis values as lists.
# * Plot them on canvas using **.plot()** function.
# * Give a name to x-axis and y-axis using **.xlabel()** and **.ylabel()** functions.
# * Give a title to your plot using **.title()** function.
# * Finally, to view your plot, we use **.show()** function.
#

# + [markdown] heading_collapsed=true hidden=true
# ## Plotting two or more lines on same plot

# + hidden=true
import matplotlib.pyplot as plt
 
# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
 
# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# * Here, we plot two lines on the same graph. We differentiate between them by giving them a name(**label**) which is passed as an argument of the .plot() function.
# * The small rectangular box giving information about the type of line and its color is called a legend. We can add a legend to our plot using **.legend()** function.

# + [markdown] heading_collapsed=true hidden=true
# ## Customization of Plots

# + [markdown] hidden=true
# Here, we discuss some elementary customizations applicable to almost any plot.

# + hidden=true
import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]
 
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# As you can see, we have done several customizations like 
#
# * setting the line-width, line-style, line-color.
# * setting the marker, marker’s face color, marker’s size.
# * overriding the x and y-axis range. If overriding is not done, pyplot module uses the auto-scale feature to set the axis range and scale.

# + [markdown] heading_collapsed=true hidden=true
# ##  Bar Chart

# + hidden=true
import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]
 
# heights of bars
height = [10, 24, 36, 40, 5]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# * Here, we use **plt.bar()** function to plot a bar chart.
# * $x$-coordinates of the left side of bars are passed along with the heights of bars.
# * you can also give some names to x-axis coordinates by defining **tick_labels**

# + [markdown] heading_collapsed=true hidden=true
# ## Histogram

# + hidden=true
import matplotlib.pyplot as plt
 
# frequencies
ages = [2,5,70,40,30,45,50,45,43,40,44,
        60,7,13,57,18,90,77,32,21,20,40]
 
# setting the ranges and no. of intervals
range = (0, 100)
bins = 10 
 
# plotting a histogram
plt.hist(ages, bins, range, color = 'green',
        histtype = 'bar', rwidth = 0.8)
 
# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# * Here, we use **plt.hist()** function to plot a histogram.
# * frequencies are passed as the **ages** list.
# * The range could be set by defining a tuple containing min and max values.
# * The next step is to “**bin**” the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. Here we have defined **bins** = 10. So, there are a total of 100/10 = 10 intervals.

# + [markdown] heading_collapsed=true hidden=true
# ## Scatter plot

# + hidden=true
import matplotlib.pyplot as plt
 
# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]
 
# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green",
            marker= "*", s=30)
 
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# * Here, we use **plt.scatter()** function to plot a scatter plot.
# * As a line, we define x and corresponding y-axis values here as well.
# * **marker** argument is used to set the character to use as a marker. Its size can be defined using the s parameter.

# + [markdown] heading_collapsed=true hidden=true
# ## Pie-chart

# + hidden=true
import matplotlib.pyplot as plt
 
# defining labels
activities = ['eat', 'sleep', 'work', 'play']
 
# portion covered by each label
slices = [3, 7, 8, 6]
 
# color for each label
colors = ['r', 'y', 'g', 'b']
 
# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
 
# plotting legend
plt.legend()
 
# showing the plot
plt.show()

# + [markdown] hidden=true
# * Here, we plot a pie chart by using **plt.pie()** method.
# * First of all, we define the **labels** using a list called **activities**.
# * Then, a portion of each label can be defined using another list called **slices**.
# * Color for each label is defined using a list called **colors**.
# * **shadow = True** will show a shadow beneath each label in pie chart.
# * **startangle** rotates the start of the pie chart by given degrees counterclockwise from the x-axis.
# * **explode** is used to set the fraction of radius with which we offset each wedge.
# * **autopct** is used to format the value of each label. Here, we have set it to show the percentage value only upto 1 decimal place.

# + [markdown] heading_collapsed=true hidden=true
# ## Plotting curves of given equation
#
#

# + hidden=true
# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
 
# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
 
# plotting the points
plt.plot(x, y)
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# Here, we use **NumPy** which is a general-purpose array-processing package in python. 
#  
#
# * To set the x-axis values, we use the **np.arange()** method in which the first two arguments are for range and the third one for step-wise increment. The result is a NumPy array.
# * To get corresponding y-axis values, we simply use the predefined **np.sin()** method on the NumPy array.
# * Finally, we plot the points by passing x and y arrays to the **plt.plot()** function.
#
# So, in this part, we discussed various types of plots we can create in matplotlib. There are more plots that haven’t been covered but the most significant ones are discussed here – 

# + [markdown] heading_collapsed=true
# # [Graph Plotting in Python | Set 2](https://www.geeksforgeeks.org/graph-plotting-python-set-2/?ref=lbp)

# + [markdown] heading_collapsed=true hidden=true
# ## Subplots

# + [markdown] hidden=true
# Subplots are required when we want to show two or more plots in same figure. We can do it in two ways using two slightly different methods.

# + [markdown] heading_collapsed=true hidden=true
# ### Method 1

# + hidden=true
# importing required modules
import matplotlib.pyplot as plt
import numpy as np
 
# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(-10, 10, 0.01)
     
    # setting the y-axis values
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4
             
    return(x, y)
 
# setting a style to use
plt.style.use('fivethirtyeight')
 
# create a figure
fig = plt.figure()
 
# define subplots and their positions in figure
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)
 
# plotting points on each subplot
x, y = create_plot('linear')
plt1.plot(x, y, color ='r')
plt1.set_title('$y_1 = x$')
 
x, y = create_plot('quadratic')
plt2.plot(x, y, color ='b')
plt2.set_title('$y_2 = x^2$')
 
x, y = create_plot('cubic')
plt3.plot(x, y, color ='g')
plt3.set_title('$y_3 = x^3$')
 
x, y = create_plot('quartic')
plt4.plot(x, y, color ='k')
plt4.set_title('$y_4 = x^4$')
 
# adjusting space between subplots
fig.subplots_adjust(hspace=.5,wspace=0.5)
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# Let us go through this program step by step: 
# ```
# plt.style.use('fivethirtyeight')
# ```
# * The styling of plots can be configured by setting different styles available or setting your own. You can learn more about this feature [here](http://matplotlib.org/users/style_sheets.html)
# ```
# fig = plt.figure()
# ```
# * Figure acts as a top level container for all plot elements. So, we define a figure as **fig** which will contain all our subplots.
# ```
# plt1 = fig.add_subplot(221)
# plt2 = fig.add_subplot(222)
# plt3 = fig.add_subplot(223)
# plt4 = fig.add_subplot(224)
# ```
# * Here we use fig.add_subplot method to define subplots and their positions. The function prototype is like this: 
# ```
# add_subplot(nrows, ncols, plot_number)
# ```
# * If a subplot is applied to a figure, the figure will be notionally split into ‘nrows’ * ‘ncols’ sub-axes. The parameter ‘plot_number’ identifies the subplot that the function call has to create. ‘plot_number’ can range from 1 to a maximum of ‘nrows’ * ‘ncols’.<br>
# If the values of the three parameters are less than 10, the function subplot can be called with one int parameter, where the hundreds represent ‘nrows’, the tens represent ‘ncols’ and the units represent ‘plot_number’. This means: Instead of subplot(2, 3, 4) we can write subplot(234).<br>
# This figure will make it clear that how positions are specified: 
#
# <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210722193312/sub11.png">
#
# ```
# x, y = create_plot('linear')
# plt1.plot(x, y, color ='r')
# plt1.set_title('$y_1 = x$')
# ```
#
# * Next, we plot our points on each subplot. First, we generate x and y axis coordinates using create_plot function by specifying the type of curve we want. <br>
# Then, we plot those points on our subplot using .plot method. Title of subplot is set by using set_title method. Using $ at starting and end of the title text will ensure that ‘_'(underscore) is read as a subscript and ‘^’ is read as a superscript.
#
# ```
# fig.subplots_adjust(hspace=.5,wspace=0.5)
# ```
#
# * This is another utility method which creates space between subplots.
#
# ```
# plt.show()
# ```
#
# * In the end, we call plt.show() method which will show the current figure.

# + [markdown] heading_collapsed=true hidden=true
# ### Method 2

# + hidden=true
# importing required modules
import matplotlib.pyplot as plt
import numpy as np
 
# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis values
    x = np.arange(0, 5, 0.01)
     
    # setting y-axis values
    if ptype == 'sin':
        # a sine wave
        y = np.sin(2*np.pi*x)
    elif ptype == 'exp':
        # negative exponential function
        y = np.exp(-x)
    elif ptype == 'hybrid':
        # a damped sine wave
        y = (np.sin(2*np.pi*x))*(np.exp(-x))
             
    return(x, y)
 
# setting a style to use
plt.style.use('ggplot')
 
# defining subplots and their positions
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1)
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1)
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1)
 
# plotting points on each subplot
x, y = create_plot('sin')
plt1.plot(x, y, label = 'sine wave', color ='b')
x, y = create_plot('exp')
plt2.plot(x, y, label = 'negative exponential', color = 'r')
x, y = create_plot('hybrid')
plt3.plot(x, y, label = 'damped sine wave', color = 'g')
 
# show legends of each subplot
plt1.legend()
plt2.legend()
plt3.legend()
 
# function to show plot
plt.show()

# + [markdown] hidden=true
# Let us go through important parts of this program as well: 
#
# ```
# plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1)
# plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1)
# plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1)
# ```
# * subplot2grid is similar to “pyplot.subplot” but uses 0-based indexing and let subplot to occupy multiple cells. 
# Let us try to understand the arguments of the subplot2grid method: 
#     1. argument 1 : geometry of the grid 
#     2. argument 2: location of the subplot in the grid 
#     3. argument 3: (rowspan) No. of rows covered by subplot. 
#     4. argument 4: (colspan) No. of columns covered by subplot.
# This figure will make this concept more clear:
#
# <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210722193421/sub4.png">
#
# * In our example, each subplot spans over 3 rows and 1 column with two empty rows (row no. 4,8) .
#
# ```
# x, y = create_plot('sin')
# plt1.plot(x, y, label = 'sine wave', color ='b')
# ```
#
# * Nothing special in this part as the syntax to plot points on a subplot remains same.
#
# ```
# plt1.legend()
# ```
#
# * This will show the label of the subplot on the figure.
#
# ```
# plt.show()
# ```
#
# * Finally, we call the plt.show() function to show the current plot.
#
# **Note:** After going through the above two examples, we can infer that one should use **subplot()** method when the plots are of uniform size where as **subplot2grid()** method should be preferred when we want more flexibility on position and sizes of our subplots. 

# + [markdown] heading_collapsed=true hidden=true
# ## 3-D plotting

# + [markdown] hidden=true
# We can easily plot 3-D figures in matplotlib. Now, we discuss some important and commonly used 3-D plots. 

# + [markdown] heading_collapsed=true hidden=true
# ### Plotting points

# + hidden=true
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
# setting a custom style to use
style.use('ggplot')
 
# create a new figure for plotting
fig = plt.figure()
 
# create a new subplot on our figure
# and set projection as 3d
ax1 = fig.add_subplot(111, projection='3d')
 
# defining x, y, z co-ordinates
x = np.random.randint(0, 10, size = 20)
y = np.random.randint(0, 10, size = 20)
z = np.random.randint(0, 10, size = 20)
 
# plotting the points on subplot
ax1.scatter(x, y, z, c = 'm', marker = 'o')
 
# setting labels for the axes
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')
 
# function to show the plot
plt.show()

# + [markdown] hidden=true
# * Let us try to understand some important aspects of this code now. 
# ```
# from mpl_toolkits.mplot3d import axes3d
# ```
# * This is the module required to plot on 3-D space. 
# ```
# ax1 = fig.add_subplot(111, projection='3d')
# ```
# * ere, we create a subplot on our figure and set projection argument as 3d. 
# ```
# ax1.scatter(x, y, z, c = 'm', marker = 'o')
# ```
# * Now we use **.scatter()** function to plot the points in XYZ plane.

# + [markdown] heading_collapsed=true hidden=true
# ### Plotting lines

# + hidden=true
# importing required modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
# setting a custom style to use
style.use('ggplot')
 
# create a new figure for plotting
fig = plt.figure()
 
# create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')
 
# defining x, y, z co-ordinates
x = np.random.randint(0, 10, size = 5)
y = np.random.randint(0, 10, size = 5)
z = np.random.randint(0, 10, size = 5)
 
# plotting the points on subplot
# ax1.plot_wireframe(x,y,z)
ax1.plot_trisurf(x,y,z)
 
# setting the labels
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')
 
plt.show()

# + [markdown] hidden=true
# **CAVEAT**
# 1. [Why Z has to be 2-dimensional for 3d plotting in matplotlib](https://stackoverflow.com/questions/53246874/why-z-has-to-be-2-dimensional-for-3d-plotting-in-matplotlib/53248136)
# 1. [plotting 3D surface using python: raise ValueError("Argument Z must be 2-dimensional.") matplotlib [duplicate]](https://stackoverflow.com/questions/51574861/plotting-3d-surface-using-python-raise-valueerrorargument-z-must-be-2-dimensi)
#

# + [markdown] hidden=true
# * The main difference in this program with previous one is: 
# ```
# ax1.plot_wireframe(x,y,z)
# ```
# * We used **.plot_wireframe()** method to plot lines over a given set of 3-D points.

# + [markdown] heading_collapsed=true hidden=true
# ### Plotting Bars

# + hidden=true
# importing required modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
# setting a custom style to use
style.use('ggplot')
 
# create a new figure for plotting
fig = plt.figure()
 
# create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')
 
# defining x, y, z co-ordinates for bar position
x = [1,2,3,4,5,6,7,8,9,10]
y = [4,3,1,6,5,3,7,5,3,7]
z = np.zeros(10)
 
# size of bars
dx = np.ones(10)              # length along x-axis
dy = np.ones(10)              # length along y-axs
dz = [1,3,4,2,6,7,5,5,10,9]   # height of bar
 
# setting color scheme
color = []
for h in dz:
    if h > 5:
        color.append('r')
    else:
        color.append('b')
 
# plotting the bars
ax1.bar3d(x, y, z, dx, dy, dz, color = color)
 
# setting axes labels
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')
 
plt.show()

# + [markdown] hidden=true
# * Let us go through important aspects of this program: 
# ```
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [4,3,1,6,5,3,7,5,3,7]
# z = np.zeros(10)
# ```
# * Here, we define the base positions of bars. Setting z = 0 means all bars start from XY plane. 
# ```
# dx = np.ones(10)              # length along x-axis
# dy = np.ones(10)              # length along y-axs
# dz = [1,3,4,2,6,7,5,5,10,9]   # height of bar
# ```
# * dx, dy, dz denote the size of bar. Consider he bar as a cuboid, then dx, dy, dz are its expansions along x, y, z axis respectively. 
# ```
# for h in dz:
#     if h > 5:
#         color.append('r')
#     else:
#         color.append('b')
# ```
# * Here, we set the color for each bar as a list. The color scheme is red for bars with height greater than 5 and blue otherwise. 
# ```
# ax1.bar3d(x, y, z, dx, dy, dz, color = color)
# ```
# * Finally, to plot the bars, we use **.bar3d()** function.

# + [markdown] heading_collapsed=true hidden=true
# ### Plotting curves

# + hidden=true
# importing required modules
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
 
# setting a custom style to use
style.use('ggplot')
 
# create a new figure for plotting
fig = plt.figure()
 
# create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')
 
# get points for a mesh grid
u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
 
# setting x, y, z co-ordinates
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
 
# plotting the curve
ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1)
 
plt.show()

# + [markdown] hidden=true
# * Here, we plotted a sphere as a mesh grid. <br>
# Let us go through some important parts: 
#
# ```
# u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
# ```
#
# * We use np.mgrid in order to get points so that we can create a mesh. <br>
# You can read more about this here. 
#
# ```
# x=np.cos(u)*np.sin(v)
# y=np.sin(u)*np.sin(v)
# z=np.cos(v)
# ```
#
# * This is nothing but the parametric equation of a sphere. 
#
# ```
# ax1.plot_wireframe(x, y, z, rstride = 5, cstride = 5, linewidth = 1)
# ```
#
# * Agan, we use **.plot_wireframe()** method. Here, **rstride** and **cstride** arguments can be used to set how much dense our mesh must be.

# + [markdown] heading_collapsed=true
# # [Graph Plotting in Python | Set 3](https://www.geeksforgeeks.org/graph-plotting-python-set-3/?ref=lbp)

# + [markdown] hidden=true
# Matplotlib is a pretty extensive library which supports **Animations** of graphs as well. The animation tools center around the **matplotlib.animation** base class, which provides a framework around which the animation functionality is built. The main interfaces are **TimedAnimation** and **FuncAnimation** and out of the two, **FuncAnimation** is the most convenient one to use.

# + [markdown] heading_collapsed=true hidden=true
# ## Installation:

# + [markdown] hidden=true
# * **Matplotlib**: Refer to [Graph Plotting in Python | Set 1](#Graph-Plotting-in-Python-|-Set-1)
# * **Numpy**: You can install numpy module using following pip command:
# pip install numpy
# * **FFMPEG**: It is required only for saving the animation as a video. The executable can be downloaded from [here](https://ffmpeg.org/download.html).

# + [markdown] heading_collapsed=true hidden=true
# ## Implementation of a Growing Coil:

# + hidden=true
# importing required modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
  
# create a figure, axis and plot element
fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)
  
# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,
  
# lists to store x and y axis points
xdata, ydata = [], []
  
# animation function
def animate(i):
    # t is a parameter
    t = 0.1*i
      
    # x, y values to be plotted
    x = t*np.sin(t)
    y = t*np.cos(t)
      
    # appending new points to x, y axes points list
    xdata.append(x)
    ydata.append(y)
      
    # set/update the x and y axes data
    line.set_data(xdata, ydata)
      
    # return line object
    return line,
      
# setting a title for the plot
plt.title('A growing coil!')
# hiding the axis details
plt.axis('off')
  
# call the animator    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=20, blit=True)
  
# save the animation as mp4 video file
anim.save('animated_coil.mp4', writer = 'ffmpeg', fps = 30)
  
# show the plot
plt.show()

# + [markdown] hidden=true
# Now, let us try to understand the code in pieces:
#
# * ```
# fig = plt.figure()
# ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
# line, = ax.plot([], [], lw=2)
# ```
# Here, we first create a figure, i.e a top level container for all our subplots.
# Then we create an axes element **ax** which acts as a subplot. The range/limit for x and y axis are also defined while creating the axes element.<br>
# Finally, we create the plot element, named as **line**. Initially, the x and y axis points have been defined as empty lists and line-width **(lw)** has been set as 2.
# * ```
# def init():
#     line.set_data([], [])
#     return line,
# ```
# Now, we declare a initialization function, **init**. This function is called by animator to create the first frame.
# * ```
# def animate(i):
#     # t is a parameter
#     t = 0.1*i
#     
#     # x, y values to be plotted
#     x = t*np.sin(t)
#     y = t*np.cos(t)
#     
#     # appending new points to x, y axes points list
#     xdata.append(x)
#     ydata.append(y)
#     
#     # set/update the x and y axes data
#     line.set_data(xdata, ydata)
#     
#     # return line object
#     return line,
# ```
# This is the most important function of above program. **animate()** function is called again and again by the animator to create each frame. The number of times this function will be called is determined by number of frames, which is passed as **frames** argument to animator.
#  **animate()** function takes the index of ith frame as argument.
# ```
# t = 0.1*i
# ```
# Here, we cleverly use the index of current frame as a parameter!
# ```
# x = t*np.sin(t)
# y = t*np.cos(t)
# ```
# Now, since we have the parameter t, we can easily plot any parametric equation. For example, here, we are plotting a spiral using its parametric equation.
# ```
# line.set_data(xdata, ydata)
# return line,
# ```
# Finally, we use **set_data()** function to set x and y data and then return plot object, **line**.
# * ```
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=500, interval=20, blit=True)
# ```
# Now, we create the FuncAnimation object, **anim**. It takes various arguments explained below:
#
# **fig** : figure to be plotted.
#
# **animate** : the function to be called repeatedly for each frame.
#
# **init_func** : function used to draw a clear frame. It is called once before the first frame.
#
# **frames** : number of frames. (Note: frames can also be an iterable or generator.)
#
# **interval** : duration between frames ( in milliseconds)
#
# **blit** : setting blit=True means that only those parts will be drawn, which have changed.
# * ```
# anim.save('animated_coil.mp4', writer = 'ffmpeg', fps = 30)
# ```
# Now, we save the animator object as a video file using **save()** function. You will need a movie writer for saving the animation video. In this example, we have used FFMPEG movie writer. So, **writer** is set as ‘ffmpeg’.<br>
#  **fps** stands for frame per second.
#

# + [markdown] heading_collapsed=true hidden=true
# ## Example of a Rotating Star

# + [markdown] hidden=true
# This example shows how one can make a rotating curve by applying some simple mathematics!

# + hidden=true
# importing required modules
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
  
# create a figure, axis and plot element
fig = plt.figure()
ax = plt.axes(xlim=(-25, 25), ylim=(-25, 25))
line, = ax.plot([], [], lw=2)
  
# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,
  
# set of points for a star (could be any curve)
p = np.arange(0, 4*np.pi, 0.1)
x = 12*np.cos(p) + 8*np.cos(1.5*p)
y = 12*np.sin(p) - 8*np.sin(1.5*p)
  
# animation function
def animate(i):
    # t is a parameter
    t = 0.1*i
      
    # x, y values to be plotted
    X = x*np.cos(t) - y*np.sin(t)
    Y = y*np.cos(t) + x*np.sin(t)
      
    # set/update the x and y axes data
    line.set_data(X, Y)
      
    # return line object
    return line,
      
# setting a title for the plot
plt.title('A rotating star!')
# hiding the axis details
plt.axis('off')
  
# call the animator    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=100, blit=True)
  
# save the animation as mp4 video file
anim.save('basic_animation.mp4', writer = 'ffmpeg', fps = 10)
  
# show the plot
plt.show()

# + [markdown] hidden=true
# Here, we have used some simple mathematics to rotate a given curve.
#
# * The star shape is obtained by putting $k = 2.5$ and $0<t<4\cdot\pi$ in the parametric equation<br>given below:
# $
# \begin{align}
# x & = (a-b)\cdot\cos t + b\cdot\cos\left(t\cdot\left(\frac{a}{b}-1\right)\right) \\
# y & = (a-b)\cdot\sin t - b\cdot\sin\left(t\cdot\left(\frac{a}{b}-1\right)\right) \\
# z & = \frac{a}{b}
# \end{align}
# $
# The same has been applied here:
# ```
# p = np.arange(0, 4*np.pi, 0.1)
# x = 12*np.cos(p) + 8*np.cos(1.5*p)
# y = 12*np.sin(p) - 8*np.sin(1.5*p)
# ```
# * Now, in each frame, we rotate the star curve using concept of rotation in complex numbers. Let $x, y$ be two ordinates. Then after rotation by angle theta, the new ordinates are:
# $
# \begin{align}
#  x &= x\cos \theta - y\sin \theta    \\
#  y &=  x\sin \theta + y\cos \theta   
# \end{align}
# $
# The same has been applied here:
# ```
# X = x*np.cos(t) - y*np.sin(t)
# Y = y*np.cos(t) + x*np.sin(t)
# ```
#
# All in all, animations are a great tool to create amazing stuff and many more things can be created using them.
#
# So, this was how animated plots can be generated and saved using Matplotlib.

# + [markdown] heading_collapsed=true
# # [Plotting graph using Seaborn | Python](https://www.geeksforgeeks.org/plotting-graph-using-seaborn-python/?ref=lbp)

# + [markdown] hidden=true
# This article will introduce you to graphing in Python with Seaborn, which is the most popular statistical visualization library in Python.

# + [markdown] hidden=true
# **Installation:** The easiest way to install seaborn is to use pip. Type following command in terminal:  

# + hidden=true
# # !pip install seaborn

# + [markdown] hidden=true
# OR, you can download it from [here](https://pypi.python.org/pypi/seaborn) (on PyPI) and install it manually.  

# + [markdown] heading_collapsed=true hidden=true
# #### Plotting categorical scatter plots with Seaborn <a class="tocSkip">

# + [markdown] heading_collapsed=true hidden=true
# ## Stripplot

# + hidden=true
# Python program to illustrate
# Plotting categorical scatter
# plots with Seaborn
 
# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns
 
# x axis values
x =['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
 
# y axis values
y =[5, 6.7, 4, 6, 2, 4.9, 1.8]
 
# plotting strip plot with seaborn
ax = sns.stripplot(x, y);
 
# giving labels to x-axis and y-axis
ax.set(xlabel ='Days', ylabel ='Amount_spend')
 
# giving title to the plot
plt.title('My first graph');
 
# function to show plot
plt.show()

# + [markdown] hidden=true
# **Explanation:** This is the one kind of scatter plot of categorical data with the help of seaborn.  
#
# * Categorical data is represented on the x-axis and values correspond to them represented through the $y$-axis.
# * **.striplot()** function is used to define the type of the plot and to plot them on canvas using.
# * **.set()** function is used to set labels of x-axis and y-aixs.
# * **.title()** function is used to give a title to the graph.
# * To view plot we use **.show()** function.

# + [markdown] heading_collapsed=true hidden=true
# #### Stripplot using inbuilt data-set given in seaborn: <a class="tocSkip">

# + hidden=true
# Python program to illustrate
# Stripplot using inbuilt data-set
# given in seaborn
 
# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns
 
# use to set style of background of plot
sns.set(style="whitegrid")
 
# loading data-set
iris = sns.load_dataset('iris')
 
# plotting strip plot with seaborn
# deciding the attributes of dataset on
# which plot should be made
ax = sns.stripplot(x='species', y='sepal_length', data=iris)
 
# giving title to the plot
plt.title('Graph')
 
# function to show plot
plt.show()

# + [markdown] hidden=true
# **Explanation:** This is the one kind of scatter plot of categorical data with the help of seaborn.  
#
# * **iris** is the dataset already present in seaborn module for use.
# * We use **.load_dataset()** function in order to load the data.We can also load any other file by giving the path and name of the file in the argument.
# * **.set(style=”whitegrid”)** function here is also use to define the background of plot.We can use **“darkgrid”** instead of whitegrid if we want the dark-colored background.
# * In **.stripplot()** function we have to define which attribute of the dataset to be on the $x$-axis and which attribute of the dataset should on $y$-axis. **data = iris** means attributes which we define earlier should be taken from the given data.
# * We can also draw this plot with matplotlib but the problem with matplotlib is its default parameters. The reason why Seaborn is so great with DataFrames is, for example, labels from DataFrames are automatically propagated to plots or other data structures as you see in the above figure column name **species** comes on the $x$-axis and column name **stepal_length** comes on the $y$-axis, that is not possible with matplotlib. We have to explicitly define the labels of the x-axis and $y$-axis.

# + [markdown] heading_collapsed=true hidden=true
# ## Swarmplot 

# + hidden=true
# Python program to illustrate
# plotting using Swarmplot
 
# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns
 
# use to set style of background of plot
sns.set(style="whitegrid")
 
# loading data-set
iris = sns.load_dataset('iris')
 
# plotting strip plot with seaborn
# deciding the attributes of dataset on
# which plot should be made
ax = sns.swarmplot(x='species', y='sepal_length', data=iris)
 
# giving title to the plot
plt.title('Graph')
 
# function to show plot
plt.show()

# + [markdown] hidden=true
# **Explanation:**
# This is very much similar to stripplot but the only difference is that it does not allow overlapping of markers. It causes jittering in the markers of the plot so that graph can easily be read without information loss as seen in the above plot. 
#
# * We use **.swarmplot()** function to plot swarn plot.
# * Another difference that we can notice in Seaborn and Matplotlib is that working with DataFrames doesn’t go quite as smoothly with Matplotlib, which can be annoying if we doing exploratory analysis with Pandas. And that’s exactly what Seaborn does easily, the plotting functions operate on DataFrames and arrays that contain a whole dataset.

# + [markdown] hidden=true
# **Note:** If we want we can also change the representation of data on a particular axis. 

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns
 
# use to set style of background of plot
sns.set(style="whitegrid")
 
# loading data-set
iris = sns.load_dataset('iris')
 
# plotting strip plot with seaborn
# deciding the attributes of dataset on
# which plot should be made
ax = sns.swarmplot(x='sepal_length', y='species', data=iris)
 
 
# giving title to the plot
plt.title('Graph')
 
# function to show plot
plt.show()

# + [markdown] hidden=true
# The same can be done in striplot. At last, we can say that Seaborn is an extended version of matplotlib which tries to make a well-defined set of hard things easy.

# + [markdown] heading_collapsed=true hidden=true
# ## Barplot

# + [markdown] hidden=true
# A **barplot** is basically used to aggregate the categorical data according to some methods and by default it’s the mean. It can also be understood as a visualization of the group by action. To use this plot we choose a categorical column for the $x$-axis and a numerical column for the $y$-axis, and we see that it creates a plot taking a mean per categorical column.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# barplot([x, y, hue, data, order, hue_order, …])
# ```

# + hidden=true
# import the seaborn library
import seaborn as sns
 
# reading the dataset
df = sns.load_dataset('tips')
 
# change the estimator from mean to
# standard deviation
sns.barplot(x ='sex', y ='total_bill', data = df, 
            palette ='plasma')

# + [markdown] hidden=true
# **Explanation:**
# Looking at the plot we can say that the average total_bill for the male is more than compared to the female.
#
# * Palette is used to set the color of the plot
# * The estimator is used as a statistical function for estimation within each categorical bin.

# + [markdown] heading_collapsed=true hidden=true
# ## Countplot

# + [markdown] hidden=true
# A countplot basically counts the categories and returns a count of their occurrences. It is one of the simplest plots provided by the seaborn library.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# countplot([x, y, hue, data, order, …])
# ```

# + hidden=true
# import the seaborn library
import seaborn as sns
 
# reading the dataset
df = sns.load_dataset('tips')
 
sns.countplot(x ='sex', data = df)

# + [markdown] hidden=true
# **Explanation:**

# + [markdown] hidden=true
# Looking at the plot we can say that the number of males is more than the number of females in the dataset. As it only returns the count based on a categorical column, we need to specify only the x parameter.

# + [markdown] heading_collapsed=true hidden=true
# ## Boxplot

# + [markdown] hidden=true
# **Box Plot** is the visual representation of the depicting groups of numerical data through their quartiles. Boxplot is also used to detect the outlier in the data set.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# boxplot([x, y, hue, data, order, hue_order, …])
# ```

# + hidden=true
# import the seaborn library
import seaborn as sns
 
# reading the dataset
df = sns.load_dataset('tips')
 
sns.boxplot(x='day', y='total_bill', data=df, hue='smoker')

# + [markdown] hidden=true
# **Explanation:**

# + [markdown] hidden=true
# $x$ takes the categorical column and $y$ is a numerical column. Hence we can see the total bill spent each day.” hue” parameter is used to further add a categorical separation. By looking at the plot we can say that the people who do not smoke had a higher bill on Friday as compared to the people who smoked.

# + [markdown] heading_collapsed=true hidden=true
# ## Violinplot

# + [markdown] hidden=true
# It is similar to the boxplot except that it provides a higher, more advanced visualization and uses the kernel density estimation to give a better description about the data distribution.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# violinplot([x, y, hue, data, order, …])
# ```

# + hidden=true
# import the seaborn library
import seaborn as sns
 
# reading the dataset
df = sns.load_dataset('tips')
sns.violinplot(x='day', y='total_bill', data=df,
               hue='sex', split=True)

# + [markdown] hidden=true
# **Explanation:**

# + [markdown] hidden=true
# * `hue` is used to separate the data further using the sex category
# * setting `split=True` will draw half of a violin for each level. This can make it easier to directly compare the distributions.

# + [markdown] heading_collapsed=true hidden=true
# ## Stripplot

# + [markdown] hidden=true
# It basically creates a scatter plot based on the category.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# stripplot([x, y, hue, data, order, …])
# ```

# + hidden=true
# import the seaborn library
import seaborn as sns
 
# reading the dataset
df = sns.load_dataset('tips')
sns.stripplot(x='day', y='total_bill', data=df,
              jitter=True, hue='smoker', dodge=True)

# + [markdown] hidden=true
# **Explanation:**

# + [markdown] hidden=true
# * One problem with strip plot is that you can’t really tell which points are stacked on top of each other and hence we use the jitter parameter to add some random noise.
# * `jitter` parameter is used to add an amount of jitter (only along the categorical axis) which can be useful when you have many points and they overlap so that it is easier to see the distribution.
# * `hue` is used to provide an additional categorical separation
# * setting `split=True` is used to draw separate strip plots based on the category specified by the hue parameter.

# + [markdown] heading_collapsed=true
# # [Box plot visualization with Pandas and Seaborn](https://www.geeksforgeeks.org/box-plot-visualization-with-pandas-and-seaborn/?ref=lbp)

# + [markdown] hidden=true
# _**Box Plot**_ is the visual representation of the depicting groups of numerical data through their quartiles. Boxplot is also used for detect the outlier in data set. It captures the summary of the data efficiently with a simple box and whiskers and allows us to compare easily across groups. Boxplot summarizes a sample data using 25th, 50th and 75th percentiles. These percentiles are also known as the lower quartile, median and upper quartile.
#
# A box plot consist of 5 things.

# + [markdown] hidden=true
# * Minimum
# * First Quartile or 25%
# * Median (Second Quartile) or 50%
# * Third Quartile or 75%
# * Maximum

# + [markdown] hidden=true
# To download the dataset used, click [here](https://media.geeksforgeeks.org/wp-content/uploads/tips.csv).

# + [markdown] heading_collapsed=true hidden=true
# #### Draw the box plot with Pandas: <a class="tocSkip">

# + [markdown] hidden=true
# One way to plot boxplot using pandas [dataframe](#Python-|-Pandas-DataFrame) is to use `boxplot()` function that is part of pandas library.

# + hidden=true
# import the required library 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# %matplotlib inline
  
  
# load the dataset
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/tips.csv")
  
# display 5 rows of dataset
df.head()   

# + [markdown] hidden=true
# Boxplot of `days` with respect `total_bill`.

# + hidden=true
df.boxplot(by ='day', column =['total_bill'], grid = False)

# + [markdown] hidden=true
# Boxplot of `size` with respect `tip`.

# + hidden=true
df.boxplot(by ='size', column =['tip'], grid = False)

# + [markdown] heading_collapsed=true hidden=true
# #### Draw the box plot using seaborn library: <a class="tocSkip">

# + [markdown] hidden=true
# **Syntax:**
#
# *seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None, \*\*kwargs)*
#
# **Parameters:**
#
# **x** = feature of dataset<br>
# **y** = feature of dataset<br>
# **hue** = feature of dataset<br>
# **data** = dataframe or full dataset<br>
# **color** = color name
#
# Let’s see how to create the box plot through seaborn library.
#
# Information about “tips” dataset.

# + hidden=true
# load the dataset
tips = sns.load_dataset('tips')
  
tips.head()

# + [markdown] hidden=true
# Boxplot of `days` with respect `total_bill`.

# + hidden=true
# Draw a vertical boxplot grouped 
# by a categorical variable:
sns.set_style("whitegrid")
  
sns.boxplot(x = 'day', y = 'total_bill', data = tips)

# + [markdown] hidden=true
# Boxplot of `size` with respect `tip`.

# + hidden=true
sns.boxplot(x = 'size', y = 'tip', data = tips)

# + [markdown] heading_collapsed=true
# # [Box Plot in Python using Matplotlib](https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/?ref=lbp)

# + [markdown] hidden=true
# A **Box Plot** is also known as **Whisker plot** is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum. In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.

# + [markdown] heading_collapsed=true hidden=true
# ## Creating Box Plot

# + [markdown] hidden=true
# The [matplotlib.pyplot](https://www.geeksforgeeks.org/pyplot-in-matplotlib/) module of matplotlib library provides `boxplot()` function with the help of which we can create box plots.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# matplotlib.pyplot.boxplot(data, notch=None, vert=None, patch_artist=None, widths=None)
# ```

# + [markdown] hidden=true
# **Parameters:**

# + [markdown] hidden=true
# | Attribute | Value |
# | --- | --- |
# | data | array or sequence of array to be plotted |
# | notch | optional parameter accepts boolean values |
# | vert | optional parameter accepts boolean values false and true for horizontal and vertical plot respectively |
# | bootstrap | optional parameter accepts int specifies intervals around notched boxplots |
# | usermedians | optional parameter accepts array or sequence of array dimension compatible with data |
# | positions | optional parameter accepts array and sets the position of boxes |
# | widths | optional parameter accepts array and sets the width of boxes |
# | patch_artist | optional parameter having boolean values |
# | labels | sequence of strings sets label for each dataset |
# | meanline | optional having boolean value try to render meanline as full width of box |
# | order | optional parameter sets the order of the boxplot |

# + [markdown] hidden=true
# The data values given to the `ax.boxplot()` method can be a Numpy array or Python list or Tuple of arrays. Let us create the box plot by using `numpy.random.normal()` to create some random data, it takes mean, standard deviation, and the desired number of values as arguments.

# + [markdown] heading_collapsed=true hidden=true
# ### Example: <a class="tocSkip">

# + hidden=true
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)
 
fig = plt.figure(figsize =(10, 7))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Customizing Box Plot

# + [markdown] hidden=true
# The `matplotlib.pyplot.boxplot()` provides endless customization possibilities to the box plot. The notch = True attribute creates the notch format to the box plot, patch_artist = True fills the boxplot with colors, we can set different colors to different boxes.The vert = 0 attribute creates horizontal box plot. labels takes same dimensions as the number data sets.

# + [markdown] heading_collapsed=true hidden=true
# ### Example 1: <a class="tocSkip">

# + hidden=true
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
 
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
 
# Creating plot
bp = ax.boxplot(data)
 
# show plot
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Example 2: <a class="tocSkip">

# + [markdown] hidden=true
# Let’s try to modify the above plot with some of the customizations: 

# + hidden=true
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
 
# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 
# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
     
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2',
                    'data_3', 'data_4'])
 
# Adding title
plt.title("Customized box plot")
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
     
# show plot
plt.show(bp)

# + [markdown] heading_collapsed=true
# # [How to get column names in Pandas dataframe](https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/?ref=lbp)

# + [markdown] hidden=true
# While analyzing the real datasets which are often very huge in size, we might need to get the column names in order to perform some certain operations.
#
# Let’s discuss how to get column names in [Pandas dataframe](#Python-|-Pandas-DataFrame).

# + [markdown] hidden=true
# First, let’s create a simple dataframe with [nba.csv](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv) file. 

# + hidden=true
# Import pandas package 
import pandas as pd 

# making data frame 
path_to_nba_csv = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
data = pd.read_csv(path_to_nba_csv) 

# calling head() method  
# storing in new variable 
data_top = data.head() 
    
# display 
data_top 

# + [markdown] hidden=true
# Now let’s try to get the columns name from above dataset.

# + [markdown] heading_collapsed=true hidden=true
# ## Method #1: Simply iterating over columns  <a class="tocSkip">

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv(path_to_nba_csv) 
  
# iterating the columns
for col in data.columns:
    print(col)

# + [markdown] heading_collapsed=true hidden=true
# ## Method #2: Using columns with dataframe object <a class="tocSkip">

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv(path_to_nba_csv) 
    
# list(data) or
list(data.columns)

# + [markdown] heading_collapsed=true hidden=true
# ## Method #3: column.values method returs an array of index. <a class="tocSkip">

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv(path_to_nba_csv) 
    
list(data.columns.values)

# + [markdown] heading_collapsed=true hidden=true
# ## Method #4: Using tolist() method with values with given the list of columns. <a class="tocSkip">

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv(path_to_nba_csv) 
    
list(data.columns.values.tolist())

# + [markdown] heading_collapsed=true hidden=true
# ## Method #5: Using sorted() method <a class="tocSkip">

# + [markdown] hidden=true
# `Sorted()` method will return the list of columns sorted in alphabetical order.

# + hidden=true
# Import pandas package 
import pandas as pd 
    
# making data frame 
data = pd.read_csv(path_to_nba_csv) 
    
# using sorted() method
sorted(data)

# + [markdown] heading_collapsed=true
# # [Python | Pandas dataframe.groupby()](https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/?ref=lbp)

# + [markdown] hidden=true
# Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric python packages. **Pandas** is one of those packages and makes importing and analyzing data much easier.
#
# [Pandas groupby](#Pandas-GroupBy) is used for grouping the data according to the categories and apply a function to the categories. It also helps to aggregate data efficiently.

# + [markdown] hidden=true
# Pandas `dataframe.groupby()` function is used to split the data into groups based on some criteria. pandas objects can be split on any of their axes. The abstract definition of grouping is to provide a mapping of labels to group names.

# + [markdown] hidden=true
#
# | **Syntax:** | `DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)`  |
# | --- | --- |
# | **Parameters :** | |
# | **by :** | mapping, function, str, or iterable |
# | **axis :** | int, default 0.    |
# | **level :** | If the axis is a MultiIndex (hierarchical), group by a particular level or levels |
# | **as_index :** | For aggregated output, return object with group labels as the index. Only relevant for DataFrame input. as_index=False is effectively “SQL-style” grouped output |
# | **sort :** | Sort group keys. Get better performance by turning this off. |
# |  | **Note** this does not influence the order of observations within each group. groupby preserves the order of rows within each group. |
# | **group_keys :** | When calling apply, add group keys to index to identify pieces |
# | **squeeze :** | Reduce the dimensionality of the return type if possible, otherwise return a consistent type |
# | **Returns :** | GroupBy object |
#

# + [markdown] hidden=true
# For link to CSV file Used in Code, click [here](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv)

# + [markdown] heading_collapsed=true hidden=true
# ## Example #1: Use groupby() function to group the data based on the “Team”. <a class="tocSkip">

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
# Print the dataframe
df

# + [markdown] hidden=true
# Now apply the `groupby()` function.

# + hidden=true
# applying groupby() function to
# group the data on team value.
gk = df.groupby('Team')
  
# Let's print the first entries
# in all the groups formed.
gk.first()

# + [markdown] hidden=true
# Let’s print the value contained any one of group. For that use the name of the team. We use the function `get_group()` to find the entries contained in any of the groups.

# + hidden=true
# Finding the values contained in the "Boston Celtics" group
gk.get_group('Boston Celtics')

# + [markdown] heading_collapsed=true hidden=true
# ## Example #2: Use groupby() function to form groups based on more than one category (i.e. Use more than one column to perform the splitting). <a class="tocSkip">

# + hidden=true
# importing pandas as pd
import pandas as pd
  
# Creating the dataframe 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
  
# First grouping based on "Team"
# Within each team we are grouping based on "Position"
gkk = df.groupby(['Team', 'Position'])
  
# Print the first value in each group
gkk.first()

# + [markdown] hidden=true
# `groupby()` is a very powerful function with a lot of variations. It makes the task of splitting the dataframe over some criteria really easy and efficient.

# + [markdown] heading_collapsed=true
# # [Adding new column to existing DataFrame in Pandas](https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/?ref=leftbar-rightbar)

# + [markdown] hidden=true
# Let’s discuss how to add new columns to the existing DataFrame in Pandas. There are multiple ways we can do this task.

# + [markdown] heading_collapsed=true hidden=true
# ## Method #1: By declaring a new list as a column.  <a class="tocSkip">

# + hidden=true
# Import pandas package
import pandas as pd
 
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
 
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
 
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
 
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address
 
# Observe the result
df

# + [markdown] heading_collapsed=true hidden=true
# ## Method #2: By using [DataFrame.insert()](https://www.geeksforgeeks.org/python-pandas-dataframe-insert/)   <a class="tocSkip">

# + [markdown] hidden=true
# It gives the freedom to add a column at any position we like and not just at the end. It also provides different options for inserting the column values.

# + hidden=true
# Import pandas package
import pandas as pd
 
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
 
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
 
# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24, 21], True)
 
# Observe the result
df

# + [markdown] heading_collapsed=true hidden=true
# ## Method #3: Using [Dataframe.assign()](https://www.geeksforgeeks.org/python-pandas-dataframe-assign/) method  <a class="tocSkip">

# + [markdown] hidden=true
# This method will create a new dataframe with a new column added to the old dataframe.

# + hidden=true
# Import pandas package
import pandas as pd
  
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
 
# Using 'Address' as the column name and equating it to the list
df2 = df.assign(address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'])
  
# Observe the result
df2

# + [markdown] heading_collapsed=true hidden=true
# ## Method #4: By using a dictionary   <a class="tocSkip">

# + [markdown] hidden=true
# We can use a Python dictionary to add a new column in pandas DataFrame. Use an existing column as the key values and their respective values will be the values for a new column. 

# + hidden=true
# Import pandas package
import pandas as pd
 
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
 
# Define a dictionary with key values of
# an existing column and their respective
# value pairs as the # values for our new column.
address = {'Delhi': 'Jai', 'Bangalore': 'Princi',
           'Patna': 'Gaurav', 'Chennai': 'Anuj'}
 
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
 
# Provide 'Address' as the column name
df['Address'] = address
 
# Observe the output
df


# + [markdown] heading_collapsed=true
# # [Python map() function](https://www.geeksforgeeks.org/python-map-function/?ref=leftbar-rightbar)

# + [markdown] hidden=true
# `map()` function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
#
# | **Syntax:** | `map(fun, iter)`  |
# | --- | --- |
# | **Parameters :** | |
# | **fun :** | A function to which map passes each element of given iterable. |
# | **iter :** | An iterable which is to be mapped.    |
# | **Returns :** | Returns a list of the results after applying the given function |
# |               | to each item of a given iterable (list, tuple etc.) |
#

# + [markdown] hidden=true
# **NOTE :** The returned value from `map()` (map object) then can be passed to functions like `list()` (to create a list), `set()` (to create a set) .

# + [markdown] heading_collapsed=true hidden=true
# ## CODE 1 <a class="tocSkip">

# + hidden=true
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# + [markdown] heading_collapsed=true hidden=true
# ## CODE 2 <a class="tocSkip">

# + [markdown] hidden=true
# We can also use [lambda expressions](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/) with map to achieve above result.

# + hidden=true
# Double all numbers using map and lambda
  
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# + [markdown] heading_collapsed=true hidden=true
# ## CODE 3 <a class="tocSkip">

# + hidden=true
# Add two lists using map and lambda
  
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# + [markdown] heading_collapsed=true hidden=true
# ## CODE 4 <a class="tocSkip">

# + hidden=true
# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# + [markdown] heading_collapsed=true
# # [Taking input in Python](https://www.geeksforgeeks.org/taking-input-in-python/?ref=leftbar-rightbar)

# + [markdown] hidden=true
# Developers often have a need to interact with users, either to get data or to provide some sort of result. Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python provides us with two inbuilt functions to read the input from the keyboard.

# + [markdown] hidden=true
# * input ( prompt )
# * raw_input ( prompt )

# + [markdown] hidden=true
# ## input ( ) :  <a class="tocSkip">

# + [markdown] hidden=true
# This function first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether user entered a string or a number or list. If the input provided is not correct then either syntax error or exception is raised by python. For example –

# + hidden=true
# Python program showing 
# a use of input()
  
val = input("Enter your value: ")
print(val)

# + [markdown] hidden=true
# **How the input function works in Python :**
#
# * When `input()` function executes program flow will be stopped until the user has given an input.
# * The text or message display on the output screen to ask a user to enter input value is optional i.e. the prompt, will be printed on the screen is optional.
# * Whatever you enter as input, input function convert it into a string. if you enter an integer value still `input()` function convert it into a string. You need to explicitly convert it into an integer in your code using typecasting.

# + [markdown] hidden=true
# **Code**

# + hidden=true
# Program to check input 
# type in Python
  
num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
  
# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))

# + [markdown] hidden=true
# ## raw_input ( ) : <a class="tocSkip">

# + [markdown] hidden=true
# This function works in older version (like Python 2.x). This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store. For example –

# + hidden=true
# Python program showing 
# a use of raw_input()
  
g = raw_input("Enter your name : ")
print g

# + [markdown] hidden=true
# Here, $g$ is a variable which will get the string value, typed by user during the execution of program. Typing of data for the `raw_input()` function is terminated by enter key. We can use `raw_input()` to enter numeric data also. In that case we use typecasting.For more details on typecasting refer [this](https://www.geeksforgeeks.org/taking-input-from-console-in-python/).

# + [markdown] heading_collapsed=true
# # [Iterate over a list in Python](https://www.geeksforgeeks.org/iterate-over-a-list-in-python/?ref=leftbar-rightbar)

# + [markdown] hidden=true
# [List](https://www.geeksforgeeks.org/python-list/) is equivalent to arrays in other languages, with the extra benefit of being dynamic in size. In Python, the list is a type of container in Data Structures, which is used to store multiple data at the same time. Unlike Sets, lists in Python are ordered and have a definite count.
#
# There are multiple ways to iterate over a list in Python. Let’s see all the different ways to iterate over a list in Python, and performance comparison between them.
#

# + [markdown] heading_collapsed=true hidden=true
# ## Method #1: Using For loop  <a class="tocSkip">

# + hidden=true
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using for loop
for i in list:
    print(i)

del list

# + [markdown] heading_collapsed=true hidden=true
# ## Method #2: For loop and range()    <a class="tocSkip">

# + [markdown] hidden=true
# In case we want to use the traditional for loop which iterates from number $x$ to number $y$.  

# + hidden=true
# Python3 code to iterate over a list
ls = [1, 3, 5, 7, 9]
  
# getting length of list
length = len(ls)

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(ls[i])


# + [markdown] heading_collapsed=true
# # [Python program to convert a list to string](https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/?ref=leftbar-rightbar)

# + [markdown] hidden=true
# Given a list, write a Python program to convert the given list to string.
#
# There are various situation we might encounter when a list is given and we convert it to string. For example, conversion to string from the list of string or the list of integer.

# + [markdown] hidden=true
# **Example:**
#
# ```
# Input: ['Geeks', 'for', 'Geeks']
# Output: Geeks for Geeks
#
# Input: ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
# Output: I want 4 apples and 18 bananas
# ```

# + [markdown] hidden=true
# Let’s see various ways we can convert the list to string.

# + [markdown] heading_collapsed=true hidden=true
# ## Method #1: Using For loop  <a class="tocSkip">

# + [markdown] hidden=true
# Iterate through the list and keep adding the element for every index in some empty string.

# + hidden=true
# Python program to convert a list to string
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        
        
# Driver code    
s = ['Geeks', 'for', 'Geeks']
print(listToString(s)) 


# + [markdown] heading_collapsed=true hidden=true
# ## Method #2: Using .join() method  <a class="tocSkip">

# + hidden=true
# Python program to convert a list
# to string using join() function
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
        
# Driver code    
s = ['Geeks', 'for', 'Geeks']
print(listToString(s)) 

# + [markdown] hidden=true
# ##   <a class="tocSkip">

# + [markdown] hidden=true
# But what if the list contains both string and integer as its element. In those cases, above code won’t work. We need to convert it to string while adding to string.

# + [markdown] heading_collapsed=true hidden=true
# ## Method #3: Using list comprehension  <a class="tocSkip">

# + hidden=true
# Python program to convert a list
# to string using list comprehension
   
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
  
# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])
  
print(listToStr) 

# + [markdown] heading_collapsed=true hidden=true
# ## Method #4: Using map() <a class="tocSkip">

# + [markdown] hidden=true
# Use `map()` method for mapping `str` (for converting elements in list to string) with given iterator, the list.

# + hidden=true
# Python program to convert a list
# to string using list comprehension
   
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
  
# using list comprehension
listToStr = ' '.join(map(str, s))
  
print(listToStr) 
