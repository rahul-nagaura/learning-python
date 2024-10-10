'''Pandas – Statistical Functions
In this lesson, we will work around statistics operations using the statistical functions in Python Pandas.  It can be applied to a Series or DataFrame.

sum(): Return the sum of the values.
count(): Return the count of non-empty values.
max(): Return the maximum of the values.
min(): Return the minimum of the values.
mean(): Return the mean of the values.
median(): Return the median of the values.
std(): Return the standard deviation of the values.
describe(): Return the summary statistics for each column.'''


import pandas as pd 
data = {
    'maths':[98,89,99,85,78],
    'english':[90,97,98,95,88],
    'ssc':[80,88,98,58,87],
}

df = pd.DataFrame(data)
print(df.sum())
'''maths      449
english    468
ssc        411'''

print('count:\n',df.count())
print('max:\n',df.max())
print('min:',df.min())
print('mean:',df.mean())
print('median:',df.median())
print('std:',df.std())
print('std:',df.std())
print('describe:\n',df.describe())


'''Pandas – Plotting
To plot in Pandas, we need to use the plot() method and the Matplotlib library. The pyplot module from Matplotlib is also used for plotting in Pandas. The pyplot.show() is used to display the figure.'''

import pandas as pd
import matplotlib.pyplot as plt

# Dataset
dataset = {
    'temp': [18, 20, 24, 22, 38, 26, 30, 34, 32, 24],
    'humidity': [32, 36, 38, 40, 22, 28, 44, 30, 40,32],
    'wind': [12, 20, 9, 8, 26, 29, 28, 34, 11, 12],
    'precipitation': [17, 37, 36, 45, 23, 23, 35, 74, 38, 34]
}

# Creating a DataFrame from the dataset
df = pd.DataFrame(dataset)

# Plotting the dataset
# df.plot()
# plt.show()
# Displaying the plot

# df['humidity'].plot(kind='hist')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt




# Extended dataset with 10 rows
data = {
    'temp': [18, 20, 24, 22, 38, 26, 30, 34, 32, 24],
    'humidity': [32, 36, 38, 40, 22, 28, 44, 30, 40, 42],
    'wind': [12, 20, 9, 8, 26, 29, 28, 34, 11, 12],
    'precipitation': [17, 37, 36, 45, 23, 23, 35, 74, 38, 34]
}

# Create a DataFrame with 10 rows and 10 index labels
df = pd.DataFrame(data, index=['city1', 'city2', 'city3', 'city4', 'city5', 'city6', 'city7', 'city8', 'city9', 'city10'])

# Plot a pie chart for the 'humidity' column
df.plot.pie(y='humidity', autopct='%1.1f%%')

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Extended dataset with 10 rows
data = {
    'temp': [18, 20, 24, 22, 38, 26, 30, 34, 32, 24],
    'humidity': [32, 36, 38, 40, 22, 28, 44, 30, 40, 42],
    'wind': [12, 20, 9, 8, 26, 29, 28, 34, 11, 12],
    'precipitation': [17, 37, 36, 45, 23, 23, 35, 74, 38, 34]
}

# Create a DataFrame with 10 rows and 10 index labels
df = pd.DataFrame(data, index=['city1', 'city2', 'city3', 'city4', 'city5', 'city6', 'city7', 'city8', 'city9', 'city10'])

# Create a scatter plot for temperature vs. humidity
plt.figure(figsize=(10, 6))
plt.scatter(df['temp'], df['humidity'], color='blue', s=100, alpha=0.6, edgecolors='black')
plt.title('Scatter Plot of Temperature vs. Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')

# Add grid and show plot
plt.grid()
plt.show()


df.plot.area()
plt.show()


