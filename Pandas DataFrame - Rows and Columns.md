---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# [Get first row of dataframe in Python Pandas based on criteria](https://stackoverflow.com/questions/40660088/get-first-row-of-dataframe-in-python-pandas-based-on-criteria)

```python
import pandas as pd
df = pd.DataFrame([[1, 2, 1], [1, 3, 2], [4, 6, 3], [4, 3, 4], [5, 4, 5]], columns=['A', 'B', 'C'])
df
```

For this  want to get the first row that fulfil some criteria. Examples:

1. Get first row where A > 3 (returns row 2)
1. Get first row where A > 4 AND B > 3 (returns row 4)
1. Get first row where A > 3 AND (B > 3 OR C > 2) (returns row 2)


[This tutorial](http://pandas.pydata.org/pandas-docs/stable/10min.html)
is a very good one for pandas slicing. Make sure you check it out. Onto some snippets... To slice a dataframe with a condition, you use this format:

```
>>> df[condition]
```


This will return a slice of your dataframe which you can index using `iloc`. Here are your examples:

1. Get first row where A > 3 (returns row 2)

```python
df[df.A > 3].iloc[0]
```

If what you actually want is the row number, rather than using `iloc`, it would be `df[df.A > 3].index[0]`.


2. Get first row where A > 4 AND B > 3:

```python
df[(df.A > 4) & (df.B > 3)].iloc[0]
```

3. Get first row where A > 3 AND (B > 3 OR C > 2) (returns row 2)

```python
df[(df.A > 3) & ((df.B > 3) | (df.C > 2))].iloc[0]
```

Now, with your last case we can write a function that handles the default case of returning the descending-sorted frame:

```python
def series_or_default(X, condition, default_col, ascending=False):
    sliced = X[condition]
    if sliced.shape[0] == 0:
        return X.sort_values(default_col, ascending=ascending).iloc[0]
    return sliced.iloc[0]

series_or_default(df, df.A > 6, 'A')
```

# [Interesting Ways to Select Pandas DataFrame Columns](https://towardsdatascience.com/interesting-ways-to-select-pandas-dataframe-columns-b29b82bbfb33)

Casey Whorton - Apr 16·4 min read


<img src="0_MArNnCyyR4B8zsbp.jfif" />
Photo by Cristina Gottardi on Unsplash


Manipulating pandas data frames is a common task during exploratory analysis or preprocessing in a Data Science project. Filtering and sub-setting the data is also common. Over time, I have found myself needing to select columns based on different criteria. I hope readers find this article as a reference.


## Example Data


If you want to use the data I used to test out these methods of selecting columns from a pandas data frame, use the code snippet below to get the wine dataset into your IDE or a notebook.
from sklearn.datasets import load_wine

```python
from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
import re

X = load_wine()
df = pd.DataFrame(X.data, columns = X.feature_names)

df.head()
```

Image of Table of Wine Data
Screenshot by Author of Wine Dataset in a Jupyter notebook



Now, depending on what you want to do, check out each one of the code snippets below and try for yourself!


## Selecting columns based on their name


This is the most basic way to select a single column from a dataframe, just put the string name of the column in brackets. Returns a pandas series.


```python
df['hue']

```

Passing a list in the brackets lets you select multiple columns at the same time.


```python
df[['alcohol','hue']]

```

## Selecting a subset of columns found in a list


Similar to the previous example, but here you can search over all the columns in the dataframe.


```python
df[df.columns[df.columns.isin(['alcohol','hue','NON-EXISTANT COLUMN'])]]

```

## Selecting a subset of columns based on difference of columns



Let’s say you know what columns you don’t want in the dataframe. Pass those as a list to the difference method and you’ll get back everything except them.


```python
df[df.columns.difference(['alcohol','hue'])]

```

## Selecting a subset of columns that is not in a list



Return a data frame that has columns that are not in a list that you want to search over.


```python
df[df.columns[~df.columns.isin(['alcohol','hue'])]]

```

## Selecting columns based on their data type



Data types include ‘float64’ and ‘object’ and are inferred from the columns passed to the dtypes method. By matching on columns that are the same data type, you’ll get a series of True/False. Use the values method to get just the True/False values and not the index.


```python
df.loc[:,(df.dtypes=='float64').values]

```

## Selecting columns based on their column name containing a substring



If you have tons of columns in a data frame and their column names all have a similar substring that you are interested in, you can return the columns who’s names contain a substring. Here we want everything that has the “al” substring in it.


```python
df.loc[:,['al' in i for i in df.columns]]

```

## Selecting columns based on their column name containing a string wildcard



You could have hundreds of columns, so it might make sense to find columns that match a pattern. Searching for column names that match a wildcard can be done with the “search” function from the re package (see the link in the reference section for more details on using the regular expression package).


```python
df.loc[:,[True if re.search('flava+',column) else False for column in df.columns]]

```

## Selecting columns based on how their column name starts



If you want to select columns with names that start with a certain string, you can use the startswith method and pass it in the columns spot for the data frame location.


```python
df.loc[:,df.columns.str.startswith('al')]

```

## Selecting columns based on how their column name ends



Same as the last example, but finds columns with names that end a certain way.


```python
df.loc[:,df.columns.str.endswith('oids')]

```

## Selecting columns if all rows meet a condition



You can pick columns if the rows meet a condition. Here, if all the the values in a column is greater than 14, we return the column from the data frame.


```python
df.loc[:,[(df[col] > 14).all() for col in df.columns]]

```

## Selecting columns if any row of a column meets a condition



Here, if any of the the values in a column is greater than 14, we return the column from the data frame.


```python
df.loc[:,[(df[col] > 14).any() for col in df.columns]]

```

## Selecting columns if the average of rows in a column meet a condition



Here, if the mean of all the values in a column meet a condition, return the column.


```python
df.loc[:,[(df[col].mean() > 7) for col in df.columns]]

```

Thanks for checking this out and feel free to reference it often.

```python

```
