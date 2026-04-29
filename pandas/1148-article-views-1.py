"""
Problem: 1148 - Article Views I
Link: https://leetcode.com/problems/article-views-i/
Difficulty: Easy
Category: DataFrame Manipulation

Description:
Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.

Approach:
Applied a vectorized method chain. Utilized the `.loc` accessor to filter records 
where `author_id` equals `viewer_id` while subsetting the target column. Chained 
`.drop_duplicates()` to guarantee unique records, `.rename()` to map to the output 
schema, and `.sort_values()` to meet the ascending order requirement. This avoids 
allocating intermediate variables.

Complexity:
- Time: O(N log N), heavily dominated by the `.sort_values()` operation on the filtered set. 
  The initial scan and deduplication run in O(M) where M is the total number of rows.
- Space: O(N) where N is the memory allocated for the final filtered DataFrame.
"""

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[
        views['author_id'] == views['viewer_id'], 
        ['author_id']
    ].drop_duplicates().rename(columns={'author_id' : 'id'}).sort_values('id')