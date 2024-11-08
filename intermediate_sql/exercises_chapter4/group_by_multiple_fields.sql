-- Find the release_year, country, and max_budget, then group and order by release_year and country
SELECT release_year, country, MAX(budget) as max_budget
FROM films
GROUP BY release_year, country