"""
Problem: 1907 - Count Salary Categories
Link: https://leetcode.com/problems/count-salary-categories/
Difficulty: Medium
Category: Aggregation / Categorization

Description:
Write a solution to calculate the number of bank accounts for each salary category. 
The salary categories are:
- "Low Salary": All the salaries strictly less than $20000.
- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
- "High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a 
category, return 0.

Approach:
Utilized boolean masking to evaluate the specific conditions for each salary tier. 
Applying `.sum()` on a boolean Series mathematically evaluates `True` as 1 and `False` 
as 0, effectively counting the matching records. Constructing a new DataFrame manually 
ensures that all three required categories are explicitly present in the output, 
preventing the missing-category errors common with dynamic grouping methods.

Complexity:
- Time: O(N), where N is the number of rows. The code performs three O(N) vectorized scans over the Series.
- Space: O(1) auxiliary space, or O(N) if considering the memory allocated for the intermediate boolean masks.
"""

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = (accounts['income'] < 20000).sum()
    avg_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()

    return pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [low_count, avg_count, high_count]
        })