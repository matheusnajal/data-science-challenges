/*
Problem: 1581 - Customer Who Visited but Did Not Make Any Transactions
Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
Difficulty: Easy
Category: Joins / Aggregation

Description:
Write a solution to find the IDs of the users who visited without making any transactions 
and the number of times they made these types of visits. Return the result table sorted in any order.

Optimization / Approach:
Implemented an Anti-Join pattern. The `LEFT JOIN` preserves all records from the `Visits` table. 
The `WHERE Transactions.transaction_id IS NULL` clause efficiently filters out the visits that 
resulted in a transaction. Finally, `GROUP BY` aggregates the remaining orphaned records to 
count the occurrences per customer. This avoids computationally expensive `NOT IN` subqueries.
*/

SELECT
    Visits.customer_id,
    COUNT(Visits.visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions 
    ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id;