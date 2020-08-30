SELECT e1.Name as Employee
fROM Employee e1
JOIN Employee e2
ON e1.Managerid = e2.Id
WHERE e1.Salary > e2.Salary;
