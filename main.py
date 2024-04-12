# Pandas: Get the Rows that are NOT in another DataFrame


import pandas as pd


df1 = pd.DataFrame({
    'a': [2, 4, 6, 8, 10],
    'b': [112, 114, 115, 118, 120]
})

df2 = pd.DataFrame({
    'a': [2, 4, 6, 9, 11],
    'b': [112, 114, 115, 190, 250]
})

all_rows = df1.merge(df2.drop_duplicates(), on=[
    'a', 'b'], how='left', indicator=True)

print(all_rows)

rows_not_in = all_rows[all_rows['_merge'] == 'left_only']

print('-' * 50)

print(rows_not_in)