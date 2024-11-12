-- Select fields from cities
SELECT name, country_code, city_proper_pop, metroarea_pop, 
    (city_proper_pop / metroarea_pop * 100) AS city_perc
-- Use subquery to filter city name
FROM (SELECT *
      FROM cities
      WHERE cities.country_code in 
        (SELECT code
         FROM countries
         WHERE (continent = 'Europe'
                OR continent LIKE '%America')
            AND capital = cities.name)) AS good_cities
-- Add filter condition such that metroarea_pop does not have null values
WHERE metroarea_pop IS NOT NULL
-- Sort and limit the result
ORDER BY city_perc DESC
LIMIT 10