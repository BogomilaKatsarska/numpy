import numpy as np
my_list = [1, 2, 3]

arr = np.array(my_list)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(my_mat)
print(my_mat)
new_array = np.arange(0, 10, 2)
print(new_array)
zeros_array = np.zeros(4)
ones_array = np.ones(4)
zeros_matrix = np.zeros((2, 3))
print(zeros_array)
print(zeros_matrix)
evenly_spaced_points = np.linspace(0, 5, 10)
print(evenly_spaced_points)
identity_matrix = np.eye(4)
print(identity_matrix)

#Create an array of random numbers:
one_dimensional_arr = np.random.rand(5)
print(one_dimensional_arr)
two_dimensional_arr = np.random.rand(5, 5)
print(two_dimensional_arr)
print(np.random.randn(2))
print(np.random.randint(1, 100, 10))

var_one = np.arange(25)
print(var_one)
ran_arr = np.random.randint(0, 50, 10)
print(ran_arr)
print(f" max: {ran_arr.max()}")
print(f" index max: {ran_arr.argmax()}")
print(ran_arr.min())
var_one.reshape(5, 5)
print(var_one)
print(var_one.shape)
print(var_one.dtype)