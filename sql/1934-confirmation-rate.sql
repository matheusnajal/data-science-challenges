/*
Problem: 1934 - Confirmation Rate
Link: https://leetcode.com/problems/confirmation-rate/
Difficulty: Medium
Category: Aggregation / Joins

Description:
The confirmation rate of a user is the number of 'confirmed' messages divided by the total 
number of requested confirmation messages. The confirmation rate of a user that did not request 
any confirmation messages is 0. Round the confirmation rate to two decimal places. Write a 
solution to find the confirmation rate of each user.

Optimization / Approach:
Implemented a `LEFT JOIN` establishing `Signups` as the driving table, ensuring all users 
are retained regardless of activity. The core optimization utilizes `AVG()` wrapping a `CASE` 
statement. By mapping 'confirmed' actions to 1.0 and all other states to 0.0, the average 
function natively computes the proportion ratio in a single execution pass. `COALESCE()` 
provides a safe fallback to 0 for users lacking transaction logs, effectively handling 
potential NULL outputs before the final `ROUND()` operation.
*/

SELECT 
    s.user_id,
    ROUND(
        COALESCE(
            AVG(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0.0 END), 
        0), 
    2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c 
    ON s.user_id = c.user_id
GROUP BY 
    s.user_id;