import pandas as pd

s1 = pd.Series([10, 20, 30, 40])

# 20-dən böyük elementləri 10-a bölmək
s1[s1 > 20] = s1[s1 > 20] / 10
print(s1)
