#####################################################
# Comparing Conversion of Bidding Methods with A/B Testing
#####################################################

#####################################################
# Business Problem
#####################################################

# Facebook recently introduced a new bidding type called "average bidding" as an alternative to the existing "maximum bidding" bidding type.
# One of our clients, bombabomba.com, has decided to test this new feature and wants to conduct an A/B test to determine whether "average bidding" brings more conversions than "maximum bidding."
# The A/B test has been ongoing for 1 month, and bombabomba.com now expects you to analyze the results of this A/B test.
# The ultimate success metric for bombabomba.com is "Purchase." Therefore, statistical tests should focus on the "Purchase" metric.

#####################################################
# Data Set Story
#####################################################

# This data set contains information from a company's website, including data about users' ad views, clicks on ads, and earnings generated from these data.
# There are two separate data sets for the control and test groups, "ab_testing_data.xlsx," and they are on different sheets in the Excel file. The control group used "Maximum Bidding," and the test group used "Average Bidding."

# Variables:
# impression: Number of ad views
# Click: Number of clicks on viewed ads
# Purchase: Number of products purchased after clicking on ads
# Earning: Earnings generated from the purchased products

#####################################################
# Project Tasks
#####################################################

#####################################################
# A/B Testing (Independent Two Sample T-Test)
#####################################################

# 1. Formulate Hypotheses
# 2. Assumption Checks
# - 1. Normality Assumption (Shapiro)
# - 2. Homogeneity of Variances (Levene)
# 3. Applying the Hypothesis
# - 1. If assumptions are met, perform an independent two-sample t-test
# - 2. If assumptions are not met, perform the Mann-Whitney U test
# 4. Interpret the results based on the p-value.
# Note:
# - If normality is not met, directly move to number 2. If homogeneity of variances is not met, enter 1 as an argument.

#####################################################
# Task 1: Data Preparation and Analysis
#####################################################

# Step 1: Read the data set consisting of control and test group data from "ab_testing_data.xlsx" and assign them to separate variables.

# Step 2: Analyze the control and test group data.

# Step 3: After the analysis, use the concat method to combine the control and test group data.

#####################################################
# Task 2: Defining the Hypothesis of A/B Testing
#####################################################

# Step 1: Define the hypothesis.

# Step 2: Analyze the purchase (earnings) averages for the control and test groups.

#####################################################
# Task 3: Conducting the Hypothesis Test
#####################################################

#####################################################
# A/B Testing (Independent Two Sample T-Test)
#####################################################

# Step 1: Before conducting the hypothesis test, perform assumption checks. These are the Normality Assumption and Homogeneity of Variances.

# Test whether the control and test groups satisfy the normality assumption for the "Purchase" variable separately.

# Step 2: Select the appropriate test based on the results of normality assumption and homogeneity of variances.

# Step 3: Interpret whether there is a statistically significant difference between the control and test group purchase averages based on the p-value.

#####################################################
# Task 4: Analysis of Results
#####################################################

# Step 1: Explain which test you used and provide the reasons.

# Step 2: Provide recommendations to the customer based on the test results.
