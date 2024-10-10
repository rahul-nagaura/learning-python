'''Add a new column to Pandas DataFrame
In this lesson, we will learn how to add a new column to Pandas DataFrame in Python. We will insert a column to an already created DataFrame. Let us see various ways to achieve this:

1. Add a new column using the insert() method(set the location)
2. Assign a new column using the assign() method(place at the end)'''

import pandas as pd
dataFrame = {
    'student': ['ALice','David','Lusi','Alex','Emmly'],
    'Id': ['S01','S02','S03','S04','S05'],
    'marks': [97,94,92,89,87]
}

# print(dataFrame)
df = pd.DataFrame(dataFrame)
print(df)

newCol = df.insert(2,'rank',[1,2,3,4,5])
print('After adding new newCol:\n',df)

'''  student   Id  marks
0   ALice  S01     97
1   David  S02     94
2    Lusi  S03     92
3    Alex  S04     89
4   Emmly  S05     87
After adding new newCol:
   student   Id  rank  marks
0   ALice  S01     1     97
1   David  S02     2     94
2    Lusi  S03     3     92
3    Alex  S04     4     89
4   Emmly  S05     5     87'''


newCol2 = df.assign(roll = [101,102,103,104,105])
print('using assign operator:\n',newCol2)
'''using assign operator:
   student   Id  rank  marks  roll
0   ALice  S01     1     97   101
1   David  S02     2     94   102
2    Lusi  S03     3     92   103
3    Alex  S04     4     89   104
4   Emmly  S05     5     87   105'''


'''Delete rows/ columns in a Pandas DataFrame
The drop() method is used in Python to delete rows/ columns in a Pandas DataFrame. It is used to remove a particular row or column. Under the parameters of the drop() method, mention the column you want to delete with the axis.

We will now see two examples:

Drop columns
Drop rows'''


data = {
    'student': ['Alice','John','Marry','Alex','Devid'],
    'rollno': [101,102,103,104,105],
    'ID': ['S01','S02','S03','S04','S05',],
    'marks': [99,86,75,65,54],
    'rank':[1,2,3,4,5]
}

df1 = pd.DataFrame(data)
print('data:\n',df1)
# axis='columns' or axis=1 provide the same result 

res = df1.drop(labels ="rollno",axis='columns')
print('after drop roll no column:\n',res)


resrow = df1.drop(labels=2,axis=0)
print('after deleting a row:\n',resrow)

'''data:
   student  rollno   ID  marks  rank
0   Alice     101  S01     99     1
1    John     102  S02     86     2
2   Marry     103  S03     75     3
3    Alex     104  S04     65     4
4   Devid     105  S05     54     5
after drop roll no column:
   student   ID  marks  rank
0   Alice  S01     99     1
1    John  S02     86     2
2   Marry  S03     75     3
3    Alex  S04     65     4
4   Devid  S05     54     5
after deleting a row:
   student  rollno   ID  marks  rank
0   Alice     101  S01     99     1
1    John     102  S02     86     2
3    Alex     104  S04     65     4
4   Devid     105  S05     54     5'''

'''Iterate over rows and columns in a Pandas DataFrame
In this lesson, we will learn how to iterate over rows and columns in a Pandas DataFrame. Let’s see examples of how to:

1. Iterate over rows
2. Iterate over columns
Iterate over rows
To iterate over the rows, use the following methods in Pandas:

    -->iterrows(): To Iterate over the rows
    -->itertuples(): To Iterate over the rows'''

for row in df1.iterrows():
    print(row)

print('using tuples method')
for row in df1.itertuples():
    print(row)

print('iterate over columns in a df')
for a,b in df1.items():
    print(a)
    print(b)

'''Sorting in Pandas
To sort the data in Pandas, we can use various methods. In this lesson, we will see how to sort the DataFrame in Pandas using the sort_values() method. Let us first see some examples:

1. Sort the Pandas DataFrame (default ascending order)
2. Sort the Pandas DataFrame in Descending Order
Sort the Pandas DataFrame (default ascending order)
To sort the dataframe, use the sort_values() method. The default is ascending. Therefore, you don’t need to mention any value in the parameter for ascending sort.

We will sort by value i.e. the by parameter will be set to the column name by which we need to sort the DataFrame in ascending'''

sdata  = {
    'student': ['Alex','alice','john','marry','david'],
    'rollno': [103,102,105,104,101],
    'marks': [45,67,43,90,78],
    'rank': [5,3,4,1,2]
}


df = pd.DataFrame(sdata)
print(df)

print('we are arrange the data in ascending order wrt rank')
res = df.sort_values(by='rank')
print(res)

'''  student  rollno  marks  rank
0    Alex     103     45     5
1   alice     102     67     3
2    john     105     43     4
3   marry     104     90     1
4   david     101     78     2
we are arrange the data in ascending order wrt rank
  student  rollno  marks  rank
3   marry     104     90     1
4   david     101     78     2
1   alice     102     67     3
2    john     105     43     4
0    Alex     103     45     5

we are arrange the data in decending order wrt rollno
  student  rollno  marks  rank
2    john     105     43     4
3   marry     104     90     1
0    Alex     103     45     5
1   alice     102     67     3
4   david     101     78     2'''
print('we are arrange the data in decending order wrt rollno')
res = df.sort_values(by='rollno',ascending=False)
print(res);







