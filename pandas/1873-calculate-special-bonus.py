"""
Problem: 1873 - Calculate Special Bonus
Link: https://leetcode.com/problems/calculate-special-bonus/
Difficulty: Easy
Category: Conditional Feature Engineering

Description:
Calculate the bonus of each employee. The bonus is 100% of their salary if the ID of the 
employee is an odd number and the employee's name does not start with the character 'M'. 
The bonus of an employee is 0 otherwise. Return the result table ordered by employee_id.

Approach:
Initialized a default `bonus` column with a scalar value of 0. Utilized the `.loc` accessor 
with vectorized boolean masks: the modulo operator (`%`) isolates odd IDs, and the string 
method `.str.startswith()` combined with the bitwise NOT operator (`~`) filters the names. 
The matching rows are then updated with the `salary` values in place. This approach strictly 
avoids row-by-row iteration (e.g., `.apply()`), ensuring fast execution.

Complexity:
- Time: O(N log N), dictated by the `.sort_values()` operation. The conditional assignment runs in O(N).
- Space: O(N) to store the result set and intermediate boolean masks.
"""

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0

    employees.loc[
        (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 
        'bonus'
    ] = employees['salary']

    return employees[['employee_id', 'bonus']].sort_values('employee_id')