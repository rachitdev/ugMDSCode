import numpy as np
n = int(input())
a = np.full((n, n), 0)

# Swapping values of the border elements to 1

a[0, :] = 1
a[n-1, :] = 1
a[:, 0] = 1
a[:, n-1] = 1
print(a)