import numpy as np
import numpy.random as random
seed=int(input())
n=int(input())
p=float(input())
x = random.seed(seed)
s = np.random.binomial(n, p, 10)
print(s)