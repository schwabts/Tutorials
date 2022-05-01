# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:light
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

# # [Python Seaborn Tutorial](https://www.geeksforgeeks.org/python-seaborn-tutorial/?ref=lbp) <a class="tocSkip">

# by GeeksForGeeks 

# Seaborn is a library mostly used for statistical plotting in Python. It is built on top of Matplotlib and provides beautiful default styles and color palettes to make statistical plots more attractive.

# In this tutorial, we will learn about Python Seaborn from basics to advance using a huge dataset of seaborn basics, concepts, and different graphs that can be plotted.

# + [markdown] heading_collapsed=true
# # Getting Started

# + [markdown] hidden=true
# First of all, let us install Seaborn. Seaborn can be installed using the pip. Type the below command in the terminal.

# + hidden=true
# # !pip install seaborn

# + [markdown] hidden=true
# After the installation is completed you will get a successfully installed message at the end of the terminal as shown below.

# + [markdown] hidden=true
# **Note:** Seaborn has the following dependencies – 
#
# * Python 2.7 or 3.4+
# * numpy
# * scipy
# * pandas
# * matplotlib

# + [markdown] hidden=true
# After the installation let us see an example of a simple plot using Seaborn. We will be plotting a simple line plot using the iris dataset. Iris dataset contains five columns such as Petal Length, Petal Width, Sepal Length, Sepal Width and Species Type. Iris is a flowering plant, the researchers have measured various features of the different iris flowers and recorded them digitally.

# + [markdown] heading_collapsed=true hidden=true
# ## Example:  <a class="tocSkip">

# + hidden=true
# importing packages
import seaborn as sns
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# + [markdown] hidden=true
# In the above example, a simple line plot is created using the lineplot() method. Do not worry about these functions as we will be discussing them in detail in the below sections. Now after going through a simple example let us see a brief introduction about the Seaborn. Refer to the below articles to get detailed information about the same.
#
# * [Introduction to Seaborn – Python](https://www.geeksforgeeks.org/introduction-to-seaborn-python/)
# * [Plotting graph using Seaborn](https://www.geeksforgeeks.org/plotting-graph-using-seaborn-python/)
#
# In the introduction, you must have read that Seaborn is built on the top of Matplotlib. It means that Seaborn can be used with Matplotlib. 

# + [markdown] heading_collapsed=true
# # Using Seaborn with Matplotlib

# + [markdown] hidden=true
# Using both Matplotlib and Seaborn together is a very simple process. We just have to invoke the Seaborn Plotting function as normal, and then we can use Matplotlib’s customization function.

# + [markdown] heading_collapsed=true hidden=true
# ## Example 1:  <a class="tocSkip">

# + [markdown] hidden=true
# We will be using the above example and will add the title to the plot using the Matplotlib.

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Example 2:  <a class="tocSkip">

# + [markdown] hidden=true
#  Setting the `xlim` and `ylim`

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# setting the x limit of the plot
plt.xlim(5)
 
plt.show()

# + [markdown] heading_collapsed=true
# # Customizing Seaborn Plots

# + [markdown] hidden=true
# Seaborn comes with some customized themes and a high-level interface for customizing the looks of the graphs. Consider the above example where the default of the Seaborn is used. It still looks nice and pretty but we can customize the graph according to our own needs. So let’s see the styling of plots in detail.

# + [markdown] heading_collapsed=true hidden=true
# ## Changing Figure Aesthetic <a class="tocSkip">

# + [markdown] hidden=true
# **set_style()** method is used to set the aesthetic of the plot. It means it affects things like the color of the axes, whether the grid is active or not, or other aesthetic elements. There are five themes available in Seaborn.
#
# * darkgrid
# * whitegrid
# * dark
# * white
# * ticks

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# set_style(style=None, rc=None)
# ```

# + [markdown] hidden=true
# **Example:** Using the dark theme

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# changing the theme to dark
sns.set_style("dark")
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Removal of Spines  <a class="tocSkip">

# + [markdown] hidden=true
# Spines are the lines noting the data boundaries and connecting the axis tick marks. It can be removed using the despine() method.

# + [markdown] hidden=true
# **Syntax:**
#

# + [markdown] hidden=true
# ```
# sns.despine(left = True)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# Removing the spines
sns.despine()
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Changing the figure Size  <a class="tocSkip">

