-- Select the country and average_budget from films
SELECT country, ROUND(AVG(budget), 2) AS average_budget
FROM films
-- Group by country
GROUP BY country 
-- Filter to countries with an average_budget of more than one billion
HAVING ROUND(AVG(budget), 2) > 1000000000
-- Order by descending order of the aggregated budget
ORDER BY average_budget DESC