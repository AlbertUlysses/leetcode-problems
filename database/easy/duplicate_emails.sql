# Write your MySQL query statement below
SELECT
    Email
FROM
    (
    SELECT
        COUNT(Email) AS tot,
        Email
    FROM
        Person
    GROUP BY
        Email
    ) t1
WHERE
    tot > 1;
