/*
Problem: 1251 - Average Selling Price
Link: https://leetcode.com/problems/average-selling-price/
Difficulty: Easy
Category: Joins / Aggregation

Description:
Write a solution to find the average selling price for each product. 
average_price should be rounded to 2 decimal places. If a product does not have any sold units, 
its average selling price is assumed to be 0. Return the result table in any order.

Optimization / Approach:
Implemented a `LEFT JOIN` between `Prices` and `UnitsSold`. The key architectural choice 
is placing the temporal boundary condition (`purchase_date BETWEEN start_date AND end_date`) 
inside the `ON` clause. This preserves the outer join behavior, ensuring products with zero 
sales remain in the result set. The weighted average is calculated via `SUM(price * units) / SUM(units)`, 
wrapped in a `COALESCE` to default to 0 for orphaned records before applying the final `ROUND`.
*/

SELECT 
    Prices.product_id,
    ROUND(
        COALESCE(
            SUM(Prices.price * UnitsSold.units) / SUM(UnitsSold.units), 
        0), 
    2) AS average_price
FROM Prices
LEFT JOIN UnitsSold 
    ON Prices.product_id = UnitsSold.product_id 
    AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
GROUP BY 
    Prices.product_id;