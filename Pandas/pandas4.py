'''Categorical Data in Pandas
In this lesson, we will learn how to work with Categorical data in Pandas. It is a Pandas data type corresponding to categorical variables in statistics. A categorical variable takes on a limited number of possible values. Examples are gender, blood type, country affiliation, rating, etc.

Let us see two examples:

1. Create Categorical Series in Pandas
2. Create Categorical DataFrame in Pandas'''

# Create Categorical Series
# Use the dtype=”category” while creating a series to create a Categorical Series


import pandas as pd 

s = pd.Series(['A','B','C','D','E','F'], dtype='category')
print('category:\n',s)
'''category:
 0    A
1    B
2    C
3    D
4    E
5    F
dtype: category
# Categories (6, object): ['A', 'B', 'C', 'D', 'E', 'F']'''

''' Create Categorical DataFrame 
Use the dtype=”category” while creating a DataFrame to create a Categorical 
DataFrame. Let us see an example. We have created 3 categories here:#'''

data = pd.DataFrame({'CAT1':list('pqrs'), 'CAT2':list('rstw'), 'CAT3':list('abcs'), 'CAT4':list('efgh'),"CAT5":list('mnpq') }, dtype='category')

print('Series:\n',data)
print('dtype is:',data.dtypes)
'''Series:
   CAT1 CAT2 CAT3 CAT4 CAT5
0    p    r    a    e    m
1    q    s    b    f    n
2    r    t    c    g    p
3    s    w    s    h    q
dtype is: CAT1    category
CAT2    category
CAT3    category
CAT4    category
CAT5    category
dtype: object'''

'''
Working with Categories in Pandas
In this lesson, we will understand how to work with Categories in Pandas. We will learn the following with examples:

Append new categories
Remove a category'''

'''Append new categories
To append new categories, use the add_categories() method in Python Pandas. '''
df = pd.Series(['P','Q','R','S','T'], dtype='category')
print(df)
'''
0    P
1    Q
2    R
3    S
4    T
dtype: category
Categories (5, object): ['P', 'Q', 'R', 'S', 'T']'''
x = df.cat.add_categories([5])
print(x)
'''
0    P
1    Q
2    R
3    S
4    T
dtype: category
Categories (6, object): ['P', 'Q', 'R', 'S', 'T', 5]'''

'''Remove a Category in Pandas
To remove a category, use the remove_categories() method in Python Pandas'''
x = df.cat.remove_categories('R')
print(x)
'''
0      P
1      Q
2    NaN
3      S
4      T
dtype: category
Categories (4, object): ['P', 'Q', 'S', 'T'] '''


