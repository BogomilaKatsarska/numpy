import numpy as np

arr = np.arange(0, 11)

#array with array operations
add_num_to_num = arr + arr
print(add_num_to_num)

#array with scalars
print(arr * 100)
print(arr / arr) #Runtime warning

#universal array functions
print(np.sqrt(arr))
print(np.exp(arr))
print(np.max(arr))