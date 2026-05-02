/*
Problem: 0577 - Employee Bonus
Link: https://leetcode.com/problems/employee-bonus/
Difficulty: Easy
Category: Joins

Description:
Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
Return the result table in any order.

Optimization / Approach:
Implemented a `LEFT JOIN` using `Employee` as the driving table to ensure all employees are evaluated. 
The `WHERE` clause correctly handles the `NULL` condition for employees who do not have an associated 
record in the `Bonus` table, alongside the explicit `< 1000` numerical filter. This represents the 
standard and most robust execution plan for outer join conditional filtering.
*/

SELECT
    Employee.name,
    Bonus.bonus
FROM Employee
LEFT JOIN Bonus 
    ON Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 
   OR Bonus.bonus IS NULL;