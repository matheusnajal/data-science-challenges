"""
Problem: 1795 - Rearrange Products Table
Link: https://leetcode.com/problems/rearrange-products-table/
Difficulty: Easy
Category: Data Reshaping / Unpivoting

Description:
Write a solution to rearrange the Products table so that each row has (product_id, store, price). 
If a product is not available in a store, do not include a row with that product_id and store 
combination in the result table.

Approach:
Utilized the `.set_index()` and `.stack()` chain to unpivot the wide-format table into a long-format. 
This is a highly optimized architectural choice because `.stack()` inherently drops `NaN` values 
during the reshaping process, naturally satisfying the business requirement to exclude missing 
store inventories without requiring an explicit `.dropna()` pass. `.reset_index()` flattens 
the MultiIndex, and the columns are mapped to the target output schema.

Complexity:
- Time: O(N * S), where N is the number of rows and S is the number of store columns being stacked.
- Space: O(N * S) to allocate the reshaped DataFrame in memory.
"""

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    stacked = products.set_index('product_id').stack().reset_index()
    stacked.columns = ['product_id', 'store', 'price']
    
    return stacked