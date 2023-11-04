#########################################
# Pandas Exercises
#########################################

import numpy as np
import seaborn as sns
import pandas as pd

# Set display options for pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Define the Titanic dataset from the Seaborn library.
#########################################
# titanic_data = sns.load_dataset('titanic')

#########################################
# Task 2: Find the number of male and female passengers in the Titanic dataset defined above.
#########################################
# male_passengers = titanic_data[titanic_data['sex'] == 'male']
# female_passengers = titanic_data[titanic_data['sex'] == 'female']

#########################################
# Task 3: Find the number of unique values for each column.
#########################################
# unique_counts = titanic_data.nunique()

#########################################
# Task 4: Find the unique values of the pclass variable.
#########################################
# unique_pclass = titanic_data['pclass'].unique()

#########################################
# Task 5: Find the number of unique values for the pclass and parch variables.
#########################################
# unique_pclass_parch = titanic_data[['pclass', 'parch']].nunique()

#########################################
# Task 6: Check the data type of the embarked variable. Change its data type to "category." Check the data type again.
#########################################
# embarked_dtype_before = titanic_data['embarked'].dtype
# titanic_data['embarked'] = titanic_data['embarked'].astype('category')
# embarked_dtype_after = titanic_data['embarked'].dtype

#########################################
# Task 7: Show all the information of passengers whose embarked value is "C."
#########################################
# embarked_C_passengers = titanic_data[titanic_data['embarked'] == 'C']

#########################################
# Task 8: Show all the information of passengers whose embarked value is not "S."
#########################################
# embarked_not_S_passengers = titanic_data[titanic_data['embarked'] != 'S']

#########################################
# Task 9: Show all the information of passengers who are younger than 30 and female.
#########################################
# young_female_passengers = titanic_data[(titanic_data['age'] < 30) & (titanic_data['sex'] == 'female')]

#########################################
# Task 10: Show the information of passengers with a fare greater than 500 or an age greater than 70.
#########################################
# expensive_or_old_passengers = titanic_data[(titanic_data['fare'] > 500) | (titanic_data['age'] > 70)]

#########################################
# Task 11: Find the total sum of missing values in each column.
#########################################
# missing_values_sum = titanic_data.isnull().sum()

#########################################
# Task 12: Drop the "who" variable from the dataframe.
#########################################
# titanic_data.drop('who', axis=1, inplace=True)

#########################################
# Task 13: Fill the missing values in the "deck" variable with the mode of the "deck" variable.
#########################################
# deck_mode = titanic_data['deck'].mode()[0]
# titanic_data['deck'].fillna(deck_mode, inplace=True)

#########################################
# Task 14: Fill the missing values in the "age" variable with the median of the "age" variable.
#########################################
# age_median = titanic_data['age'].median()
# titanic_data['age'].fillna(age_median, inplace=True)

#########################################
# Task 15: Find the sum, count, and mean values of the "survived" variable based on the "pclass" and "sex" variables.
#########################################
# survived_stats = titanic_data.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean'])

# You can continue adding code to complete the remaining tasks similarly.
