'''String Operations on Text Data in Pandas
We can easily perform operations on strings in Pandas using the string methods. In this lesson, we will see how to perform the following string operations on text data in Pandas Series:

1. lower(): Perform lowercase on text data
2. upper(): Perform uppercase on text data
3. title(): Convert text data to camel case
4. len(): To get the length of each element in the Series.
5. count(): Count the non-empty cells for each column or row
6. contain(): Search for a value in a column.'''


import pandas as pd 
data = ['Amit','Alice','Jocab','alex','AMRITA','POONAM']
series = pd.Series(data)
lowerCase = series.str.lower()
print('print all the text in lower case:\n',lowerCase)
print()
upperCase = series.str.upper()
print('print all the text in the upper case:\n',upperCase)
print()
titleCase = series.str.title()
print('print all the letter in a heading or title case like first letter is capital:\n',titleCase)
print()
lengthCal = series.str.len()
print('print the length of the element:\n',lengthCal)
print()
countCase = series.count()
print('count the number of the elements we have',countCase)
print()
searchCase = series.str.contains('Amit')
print('To find a particular value in a data:\n',searchCase)
print()

'''print all the text in lower case:

 0      amit
1     alice
2     jocab
3      alex
4    amrita
5    poonam
dtype: object

print all the text in the upper case:
 0      AMIT
1     ALICE
2     JOCAB
3      ALEX
4    AMRITA
5    POONAM
dtype: object

print all the letter in a heading or title case like first letter is capital:
 0      Amit
1     Alice
2     Jocab
3      Alex
4    Amrita
5    Poonam
dtype: object

print the length of the word:  
 0    4
1    5
2    5
3    4
4    6
5    6
dtype: int64

count the number of the elements we have 6

To find a particular value in a data:
 0     True
1    False
2    False
3    False
4    False
5    False
dtype: bool'''



'''Pandas – Date Time
In this lesson, learn how to work with the Date Time operations in Pandas. Let us first see how to get the current date and time, then we will check for leap year, last day of the month, week, etc. The following examples are covered:

1. Get the current date and time
2. Get the day of the week
3. Get the day of the year
4. Get the number of days in a month
5. Check if the year is a leap year
6. Check if the date is the last day of the month
7. Check if the date is the first day of the month
8. Check if the date is the last day of the year
9. Check if the date is the first day of the year'''

# 1 get the current date
import pandas as pd 
date = pd.Timestamp.now()
print('current data:',date) #2024-10-09 14:40:48.530285

# 2 get the day of the week
date = pd.Timestamp(year=2025,month=1,day=25,hour=8)
dayOfWeek = date.dayofweek
# what is the number of this day in a 7 day's/week
print('day of the week:',dayOfWeek) #day of the week: 5

# 3 get the day of the year
date = pd.Timestamp(year=2025,month=4,day=8,hour=11)
dayOfYear = date.dayofyear
print('day of the year',dayOfYear) #day of the year 98

# 4 get the number of day's in a month
date = pd.Timestamp(year=2023,month=2,day=2,hour=4)
days = date.daysinmonth
print("total number of day's in feb",days) #ttotal number of day's in a month 28

# 5 check if the year is a the leap year or not 
date = pd.Timestamp(year=2024,month=4,day=4,hour=4)
leapyear = date.is_leap_year
print('check weather it is a leap year or not:',leapyear) #check weather it is a leap year or not: True

# 6 Check if the date is the last day of the month
lastDayOf = date.is_month_end
print('islast day of hte month:',lastDayOf) #islast day of hte month: False 

# 7 Check if the date is the first day of the month 
firstDayMonth = date.is_month_start
print('isfirst day of the month:', firstDayMonth) #isfirst day of the month: False 

# 8 date is the start day of the year
firstYearDay = date.is_year_start
print('isfirst date of teh year:',firstYearDay) #isfirst date of teh year: False

# 9 date is the last day of the year
lastYeadDay = date.is_year_end
print('isthis is a last day of the year:',lastYeadDay) #this is a last day of the year: False


'''
Remove Whitespace or specific characters tin Pandas
To remove whitespace (including newlines) or specific characters on text data in a Series or DataFrame, use the following methods in Python Pandas:

strip(): Strip whitespace (including newlines) or specific characters from the left and right
lstrip(): Strip whitespace (including newlines) or specific characters from only the left side
rstrip(): Strip whitespace (including newlines) or specific characters from only the right side
strip() method
To strip whitespace (including newlines) or specific characters from both the left and right side of values in a Series or DataFrame, use the strip() method in Pandas.'''
data = ['Amit\n\t','!!Rahul\n','!@\nJohn','Anil\n\t','\n\trech']
series = pd.Series(data)
print(series,'\n')
print('remove white space both this side:\n',series.str.strip('\n\t!@'))
print('remove white spaces form the right side:\n',series.str.rstrip('\n\t!@'))
print('remove white spaces form the left side:\n',series.str.lstrip('\n\t!@'))

'''0     Amit\n\t
1    !!Rahul\n
2     !@\nJohn
3     Anil\n\t
4     \n\trech
dtype: object

remove white space both this side:   
 0     Amit
1    Rahul
2     John
3     Anil
4     rech
dtype: object

remove white spaces form the right side:
 0        Amit
1     !!Rahul
2    !@\nJohn
3        Anil
4    \n\trech
dtype: object
remove white spaces form the left side:
 0    Amit\n\t
1     Rahul\n
2        John
3    Anil\n\t
4        rech
dtype: object'''