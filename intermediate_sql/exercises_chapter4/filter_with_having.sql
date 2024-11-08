-- Select the country and distinct count of certification as certification_count
SELECT country, Count(DISTINCT certification) as certification_count
FROM films
-- Group by country
GROUP BY country
-- Filter results to countries with more than 10 different certifications
HAVING Count(DISTINCT certification) > 10