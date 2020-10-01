# Write your MySQL query statement below
SELECT Email
FROM (
    SELECT COUNT(Email) total, Email
    FROM Person p
    GROUP BY Email
    ) E
WHERE total >= 2;
