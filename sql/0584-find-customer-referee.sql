/*
Problem: 0584 - Find Customer Referee
Link: https://leetcode.com/problems/find-customer-referee/
Difficulty: Easy
Category: Basic Filtering

Description:
Find the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.

Optimization / Approach:
Utilized the `WHERE` clause with a logical `OR` to explicitly handle SQL Three-Valued 
Logic (3VL). Standard comparison operators (`!=`) evaluate `NULL` as `UNKNOWN`, which 
filters them out by default. Adding `IS NULL` ensures all non-matching records, 
including those without a referee, are accurately retrieved during the table scan.
*/

SELECT 
    name 
FROM Customer 
WHERE referee_id != 2 
   OR referee_id IS NULL;