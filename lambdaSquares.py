import numpy as np
import pandas as pd
n = int(input("Please enter a number where the series should end: "))
sqSeries = pd.Series(np.array(range(1, n+1))**2, index=range(1, n+1))
print(sqSeries)