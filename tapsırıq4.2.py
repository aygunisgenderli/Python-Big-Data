import pandas as pd

s1 = pd.Series([10, 20, 30, 40])

s1.index = ['w', 'x', 'y', 'z']
print(s1)
