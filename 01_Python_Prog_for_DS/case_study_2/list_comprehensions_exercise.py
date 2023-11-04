#################################################
# List Comprehensions
#################################################

###############################################
# TASK 1: Use the List Comprehension structure to convert the names of numeric variables in the car_crashes data to uppercase and add "NUM" in front.
###############################################

# Expected Output

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notes:
# The names of non-numeric variables should also be in uppercase.
# It should be done in a single list comprehension.

import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

###############################################
# TASK 2: Use the List Comprehension structure to add "FLAG" to the end of the names of variables in the car_crashes data that do not contain "no" in their names.
###############################################

# Notes:
# All variable names should be in uppercase.
# It should be done in a single list comprehension.

# Expected Output:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

###############################################
# Task 3: Use List Comprehension to select variable names that are DIFFERENT from the variable names given below and create a new dataframe.
###############################################

og_list = ["abbrev", "no_previous"]

# Notes:
# First, create a new list called new_cols using list comprehension based on the list above.
# Then, select these variables using df[new_cols] to create a new dataframe named new_df.

# Expected Output:

#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630