# + [markdown] hidden=true
# The figure size can be changed using the [figure()](https://www.geeksforgeeks.org/matplotlib-pyplot-figure-in-python/) method of Matplotlib. figure() method creates a new figure of the specified size passed in the **figsize** parameter.

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# changing the figure size
plt.figure(figsize = (2, 4))
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# Removing the spines
sns.despine()
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Scaling the plots  <a class="tocSkip">

# + [markdown] hidden=true
# It can be done using the set_context() method. It allows us to override default parameters. This affects things like the size of the labels, lines, and other elements of the plot, but not the overall style. The base context is “notebook”, and the other contexts are “paper”, “talk”, and “poster”. font_scale sets the font size.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# set_context(context=None, font_scale=1, rc=None)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true

# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# Setting the scale of the plot
sns.set_context("paper")
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Setting the Style Temporarily <a class="tocSkip">

# + [markdown] hidden=true
# `axes_style()` method is used to set the style temporarily. It is used along with the **with** statement.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# axes_style(style=None, rc=None)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
 
def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
with sns.axes_style('darkgrid'):
     
    # Adding the subplot
    plt.subplot(211)
    plot()
     
plt.subplot(212)
plot()

# + [markdown] heading_collapsed=true
# # Color Palette

# + [markdown] hidden=true
# Colormaps are used to visualize plots effectively and easily. One might use different sorts of colormaps for different kinds of plots. **color_palette()** method is used to give colors to the plot. Another function **palplot()** is used to deal with the color palettes and plots the color palette as a horizontal array.

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# current colot palette
palette = sns.color_palette()
 
# plots the color palette as a
# horizontal array
sns.palplot(palette)
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Diverging Color Palette <a class="tocSkip">

# + [markdown] hidden=true
# This type of color palette uses two different colors where each color depicts different points ranging from a common point in either direction. Consider a range of -10 to 10 so the value from -10 to 0 takes one color and values from 0 to 10 take another.

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# current colot palette
palette = sns.color_palette('PiYG', 11)
 
# diverging color palette
sns.palplot(palette)
 
plt.show()

# + [markdown] hidden=true
# In the above example, we have used an in-built diverging color palette which shows 11 different points of color. The color on the left shows pink color and color on the right shows green color.

# + [markdown] heading_collapsed=true hidden=true
# ## Sequential Color Palette <a class="tocSkip">

# + [markdown] hidden=true
# A sequential palette is used where the distribution ranges from a lower value to a higher value. To do this add the character ‘s’ to the color passed in the color palette.

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# current colot palette
palette = sns.color_palette('Greens', 11)
 
# sequential color palette
sns.palplot(palette)
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Setting the default Color Palette <a class="tocSkip">

# + [markdown] hidden=true
# **set_palette()** method is used to set the default color palette for all the plots. The arguments for both color_palette() and set_palette() is same. set_palette() changes the default matplotlib parameters.

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# setting the default color palette
sns.set_palette('vlag')
plt.subplot(211)
 
# plotting with the color palette
# as vlag
plot()
 
# setting another default color palette
sns.set_palette('Accent')
plt.subplot(212)
plot()
 
plt.show()

# + [markdown] heading_collapsed=true
# # Multiple plots with Seaborn

# + [markdown] hidden=true
# You might have seen multiple plots in the above examples and some of you might have got confused. Don’t worry we will cover multiple plots in this section. Multiple plots in Seaborn can also be created using the Matplotlib as well as Seaborn also provides some functions for the same.

# + [markdown] hidden=true
# **Using Matplotlib**

# + [markdown] hidden=true
# Matplotlib provides various functions for plotting subplots. Some of them are [add_axes()](https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/), [subplot()](https://www.geeksforgeeks.org/matplotlib-pyplot-subplot-function-in-python/), and [subplot2grid()](https://www.geeksforgeeks.org/matplotlib-pyplot-subplot2grid-in-python/).
# Let’s see an example of each function for better understanding.

# + [markdown] heading_collapsed=true hidden=true
# ## Example 1: <a class="tocSkip">

# + [markdown] hidden=true
# Using [add_axes()](https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/) method

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
 
# loading dataset
data = sns.load_dataset("iris")
 
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))
 
# Creating first axes for the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
 
# plotting the graph
graph()
 
# Creating second axes for the figure
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])
 
