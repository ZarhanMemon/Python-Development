import matplotlib as mp

print( mp.__version__)

#-----------------------------------------

# Pyplot - provides a user friendly interface for ploting graph inside matplot.pyplot

import matplotlib.pyplot as plt


x = [ 2018 , 2019 , 2020 , 2021 , 2022]

y = [ 60 , 60 , 1000 , 100 , 80 ]

plt.plot(x,y)   # design the grpah -> ( x_axis coord , y_axis)

# plt.plot(y) -> one parameter , it take defaultly to Y_axis

plt.show()         #display grh

#---------------------------------------------

# Numpy + Plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([10 , 20 , 30 , 40])
y = np.array([43, 45 ,9 , 33])

plt.plot( x , y )
plt.show()


#-----------------------------------
# Create a graph of my mobile nos v/s year

mobile_nos = np.array([0 , 0 , 0 , 1 , 2 , 2 , 1])
year = np.array([ 2019 , 2020 , 2021 ,2022 ,2023 ,2024 , 2025])

plt.plot( year , mobile_nos)
plt.show()

#=========================================================

# Plot customization :

x = np.array([ 2021 , 2022 , 2023 ,2024 , 2025])

y1 = np.array([15 , 23 , 8 , 21 , 34])
y2 = np.array([33 , 43 , 24 , 5 , 6])
y3 = np.array([20 ,30 ,40 ,50 ,60])


plt.plot(x , y1 , marker="." ,
                 markersize=30,
                 markerfacecolor="red",  # hsl , rgb
                 markeredgecolor ="green",  # border of the marker,
                 
                 linestyle="dotted",         # dashdot -.- , None -noline
                 linewidth=4,
                 color="cyan"   
                 )   

plt.plot(x,y2 ,  marker="<" ,
                 markersize=20,
                 markerfacecolor="green",  # hsl , rgb
                 markeredgecolor ="blue",  # border of the marker,
                 
                 linestyle="dashdot",         # dashdot -.- , None -noline
                 linewidth=3,
                 color="red" )

#--------------------------------------------
 
# DICTIONARY function
line_style = dict(
                 marker="." ,
                 markersize=30,
                 markerfacecolor="red",  # hsl , rgb
                 markeredgecolor ="green",  # border of the marker,
                 
                 linestyle="dotted",         # dashdot -.- , None -noline
                 linewidth=4,
                #  color="cyan"  -> want to customize then remove from common style class 
)

plt.plot(x  , y2  , color="green"  ,**line_style)     # add inline style
plt.plot(x  , y1  , color="yellow" , **line_style )
plt.plot(x  , y3  , color="red"    ,**line_style)

plt.show()

# ================================================


# LABELS :   

x = np.array([ 2021 , 2022 , 2023 ,2024 , 2025])

y1 = np.array([15 , 23 , 8 , 21 , 34])
y2 = np.array([33 , 43 , 24 , 5 , 6])
y3 = np.array([20 , 30 ,40 , 40 ,  16])

#Graph title
plt.title(" CLASS Size",
          
          fontsize=30,         # style to title
          family="Arial",
          fontweight="bold",
          color="yellow",
          ); 

plt.xlabel(" Years (X-axis)" , fontsize=20 ,color="green")

plt.ylabel(" No of Student (Y-axis)" ,fontsize=20,color="red" )

plt.plot( x , y1 , color="orange")
plt.plot( x , y2 , color="blue")
plt.plot( x , y3 , color="green")


# NOTE :------------------------------------------

# You can see on X axis we have whole no are-> 2021 ,2022 ,..
#  ; but on graph it no are-> 2021 , 2021.5 , 2022 ,.. so to make it whole no only

plt.xticks(x)  # make fixed point as given

# Ticks styling:
plt.tick_params(axis="both" , colors="cyan" , size=10)


plt.show()


#===========================================


# GRID Lines :

# grid() -> Helps plots easier to read by adding references lines with X/Y axises.

x = np.array([1 ,2 ,3 ,4 ,5])
y = np.array([ 3 , 6 ,9 ,12 , 15])


plt.grid()         # Syntax

# plt.grid( axis="both" )  #- both reference axis drawn
# plt.grid( axis="x" )     #- X reference axis drawn
# plt.grid( axis="y" )     #- Y reference axis drawn


