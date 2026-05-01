"""
Problem: 1667 - Fix Names in a Table
Link: https://leetcode.com/problems/fix-names-in-a-table/
Difficulty: Easy
Category: String Manipulation

Description:
Write a solution to fix the names so that only the first character is uppercase 
and the rest are lowercase. Return the result table ordered by user_id.

Approach:
Utilized the Pandas vectorized string method `.str.capitalize()`. This function natively 
handles the dual requirement of capitalizing the first letter and lowercasing the remainder 
of the string in a single optimized pass. The DataFrame is modified in place and then 
sorted using `.sort_values()` to meet the specific output ordering requirement.

Complexity:
- Time: O(N log N), heavily dominated by the `.sort_values()` operation. The string capitalization runs in O(N * C), where C is the maximum length of the names.
- Space: O(N) to store the modified strings in memory.
"""

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')