import pandas as pd
# Dictionary-dən DataFrame yaratmaq
data_dict = {'A': [1, 2], 'B': [3, 4]}
df2 = pd.DataFrame(data_dict)
print(df2)
# 'A' sütunu 1-dən böyük olan sətirləri seçmək
df2_filtered = df2[df2['A'] > 1]
print(df2_filtered)
