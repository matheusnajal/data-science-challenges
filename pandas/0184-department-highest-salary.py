"""
Problem: 0184 - Department Highest Salary
Link: https://leetcode.com/problems/department-highest-salary/
Difficulty: Medium
Category: Aggregation / Joins

Description:
Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.

Approach:
Utilized the Pandas `.groupby().transform('max')` method to calculate the maximum 
salary within each department and broadcast it back to the original DataFrame's shape. 
This avoids an intermediate grouping DataFrame and a subsequent join. The dataset is 
then filtered via `.loc` where the employee's salary matches the departmental maximum. 
Finally, an `INNER JOIN` (`pd.merge`) is performed with the Department table to 
retrieve the department names, ensuring referential integrity before formatting the 
output columns.

Complexity:
- Time: O(N + M), where N is the number of employees and M is the number of departments. The group-by transform and merge operations are highly optimized in C.
- Space: O(N) to store the intermediate broadcasted maximums and the filtered resulting DataFrame.
"""

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')

    top_employees = employee.loc[employee['salary'] == employee['max_salary']]

    merged_df = pd.merge(
        left=top_employees, 
        right=department, 
        left_on='departmentId', 
        right_on='id', 
        how='inner',
        suffixes=('_emp', '_dept')
    )

    result = merged_df[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result