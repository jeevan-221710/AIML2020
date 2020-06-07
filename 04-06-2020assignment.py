#Write a NumPy program to reverse an array (first element becomes last). 

import numpy as np
import numpy as np
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)
Original array:
[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
 36 37]
Reverse array:
[37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14
 13 12]
#Write a NumPy program to create a 2d array with 1 on the border and 0 inside. 

import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)
Original array:
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
1 on the border and 0 inside in the array
[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
#Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))
Array1:  [ 0 10 20 40 60]
Array2:  [0, 40]
Compare each element of array1 and array2
[ True False False  True False]
#Write a NumPy program to find the set difference of two arrays. The set difference will 
#return the sorted, unique values in array1 that are not in array2.

import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))
Array1:  [ 0 10 20 40 60 80]
Array2:  [10, 30, 40, 50, 70]
Unique values in array1 that are not in array2:
[ 0 20 60 80]
#Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.

import numpy as np
x =  np.diagflat([4, 5, 6, 8])
print(x)
[[4 0 0 0]
 [0 5 0 0]
 [0 0 6 0]
 [0 0 0 8]]
 
