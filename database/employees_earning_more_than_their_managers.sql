SELECT e1.name AS employee
FROM Employee e1
JOIN Employee e2
ON e1.managerid = e2.id
WHERE e1.salary > e2.salary;
