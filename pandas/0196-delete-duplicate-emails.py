"""
Problem: 0196 - Delete Duplicate Emails
Link: https://leetcode.com/problems/delete-duplicate-emails/
Difficulty: Easy
Category: Data Mutation / Deduplication

Description:
Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
For Pandas users, please note that you are supposed to modify Person in place.

Approach:
Utilized in-place data mutation to satisfy the strict memory-reference constraints of the problem. 
First, the DataFrame is sorted by `id` in ascending order (`inplace=True`). Subsequently, 
`.drop_duplicates()` is applied on the `email` subset. By specifying `keep='first'`, the algorithm 
retains the first occurrence of each email (which, post-sort, corresponds to the minimum `id`) and 
discards the rest. The operation is performed directly on the original object in memory.

Complexity:
- Time: O(N log N), dictated by the `.sort_values()` operation. The deduplication pass runs in O(N).
- Space: O(1) auxiliary space, as operations are strictly executed in place.
"""

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)