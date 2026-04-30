"""
Problem: 1683 - Invalid Tweets
Link: https://leetcode.com/problems/invalid-tweets/
Difficulty: Easy
Category: String Manipulation

Description:
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the 
number of characters used in the content of the tweet is strictly greater than 15.

Approach:
Utilized the Pandas `.str.len()` vector-based accessor to evaluate the string length 
of each tweet. This method inherently calculates character count (Unicode-safe) rather 
than byte count, preventing inaccurate evaluations. The condition is passed directly 
into `.loc` for simultaneous boolean indexing and column subsetting, avoiding chained 
assignments and maintaining optimal memory usage.

Complexity:
- Time: O(N * C) where N is the number of rows and C is the average character length of the tweets.
- Space: O(N) in the worst-case scenario where all tweets are invalid.
"""

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[
        tweets['content'].str.len() > 15, 
        ['tweet_id']
    ]