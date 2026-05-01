/*
Problem: 0197 - Rising Temperature
Link: https://leetcode.com/problems/rising-temperature/
Difficulty: Easy
Category: Joins / Date Manipulation

Description:
Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.

Optimization / Approach:
Implemented a Self-Join on the `Weather` table. The core architectural decision here 
is the use of `DATE_ADD(..., INTERVAL 1 DAY)` in the join condition. This mathematically 
enforces that records are only compared to their exact chronological predecessor. 
This approach is robust against missing data points (gaps in recorded dates), whereas 
window functions like `LAG()` would incorrectly compare non-consecutive days.
*/

SELECT w1.id
FROM Weather w1
JOIN Weather w2 
    ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;