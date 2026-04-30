/*
Problem: 1378 - Replace Employee ID With The Unique Identifier
Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
Difficulty: Easy
Category: Joins

Description:
Write a solution to show the unique ID of each user. If a user does not have a unique ID 
replace just show null. Return the result table in any order.

Optimization / Approach:
Implemented a `LEFT JOIN` originating from the `Employees` table. This relational operation 
guarantees that all primary employee records are preserved in the execution plan. Missing 
matches in the `EmployeeUNI` table naturally evaluate to `NULL` without requiring explicit 
conditional logic or computationally expensive subqueries.
*/

SELECT 
    EmployeeUNI.unique_id, 
    Employees.name
FROM Employees
LEFT JOIN EmployeeUNI 
    ON Employees.id = EmployeeUNI.id;