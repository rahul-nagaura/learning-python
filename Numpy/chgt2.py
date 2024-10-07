1. # Array Broadcasting 
'''We touched on this earlier, but it's a very important concept. 
Broadcasting allows operations between arrays of different 
shapes. It can be tricky at first but is very powerful when 
working with arrays of different dimensions.'''

import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3])

# Broadcasting arr2 to match the shape of arr1
result = arr1 + arr2
print(result)
# Output:
# [[2 4 6]
#  [5 7 9]]

# 2. Array Concatenation and Splitting 
''' concatenate (join) or split arrays easily using functions like np.concatenate, np.vstack, np.hstack, np.split, etc.'''
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

# Concatenating along axis 0 (rows)
concatenated = np.concatenate((arr1, arr2), axis=0)
print(concatenated)
# Output: [[1 2]
#          [3 4]
#          [5 6]] 

# Splitting:
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)
print('Splitting array:',split_arr)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]


# 3. Advanced Indexing 
'''NumPy allows boolean indexing and fancy indexing, which can be 
used to filter arrays based on certain conditions or select 
specific elements.'''
# Boolean Indexing:
print('Boolean Indexing:',end=' ')
arr = np.array([10, 20, 30, 40, 50])
filtered = arr[arr > 30]  # Only select elements greater than 30
print(filtered)  # Output: [40 50]


# Fancy Indexing: 
print('Fancy Indexing:',end=' ')
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]  # Specific indices
print(arr[indices])  # Output: [10 30 50]

# 4. Universal Functions (ufuncs)
'''NumPy provides universal functions (ufuncs) that operate 
 element-wise on arrays. These include basic mathematical 
 functions like np.sqrt, np.exp, and trigonometric functions (np.
 sin, np.cos), and more.'''

arr = np.array([1, 4, 9, 16])
sqrt_arr = np.sqrt(arr)  # Square root of each element
print(sqrt_arr)  # Output: [1. 2. 3. 4.]

# Exponential function
exp_arr = np.exp(np.array([1, 2, 3]))
print(exp_arr)  # Output: [ 2.71828183  7.3890561  20.08553692]


# 5. Linear Algebra Operations 
'''NumPy has built-in support for common linear algebra operations like matrix multiplication, matrix inversion, eigenvalues, etc.'''
# Matrix Multiplication:
print('Matrix Multiplication:')
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

result = np.dot(arr1, arr2)  # Matrix multiplication
print(result)
# Output: [[19 22]
#          [43 50]]

# Inverse of a Matrix:
print('Inverse of a Matrix:')
arr = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(arr)
print(inverse)

# Eigenvalues and Eigenvectors:
print('Eigenvalues and Eigenvectors:')
arr = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(arr)
print(eigenvalues)
print(eigenvectors)


# 6. Sorting and Searching
print('Sorting and Searching') 
'''NumPy provides efficient sorting and searching functions, such as np.sort(), np.argsort(), np.searchsorted(), etc.'''
arr = np.array([3, 1, 2, 4])
sorted_arr = np.sort(arr)  # Output: [1 2 3 4]

print('Searching for elements:')
arr = np.array([1, 2, 3, 4, 5])
index = np.searchsorted(arr, 3)  # Output: 2


# Handling Missing Values 
'''In large datasets, you might encounter missing or invalid data. NumPy provides mechanisms to handle such cases using np.nan (Not a Number).'''
arr = np.array([1, 2, np.nan, 4])
print(np.isnan(arr))  # Output: [False False  True False]

'''You can use np.nanmean, np.nansum, and other functions to ignore NaNs:'''
mean = np.nanmean(arr)  # Output: 2.333... (mean ignoring NaN)


# 8. Saving and Loading Arrays 
'''When working with large datasets, you may want to save NumPy arrays to a file for later use, and you can do this efficiently with np.save and np.load.
'''
print('Saving and Loading:')
arr = np.array([1, 2, 3, 4])
np.save('my_array.npy', arr)  # Save to a file

loaded_arr = np.load('my_array.npy')  # Load from the file
print(loaded_arr)  # Output: [1 2 3 4]

# 9. Random Number Generation 
'''You can generate random numbers or arrays using the numpy.random module. This includes random integers, floating-point numbers, or numbers drawn from specific distributions.'''
# Random integers between 0 and 10
print('Random integers between 0 and 10')
rand_ints = np.random.randint(0, 10, size=(3, 3))
print(rand_ints)

print('Random floating-point numbers between 0 and 1')
# Random floating-point numbers between 0 and 1
rand_floats = np.random.rand(2, 2)
print(rand_floats)

# Random numbers from a normal distribution
print('Random numbers from a normal distribution')
normal_arr = np.random.randn(4)
print(normal_arr)

# 10. Performance and Memory Optimization 
'''NumPy arrays are more memory-efficient and faster than regular Python lists. If performance is a concern, here are some advanced tips:

Use views instead of copies: When you slice an array, it returns a view (not a copy), which is more memory-efficient.
Utilize in-place operations whenever possible to avoid creating additional arrays.'''

arr = np.array([1, 2, 3, 4])
arr += 5  # Adds 5 to each element, modifies the array in-place
print(arr)  # Output: [6 7 8 9]


