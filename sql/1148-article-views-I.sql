/*
Problem: 1148 - Article Views I
Link: https://leetcode.com/problems/article-views-i/
Difficulty: Easy
Category: Basic Filtering

Description:
Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.

Optimization / Approach:
Utilized the `WHERE` clause to filter the dataset early in the execution plan based on 
the self-view condition (`author_id = viewer_id`). The `DISTINCT` keyword is applied 
to remove duplicate entries for authors with multiple self-views. Sorting is handled 
by `ORDER BY id`. Filtering before the resource-intensive distinct and sort operations 
ensures optimal memory efficiency.
*/

SELECT DISTINCT 
    author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;