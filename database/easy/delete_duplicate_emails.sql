# Write your MySQL query statement below
DELETE
    p1
FROM
    Person p1,
    Person p2
WHERE
    p1.Email= p2.Email
AND
    P1.Id > p2.id;
