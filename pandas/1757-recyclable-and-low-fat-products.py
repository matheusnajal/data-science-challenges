"""
Problem: 1757 - Recyclable and Low Fat Products
Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
Difficulty: Easy
Category: DataFrame Manipulation

Description:
Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.

Approach:
Applied the Pandas `.loc` accessor to perform simultaneous boolean indexing 
with multiple conditions (using the bitwise AND operator `&`) and column subsetting. 
This execution in a single pass prevents chained assignment and avoids temporary 
DataFrame allocation, maintaining optimal performance.

Complexity:
- Time: O(N) where N is the number of rows in the DataFrame.
- Space: O(N) in the worst-case scenario where all products match the criteria.
"""

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), 
        ['product_id']
    ]