###############################################################
# Customer Segmentation with RFM (RFM ile Müşteri Segmentasyonu)
###############################################################

###############################################################
# Business Problem (İş Problemi)
###############################################################
# FLO wants to segment its customers and determine marketing strategies based on these segments.
# To achieve this, customer behaviors will be defined, and groups will be created based on these behavioral clusters.

###############################################################
# Data Set Story (Veri Seti Hikayesi)
###############################################################

# The data set consists of information obtained from the past shopping behaviors of customers who made their last purchases in 2020-2021 as OmniChannel (both online and offline shoppers).

# master_id: Unique customer number
# order_channel: Which channel belongs to the shopping platform (Android, ios, Desktop, Mobile, Offline)
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
# TASKS (GÖREVLER)
###############################################################

import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# TASK 1: Data Understanding and Preparation (Veriyi Anlama ve Hazırlama)
# 1. Read the flo_data_20K.csv data.
df = pd.read_csv("flo_data_20k.csv")
# 2. In the data set,
# a. First 10 observations,
df.head(10)
df.head()
df.shape
# b. Variable names,
df.columns
# c. Descriptive statistics,
df.describe().T
# d. Missing values,
df.isnull().values.any()
df.isnull().sum()
# e. Variable types, analyze them.
df.info()
# 3. Create new variables for the total number of purchases and expenditure for each customer as omnichannel customers shop both online and offline.
df["total_expenditure"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"] 
df["total_num_of_purchase"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]
# 4. Examine variable types. Convert date variables to date type.
# 5. Examine the distribution of the number of customers, average number of products purchased, and average expenditures in shopping channels.
# 6. List the top 10 customers with the highest revenue.
# 7. List the top 10 customers with the most orders.
# 8. Modularize the data preprocessing process.

# TASK 2: Calculating RFM Metrics (RFM Metriklerinin Hesaplanması)

# TASK 3: Calculating RF and RFM Scores (RF ve RFM Skorlarının Hesaplanması)

# TASK 4: Defining RF Scores as Segments (RF Skorlarının Segment Olarak Tanımlanması)

# TASK 5: Action Time! (Aksiyon zamanı!)
# 1. Examine the averages of recency, frequency, and monetary values for segments.
# 2. Find customers with relevant profiles for 2 cases using RFM analysis and save their customer IDs in a CSV file.
# a. FLO is introducing a new women's shoe brand. It is planned to target loyal customers (champions, loyal_customers) who have an average expenditure of over 250 TL and shop in the women's category. Save the customer IDs to a CSV file named new_brand_target_customer_ids.csv.
# b. A 40% discount is planned for men's and children's products. Special attention is desired for customers who are interested in these categories, who were good customers in the past but haven't shopped for a long time, and new customers. Save the IDs of suitable customers to a CSV file named discount_target_customer_ids.csv.

# TASK 6: Modularize the entire process.

###############################################################
# TASK 1: Data Understanding and Preparation (Veriyi Hazırlama ve Anlama)
###############################################################

# 2. In the data set,
# a. First 10 observations,
# b. Variable names,
# c. Size,
# d. Descriptive statistics,
# e. Missing values,
# f. Analyze variable types.

# 3. Omnichannel customers indicate that they shop from both online and offline platforms.
# Create new variables for the total number of purchases and expenditure for each customer.

# 4. Examine variable types. Convert date variables to date type.

# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)

# 5. Examine the distribution of the number of customers, total number of products purchased, and total expenditures in shopping channels.

# 6. List the top 10 customers with the highest revenue.

# 7. List the top 10 customers with the most orders.

# 8. Modularize the data preprocessing process.

###############################################################
# TASK 2: Calculating RFM Metrics (RFM Metriklerinin Hesaplanması)
###############################################################

# Analysis date is 2 days after the last shopping date in the data set.

# Create a new RFM dataframe that includes customer_id, recency, frequency, and monetary values.

###############################################################
# TASK 3: Calculating RF and RFM Scores (RF ve RFM Skorlarının Hesaplanması)
###############################################################

# Convert Recency, Frequency, and Monetary metrics into scores from 1 to 5 using qcut and save these scores as recency_score, frequency_score, and monetary_score.

# Express recency_score and frequency_score as a single variable and save it as RF_SCORE.

###############################################################
# TASK 4: Defining RF Scores as Segments (RF Skorlarının Segment Olarak Tanımlanması)
###############################################################

# For more understandable RFM scores, define segments and convert RF_SCORE to segments using the defined seg_map.

###############################################################
# TASK 5: Action Time! (Aksiyon zamanı!)
###############################################################

# 1. Examine the averages of recency, frequency, and monetary values for segments.

# 2. Find customers with relevant profiles for 2 cases using RFM analysis and save their customer IDs in CSV files.

# a. FLO is introducing a new women's shoe brand. It is planned to target loyal customers who shop in the women's category and have an average expenditure of over 250 TL. Save the customer IDs to a CSV file named new_brand_target_customer_ids.csv.

# b. A 40% discount is planned for men's and children's products. Special attention is desired for customers who are interested in these categories, who were good customers in the past but haven't shopped for a long time, and new customers. Save the IDs of suitable customers to a CSV file named discount_target_customer_ids.csv.

# TASK 6: Modularize the entire process.
