SELECT DISTINCT Salary as SecondHighestSalary
FROM Employee
ORDER BY Salary
LIMIT 1
OFFSET 1;
