/*
Problem: 1661 - Average Time of Process per Machine
Link: https://leetcode.com/problems/average-time-of-process-per-machine/
Difficulty: Easy
Category: Aggregation

Description:
Write a solution to find the average time each machine takes to complete a process.
The time to complete a process is the 'end' timestamp minus the 'start' timestamp. 
The average time is calculated by the total time to complete every process on the machine 
divided by the number of processes that were run. Return the result table with the average 
processing time rounded to 3 decimal places.

Optimization / Approach:
Implemented conditional aggregation to calculate the average processing time. 
This is a highly optimized architectural decision. By leveraging the mathematical 
property that Sum(End - Start)/N equals (Sum(End)/N) - (Sum(Start)/N), the query 
avoids expensive Self-Joins. The database computes the result in a single table 
scan, using `CASE WHEN` inside the `AVG()` function to separate and aggregate 
timestamps by activity type.
*/

SELECT 
    machine_id,
    ROUND(
        AVG(CASE WHEN activity_type = 'end' THEN timestamp END) - 
        AVG(CASE WHEN activity_type = 'start' THEN timestamp END), 
    3) AS processing_time
FROM Activity
GROUP BY machine_id;