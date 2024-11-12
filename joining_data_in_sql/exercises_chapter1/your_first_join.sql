-- Select name fields (with alias) and region 
SELECT cities.name as city, countries.name as country, region
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;