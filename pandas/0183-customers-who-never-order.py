"""
Problem: 0183 - Customers Who Never Order
Link: https://leetcode.com/problems/customers-who-never-order/
Difficulty: Easy
Category: DataFrame Manipulation

Description:
Write a solution to find all customers who never order anything.
Return the result table in any order.

Approach:
Utilized the `.isin()` method combined with the bitwise NOT operator (`~`) to 
perform an efficient anti-join operation. The `.loc` accessor filters the rows 
and subsets the target column simultaneously. Finally, the `.rename()` method 
is chained to match the required output schema. This vectorized approach avoids 
costly merge operations and minimizes memory overhead.

Complexity:
- Time: O(N + M) where N is the number of customers and M is the number of orders.
- Space: O(N) for the resulting DataFrame in the worst-case scenario.
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[
        ~customers['id'].isin(orders['customerId']), 
        ['name']
    ].rename(columns={'name' : 'Customers'})