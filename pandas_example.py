import pandas as pd
from pandas import DataFrame

df_1 = pd.DataFrame({'A':['A0', 'A1', 'A2'],
                     'B':['B0', 'B1', 'B2'],
                     'C':['C0', 'C1', 'C2'],
                     'D':['D0', 'D1', 'D2']},
                     index=[0, 1, 2])

df_2 = pd.DataFrame({'A':['A3', 'A4', 'A5'],
                     'B':['B3', 'B4', 'B5'],
                     'C':['C3', 'C4', 'C5'],
                     'D':['D3', 'D4', 'D5']},
                     index=[3, 4, 5])

print(df_1)
print(df_2)

# concatenation DataFrame1, 2 ,along rows, axis = 0, default
df_12_axis0 = pd.concat([df_1, df_2])#row bind : axis = 0, default

print(df_12_axis0)

df_3 = pd.DataFrame({'A':['A6', 'A7', 'A8'],
                     'B':['B6', 'B7', 'B8'],
                     'C':['C6', 'C7', 'C8'],
                     'D':['D6', 'D7', 'D8']},
                     index=[0, 1, 2])

# concatenation DataFrame1, 3 ,along COLUMNS, axis = 1
df_13_axis1 = pd.concat([df_1, df_3], axis=1)# Columns bind

print(df_13_axis1)

df_4 = pd.DataFrame({'A':['A0', 'A1', 'A2'],
                     'B':['B0', 'B1', 'B2'],
                     'C':['C0', 'C1', 'C2'],
                     'E':['E0', 'E1', 'E2']},
                     index=[0, 1, 3])

print(df_1)

print(df_4)
#  pd.concat join = 'outer'
df_14_outer = pd.concat([df_1, df_4], join='outer')

print(df_14_outer)
#  pd.concat join = 'inner'
df_14_inner = pd.concat([df_1, df_4], join='inner')

print(df_14_inner)

# pd.concat join = 'outer', axis=1
df_14_outer_axis1 = pd.concat([df_1, df_4], join='outer', axis=1)

print(df_14_outer_axis1)

# pd.concat join = 'inner', axis=1
df_14_inner_axis1 = pd.concat([df_1, df_4], join='inner', axis=1)

print(df_14_inner_axis1)

#reindex example1
df_14_axis1_reindex1 = pd.concat([df_1, df_4], axis=1).reindex(df_1.index)

print(df_14_axis1_reindex1)

#reindex example2
df_14_axis1_reindex2 = pd.concat([df_1, df_4], axis=1).reindex(index=[0 ,1 ,2 ,3])

print(df_14_axis1_reindex2.abs)

print(df_14_axis1_reindex2.query)