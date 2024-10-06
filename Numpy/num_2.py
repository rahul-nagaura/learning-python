# Now I will create a numpy ndarray object
# the array object in numpy is call ndarray 
# array()

import numpy as np
x = np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x[0])
# by loop 
for ele in x:
    print(ele)

# We can also pass a list, tuple or any array like object with array(). ad it will be converted to ndarray.

y = np.array((1,2,3,4,5))
print(y)
print(type(y))

# dimension inn Arrays 
# a dimension in array in array is one level of array depth(nested array)

# 0-D Arrays --> scalears, are the elements in an array, each value in an array is a 0-d array.

# Now we will create 0_d array with value 42
z = np.array(42)
print(z)

# 1-D arrays --> an arrays that has 0-D arrays as the its elements is called uni directional or 1-D 
a = np.array([12,3,4,5,6,6])
print(a)

# create a 2-D array containing 2 Arrays with certain values. 
b = np.array([[1,2,3],[4,5,6]])
print(b)
# print 2 b[0][1]
print(b[0][1])
# also this 
print('2 num is', b[0,1])



# Now I will create a 3-D array with 2-D array.
c = np.array([[[1,2,3],[4,5,6]],[[11,22,33],[44,55,66]]])
print(c)
print('3D array is element 11: ',c[1,0,0])
print('3D array is element 6: ',c[0,1,2])


# check how many dimension the array have: ndim attribute 
print(x.ndim)
print(y.ndim)
print(z.ndim)
print(a.ndim)
print(b.ndim)
print(c.ndim)

# a = np.array([12,3,4,5,6,6], ndmin = 5)ndmin = 5  use to specify a dimension of a array
