"""
Problem: 0178 - Rank Scores
Link: https://leetcode.com/problems/rank-scores/
Difficulty: Medium
Category: Window Functions / Ranking

Description:
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
- The scores should be ranked from the highest to the lowest.
- If there is a tie between two scores, both should have the same ranking.
- After a tie, the next ranking number should be the next consecutive integer value (no gaps).
Return the result table ordered by score in descending order.

Approach:
Implemented a vectorized method chain. The `.rank(method='dense', ascending=False)` 
function natively satisfies the exact business rule for gapless, tied rankings. 
The `.assign()` method appends the new column dynamically, followed by `.sort_values()` 
to enforce the required descending output order. This single-pass execution is highly 
efficient and avoids intermediate variable assignments.

Complexity:
- Time: O(N log N), dictated by the underlying sorting and ranking algorithms.
- Space: O(N) allocated for the resulting DataFrame and the new rank column.
"""

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return (
        scores[['score']]
        .assign(rank=scores['score'].rank(method='dense', ascending=False))
        .sort_values(by='score', ascending=False)
    )