'''Find and Remove Duplicates from rows in Pandas
To find and remove duplicates from rows in a Pandas DataFrame or Series,
use the duplicated() and drop_duplicates() method respectively.

Find Duplicates
To find duplicates from rows in a Pandas DataFrame or Series, use the
duplicated() method. It returns a Series with True and False values 
i.e. for duplicate rows True is returned.'''

import pandas as pd 
data = {
    'student': ['alex','alice','alex','john','wildfire'],
    'rollno': [101,103,101,104,105],
    'rank':[1,2,1,5,4]
}

df = pd.DataFrame(data)
print(df)

res = df.duplicated()
print('is therer any duplicate value:\n',res)

# remove the duplicate value
res = df.drop_duplicates()
print('after removing duplicate values:\n',res)
'''    student  rollno  rank
0      alex     101     1
1     alice     103     2
2      alex     101     1
3      john     104     5
4  wildfire     105     4
is therer any duplicate value:
 0    False
1    False
2     True
3    False
4    False
dtype: bool

Removeing duplicates values
after removing duplicate values:
     student  rollno  rank
0      alex     101     1
1     alice     103     2
3      john     104     5
4  wildfire     105     4'''


# Load the CSV file using double backslashes in the path
# Specify the encoding if utf-8 fails
df = pd.read_csv(r'C:\Users\asus\Desktop\Data\Python\Pandas\newDataCLeaningFile.csv')

print(df)

# find the null values and replace with true 
res = df.isnull()
print('Find the null values:\n',res.to_string() )


# now we are replace the not null values with true and null values with false 
res = df.notnull()
print('notnull values with true:\n',res)

# find null values and delete the entire row 
res = df.dropna()
print('drop null values:\n',res)

# fillna method used to replace null values with specific values 
res = df.fillna(111)
print('after using fillna(111):\n',res)
'''
   Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1     NaN
3        1.2    45.9
4        2.9    19.3
5        4.5    23.3
6        8.3     NaN
7        7.9    66.3
8        8.3    74.7
9        5.8    67.5
Find the null values:
    Frequency  Points
0      False   False
1      False   False
2      False    True
3      False   False
4      False   False
5      False   False
6      False    True
7      False   False
8      False   False
9      False   False

notnull values with true:
    Frequency  Points
0       True    True
1       True    True
2       True   False
3       True    True
4       True    True
5       True    True
6       True   False
7       True    True
8       True    True
9       True    True

drop null values:
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
3        1.2    45.9
4        2.9    19.3
5        4.5    23.3
7        7.9    66.3
8        8.3    74.7
9        5.8    67.5 

after using fillna(111):
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1   111.0
3        1.2    45.9
4        2.9    19.3
5        4.5    23.3
6        8.3   111.0
7        7.9    66.3
8        8.3    74.7
9        5.8    67.5'''


