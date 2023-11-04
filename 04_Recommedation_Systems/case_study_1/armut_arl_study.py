#############################
# Business Problem
#############################

# Armut, Turkey's largest online service platform, brings together service providers and those who want to receive service.
# You can easily access services such as cleaning, renovation and transportation with a few taps on your computer or smartphone.
# provides access.
# Using the data set containing service users and the services and categories they received
# It is desired to create a product recommendation system with Association Rule Learning.


#############################
# Data set
#############################
# The data set consists of the services received by customers and the categories of these services.
# Contains date and time information of each service received.

# UserId: Customer number
# ServiceId: Anonymized services belonging to each category. (Example: Sofa washing service under the cleaning category)
# A ServiceId can be found under different categories and represents different services under different categories.
# (Example: The service with CategoryId 7 and ServiceId 4 is radiator cleaning, while the service with CategoryId 2 and ServiceId 4 is furniture assembly)
# CategoryId: These are anonymized categories. (Example: Cleaning, transportation, renovation category)
# CreateDate: Date the service was purchased

import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)
from mlxtend.frequent_patterns import apriori, association_rules


#############################
# TASK 1: Preparing the Data
#############################

# Step 1: Read your pear_data.csv file.

df_ = pd.read_csv("../materials/armut/armut_data.csv")
df = df_.copy()

# Step 2: ServiceID represents a different service for each CategoryID.
# Create a new variable to represent the services by combining ServiceID and CategoryID with "_".



# Step 3: The data set consists of the date and time the services were received, there is no basket definition (invoice, etc.).
# In order to apply Association Rule Learning, a basket (invoice, etc.) definition must be created.
# Here, the basket definition is the services that each customer receives monthly. For example; The customer with ID 7256 received a basket of 9_4, 46_4 services in the 8th month of 2017;
# The 9_4 and 38_4 services received in the 10th month of 2017 represent another basket. Carts must be identified with a unique ID.
# To do this, first create a new date variable that contains only the year and month. Add UserID and the date variable you just created to "_" 
# Assign it to a new variable named ID by combining it with #.



#############################
# TASK 2: Create Association Rules
#############################

# Step 1: Create the cart service pivot table as follows.

# Service 0_8 10_9 11_11 12_7 13_11 14_7 15_1 16_8 17_5 18_4..
# CartID
# 0_2017-08 0 0 0 0 0 0 0 0 0 0..
# 0_2017-09 0 0 0 0 0 0 0 0 0 0..
# 0_2018-01 0 0 0 0 0 0 0 0 0 0..
# 0_2018-04 0 0 0 0 0 1 0 0 0 0..
# 10000_2017-08 0 0 0 0 0 0 0 0 0 0..




# Step 2: Create association rules.



#Step 3: Use the arl_recommender function to recommend a service to a user who last received the 2_0 service.