# plotting the graph
graph()
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Example 2: <a class="tocSkip">

# + [markdown] hidden=true
# Using [subplot()](https://www.geeksforgeeks.org/matplotlib-pyplot-subplot-function-in-python/) method

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# Adding the subplot at the specified
# grid position
plt.subplot(121)
graph()
 
# Adding the subplot at the specified
# grid position
plt.subplot(122)
graph()
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Example 3: <a class="tocSkip">

# + [markdown] hidden=true
# Using [subplot2grid()](https://www.geeksforgeeks.org/matplotlib-pyplot-subplot2grid-in-python/) method

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
 
# adding the subplots
axes1 = plt.subplot2grid (
  (7, 1), (0, 0), rowspan = 2,  colspan = 1)
graph()
 
axes2 = plt.subplot2grid (
  (7, 1), (2, 0), rowspan = 2, colspan = 1)
graph()
   
axes3 = plt.subplot2grid (
  (7, 1), (4, 0), rowspan = 2, colspan = 1)
graph()

# + [markdown] heading_collapsed=true hidden=true
# ## Using Seaborn  <a class="tocSkip">

# + [markdown] hidden=true
# Seaborn also provides some functions for plotting multiple plots. Let’s see them in detail

# + [markdown] heading_collapsed=true hidden=true
# ### Method 1:  <a class="tocSkip">

# + [markdown] hidden=true
# Using [FacetGrid()]() method
#  
# * FacetGrid class helps in visualizing distribution of one variable as well as the relationship between multiple variables separately within subsets of your dataset using multiple panels.
# * A FacetGrid can be drawn with up to three dimensions ? row, col, and hue. The first two have obvious correspondence with the resulting array of axes; think of the hue variable as a third dimension along a depth axis, where different levels are plotted with different colors.
# * FacetGrid object takes a dataframe as input and the names of the variables that will form the row, column, or hue dimensions of the grid. The variables should be categorical and the data at each level of the variable will be used for a facet along that axis.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.FacetGrid( data, \*\*kwargs)
#
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
plot = sns.FacetGrid(data, col="species")
plot.map(plt.plot, "sepal_width")
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Method 2:  <a class="tocSkip">

# + [markdown] hidden=true
# Using [PairGrid()](https://www.geeksforgeeks.org/python-seaborn-pairgrid-method/) method
#
# * Subplot grid for plotting pairwise relationships in a dataset.
# * This class maps each variable in a dataset onto a column and row in a grid of multiple axes. Different axes-level plotting functions can be used to draw bivariate plots in the upper and lower triangles, and the marginal distribution of each variable can be shown on the diagonal.
# * It can also represent an additional level of conventionalization with the hue parameter, which plots different subsets of data in different colors. This uses color to resolve elements on a third dimension, but only draws subsets on top of each other and will not tailor the hue parameter for the specific visualization the way that axes-level functions that accept hue will.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.PairGrid( data, \*\*kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("flights")
 
plot = sns.PairGrid(data)
plot.map(plt.plot)
 
plt.show()

# + [markdown] hidden=true
# Refer to the below articles to get detailed information about the multiple plots
#
# * [Python – seaborn.FacetGrid() method](https://www.geeksforgeeks.org/python-seaborn-facetgrid-method/)
# * [Python – seaborn.PairGrid() method](https://www.geeksforgeeks.org/python-seaborn-pairgrid-method/)

# + [markdown] heading_collapsed=true
# # Creating Different Types of Plots

# + [markdown] heading_collapsed=true hidden=true
# ## Relational Plots <a class="tocSkip">

# + [markdown] hidden=true
# **Relational plots** are used for visualizing the statistical relationship between the data points. Visualization is necessary because it allows the human to see trends and patterns in the data. The process of understanding how the variables in the dataset relate each other and their relationships are termed as Statistical analysis. Refer to the below articles for detailed information. 
#
# * [Relational plots in Seaborn – Part I](https://www.geeksforgeeks.org/relational-plots-in-seaborn-part-i/)
# * [Relational plots in Seaborn – Part II](https://www.geeksforgeeks.org/relational-plots-in-seaborn-part-ii/)
#
# **There are different types of Relational Plots. We will discuss each of them in detail** –

# + [markdown] heading_collapsed=true hidden=true
# ### Relplot()  <a class="tocSkip">

