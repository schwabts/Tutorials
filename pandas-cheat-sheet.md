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

# [Pandas cheat sheet](https://morphocode.com/pandas-cheat-sheet/)


Data can be messy: it often comes from various sources, doesn’t have structure or contains errors and missing fields. Working with data requires to clean, refine and filter the dataset before making use of it.

[Pandas](http://pandas.pydata.org/) is one of the most popular tools to perform such data transformations. It is an open source library for Python offering a simple way to aggregate, filter and analyze data. The library is often used together with Jupyter notebooks to empower data exploration in various research and data visualization projects.

Pandas introduces the concept of a [DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html)
 – a table-like data structure similar to a spreadsheet. You can import data in a data frame, join frames together, filter rows and columns and export the results in various file formats. Here is a pandas cheat sheet of the most common data operations:


# Getting Started


Import Pandas & Numpy

```python
import numpy as np
import pandas as pd
```

```python
import seaborn as sns

df = sns.load_dataset('iris')
print("df.size==",df.size,", df.shape: ",df.shape)
df.head()
```

Get the first 5 rows in a dataframe:

```python
df.head(3)
```

Get the last 5 rows in a dataframe:

```python
df.tail(5)
```

# Create DataFrame from columns (in dictionary):

```python
df = pd.DataFrame.from_dict({
    'company': 'Pandology', 
    'metrics': [[{'score': 10}, {'score': 20}, {'score': 35}]]
})
df
```

# Export Data


Export as an Excel Spreadsheet:

```python
df[['name_company', 'name_candidate']].to_excel('./output/companies.xls')
```

Export to a CSV file:

```python
df.to_csv('data-output/my-data.csv')
```

Export created DataFrame to a CSV file (just for importing it below):

```python
file_name='my-data.csv'

print("df.to_csv('{}'):".format(file_name))
df.to_csv(file_name) # , sep='\t')
```

# Import Data


Import data from a CSV file:

```python
other_df = pd.read_csv(file_name)
other_df
```

Import data from an Excel Spreadsheet:

```python
df_excel = pd.read_excel('./data/spreadsheet.xls',
    sheetname='sheet1',
    skiprows=[1] # header data
)
```

Import data from an Excel Spreadsheet without the header:

```python
df_names = pd.read_excel('./data/names_all.xls', header=None)
```

# Convert Data Types


Convert column data to string:

```python
df['name'] = df['name'].astype('str')
```

Convert column data to integer (nan values are set to -1):

```python
df['col'] = df['col'].fillna(-1).astype(int)
```

Convert column data to numeric type:

```python
df['col'] = pd.to_numeric(df['col'])
```

# Get / Set Values


Get the value of a column on a row with index $idx$:

```python
df.get_value(idx, 'col_name')
```

Set column value on a given row:

```python
idx = df[df['address'] == '4th Avenue'].index
df.set_value(idx, 'id', '502')
```

# Count



Number of rows in a DataFrame:

```python
len(df)
```

Count rows where column is equal to a value:

```python
len(df[df['score'] == 1.0])
```

Count unique values in a column:

```python
df['name'].nunique()
```

Count rows based on a value:

```python
df['is_removed'].value_counts()

# Count null values as well:
df['is_removed'].value_counts(dropna=False)
```

# Filter Data


Filter rows based on a value:


```python
df[df['id'] == '48']
```

Filter rows based on multiple values:

```python
df[(df['category'] == 'national') & (df['is_removed'] == '1')]
```

Filter rows that contain a string:

```python
df[df['category'].str.contains('national')]
```

Filter rows containing some of the strings:

```python
df['address'].str.contains('|'.join(['4th Avenue', 'Broadway']))
```

Filter rows where value is in a list:

```python
df[df['id'].isin(['109', '673'])]
```

Filter rows where value is **_not_** in a list:

```python
df = df[~df['id'].isin(['1', '2', '3'])]
```

Filter all rows that have valid values (not null):

```python
df = df[pd.notnull(df['latitude'])]
```

# Sort Data


Sort rows by value:

```python
df.sort_values('nom', inplace=True)
```

Sort Columns By Name:

```python
df = df.reindex_axis(sorted(df.columns), axis=1)
```

# Rename columns


Rename particular columns:

```python
df.rename(columns={'id': 'id_new', 'object': 'object_new'}, inplace=True)
```

Rename all columns:

```python
df.columns = ['id', 'object', 'address', 'type', 'category']
```

Make all columns lowercase:

```python
df.columns = map(str.lower, df.columns)
```

# Drop data


Drop column named $col$

```python
df = df.drop('col', axis=1)
```

Drop all rows with *null* index:

```python
df[pd.notnull(df.index)]
```

Drop rows that have missing values in some columns:

```python
df.dropna(subset=['plsnkv', 'plsnnum'])
```

Drop duplicate rows:

```python
df = df.drop_duplicates(subset='id', keep='first')
```

# Create columns


Create a new column based on row data:

```python
def cad_id(row):    
    return row['region'] + '.' + row['lot'] + '.' + row['building']
      
df['cad_id'] = df.apply(cad_id, axis=1)
```

Create a new column based on another column:

```python
df['is_removed'] = df['object'].map(lambda x: 1 if 'removed' in x else 0)
```

Create multiple new columns based on row data:

```python
def geocode(row):
    address = api_geocode(street=row['street'], house_number=row['building'], zip_code=row['zip'])   
    return pd.Series([address.get('lat'), address.get('lon'), address.get('borough')])
     
df[['lat', 'lon', 'borough']] = df.apply(geocode, axis=1)
```

Match id to label:

```python
def zone_label(zone_id):
    return {
        'C': 'City Center',
        'S': 'Suburbs',       
        'R': 'Residential District'
    }.get(zone_id, zone_id)   
df['zone_label'] = df['zone_id'].map(zone_label)
```

# Data Joins


Join data frames by columns:

```python
df_lots.merge(df_buildings, on=['lot_id', 'mun_id'], suffixes=('_lot', '_building'))
```

Concatenate two data frames (one after the other):

```python
df_all = pd.concat([df_first, df_second])
```

# Utilities


Increase the number of table rows & columns shown:

```python
pd.options.display.max_rows = 999 
pd.options.display.max_columns = 999
```

# Learn More


We are covering data analysis and visualization in our upcoming course
[“Data & the City”](http://morphocode.com/academy/).
The course will discuss how to collect, store and visualize urban data in a useful way. Subscribe bellow and we’ll notify you when the course becomes available.


```python

```
