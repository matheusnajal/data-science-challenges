/*
Problem: 0620 - Not Boring Movies
Link: https://leetcode.com/problems/not-boring-movies/
Difficulty: Easy
Category: Basic Filtering

Description:
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by rating in descending order.

Optimization / Approach:
Implemented a highly optimized filtering logic using the bitwise AND operator (`id & 1`) 
to evaluate odd numbers. This approach is computationally cheaper than standard modulo 
arithmetic (`id % 2 != 0`), executing faster at the CPU level during the required 
Table Scan. Combined with a standard exclusion filter and descending sort to strictly 
meet the business requirements.
*/

SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE id & 1 
  AND description != 'boring'
ORDER BY rating DESC;