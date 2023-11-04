###################################################
# PROJECT: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# Business Problem
###################################################

# One of the most important problems in e-commerce is the accurate calculation of post-purchase ratings for products.
# Solving this problem means more customer satisfaction for the e-commerce website, increased visibility for sellers, and a seamless shopping experience for buyers.
# Another problem is the accurate sorting of product reviews. Misleading reviews coming to the forefront will directly affect the product's sales, resulting in both financial loss and customer loss.
# The solution to these two fundamental problems will increase sales for e-commerce websites and sellers, while providing a smooth shopping journey for customers.

###################################################
# Data Set Story
###################################################

# This data set contains Amazon product data, including product categories and various metadata.
# It contains user ratings and reviews for the product with the most reviews in the Electronics category.

# Variables:
# reviewerID: User ID
# asin: Product ID
# reviewerName: User Name
# helpful: Helpful rating score
# reviewText: Review
# overall: Product rating
# summary: Review summary
# unixReviewTime: Review time
# reviewTime: Raw review time
# day_diff: Number of days elapsed since the review
# helpful_yes: Number of times the review was found helpful
# total_vote: Total number of votes for the review

###################################################
# TASK 1: Calculate the Average Rating Based on Recent Reviews and Compare It with the Existing Average Rating.
###################################################

# In the shared data set, users have rated and reviewed a product.
# The aim of this task is to evaluate the given ratings by weighting them based on the date.
# A comparison should be made between the initial average rating and the weighted rating to be obtained based on the date.

###################################################
# Step 1: Read the Data Set and Calculate the Average Product Rating.
###################################################

###################################################
# Step 2: Calculate the Weighted Average Rating Based on the Date.
###################################################

###################################################
# Task 2: Determine the 20 Reviews That Will Be Displayed on the Product Detail Page for the Product.
###################################################

###################################################
# Step 1. Generate the helpful_no Variable.
###################################################

# Note:
# total_vote is the total number of up-down votes for a review.
# up means helpful.
# There is no helpful_no variable in the data set, so it needs to be generated using existing variables.

###################################################
# Step 2. Calculate the score_pos_neg_diff, score_average_rating, and wilson_lower_bound Scores and Add Them to the Data.
###################################################

###################################################
# Step 3. Determine the 20 Reviews and Interpret the Results.
###################################################
