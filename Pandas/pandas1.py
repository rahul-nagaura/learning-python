# create a Pandas DataFrame 
'''To create a dataframe in pandas, use the pandas.DataFrame() method. Let us see an example wherein we have student records:'''


import pandas as pd
# Dataset
data = {
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
df = pd.DataFrame(data)
print("Student Records\n\n",df)

'''
Student Records

   student  rank  marks
0    Amit     1     95
1    John     4     70
2   Jacob     3     80
3   David     5     60
4   Steve     2     90
'''

data2 = {
    'student': ['Rahul','Ajay','Sumit','Naveen','Raghav','Harman'],
    'rank': [1234,2345,1234,123,123,123],
    'marks': [1,2,3,4,5,6],
    'Age': [21,22,21,21,21,21],
    'Branch': ['Chem','ECE','CSE','MLMT','Mech  ','ECE']
}

studentList = pd.DataFrame(data2)
print('Studnets List\n',studentList)

# output 
'''
Studnets List
   student  rank  marks  Age Branch
0   Rahul  1234      1   21   Chem
1    Ajay  2345      2   22    ECE
2   Sumit  1234      3   21    CSE
3  Naveen   123      4   21   MLMT
4  Raghav   123      5   21   Mech
5  Harman   123      6   21    ECE
'''
# The 0, 1, 2, etc. are the index or label that gets automatically added to the table


#2. Access a group of rows or columns in a Pandas DataFrame 
'''The dataframe.loc is used in Pandas to access a group of rows or columns in a DataFrame. Let us see an example:'''

df2 = pd.DataFrame(data, index=['Row1','Row2', 'Row3', 'Row4','Row5'])
print('df2 is:\n',df2);
'''
Access data
      student  rank  marks
Row1    Amit     1     95
Row2    John     4     70
Row3   Jacob     3     80
Row4   David     5     60
Row5   Steve     2     90'''

# Access the value in the Student column corresponding to Row1 in label
print('Value = ', df2.loc['Row1','student'])  # Value =  Amit
print('marks of John', df2.loc['Row2','marks'])  #marks of John 70

# 3. Access using rows and columns by integer positions 

'''
Access a group of rows or columns by integer positions in a Pandas DataFrame
The dataframe.iloc is used to access a group of rows or columns by integers. We have also set columns and indexes. Let us see an example:'''

df3 = df.iloc[[1,2]]
print('df3 is:\n',df3)
'''
      student  rank  marks
Row2    John     4     70
Row3   Jacob     3     80'''

'''
4.Name your indexes in a Pandas DataFrame
The index argument is used to set and name your indexes in a DataFrame. Let us see an example:'''
df4 = pd.DataFrame(data,index=['s1','s2','s3','s4','s5'])
print('df4 is:\n',df4)
'''
df4 is:
    student  rank  marks
s1    Amit     1     95
s2    John     4     70
s3   Jacob     3     80
s4   David     5     60
s5   Steve     2     90'''


'''
5.Iterate a DataFrame
To iterate a DataFrame and display the column names, use the for loop as in the below example:'''
df5 = pd.DataFrame(data)
print('Displaying the columns:')
for col in df5:
    print(col)
    # for ele in col:
    #     print(ele)
for row in df5:
    print(row)
'''Displaying the columns:
student
rank
marks
student
rank
marks'''





