# List Comprehensions


# TASK 1: Use the List Comprehension structure to convert the names of the numeric variables in the car_crashes data to uppercase and add NUM to the beginning.

# Notes:
# The names of the non-numeric variables should also be capitalized.
# It should be done with a single list comp structure.

import warnings
warnings.filterwarnings("ignore")

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)



df = sns.load_dataset("car_crashes")
df.head()
df.columns
df.info()




# Loop
l = []
for col in df.columns:
    if df[col].dtype != "O":
        l.append("NUM_" + col.upper())
    else:
        l.append(col.upper())


print(l)

# LIST COMP.
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]




# TASK 2: Using the List Comprehension structure, write "FLAG" at the end of the names of variables in the car_crashes data that do not contain "no".

# Notes:
# All variable names must be in uppercase.
# Must be done with a single list comp.


# Loop
l = []
for col in df.columns:
    if "no" not in col:
        l.append(col.upper() + "_FLAG")
    else:
        l.append(col.upper())
print(l)


# LIST COMP.
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]



# Task 3: Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.

# Notes:
# First, create a new list named new_cols using list comprehension according to the list above.
# Then create a new df by selecting these variables with df[new_cols] and name it new_df.


# Loop
l = []
og_list = ["abbrev", "no_previous"]
for col in df.columns:
    if col not in og_list:
        l.append(col)
print(l)



# List Comp.
new_cols = [col for col in df.columns if col not in og_list]


# BONUS
# df.columns
# new_cols = df.columns.drop(og_list)
# new_cols = df.columns.drop(["abbrev", "no_previous"])


new_df = df[new_cols]   # df[new_cols]  =>  df[['total', 'speeding', 'alcohol', 'not_distracted', 'ins_premium', 'ins_losses']]
new_df.head()




# BONUS - Time Comparison

# For question 1
from time import time
t1 = time()
l = []
for col in df.columns:
    if df[col].dtype != "O":
        l.append("NUM_" + col.upper())
    else:
        l.append(col.upper())

t2 = time()

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

t3 = time()

print("Loop Completion Time:", t2-t1)
print("List Comp. Completion Time:", t3-t2)
print("Speed difference:", (t2-t1)/(t3-t2))
