import pandas as pd
data = [(1, 2), (3, 4)]
df1 = pd.DataFrame(data)
print(df1)
df1.columns = ['c1', 'c2']
df1.index = ['r1', 'r2']
print(df1)
