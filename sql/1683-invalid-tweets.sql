/*
Problem: 1683 - Invalid Tweets
Link: https://leetcode.com/problems/invalid-tweets/
Difficulty: Easy
Category: String Functions

Description:
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the 
number of characters used in the content of the tweet is strictly greater than 15.

Optimization / Approach:
Utilized the `CHAR_LENGTH()` function to perform the string evaluation. This is 
a critical architectural choice over `LENGTH()`, as `CHAR_LENGTH()` counts characters 
rather than bytes, ensuring correct evaluation for multi-byte Unicode characters 
(such as emojis or accented letters) common in social media text data.
*/

SELECT
    tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;