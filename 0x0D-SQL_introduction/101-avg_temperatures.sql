-- Calculate the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temp) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
