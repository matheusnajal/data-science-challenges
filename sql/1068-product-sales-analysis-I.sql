/*
Problem: 1068 - Product Sales Analysis I
Link: https://leetcode.com/problems/product-sales-analysis-i/
Difficulty: Easy
Category: Joins

Description:
Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
Return the resulting table in any order.

Optimization / Approach:
Implemented an `INNER JOIN` between the `Sales` and `Product` tables. Assuming strict 
referential integrity, this is the most performant execution plan. The database engine 
calculates only the exact intersection of both tables based on `product_id`, eliminating 
the computational overhead of preserving unmatched rows from the fact table.
*/

SELECT
    Product.product_name,
    Sales.year,
    Sales.price
FROM Sales
INNER JOIN Product 
    ON Product.product_id = Sales.product_id;