# + [markdown] hidden=true
# This function provides us the access to some other different axes-level functions which shows the relationships between two variables with semantic mappings of subsets. It is plotted using the relplot() method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.relplot(x=None, y=None, data=None, **kwargs) 
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
# creating the relplot
sns.relplot(x='sepal_width', y='species', data=data)
 
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Scatter Plot   <a class="tocSkip">

# + [markdown] hidden=true
# The **scatter plot** is a mainstay of statistical visualization. It depicts the joint distribution of two variables using a cloud of points, where each point represents an observation in the dataset. This depiction allows the eye to infer a substantial amount of information about whether there is any meaningful relationship between them. It is plotted using the **scatterplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.scatterplot(x=None, y=None, data=None, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Line Plot <a class="tocSkip">

# + [markdown] hidden=true
# For certain datasets, you may want to consider changes as a function of time in one variable, or as a similarly continuous variable. In this case, drawing a line-plot is a better option. It is plotted using the **lineplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.lineplot(x=None, y=None, data=None, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.lineplot(x='sepal_length', y='species', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Categorical Plots <a class="tocSkip">

# + [markdown] hidden=true
# **Categorical Plots** are used where we have to visualize relationship between two numerical values. A more specialized approach can be used if one of the main variable is categorical which means such variables that take on a fixed and limited number of possible values. Refer to the below articles to get detailed information.
#
# * [Categorical Plots](https://www.geeksforgeeks.org/seaborn-categorical-plots/)
#  
# There are various types of categorical plots let’s discuss each one them in detail.

# + [markdown] heading_collapsed=true hidden=true
# ### Bar Plot   <a class="tocSkip">

# + [markdown] hidden=true
# A **barplot** is basically used to aggregate the categorical data according to some methods and by default its the mean. It can also be understood as a visualization of the group by action. To use this plot we choose a categorical column for the x axis and a numerical column for the y axis and we see that it creates a plot taking a mean per categorical column. It can be created using the [barplot()](https://www.geeksforgeeks.org/seaborn-barplot-method-in-python/) method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# barplot([x, y, hue, data, order, hue_order, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.barplot(x='species', y='sepal_length', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Count Plot   <a class="tocSkip">

# + [markdown] hidden=true
# A **countplot** basically counts the categories and returns a count of their occurrences. It is one of the most simple plots provided by the seaborn library. It can be created using the countplot() method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# countplot([x, y, hue, data, order, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.countplot(x='species', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Box Plot   <a class="tocSkip">

# + [markdown] hidden=true
# A boxplot is sometimes known as the box and whisker plot.It shows the distribution of the quantitative data that represents the comparisons between variables. boxplot shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution i.e. the dots indicating the presence of outliers. It is created using the boxplot() method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# boxplot([x, y, hue, data, order, hue_order, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.boxplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Violin Plot   <a class="tocSkip">

# + [markdown] hidden=true
# It is similar to the boxplot except that it provides a higher, more advanced visualization and uses the kernel density estimation to give a better description about the data distribution. It is created using the violinplot() method.
#

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# violinplot([x, y, hue, data, order, …]
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.violinplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Stripplot  <a class="tocSkip">

# + [markdown] hidden=true
# It basically creates a scatter plot based on the category. It is created using the stripplot() method.
#
#  

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# stripplot([x, y, hue, data, order, …])
# ```

# + [markdown] hidden=true
#  **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.stripplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Swarmplot   <a class="tocSkip">

# + [markdown] hidden=true
# Swarmplot is very similar to the stripplot except the fact that the points are adjusted so that they do not overlap.Some people also like combining the idea of a violin plot and a stripplot to form this plot. One drawback to using swarmplot is that sometimes they dont scale well to really large numbers and takes a lot of computation to arrange them. So in case we want to visualize a swarmplot properly we can plot it on top of a violinplot. It is plotted using the swarmplot() method.
#
#  

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# swarmplot([x, y, hue, data, order, …])
# ```
#

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.swarmplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Factorplot  <a class="tocSkip">

# + [markdown] hidden=true
#
#
# Factorplot is the most general of all these plots and provides a parameter called kind to choose the kind of plot we want thus saving us from the trouble of writing these plots separately. The kind parameter can be bar, violin, swarm etc. It is plotted using the factorplot() method.
#
#  

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# sns.factorplot([x, y, hue, data, row, col, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.factorplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Distribution Plots <a class="tocSkip">

