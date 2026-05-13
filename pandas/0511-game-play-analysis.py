"""
Problem: 0511 - Game Play Analysis I
Link: https://leetcode.com/problems/game-play-analysis-i/
Difficulty: Easy
Category: Aggregation

Description:
Write a solution to report the first login date for each player.
Return the result table in any order.

Approach:
Utilized Pandas vectorized grouping to aggregate data by `player_id`. The `.min()` 
function is applied to the `event_date` column to chronologically isolate the 
first occurrence of a login for each distinct player. The `as_index=False` parameter 
prevents the grouping key from becoming the DataFrame index, bypassing the need for 
a subsequent reset operation. The column is then mapped to the target schema using `.rename()`.

Complexity:
- Time: O(N), where N is the number of rows in the Activity dataframe.
- Space: O(U), where U is the number of unique players allocated for the resulting subset.
"""

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return (
        activity.groupby('player_id', as_index=False)['event_date']
        .min()
        .rename(columns={'event_date': 'first_login'})
    )