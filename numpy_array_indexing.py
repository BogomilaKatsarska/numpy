import numpy as np

arr = np.arange(0,11)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[:6])
arr[0:5] = 500
print(arr)
arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print(slice_of_arr)
print(arr) #data is not copied
#if you want a copy, not the original arr
arr_copy = arr.copy()

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d[0][1])
print(arr_2d[:2,1:])

#Conditional selection:
arr = np.arange(1, 11)
print(arr > 5)
bool_arr = arr > 5
print(arr[bool_arr])
print(arr[arr > 5])