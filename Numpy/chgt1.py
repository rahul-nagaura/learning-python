# 1. Creating Arrays 
import numpy as np 
a = np.array([1,2,3,4,5,6,7,8])
print(a)

for ele in a:
    print(ele,end=' ')
print()

# other array creation methods 
a = np.arange(0,20,2)
for ele in a:
    print(ele,end=' ')
print()

# np.linspace(start, stop, num): Creates an array of num equally spaced values between start and stop.
a = np.linspace(0,1,5)
for ele in a:
    print(ele,end=' ')
print()

# np.random.rand(shape): Generates an array with random floats from 0 to 1.
rand_arr = np.random.rand(2, 3)
print(rand_arr)
print()

# np.random.randint(low, high, size): Generates an array of random integers. 
int_arr = np.random.randint(0, 202, (2, 2))  # 2x2 array of random integers
for ele in int_arr:
    for e in ele:
        print(e,end=' ')
print()


# arr.shape: Returns the dimensions of the array (rows, columns).
# arr.size: Returns the total number of elements in the array.
# arr.ndim: Returns the number of dimensions (1D, 2D, etc.).
# arr.dtype: Returns the data type of the array elements.
# arr.itemsize: Returns the size (in bytes) of each element.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Shape: {arr.shape}")   # Output: Shape: (2, 3)
print(f"Size: {arr.size}")     # Output: Size: 6
print(f"Data Type: {arr.dtype}")  # Output: int32
print(f"Item Size: {arr.itemsize} bytes")  # Output: 4 bytes



arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 - arr2)  # Output: [-3 -3 -3]
print(arr1 * arr2)  # Output: [ 4 10 18]
print(arr1 / arr2)  # Output: [0.25 0.4  0.5 ]
print(arr1 * 2)  # Output: [2 4 6]
print(arr2 + 10) # Output: [14 15 16]

# np.zeros(shape): Create an array of all zeros. 
zeros = np.zeros((3, 3))
print(zeros)

# np.ones(shape): Cretae a n array of all ones
one = np.ones((3,3))
print(one)

# np.eye(n): create an Identical matrix (square matrix with ones on the daigonal and zeros elsewhere.)

print('Reshaping Arrays')
# Reshape: Change a 1D array into a 2D array.
arr = np.arange(6)  # [0 1 2 3 4 5]
print(arr)
reshaped_arr = arr.reshape(2,3)  # Reshape into 2 rows, 3 columns
print(reshaped_arr)


# Flatten: Convert a multi-dimensional array into a 1D array.
flattened = reshaped_arr.flatten()
print(flattened)  # [0 1 2 3 4 5]

# Mathematical Operations
arr = np.array([1, 2, 3, 4])
print(np.sum(arr))  # Output: 10

# Axis-wise Operations: 
# Sum elements along a specific axis in a multi-dimensional array.
# python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr, axis=0))  # Output: [5 7 9] (sum of columns)
print(np.sum(arr, axis=1))  # Output: [6 15] (sum of rows)

# Statistical Operations:
# np.mean(): Compute the mean.
# np.median(): Compute the median.
# np.std(): Compute the standard deviation.


arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))  # Output: 3.0
print(np.std(arr))   # Output: 1.414

# Broadcasting
# Broadcasting allows NumPy to work with arrays of different shapes when performing arithmetic operations. Instead of requiring the arrays to have the same shape, NumPy “broadcasts” smaller arrays to match the shape of the larger array.

arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

# Broadcasting the scalar to match the array's shape
print(arr * scalar)  # Output: [[ 2  4  6], [ 8 10 12]]

