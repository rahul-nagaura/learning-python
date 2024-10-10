'''Matplotlib is an open-source plotting library developed by John D. Hunter. 
Create interactive visualizations in Python with Matplotlib. 
It is built on NumPy and is one of the most popular libraries 
for data visualization in Python.

In this tutorial, we will learn how to perform plotting with Python. 
Visualizations are far better than textual data. Using matplotlib, 
we can easily create graphs, histograms, bar graphs, etc.

Features
The following are the features of Matplotlib:

Free and open-source Python library
Load and plot the data easily
Easily Make interactive figures that can zoom, pan, update.
Export to various file formats, such as PNG, PDF, SVG, etc.
Use third-party packages built on Matplotlib for plotting, animations, styles, etc.
'''

# import matplotlib.pyplot as plt 
# 1. first code
'''xpnts = [0,24]
ypnts = [0,125]
plt.plot(xpnts,ypnts)
plt.show()'''

'''
import pandas as pd 

data = {
    'criket_bat': ['SG','CG','MG','HG','JG','MG','KG','AG','OG','LG'],
    'mrp': [1100,1200,1300,1400,1500,1600,1700,1800,1900,2000],
    'weight': [300,350,400,450,200,550,600,650,1700,750]
}

df = pd.DataFrame(data)
print(df)

plt.plot(df['mrp'],df['weight'])
plt.grid()
# plt.show()

# How to add labels to a plot 
plt.xlabel('Bat Price')
plt.ylabel('Bat weight (grams)')

#  how to add title to a plot and change the position
plt.title('Bat Menu')
# plt.title('Bat Menu', loc='right')
# plt.title('Bat Menu',loc='left')



plt.show()'''



# 2
import matplotlib.pyplot as plt
import numpy as np

# Data 
a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]

# Create plots 
fig = plt.figure()
ax = plt.subplot()

# Plotting the data with corrected format strings
ax.plot(a, b, 'k--', label='Frequency')  # Black dashed line
ax.plot(a, c, 'k:', label='Periods')      # Black dotted line

# Create a legend using the Matplotlib Axis legend() method 
# ax.legend()

# position legend 
l =ax.legend(loc='upper left')
# ax.legend(loc='upper center')
# ax.legend(loc='upper right')
# same for lower 

# How to change the background of label
l.get_frame().set_facecolor('purple')

# how to cahnge the font size of lagend 
''''''

# Plot title 
plt.title('Frequency of Signal')

# Show plot 
plt.show()











