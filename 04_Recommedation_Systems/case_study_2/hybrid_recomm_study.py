#######################
# PROJECT: Hybrid Recommender System
#######################

# Make a prediction using the item-based and user-based recommender methods for the user whose ID is given.
# Consider 5 suggestions from the user-based model, 5 suggestions from the item-based model, and finally make 10 suggestions from 2 models.

#######################
# Task 1: Preparation of Data
#######################


# Step 1: Read the Movie and Rating data sets.
# dataset containing movieId, movie name and movie genre information


# Data set containing UserID, movie name, vote for the movie and time information



# Step 2: Add the names and genres of the movies to the rating data set using the movie movie set.
# Only the IDs of the movies voted by users in the rating are available.
# We add the movie names and genres of the ids from the movie data set.



# Step 3: Calculate how many people voted for each movie. Remove movies with less than 1000 votes from the data set.
# We calculate how many people voted for each movie.


# We keep the names of movies with less than 1000 votes in rare_movies.
# And we subtract it from the data set



# Step 4: # The index contains userIDs, movie names in the columns and ratings as values.
# Create a pivot table for the dataframe.



# Step 5: Let's functionalize all the above operations



#######################
# Task 2: Determining the Movies Watched by the User to Make a Recommendation
#######################

# Step 1: Choose a random user ID.


# Step 2: Create a new dataframe named random_user_df consisting of observation units of the selected user.


# Step 3: Assign the movies voted by the selected user to a list named movies_watched.

#######################
# Task 3: Accessing the Data and IDs of Other Users Watching the Same Movies
#######################

# Step 1: Select the columns of the movies watched by the selected user from user_movie_df and create a new dataframe called movies_watched_df.


# Step 2: Create a new dataframe named user_movie_count, which contains information about how many movies each user watched that the selected user watched.
# And we create a new df.


# Step 3: We consider those who watched 60 percent or more of the movies voted by the selected user as similar users.
# Create a list named users_same_movies from the ids of these users.




#######################
# Task 4: Determining the Users Most Similar to the User to Make a Recommendation
#######################

# Step 1: Filter the movies_watched_df dataframe to find the IDs of users that are similar to the selected user in the user_same_movies list.


# Step 2: Create a new corr_df dataframe in which the correlations of users with each other will be found.


#corr_df[corr_df["user_id_1"] == random_user]



# Step 3: Create a new dataframe named top_users by filtering out users with a high correlation (over 0.65) with the selected user.


# Step 4: Merge the top_users dataframe with the rating data set




#######################
# Task 5: Calculating the Weighted Average Recommendation Score and Keeping the Top 5 Movies
#######################

# Step 1: Create a new variable named weighted_rating, which is the product of each user's corr and rating values.


# Step 2: Create a new file called recommendation_df, which contains the movie id and the average value of the weighted ratings of all users for each movie.
# create dataframe.


# Step 3: Step3: Select the movies with a weighted rating greater than 3.5 in recommendation_df and sort them according to the weighted rating.
# Save the first 5 observations as movies_to_be_recommend.


# Step 4: Bring the names of the 5 recommended movies.




#######################
# Step 6: Item-Based Recommendation
#######################

# Make an item-based suggestion based on the name of the movie the user last watched and gave the highest rating.
user = 108170

# Step 1: Read the movie,rating data sets.

# Step 2: Get the ID of the movie with the most current score among the movies that the user to be recommended gave 5 points.

# Step 3: Filter the user_movie_df dataframe created in the User based recommendation section according to the selected movie id.


# Step 4: Using the filtered dataframe, find the correlation between the selected movie and other movies and rank them.


# Step 5: Give the first 5 movies as suggestions, apart from the selected movie itself.