# + [markdown] hidden=true
# **Distribution Plots** are used for examining univariate and bivariate distributions meaning such distributions that involve one variable or two discrete variables.
#  
# Refer to the below article to get detailed informaon about the distribution plots.
#
# * Distribution Plots
#  
# There are various types of distribution plots let’s discuss each one them in detail.

# + [markdown] heading_collapsed=true hidden=true
# ### Histogram   <a class="tocSkip">

# + [markdown] hidden=true
# A histogram is basically used to represent data provided in a form of some groups.It is accurate method for the graphical representation of numerical data distribution. It can be plotted using the **histplot()** function.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# histplot(data=None, *, x=None, y=None, hue=None,  **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.histplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Distplot   <a class="tocSkip">

# + [markdown] hidden=true
# **Distplot** is used basically for univariant set of observations and visualizes it through a histogram i.e. only one observation and hence we choose one particular column of the dataset. It is potted using the **distplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# distplot(a[, bins, hist, kde, rug, fit, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.distplot(data['sepal_width'])
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Jointplot   <a class="tocSkip">

# + [markdown] hidden=true
# Jointplot is used to draw a plot of two variables with bivariate and univariate graphs. It basically combines two different plots. It is plotted using the **jointplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# jointplot(x, y[, data, kind, stat_func, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.jointplot(x='species', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Pairplot   <a class="tocSkip">

# + [markdown] hidden=true
# **Pairplot** represents pairwise relation across the entire dataframe and supports an additional argument called hue for categorical separation. What it does basically is create a jointplot between every possible numerical column and takes a while if the dataframe is really huge. It is plotted using the **pairplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# pairplot(data[, hue, hue_order, palette, …])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.pairplot(data=data, hue='species')
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Rugplot   <a class="tocSkip">

