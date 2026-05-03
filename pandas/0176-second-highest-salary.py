"""
Problem: 0176 - Second Highest Salary
Link: https://leetcode.com/problems/second-highest-salary/
Difficulty: Medium
Category: Sorting / Positional Indexing

Description:
Write a solution to find the second highest distinct salary from the Employee table. 
If there is no second highest salary, return null.

Approach:
Extracted the 'salary' column and applied `.drop_duplicates()` to ensure absolute 
ranking. Utilized `.nlargest(2)` to extract the top two values, optimizing the time 
complexity compared to a full sort. Implemented defensive length validation to check 
if at least two distinct salaries exist. If true, the second element is extracted via 
the `.iloc[1]` positional indexer; otherwise, it assigns `None`. 

Complexity:
- Time: O(N), where N is the number of rows. Finding the top 2 elements via `.nlargest()` avoids the O(N log N) penalty of a full `.sort_values()`.
- Space: O(N) to store the deduplicated intermediate Series in memory.
"""

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    maiores = employee['salary'].drop_duplicates().nlargest(2)
    
    if len(maiores) == 2:
        segundo_maior = maiores.iloc[1]
    else:
        segundo_maior = None
        
    return pd.DataFrame({'SecondHighestSalary': [segundo_maior]})