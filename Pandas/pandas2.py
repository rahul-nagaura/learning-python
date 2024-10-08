# DataFrame – Attributes and Methods 
'''The Pandas DataFrame is a Two-dimensional, tabular data, 
that uses the DataFrame() method to create a DataFrame.
It also uses different built-in attributes and methods for basic 
functionalities. In this lesson, let us see such attributes and
methods in Python Pandas for DataFrame:'''
'''
dtypes: Return the dtypes in the DataFrame
ndim: Return the number of dimensions of the DataFrame
size: Return the number of elements in the DataFrame.
shape: Return the dimensionality of the DataFrame in the form of a tuple.
index: Return the index of the DataFrame
T: Transpose the rows and columns
head(): Return the first n rows.
tail(): Return the last n rows.'''
# Let us understand them one by one: 


# dtypes 
# dtypes is used to return the dtypes in the DataFrame. 


import pandas as pd 
data = {
    'students': ['rahul','John','david','wildrush','fire'],
    'marks': [56,54,57,58,59],
    'rank': [1,2,3,4,5]
}

df = pd.DataFrame(data, index=['Row1','Row2','Row3','Row4','Row5'])
print('Your data is here:\n',df)
'''Your data is here:
       students  marks  rank
Row1     rahul     56     1
Row2      John     54     2
Row3     david     57     3
Row4  wildrush     58     4
Row5      fire     59     5'''

# 1.DataType 
print('DataType:\n',df.dtypes) #dtype: object

# 2. ndim --> ndim is used to return the number of dimensions of the DataFrame.
print('number of dimension:',df.ndim) #number of dimension: 2

# 3. size --> size is used to return the number of elements in the DataFrame.
print('number of element:',df.size) #number of element: 15

# 4. shape --> shape is used to return the dimensionality of the DataFrame in the form of a tuple.
print('Shape:',df.shape) #Shape: (5, 3) (row,column)

# 5. indexe --> index is used to return the index of the DataFrame.
print('indexes:',df.index) #indexes: Index(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], dtype='object')   

# 6. Transpose --> T is used to Transpose the rows and columns.
print('Transpose:\n',df.T)
'''Transpose:
            Row1  Row2  ...      Row4  Row5
students  rahul  John  ...  wildrush  fire
marks        56    54  ...        58    59
rank          1     2  ...         4     5

[3 rows x 5 columns]'''

#  7. Head --> head() is used to return the first n rows.
print('First 5 rows:\n',df.head())
print('First 3 rows:\n',df.head(3))

# 8. Tail --> tail() is used to return the last n rows.
print('Last 5 rows\n',df.tail())
print('last 3 rows\n',df.tail(3))



