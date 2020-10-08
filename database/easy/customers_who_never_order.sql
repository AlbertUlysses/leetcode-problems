# Write your MySQL query statement below
SELECT 
    Name as Customers
FROM 
    Customers c
LEFT JOIN 
    Orders o
ON 
    c.id = o.CustomerId
WHERE 
    CustomerId is Null;
