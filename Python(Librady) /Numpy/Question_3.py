'''Print Array Attributes.
Print the following attributes of the array:
The shape of the array.
The number of array dimensions.
The size of each element in bytes.
'''
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)

print("The shape of the array:",np.shape(a))
print("The number of array dimensions:",np.ndim(a))
print("The size of each element in bytes:",np.size(a))
