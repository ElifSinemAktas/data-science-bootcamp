###############################################################
# CLTV Prediction with BG-NBD and Gamma-Gamma
###############################################################

###############################################################
# Business Problem
###############################################################
# FLO wants to determine a roadmap for sales and marketing activities.
# In order for the company to plan for the medium to long term, it is necessary to predict the potential value that existing customers will provide to the company in the future.

###############################################################
# Data Set Story
###############################################################

# The data set consists of information obtained from the past shopping behaviors of customers who made their last purchases in 2020-2021 as OmniChannel (both online and offline shoppers).

# master_id: Unique customer number
# order_channel: The channel used for shopping on the platform (Android, iOS, Desktop, Mobile, Offline)
# last_order_channel: The channel where the last purchase was made
# first_order_date: The date of the customer's first purchase
# last_order_date: The date of the customer's last purchase
# last_order_date_online: The date of the customer's last online platform purchase
# last_order_date_offline: The date of the customer's last offline platform purchase
# order_num_total_ever_online: The total number of purchases made by the customer on the online platform
# order_num_total_ever_offline: The total number of purchases made by the customer offline
# customer_value_total_ever_offline: The total amount paid by the customer for offline purchases
# customer_value_total_ever_online: The total amount paid by the customer for online purchases
# interested_in_categories_12: The list of categories the customer shopped in the last 12 months

###############################################################
# Tasks
###############################################################
# Task 1: Data Preparation
# 1. Read the flo_data_20K.csv data and create a copy of the DataFrame.
# 2. Define the necessary functions, "outlier_thresholds" and "replace_with_thresholds," to suppress outliers.
# Note: For CLTV calculation, frequency values need to be integers, so round the lower and upper limits.
# 3. Suppress the outliers if there are any for the variables "order_num_total_ever_online," "order_num_total_ever_offline," "customer_value_total_ever_offline," and "customer_value_total_ever_online."
# 4. Create new variables for the total number of purchases and expenditure for each customer as omnichannel customers shop both online and offline.
# 5. Examine variable types. Convert date variables to date type.

# Task 2: Creating the CLTV Data Structure
# 1. Take the date after which the last purchase was made in the data set as the analysis date.
# 2. Create a new CLTV dataframe that includes customer_id, recency_cltv_weekly, T_weekly, frequency, and monetary_cltv_avg.
# Monetary value will be expressed as the average value per purchase, while recency and tenure values will be expressed on a weekly basis.

# Task 3: Building BG/NBD and Gamma-Gamma Models, Calculating 6-Month CLTV
# 1. Fit the BG/NBD model.
# a. Predict expected purchases from customers within 3 months and add it to the CLTV dataframe as "exp_sales_3_month."
# b. Predict expected purchases from customers within 6 months and add it to the CLTV dataframe as "exp_sales_6_month."
# 2. Fit the Gamma-Gamma model. Predict the average value that customers are expected to leave and add it to the CLTV dataframe as "exp_average_value."
# 3. Calculate the 6-month CLTV and add it to the dataframe as "cltv."
# b. Examine the top 20 customers with the highest CLTV values.

# Task 4: Creating Segments Based on CLTV
# 1. Divide all customers into 4 groups (segments) based on 6-month CLTV and add group names to the data set. Assign them as "cltv_segment."
# 2. Examine the averages of recency, frequency, and monetary values for the segments.

# Bonus: Modularize the entire process.

###############################################################
# Task 1: Data Preparation
###############################################################

# 1. Read the OmniChannel.csv data and create a copy of the DataFrame.

# 2. Define the necessary functions, "outlier_thresholds" and "replace_with_thresholds," to suppress outliers.
# Note: For CLTV calculation, frequency values need to be integers, so round the lower and upper limits.

# 3. Suppress the outliers if there are any for the variables "order_num_total_ever_online," "order_num_total_ever_offline," "customer_value_total_ever_offline," and "customer_value_total_ever_online."

# 4. Create new variables for the total number of purchases and expenditure for each customer as omnichannel customers shop both online and offline.

# 5. Examine variable types. Convert date variables to date type.

###############################################################
# Task 2: Creating the CLTV Data Structure
###############################################################

# 1. Take the date after which the last purchase was made in the data set as the analysis date.

# 2. Create a new CLTV dataframe that includes customer_id, recency_cltv_weekly, T_weekly, frequency, and monetary_cltv_avg.

###############################################################
# Task 3: Building BG/NBD and Gamma-Gamma Models, Calculating 6-Month CLTV
###############################################################

# 1. Fit the BG/NBD model.
# a. Predict expected purchases from customers within 3 months and add it to the CLTV dataframe as "exp_sales_3_month."
# b. Predict expected purchases from customers within 6 months and add it to the CLTV dataframe as "exp_sales_6_month."

# 2. Fit the Gamma-Gamma model. Predict the average value that customers are expected to leave and add it to the CLTV dataframe as "exp_average_value."

# 3. Calculate the 6-month CLTV and add it to the dataframe as "cltv."
# b. Examine the top 20 customers with the highest CLTV values.

###############################################################
# Task 4: Creating Segments Based on CLTV
###############################################################

# 1. Divide all customers into 4 groups (segments) based on 6-month CLTV and add group names to the data set. Assign them as "cltv_segment."

# 2. Examine the averages of recency, frequency, and monetary values for the segments.
