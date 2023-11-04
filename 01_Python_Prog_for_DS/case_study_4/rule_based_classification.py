# #############################################
# Calculation of Potential Customer Revenue with Rule-Based Classification
# #############################################

# #############################################
# Business Problem
# #############################################

# A gaming company wants to create new customer personas based on some characteristics of its customers and create segments based on these new customer personas to estimate how much potential new customers could bring to the company.
# For example: They want to determine how much, on average, a 25-year-old male user from Turkey who uses IOS can potentially earn.

# #############################################
# Data Set Story
# #############################################

# The Persona.csv dataset contains the prices of products sold by an international gaming company and some demographic information of users who purchased these products. The dataset is composed of records generated in each sales transaction. This means that the table is not deduplicated. In other words, a user with certain demographic characteristics may have made multiple purchases.
# Price: The amount spent by the customer
# Source: The type of device the customer connected with
# Sex: The gender of the customer
# Country: The country of the customer
# Age: The age of the customer


# ################# Before Application #####################
#
# PRICE SOURCE SEX COUNTRY AGE
# 0 39 android male bra 17
# 1 39 android male bra 17
# 2 49 android male bra 17
# 3 29 android male tur 17
# 4 49 android male tur 17
# ################# After Application #####################
#
# customers_level_based PRICE SEGMENT
# 0 BRA_ANDROID_FEMALE_0_18 1139.800000 A
# 1 BRA_ANDROID_FEMALE_19_23 1070.600000 A
# 2 BRA_ANDROID_FEMALE_24_30 508.142857 A
# 3 BRA_ANDROID_FEMALE_31_40 233.166667 C
# 4 BRA_ANDROID_FEMALE_41_66 236.666667 C


# #############################################
# PROJECT TASKS
# #############################################


# #############################################
# TASK 1: Answer the following questions.
# #############################################
#
# Question 1: Read the persona.csv file and show general information about the dataset.
# Question 2: How many unique SOURCE types are there? What are their frequencies?
# Question 3: How many unique PRICE values are there?
# Question 4: How many sales have been made for each PRICE?
# Question 5: How many sales have been made from each country?
# Question 6: How much has been earned from sales in each country?
# Question 7: What are the sales counts by SOURCE type?
# Question 8: What are the PRICE averages by country?
# Question 9: What are the PRICE averages by SOURCE type?
# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?

# #############################################
# TASK 2: Calculate average earnings by COUNTRY, SOURCE, SEX, and AGE.
# #############################################

# #############################################
# TASK 3: Sort the output by PRICE.
# #############################################

# Apply the sort_values method to the output by descending PRICE and save it as agg_df.

# #############################################
# TASK 4: Convert the index names to variable names.
# #############################################

# Convert the names in the index of the output of the third question to variable names using reset_index().
agg_df.reset_index(inplace=True)

# #############################################
# TASK 5: Convert the AGE variable into a categorical variable and add it to agg_df.
# #############################################

# Convert the numerical variable Age into a categorical variable.
# Create intervals that you find convincing, for example: '0_18', '19_23', '24_30', '31_40', '41_70'.

# #############################################
# TASK 6: Define new level-based customers and add them as a variable to the dataset.
# #############################################

# Define a variable named customers_level_based and add this variable to the dataset.
# Attention!
# After the values of customers_level_based are created with list comprehension, they need to be deduplicated.
# For example, it can have multiple expressions like: USA_ANDROID_MALE_0_18.
# These should be grouped and the price averages should be taken.

# #############################################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
# #############################################

# Segment new customers based on PRICE.
# Add the segments to agg_df with the name "SEGMENT".
# Describe the segments.

# #############################################
# TASK 8: Classify new incoming customers and estimate how much revenue they can bring.
# #############################################
#
# Which segment does a 33-year-old Turkish female who uses ANDROID belong to, and how much revenue is expected on average?
# Which segment does a 35-year-old French female who uses IOS belong to, and how much revenue is expected on average?