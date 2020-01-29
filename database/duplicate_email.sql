SELECT Email
FROM (SELECT Email, COUNT(email) AS count_email
FROM Person
GROUP BY email) AS count_table
WHERE count_email > 1;

