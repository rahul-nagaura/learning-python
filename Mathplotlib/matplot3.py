'''Matplotlib – Bar Graph
To plot a bar graph in Matplotlib, use the bar() method. Let us see an example wherein we will plot a  bar graph for student and student marks:'''

'''import matplotlib.pyplot as plt
import numpy as np

student = np.array(['john','rohan','alice','alex','joe','rehana'])
marks = np.array([45,86,34,97,54,69])

# plot a bar graph 
plt.bar(student,marks)


plt.xlabel('student name')
plt.ylabel('student marks')

plt.title('student result')
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np

# Defining the cricketer names and their corresponding runs scored
cricketer = np.array(['john', 'alice', 'max', 'alex', 'reh'])
runs = np.array([57, 76, 59, 76, 72])

# Creating a pie chart
plt.pie(runs, labels=cricketer, autopct='%1.2f%%')

# Adding a title to the pie chart
plt.title('Runs Scored in Matches')

# Displaying the pie chart
plt.show()
'''


# how to create a line graph
'''import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,8,14,20,26])
b = np.array([20,40,50,20,60])

plt.plot(a,b)
plt.title('Line chart')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.show()'''

# How to create a histogram 
'''Matplotlib – Histogram
To plot a histogram, in Matplotlib, use the hist() method. Let us see an example wherein we will plot a Histogram of scores by cricket players. In the example, we have set the following bins:

'''
import matplotlib.pyplot as plt
import numpy as np
 
# Data to plot
arr = np.array([10, 50, 34, 67, 21, 7, 59, 62, 45, 48, 10, 8, 41, 32, 66, 59, 18, 26, 51, 9])
 
# Plot a Histogram using pyplot.hist() method
# The bins parameter sets the bin i.e. an integer or sequence
plt.hist(arr, bins = [0, 20, 40, 60, 80])
 
# The labels for x-coordinate and y-coordinate
plt.xlabel("Score")
plt.ylabel("Player")
 
# Display the figure
plt.show()


'''Matplotlib – Scatter Plot
To draw a scatter plot in Matplotlib, use the scatter() method. Let us see an example wherein we will use the data of the score of two cricket teams. The range set is the score range of lower order batsman:'''


 
import matplotlib.pyplot as plt
 
# Data to plot
# Score of two Teams
team1_Score = [25, 47, 34, 38, 27, 40, 42, 18]
team2_Score = [7, 22, 40, 29, 27, 10, 19, 31]
 
# Score Range of tailenders (lower order batsman) in Cricket
scoreRange = [5, 10, 15, 20, 25, 30, 35, 40]
 
# Plot a Scatter Plot using pyplot.scatter() method
plt.scatter(team1_Score, scoreRange, color='r')
plt.scatter(team2_Score, scoreRange, color='b')
 
# The labels for x-coordinate and y-coordinate
plt.xlabel("Team Score")
plt.ylabel("Score Range")
 
# Display the figure
plt.show()


