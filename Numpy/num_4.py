# Iterating Array means going through the element on by one or step by step. like For loop. 

import numpy as np
x = np.array([1,2,3,4,5])
for ele in x:
    print(ele, end=", ")
print('')


x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for ele in x:
    print(ele,end=", " )
print('')

x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for y in x:
    for a in y:
        print(a,end=", " )


# same for 3-D,4-D.........
# also use nditer 
x = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
for i in np.nditer(x):
    print(i)

# 1_. Joining the numpy array - here for this we will pass concatenate()

x = np.array([1,2,3])
xy = np.array([4,5,6])
z = np.concatenate((x,xy))
print(np.concatenate((x,xy)))
print('z is', z)

# 2-D arrays along with rows(axis = 1)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
z = np.concatenate((a,b),axis=1)
print('z is now',z)

# Joining array using the stack function
x = np.array([1,2,3])
xy = np.array([4,5,6])
z = np.stack((x,xy),axis=1)
print(np.concatenate((x,xy)))
print('z is',z)    

# return 1-6    stacking along with rows 
x = np.array([1,2,3])
xy = np.array([4,5,6])
z = np.hstack((x,xy))
print(np.concatenate((x,xy)))
print('hstack is:',z)  

# vstack return normal array  -- stacking along with column
x = np.array([1,2,3])
xy = np.array([4,5,6])
z = np.vstack((x,xy))
print(np.concatenate((x,xy)))
print('vstack is: ',z)  



# Spliting arrays in numpy- it is reverse to joining, breaking the array. 
# array_split()

# split the array in 3 parts 
arr = np.array([1,2,3,4,5,6,7,8,9])
narr = np.split(arr,3)
print('splited arr is: ',narr)

arr = np.array([1,2,3,4,5,6,7,8,9])
narr = np.array_split(arr,4)
print('splited arr is: ',narr)



