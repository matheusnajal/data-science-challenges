/*
Problem: 0595 - Big Countries
Link: https://leetcode.com/problems/big-countries/
Difficulty: Easy
Category: Basic Filtering

Description:
A country is big if it has an area of at least three million km² or 
a population of at least twenty-five million. Write a solution to 
find the name, population, and area of the big countries.

Optimization / Approach:
Utilized the `WHERE` clause with a logical `OR` operator to ensure a single 
table scan. This avoids the severe performance penalty, memory overhead, 
and implicit deduplication sorting associated with the `UNION` operator.
*/

SELECT 
    name,
    population,
    area
FROM World
WHERE area >= 3000000 
   OR population >= 25000000;