'''
hw2

Tianqi Fang


(1 points) Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or CSVs in data.gov.

(6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:

    The DataFrame contains only the columns that you specified as the second argument.
    The values in each column have the same python type
    There are at least 10 rows in the DataFrame.
'''

import numpy as np
import pandas as pd

def read_url(url):
    df = pd.read_csv(url)
    # print(df)
    return df

def test_create_dataframe(df, list_col_name):

    # 1 only have the column with same type
    if df.columns.tolist() != list_col_name:
        return False

    # 2 same type in each column
    for i in range(len(list(df.dtypes))):
        # print(i)
        for j in range(list(df.count())[i]):
            if (type(df.iloc[j,i]) != type(df.iloc[0,i])):
                # print(str(type(df.iloc[j,i]))+'vs'+str(type(df.iloc[0,i])))
                return False
            # else: continue

    # 3 10 rows
    if (df.shape[0] < 10):
        return False

    # print('True')
    return True
            



# read_url(url)
# url = 'https://data.ct.gov/api/views/kbxi-4ia7/rows.csv'

# list_col_name = ['District Number', 'District', 'School', 'Test-takers: 2012',
#        'Test-takers: 2013', 'Test-takers: Change%',
#        'Participation Rate (estimate): 2012',
#        'Participation Rate (estimate): 2013',
#        'Participation Rate (estimate): Change%',
#        'Percent Meeting Benchmark: 2012', 'Percent Meeting Benchmark: 2013',
#        'Percent Meeting Benchmark: Change%']
# test_create_dataframe(read_url(url), list_col_name)

