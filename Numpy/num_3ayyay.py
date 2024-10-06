# Slicing in array 
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x[0:5])
print(x[5:]) #return 6 - 10 values [ 6  7  8  9 10] 
print(x[:5]) # start indexing form 0 --> [1 2 3 4 5]
print(x[1:10:2]) # print even number
# we also like this for even numbers 
print(x[::2])

# slicing 2-D array 
y = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(y[1,2:5])
print('second index of the both the array',y[0,1:2], y[1,1:2])

# print(x[array_num_1:array_num_2,index num])
print(y[0:2,5])
print(y[0:2,3])
print(y[0:2,1:4]) 


# data type 
# i - integet 
# b - boolean 
# u - unsigned i
# f - float 
# c - complex f 
# m - tiemdelta 
# M - datetime 
# O - object 
# S - string 
# U - unicode S 
# V  - memory 
# checking teh data type of numpy 
 
g= np.array([1,2,3,4])
print(g.dtype)

d = np.array(['aaple', 'banana','cherry'])
print(d.dtype)

# create a array with a defined data type:
h = np.array([1,2,3,4,5], dtype='S')
print(h)
print(h.dtype)

# converting data type in existing array - astype()
n = np.array([1.2,2.3,4.5])
m = n.astype('i')
print(m)
print(m.dtype)
print(n.dtype)


