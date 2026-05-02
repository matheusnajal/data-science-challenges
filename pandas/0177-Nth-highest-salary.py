"""
Problem: 0177 - Nth Highest Salary
Link: https://leetcode.com/problems/nth-highest-salary/
Difficulty: Medium
Category: Sorting / Positional Indexing

Description:
Write a solution to find the nth highest salary from the Employee table. 
If there is no nth highest salary, return null.

Approach:
Extracted the 'salary' column, applied `.drop_duplicates()` to ensure absolute 
ranking, and sorted the values in descending order. Implemented defensive bounds 
checking to verify if the requested rank `N` exists within the dataset's dimensions 
(handling N <= 0 and N > total unique records). Extracted the target value using 
the `.iloc` positional indexer (zero-indexed, hence N - 1). Dynamically constructed 
the output DataFrame and column name to meet the specific platform schema requirements.

Complexity:
- Time: O(M log M), where M is the number of unique salaries in the DataFrame, driven by the `.sort_values()` operation.
- Space: O(M) allocated for the deduplicated and sorted Series in memory.
"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N <= 0 or N > len(unique_salary):
        result = None
    else:
        result = unique_salary.iloc[N - 1]
    
    new_column = f'getNthHighestSalary({N})'
    return pd.DataFrame({new_column: [result]})