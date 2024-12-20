-- Find top nine countries with the most cities
SELECT countries.name AS country, COUNT(*) AS cities_num 
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
-- Order by count of cities as cities_num
GROUP BY country
ORDER BY cities_num DESC, country 
-- Limit the results
LIMIT 9


SELECT countries.name AS country,
-- Subquery that provides the count of cities   
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;