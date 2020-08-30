# Write your MySQL query statement below
SELECT Firstname, LastName, City, State
FROM Person p
LEFT JOIN Address a
ON p.PersonId = a.Personid;
