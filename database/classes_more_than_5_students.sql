SELECT class
FROM (SELECT COUNT(DISTINCT student) as count_student, class
        FROM courses
        GROUP BY class) AS agg
WHERE count_student > 4;
