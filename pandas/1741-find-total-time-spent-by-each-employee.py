"""
Problem: 1741 - Find Total Time Spent by Each Employee
Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee/
Difficulty: Easy
Category: Aggregation / Math

Description:
Write a solution to calculate the total time in minutes spent by each employee on each day at the office. 
Note that within one day, an employee can enter and leave more than once. The time spent in the office 
for a single entry is out_time - in_time. Return the result table in any order.

Approach:
Utilized the mathematical equivalence Sum(Out) - Sum(In) = Sum(Out - In) to optimize the execution. 
By applying `.groupby().sum()` directly to the `in_time` and `out_time` columns, the dataframe is 
aggregated first. The subtraction to find the total time is then performed exclusively on the grouped 
results. This significantly reduces the total number of arithmetic operations compared to subtracting 
row-by-row before grouping. Finally, the columns are filtered and renamed to match the target schema.

Complexity:
- Time: O(N log N) or O(N) depending on the Pandas grouping hash map internal execution.
- Space: O(G), where G is the number of unique combinations of (emp_id, event_day) required to store the aggregated groups.
"""

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    grouped = employees.groupby(['emp_id', 'event_day'], as_index=False)[['in_time', 'out_time']].sum()
    grouped['total_time'] = grouped['out_time'] - grouped['in_time']

    return grouped[['event_day', 'emp_id', 'total_time']].rename(columns={'event_day': 'day'})