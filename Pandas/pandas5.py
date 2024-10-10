'''
Read CSV in Python Pandas
One of the major benefits of working on Python is the ease of reading and accessing CSV (comma-separated files). For this, Python has the Pandas library. In this lesson, we will learn how to read CSV in Python Pandas using the read_csv() method.

Let’s say we have the following CSV file Students.csv:'''

import pandas as pd

df = pd.read_csv(r'C:\Users\asus\Desktop\studentNew.csv')
print(df)

print('top n rows\n',df.head())
print('top 3 rows\n',df.head(3))

print('bottom n rows:\n',df.tail())
print('bottom 3 rows:\n',df.tail(3))


'''Read Excel in Python Pandas
To read an Excel file in Python, we use the Pandas
read_excel() method. First, install the openpyxl 
package using pip. Type the following command to install 
openpyxl:'''
# How to read and use excel data in python 
# input Excel file 
# Local excel in the DataFrame 
df = pd.read_excel(r"C:\Users\asus\Desktop\Data\Python\Pandas\cricket.xlsx")
print('excel file:\n',df)
'''
excel file:
       Player  points  rank
0       John       9     1
1        Dev       8     2
2       Alex       7     3
3       Cost       7     4
4      Divid       6     5
5      Gimmy       5     6
6       wlid       4     7
7       Walt       3     8
8  speedrush       2     9
9      truck       1    10'''

# head and tail function in python 
print('top n rows in df:',df.head())
print('top 10 rows in df:',df.head(10))
print('top 7 rows in df:',df.head(7))

# now we are using tail funciton in dataFrame 
print('top n rows form the bottom:\n',df.tail())
print('top 3 rows form the bottom:\n',df.tail(3))
print('top 7 rows form the bottom:\n',df.tail(7))


''' Indexing in Pandas 
In this lesson, we will learn how Indexing works in 
Pandas. We can easily index and select data in Pandas.

Indexing
Indexing means selecting specific rows and columns of data from DataFrame. A DataFrame includes columns, index, and data. Let us see some examples:

Indexing in Pandas using the indexing operator
Indexing in Pandas using loc[]
Indexing in Pandas using iloc[]
Indexing in Pandas using the indexing operator'''   

# 1. using index operator 

df = pd.read_csv(r'C:\Users\asus\Desktop\studentNew.csv', index_col='Student')
print(df['Marks'])
# print(df['Rank'])
'''Student
John     90
Alex     89
Alice    78
David    97
Dev      78'''

# 2. loc operator
df = pd.read_csv(r'C:\Users\asus\Desktop\studentNew.csv', index_col='Student')
res = df.loc['John']
print('loc res:\n',res)
'''
loc res:
 Rank      2
Marks    90
Name: John, dtype: int64'''

# 3. iloc operator:
res = df.iloc[2]
print('iloc res:\n',res)
'''
iloc res:
 Rank      4
Marks    78
Name: Alice, dtype: int64'''



'''
Select multiple columns in a Pandas DataFrame
In Python, easily select multiple columns in a Pandas DataFrame. You can select more than one column without using built-in functions. More than two columns can also be selected in a range. In this lesson, learn how to:

Select two columns
Select multiple columns in a range
Select two columns
To select two specific columns from a Pandas DataFrame, mention the column names. Do not mention the column names you don’t want to display:

dataFrame[['Rank', 'Marks']]'''

# selecting two columns
newdata = {
    'student': ['John','David','Isha','Alex','carrin'],
    'marks': [22,23,24,25,26],
    'rank':[1,2,3,4,5]
}

df = pd.DataFrame(newdata)

print('selecting multiple column:\n',df)
print('print two column tughter:\n',df[['marks','rank']])
'''selecting multiple column:
   student  marks  rank
0    John     22     1
1   David     23     2
2    Isha     24     3
3    Alex     25     4
4  carrin     26     5
print two column tughter:
    marks  rank
0     22     1
1     23     2
2     24     3
3     25     4
4     26     5'''


# selecting multiple columns 
newdata = {
    'student': ['John','David','Isha','Alex','carrin'],
    'marks': [22,23,24,25,26],
    'rank':[1,2,3,4,5],
    'ID': ['S01','S02','S03','S04','S05'],
    'rollno': ['101','102','103','104','105'],
    'section':['A','B','C','D','E']
}

df = pd.DataFrame(newdata)
print('This is new data:\n',df)

print('using columns range:\n',df[df.columns[2:5]])
'''using columns range:
    rank   ID rollno
0     1  S01    101
1     2  S02    102
2     3  S03    103
3     4  S04    104
4     5  S05    105'''









