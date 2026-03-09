import seaborn as sb;
import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np


# SEABORN : = a tool in Python that helps you turn data into beautiful, easy-to-read charts.

# - A Python library for making graphs.
# - It makes charts look nice and easy to understand.
# - Built on: Matplotlib (another graph library).
# - Best for: Showing patterns in data (like trends, comparisons, or relationships).
# - Common charts: Heatmaps, bar plots, scatter plots, line plots.


# Matplotlib = like drawing a picture from scratch (you control every detail).

# Seaborn = like using a photo filter app (it makes things look good automatically)



df = pd.DataFrame({
    "year" : ["1949" ,"1949","1949","1949","1949","1949"],
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "passengers": [120, 150, 170, 160, 180, 200]
})


# graph - M : without the labeling
plt.plot( df["month"] , df["passengers"])
plt.show()

# graph - S : with the labeling
sb.lineplot( x="month" , y="passengers" , data=df)
plt.show()


#=========================================================================


sb.set_theme(style='darkgrid')

x = np.array([0 , 2, 4,5,6,10 ,34,55])
y = np.sin(x)  # sin (0) = 0


sb.lineplot(x = x , y =y)

plt.title("Line graph")
plt.show


#===================================================================


# Built-in Seaborn Datasets

sb.get_dataset_names()  # give the name of uilt-in seaborn dataframe/sets



#------------------------

# Fetching specific dots dataframe from seaborn

tips = sb.load_dataset('tips')   


# Get the first 5 rows
tips.head()          

# Get the summary of dataframe 
tips.info()


#==================================================================


# Type of Plot :




# 1.   Line plot

sb.lineplot( x = 'tip' , y='total_bill' , data=tips)


plt.title(" 1.)  Line Plot ")

plt.show()


#---------------------

# 2.  Scatter plot

sb.scatterplot( x = 'tip' , y='total_bill' , data=tips , hue='day')  # hue = { any cols }


plt.title(" 2.  Scatter Plot - by with Color by Day")

plt.show()


#---------------------

# 3.   Bar plot

sb.barplot( x = 'tip' , y='total_bill' , data=tips)  


plt.title(" 3.  Bar Plot ")

plt.show()

#--------------------

# 4.   Box plot

sb.boxplot( x='day' , y='total_bill' , data=tips )

plt.title("4.  Box plot")

plt.show()

#-----------------------


# Piviot table from Dataframe:

flights = sb.load_dataset('flights')

pivot_table = flights.pivot_table( index='month' , columns='year' , values='passengers')

# - Rows = months (index='month')
# - Columns = years (columns='year')
# - Values = number of passengers (values='passengers')
# - Result: A matrix with months as rows and years as columns.


print(pivot_table)

#----

# 5.  Heatmap - pivot

sb.heatmap( data=pivot_table , annot=True , fmt=".0f" , cmap='YlGnBu')

# - data=piviot_table: Uses the pivot table as input.
# - annot=True: Displays the actual passenger numbers inside each cell.
# - fmt="d": Formats annotations as integers.
# - cmap='YlGnBu': Color scheme (Yellow → Green → Blue).


plt.title("5.  Heatmap - with Piviot_table")

plt.show()


#===========================================================


# Working with Pandas df 

import pandas as pd


df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56, 55, 60, 34, 43],
    "salary": [25000, 27000, 52000, 60000, 58000, 62000, 61000, 65000, 38000, 45000],
    "gender": ["M", "F", "M", "F", "F", "M", "M", "F", "F", "M"]
})


sb.scatterplot( data= df , x='age' , y='salary' , hue='gender')

plt.show()






# Feature     	           Matplotlib    Seaborn
# Default Styles	         Basic	     Beautiful
# Syntax Level	             Low	       High
# Works with DataFrames    	 Manual	       Easy
# Plotting Complex Graphs    Tedious	 Very Easy



# Seaborn makes data visualization faster, prettier, and smarter.
# You should still know Matplotlib basics (for fine-tuning plots).
# In real-world Data Science, we usually start with Seaborn, and customize with Matplotlib.




#==========================================================================



# Adding the count on Bars 

ax = sb.countplot( data= tips , x='sex' ,  hue='sex')    # ax - object of the bars x

# Iterate over all containers(bars) and add labels
for container in ax.containers:
    ax.bar_label(container)

plt.show()