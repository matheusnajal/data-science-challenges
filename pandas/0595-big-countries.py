"""
Problem: 0595 - Big Countries
Link: https://leetcode.com/problems/big-countries/
Difficulty: Easy
Category: DataFrame Manipulation

Description:
A country is big if it has an area of at least three million km² or 
a population of at least twenty-five million. Write a solution to 
find the name, population, and area of the big countries.

Approach:
Utilized the Pandas `.loc` property to perform simultaneous boolean indexing 
and column subsetting in a single pass. This avoids the creation of intermediate 
DataFrame copies and prevents chained assignment overhead, significantly 
optimizing memory usage and processing time.

Complexity:
- Time: O(N) where N is the number of rows in the DataFrame.
- Space: O(N) for the memory allocated to the resulting filtered DataFrame.
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[
        (world['area'] >= 3000000) | (world['population'] >= 25000000), 
        ['name', 'population', 'area']
    ]