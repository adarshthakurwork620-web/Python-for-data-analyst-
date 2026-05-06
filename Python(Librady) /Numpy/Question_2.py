'''Convert 1D array to 2D.'''

import numpy as np

a=np.arange(6)
print("Original Array:",a)
b=a.reshape(2,3)
print("Reshaped 2x3 Array:",b)