'''Pandas – Group the Data
In this lesson, we will learn how to group data in a DataFrame and perform operations on it. First, we will split the data into groups, then we will iterate through the groups and then display the groups. Let us see what we will cover:

Split the object and combine the result
Iterate the Group
View the Group
Perform Aggregation Operations on Groups
Pandas – Split the object and combine the result
The groupby() method is used in Pandas to split the object. We can define groupby() as grouping the rows/columns into specific groups.'''
import numpy as np
import pandas as pd 
data = {
    'players': ['Amit','John','Rohan','Alice','John','Amit','david'],
    'rank':[1,2,3,4,5,6,7],
    'year':[2011,2021,2024,2022,2019,2003,2023]
}

df = pd.DataFrame(data)
print('DataFrame:\n',df)

dfg = df.groupby('players')
print('after group by according to the player:\n',dfg.first())
'''DataFrame:
   players  rank  year
0    Amit     1  2011
1    John     2  2021
2   Rohan     3  2024
3   Alice     4  2022
4    John     5  2019
5    Amit     6  2003
6   david     7  2023
after group by according to the player:
          rank  year
players
Alice       4  2022
Amit        1  2011
John        2  2021
Rohan       3  2024
david       7  2023'''

for name, group in dfg:
    print('\n',name)
    print(group)

# View the Group --> Use the groups property in Python Pandas to view the group.
print(dfg.groups)
'''{'Alice': [3], 'Amit': [0, 5], 'John': [1, 4], 'Rohan': [2], 'david': [6]}'''




data = {
    'players': ['Amit','John','Rohan','Alice','John','Amit','david'],
    'rank':[1,2,3,4,5,6,7],
    'year':[2011,2021,2024,2022,2019,2021,2023],
    'points': [45,75,97,96,65,87,97]
}

df = pd.DataFrame(data)
# use the groupby() to group  
groupRes = df.groupby('year')

# use agg() for aggregation 
# Find the mean of the points
print('mean:',groupRes['points'].agg(np.mean))
'''mean: year
2011    45.0
2019    65.0
2021    81.0
2022    96.0
2023    97.0
2024    97.0'''

data = {
    'players': ['Amit','John','Rohan','Alice','John','Amit','david'],
    'rank':[1,2,3,4,5,6,7],
    'year':[2011,2021,2024,2022,2019,2021,2011],
    'points': [45,75,97,96,65,87,97]
}

df = pd.DataFrame(data)
# use the groupby() to group  
groupRes = df.groupby('year')
print('size of the group:\n',groupRes.agg(np.size))
'''size of the group:
       players  rank  points
year
2011        2     2       2
2019        1     1       1
2021        2     2       2
2022        1     1       1
2024        1     1       1'''








