-- List all records of the table second_table where name is not NULL, ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
