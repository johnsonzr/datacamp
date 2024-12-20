-- Calculate the title and duration_hours from films
SELECT title, (duration / 60.0) as duration_hours
FROM films;

-- Calculate the percentage of people who are no longer alive
SELECT (Count(deathdate) * 100.0 )/ COUNT(*) AS percentage_dead
FROM people;

-- Find the number of decades in the films table
SELECT (MAX(release_year) - MIN(release_year)) / 10.0 AS number_of_decades
FROM films;