# + [markdown] hidden=true
# **Rugplot** plots datapoints in an array as sticks on an axis.Just like a distplot it takes a single column. Instead of drawing a histogram it creates dashes all across the plot. If you compare it with the joinplot you can see that what a jointplot does is that it counts the dashes and shows it as bins. It is plotted using the **rugplot()** method.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# rugplot(a[, height, axis, ax])
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.rugplot(data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### KDE Plot   <a class="tocSkip">

# + [markdown] hidden=true
# **KDE Plot** described as **Kernel Density Estimate** is used for visualizing the Probability Density of a continuous variable. It depicts the probability density at different values in a continuous variable. We can also plot a single graph for multiple samples which helps in more efficient data visualization.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.kdeplot(x=None, *, y=None, vertical=False, palette=None, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("iris")
 
sns.kdeplot(x='sepal_length', y='sepal_width', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Regression Plots <a class="tocSkip">

# + [markdown] hidden=true
# The **regression plots** are primarily intended to add a visual guide that helps to emphasize patterns in a dataset during exploratory data analyses. Regression plots as the name suggests creates a regression line between two parameters and helps to visualize their linear relationships.
#
# Refer to the below article to get detailed information about the regression plots.
#
# * [Regression Plots](https://www.geeksforgeeks.org/seaborn-regression-plots/)
#  
# there are two main functions that are used to draw linear regression models. These functions are lmplot(), and regplot(), are closely reled to each other. They even share their core functionality.

# + [markdown] hidden=true
# ### lmplot   <a class="tocSkip">

# + [markdown] hidden=true
# **lmplot()** method can be understood as a function that basically creates a linear model plot. It creates a scatter plot with a linear fit on top of it.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.lmplot(x, y, data, hue=None, col=None, row=None, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("tips")
 
sns.lmplot(x='total_bill', y='tip', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ### Regplot   <a class="tocSkip">

# + [markdown] hidden=true
# regplot() method is also similar to lmplot which creates linear regression model.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.regplot( x,  y,  data=None, x_estimator=None, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("tips")
 
sns.regplot(x='total_bill', y='tip', data=data)
plt.show()

# + [markdown] heading_collapsed=true hidden=true
# ## Matrix Plots <a class="tocSkip">

# + [markdown] hidden=true
# ### Heatmap   <a class="tocSkip">

# + [markdown] hidden=true
# **Heatmap** is defined as a graphical representation of data using colors to visualize the value of the matrix. In this, to represent more common values or higher activities brighter colors basically reddish colors are used and to represent less common or activity values, darker colors are preferred. it can be plotted using the **heatmap()** function.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# seaborn.heatmap(data, *, vmin=None, vmax=None, cmap=None, center=None, annot_kws=None, linewidths=0, linecolor=’white’, cbar=True, **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("tips")
 
# correlation between the different parameters
tc = data.corr()
 
sns.heatmap(tc)
plt.show()

# + [markdown] hidden=true
# ### Clustermap   <a class="tocSkip">

# + [markdown] hidden=true
# The clustermap() function of seaborn plots the hierarchically-clustered heatmap of the given matrix dataset. Clustering simply means grouping data based on relationship among the variables in the data.

# + [markdown] hidden=true
# **Syntax:**

# + [markdown] hidden=true
# ```
# clustermap(data, *, pivot_kws=None,  **kwargs)
# ```

# + [markdown] hidden=true
# **Example:**

# + hidden=true
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
 
# loading dataset
data = sns.load_dataset("tips")
 
# correlation between the different parameters
tc = data.corr()
 
sns.clustermap(tc)
plt.show()
# -

# # More Gaphs in Seaborn

# * [Seaborn – Bubble Plot](https://www.geeksforgeeks.org/seaborn-bubble-plot/)
# * [Python – seaborn.residplot() method](https://www.geeksforgeeks.org/python-seaborn-residplot-method/)
# * [Python – seaborn.boxenplot() method](https://www.geeksforgeeks.org/python-seaborn-boxenplot-method/)
# * [Python – seaborn.pointplot() method](https://www.geeksforgeeks.org/python-seaborn-pointplot-method/)
# * [Python Seaborn – Catplot](https://www.geeksforgeeks.org/python-seaborn-catplot/)
# * [How to Make Countplot or barplot with Seaborn Catplot?](https://www.geeksforgeeks.org/how-to-make-countplot-or-barplot-with-seaborn-catplot/)
# * [How To Make Grouped Boxplot with Seaborn Catplot?](https://www.geeksforgeeks.org/how-to-make-grouped-boxplot-with-seaborn-catplot/)
# * [Python Seaborn – Strip plot illustration using Catplot](https://www.geeksforgeeks.org/python-seaborn-strip-plot-illustration-using-catplot/)
# * [How To Make Simple Facet Plots with Seaborn Catplot in Python?](https://www.geeksforgeeks.org/how-to-make-simple-facet-plots-with-seaborn-catplot-in-python/)
# * [How To Make Ridgeline plot in Python with Seaborn?](https://www.geeksforgeeks.org/how-to-make-ridgeline-plot-in-python-with-seaborn/)

# + [markdown] heading_collapsed=true
# # More Topics on Seaborn

# + [markdown] hidden=true
# * [Change Axis Labels, Set Title and Figure Size to Plots with Seaborn](https://www.geeksforgeeks.org/change-axis-labels-set-title-and-figure-size-to-plots-with-seaborn/)
# * [How To Place Legend Outside the Plot with Seaborn in Python?](https://www.geeksforgeeks.org/how-to-place-legend-outside-the-plot-with-seaborn-in-python/)
# * [How to Plot a Confidence Interval in Python?](https://www.geeksforgeeks.org/how-to-plot-a-confidence-interval-in-python/)
# * [Creating A Time Series Plot With Seaborn And Pandas](https://www.geeksforgeeks.org/creating-a-time-series-plot-with-seaborn-and-pandas/)
# * [How to Make a Time Series Plot with Rolling Average in Python?](https://www.geeksforgeeks.org/how-to-make-a-time-series-plot-with-rolling-average-in-python/)
# * [How To Add Regression Line Per Group with Seaborn in Python?](https://www.geeksforgeeks.org/how-to-add-regression-line-per-group-with-seaborn-in-python/)
# * [Data Visualization with Python Seaborn and Pandas](https://www.geeksforgeeks.org/data-visualization-with-python-seaborn-and-pandas/)
# * [Data Visualization in Python using Matplotlib and Seaborn](https://www.geeksforgeeks.org/data-visualization-in-python-using-matplotlib-and-seaborn/)
# * [Visualizing ML DataSet Through Seaborn Plots and Matplotlib](https://www.geeksforgeeks.org/visualizing-ml-dataset-through-seaborn-plots-and-matplotlib/)
