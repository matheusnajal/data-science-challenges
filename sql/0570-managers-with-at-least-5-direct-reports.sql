/*
Problem: 0570 - Managers with at Least 5 Direct Reports
Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
Difficulty: Medium
Category: Aggregation / Subqueries

Description:
Write a solution to find managers with at least five direct reports.
Return the result table in any order.

Optimization / Approach:
Implemented a subquery with the `IN` clause. The inner query isolates the `managerId`s 
that meet the business rule (`COUNT(id) >= 5`) using the `HAVING` clause. The outer query 
then fetches the names associated with those IDs. Modern SQL optimizers execute this as 
a Semi-Join, which is highly memory-efficient as it avoids the Cartesian product risks 
and row duplication inherent to standard INNER JOINs in one-to-many relationships.
*/

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(id) >= 5
);