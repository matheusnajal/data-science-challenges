/*
Problem: 1757 - Recyclable and Low Fat Products
Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
Difficulty: Easy
Category: Basic Filtering

Description:
Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.

Optimization / Approach:
Direct row filtering utilizing the `WHERE` clause with a logical `AND` operator. 
This is the standard and most optimal method for exact-match conditional filtering 
at the database engine level, avoiding any unnecessary data retrieval before the 
result set is materialized.
*/

SELECT 
    product_id
FROM Products
WHERE low_fats = 'Y' 
  AND recyclable = 'Y';