#Styling
plt.grid( axis="x",
          linewidth=3,
          color="red",
          linestyle="dotted"
         )

plt.plot(x , y)

plt.show()

#====================================================


# Bar Chart = compare categories of data by representing each category with a bar


catogaries = np.array(["Whole Grain" , "Vegetable" , "Fruits" ,"Protien" , "Dairy" , "Sweets"])
servings = np.array([ 11 , 5 , 4 ,3 ,3 , 1  ])

 
# normal barchart
plt.bar( catogaries , servings )     


# #-------------------------------------------

# Horizontal barchart and styling it :
plt.barh( catogaries, servings , color="green" )

plt.title("The Average Healty Food Plan" , size=23 , color="red")

plt.xlabel("Food Categories" )
plt.ylabel("Quantity")

#----------------------------------------------

# Bar Unique-Coloring  

letter = np.array([ 'A' ,'B' ,'C' ,'D'])

popularity = np.array([ 10 , 7 , 6 , 3])

colors =[ "red" , "yellow" , "grey" , "brown"]  # give diffrnt colr to each bar 

plt.bar( letter , popularity , color=colors)


#----------------------------------------------

# Bars Hatching ( designing) :

symbols = [ "." , "/" , "+" , "o" ]           # give diffrnt symbol to each bar ( x , | , O )

# single hatch - apply to all of x
plt.bar( letter , popularity , hatch= symbols[0])  

#--

# multi hatch - apply diffrnt to all of x
#             - make sure len of x_items == symbols
for i in range(0 ,len(symbols) ):
    plt.bar( letter[i] , popularity[i] , hatch = symbols[i])   # here we are selecting which bar so to apply symbols


#---------------------------------------------

# Bar Styling : edges , bar_size , tranceparency_bar , etc

# 1. Bar edges and linewidths
plt.bar(letter, popularity, color='lightgreen', edgecolor='black', linewidth=2)

# 2. Transparency (alpha) - makes bar transparent
plt.bar(letter, popularity , color='orange', alpha=0.6)

# 3. Different widths - makes bar lenght diffrnt
plt.bar(letter , popularity , color='purple', width=0.2)


#------------------------------------------------- 

plt.show()


#===============================================



# Bar Chart = Circular chart divided into slices to show percentages of total.
#             Good for visualizing distribution among categories


college_years = np.array(["1st year", "2sd year" , "3rd year" , "4th year"])

students_no = np.array([160 , 80 , 60 , 34])

colors = ["purple" , "aqua" , "orange" , "maroon"]


plt.pie( students_no ,             # Slices = area that year holds in pie
         labels=college_years ,    # Lables = the name of the years

        # 1. Autopct = assign the prcent of area that year hold in pie eg- 1st year -> 47.90% pie
         autopct="%1.2f",

        # 2. Explode = used to highlite the (4 years)-> hence explode= [0 , 0 , 0 , 0] means close pie ; 
        #              values below make unclosed pie
         explode= [0.2 , 0.5 , 0 , 0],   

        # 3. Shadow = gives a shadow effect to pie
         shadow= True ,                  

        # 4. Startangle = uses for rotating the pie in Degrees
         startangle= 270 ,  

         # 5. Colors = for unque coloring to slices        
         colors=colors
         ) 

plt.title("Pie Chart for College Years/student_no")

plt.show()
 

#=============================================




# Scatter graph = Shows the relationship btw 2 variables.
                #   Helps to identify a correlation( + , - , None)
                # Ex: Study hours vs. Test scores

study_hrs = np.array([0 , 4 ,2 ,7 , 1 ,3 ,8])

test_scrs = np.array([ 30 , 70 , 67 ,88 , 59 , 72 , 91])

plt.title("Student Marksheet Analysis - 12th")
plt.xlabel( "Studing Hours")
plt.ylabel("Marks")

plt.grid(axis="both")

plt.scatter( study_hrs , test_scrs ,
            
            color = "red",    # color of scter dots

            alpha = 0.3 ,      # transparency/opacity

            s = 200 ,           # size of scatter dots

            )

plt.show()

#---------------------------------------


# Labels - Index in Plt :-

