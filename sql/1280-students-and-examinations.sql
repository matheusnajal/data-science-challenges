/*
Problem: 1280 - Students and Examinations
Link: https://leetcode.com/problems/students-and-examinations/
Difficulty: Easy
Category: Joins / Aggregation

Description:
Write a solution to find the number of times each student attended each exam. 
Return the result table ordered by student_id and subject_name.

Optimization / Approach:
Utilized a `CROSS JOIN` between the `Students` and `Subjects` tables to establish 
a complete dimensional matrix, guaranteeing that every possible student-subject 
combination exists in the baseline result set. A `LEFT JOIN` is then executed against 
the `Examinations` fact table based on a composite key. Applying `COUNT()` specifically 
to `Examinations.subject_name` ensures that missing exam records mathematically 
evaluate to 0, avoiding the computational overhead of explicit null-handling functions.
*/

SELECT
    Students.student_id,
    Students.student_name,
    Subjects.subject_name,
    COUNT(Examinations.subject_name) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations 
    ON Students.student_id = Examinations.student_id
    AND Subjects.subject_name = Examinations.subject_name
GROUP BY 
    Students.student_id,
    Students.student_name,
    Subjects.subject_name
ORDER BY 
    Students.student_id, 
    Subjects.subject_name;