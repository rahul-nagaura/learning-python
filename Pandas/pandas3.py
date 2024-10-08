'''Join Pandas DataFrame
In Python, we can easily join Pandas DataFrames using the join() method. This will join the columns of two different DataFrames.

Let us see an example and create two DataFrames and join them:'''


import pandas as pd
 
# Dataset
data1 = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'roll': [101, 102, 103, 104, 105]
}
data2 = {
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
# DataFrame
dataFrame1 = pd.DataFrame(data1)
print("DataFrame1 =\n",dataFrame1)
dataFrame2 = pd.DataFrame(data2)
print("\nDataFrame2 =\n",dataFrame2)
 
# Join two DataFrames
resDF = dataFrame1.join(dataFrame2)
print("\nJoining DataFrames =\n",resDF)
'''Joining DataFrames =
     id student  roll  rank  marks
0  S01    Amit   101     1     95
1  S02    John   102     4     70
2  S03   Jacob   103     3     80
3  S04   David   104     5     60
4  S05   Steve   105     2     90 '''


'''Concatenate Pandas DataFrames
In this lesson, learn to concatenate Pandas DataFrames in Python using the concat() method. This will concatenate the content of the DataFrames.
'''

import pandas as pd
print('\nconcatenate\n')
# Dataset
data1 = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'roll': [101, 102, 103, 104, 105]
}
data2 = {
  'id': ["S06", "S07", "S08"],
  'student': ["Ben", "Kane", "Rohit"],
  'roll': [106, 107, 108]
}
 
# DataFrame
dataFrame1 = pd.DataFrame(data1, index=[0, 1, 2, 3, 4])
print("DataFrame1 =\n",dataFrame1)
dataFrame2 = pd.DataFrame(data2, index=[5, 6, 7])
print("\nDataFrame2 =\n",dataFrame2)
 
# Concatenating two DataFrames
resDF = pd.concat([dataFrame1, dataFrame2])
print("\nConcatenating DataFrames =\n",resDF)

'''
concatenate

DataFrame1 =
     id student  roll
0  S01    Amit   101
1  S02    John   102
2  S03   Jacob   103
3  S04   David   104
4  S05   Steve   105

DataFrame2 =
     id student  roll
5  S06     Ben   106
6  S07    Kane   107
7  S08   Rohit   108

Concatenating DataFrames =
     id student  roll
0  S01    Amit   101
1  S02    John   102
2  S03   Jacob   103
3  S04   David   104
4  S05   Steve   105
5  S06     Ben   106
6  S07    Kane   107
7  S08   Rohit   108'''


data = [10,20,30,40,50]
s = pd.Series(data)
print('Series\n',s)
'''Series
 0    10
1    20
2    30
3    40
4    50'''

'''Access a value from a Pandas Series'''
data1 = [10,12,24,25,26,22,34]
x = pd.Series(data1)
print('Series ele:',x[2]) #Series ele: 30


# Name your own indexes in a Pandas Series
data1 = [10,12,24,25,26]
y = pd.Series(data1,index=['rowA','rowB','rowC','rowD','rowE'])
print(y)
'''Series ele: 24
rowA    10
rowB    12
rowC    24
rowD    25
rowE    26
dtype: int64'''

# Access a value from a Pandas Series with labels
# If you have set the custom index for labels as shown above, then accessing any value from the Series is quite easy. Refer to the label and that’s it.
print('rowA',y['rowA']) #rowA 10



'''Pandas Series – Attributes and Methods 
The Series in Pandas is a one-dimensional array that uses the Series() method to create a Series, but it also uses different built-in attributes and methods for basic functionalities. In this lesson, let us see such attributes and methods in Python Pandas for Series:
dtype: Return the dtype.
ndim: Return the Number of dimensions
size: Return the number of elements.
name: Return the name of the Series.
hasnans: Returns True if NaNs are in the series.
index: The index of the series
head(): Return the first n rows.
tail(): Return the last n rows.
info(): Display the Summary of the series
'''

# 1. dtype - dtype is used to return the datatype of the Series.
data = [1,2,3,4,5]
s = pd.Series(data,name='serial no')
print('\ndtype:\n',s) #dtype: int64

# 2. ndim - ndim is used to return the number of dimensions of the Series.
print('\nndim:',s.ndim) #ndim: 1

# 3. Size - size is used to return the number of elements in the Pandas Series
print('\nsize:',s.size)  #size: 5

# 4. name - name is used to return the name of the Series in Pandas.
print('\nname:',s.name) #name: serial no

# 5. hasnans - hasnans attribute returns True if NaNs are in the Pandas Series. 
print('\nhasnans:',s.hasnans) #hasnans: False

# 6. index
print('\nindex:',s.index)#index: RangeIndex(start=0, stop=5, step=1)

# 7. head() - head() method is used to return the first n rows of the Pandas Series.
print('\nhead(2):\n',s.head(2))
'''head(): 0    1
1    2
2    3
3    4
4    5
Name: serial no, dtype: int64'''

# 8. tail() - tail() method is used to return the last n rows of the Pandas Series. 
print('\ntail():\n',s.tail())
'''tail():
 0    1
1    2
2    3
3    4
4    5
Name: serial no, dtype: int64'''

# 9. info() - info() method is used to display the Summary of the Pandas Series. 
print('\ninfo():\n',s.tail())
'''info():
 0    1
1    2
2    3
3    4
4    5
Name: serial no, dtype: int64'''


'''Append two Pandas Series
In this lesson, we will append two Pandas series using the append() method. This will append two series. With that, the ignore_index parameter of the append() will allow you to ignore or consider the index. If ignore_index is set to True, the original indexes are ignored and replaced by 0, 1, 2, etc. in the output. The default is False.

Note: The append() method deprecated since version Pandas 1.4.0.

We will see two examples:

1. Append two Pandas series considering the original index
2.  Append two Pandas series ignoring the original index'''


d1 = [10,21,30,41,50]
d2 = [11,20,31,40,51]

series1 = pd.Series(d1)
print('series1:\n',series1)
series2 = pd.Series(d2)
print('series2:\n',series2)

def demo(x1,x2):
    if(x1>x2):
        return(x1)
    else:
        return(x2)


res = series1.combine(series2,demo)
print(res)








 