#Class-10th A
x1 = np.array([0,2,3,1,8,5])
y1 = np.array([43 ,55 ,77 , 23,10 ,23])

#Class-10th B
x2 = np.array([6,4,2,5,8,5])
y2 = np.array([33 ,95 ,70 , 13,10 ,30])

plt.title("Student Marksheet Analysis - 10th")
plt.xlabel( "Studing Hours")
plt.ylabel("Marks")

plt.grid(axis="both")

plt.scatter( x1 ,y1 , 
             color="blue" , 
             s=200,
             label="Class A")# gives Class A for blue dots

plt.scatter( x2 ,y2 ,
             color="green" ,
             s=200,
             label="Class B" )  # gives Class B for green dots


# Index of graph :-  
plt.legend()

plt.show()


#=====================================================

# Histogram = A visual representation of the distribution of quantitive data.
#             They group values into bins (intervals eg: 10yrs-16yrs are childrens range)
#             and counts how many falls in each range.

# Eg: No of peaple in town = 100    --> Mostly seen is Statistic( tally table )
#     0yr  - 9yr  -> 0 people   
#     10yr - 16yr -> 20 people
#     17yr - 20yr -> 30 people
#     21yr - 80yr -> 40 people
#     81yr - 100+ -> 10 people
 

# -----------------------------
# Step 1: Generate Data
# -----------------------------

scores = np.random.normal(loc=80, scale=10, size=100)
# np.random.normal() creates random numbers following a "bell curve" (normal distribution).
# loc = mean (average score expected)
# scale = standard deviation (spread of scores around the mean)
# size = number of students (100 scores)


# np.clip() ensures scores stay between 0 and 100
scores = np.clip(scores, 0, 100)



# -----------------------------
# Step 2: Plot Histogram
# -----------------------------

plt.hist(scores, bins=10, color="yellow", edgecolor="black")
# plt.hist() groups scores into bins (intervals) and counts how many fall in each bin.
# bins=10 → divide 0–100 into 10 equal ranges (0–10, 10–20, …, 90–100)
# color → fill color of bars
# edgecolor → outline color of bars

 
plt.title("Exam Scores")           
plt.xlabel("Score")               
plt.ylabel("Number of Students")  

 
plt.show()

#Note: no of BIN/intervals = no of Bars in plt

#----------------------------------------------------------
# Create histogram for 50 student and thier hiegth 
# from 120->200cm range (average = 160cm)

hieghts = np.random.normal( loc=160 ,  size=50 , scale=10)

hieghts = np.clip( hieghts , 120 ,200)

plt.hist( hieghts , bins= 10 , color="lightgreen" , edgecolor="black")

plt.title("Student Height distribution in 50 student class")
plt.xlabel("Hieght(cm) Groups")
plt.ylabel("Student no in the height group")

plt.show()


#=============================================================


# Sub-Plot:

# Figure = the entire canvas
# Ax = a single plot (subplot)


#print(plt.subplots(2,2))   #-> array of mini-plts

#----------------------



figure , axes = plt.subplots(2,2)
# axes => array of subplots


x0 = np.array([1 , 2, 3, 4])
x1 = np.array([3 , 4, 6, 4])

y0 = np.array([2, 4 , 6 ,8])
y1 = np.array([1 ,3, 5 , 7])

# axes[ ] = plt

# axes[ 00  01 ]
#     [ 10  11 ]

# 1. [0 ,0] --> Draws in upper-left sub-plot 
axes[0 , 0].plot( x0 , y0 , color="blue")
axes[0 , 0].set_title("Graph-1")

# 2. [0 ,1] --> Draws in upper-right sub-plot :
axes[0 , 1].plot( x0 , y1 , color="green")
axes[0 , 1].set_title("Graph-2")

# 3. [1 ,0] --> Draws in lower-left sub-plot :
axes[1 , 0].scatter( x1 , y0 , color="red")
axes[1 , 0].set_title("Graph-3")

# 4. [1 ,1] --> Draws in lower-right sub-plot :
axes[1 , 1].bar( x1 , y1 , color="yellow")
axes[1 , 1].set_title("Graph-4")


plt.tight_layout() # -> add some gaps btw sub-plot
plt.show()


#===========================================
