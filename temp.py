#!/usr/bin/env python3

import numpy as np

#new change

a = np.array([1, 2, 3])   # Create a rank 1 array\n",
print(type(a))            # Prints \"<class 'numpy.ndarray'>\"\n",
print(a.shape)            # Prints \"(3,)\"\n",
print(a[0], a[1], a[2])   # Prints \"1 2 3\"\n",
a[0] = 5                  # Change an element of the array\n",
print(a)                  # Prints \"[5, 2, 3]\""