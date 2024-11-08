-- Query the sum of film durations
SELECT SUM(duration) AS total_duration
FROM films;

-- Calculate the average duration of all films
SELECT AVG(duration) as average_duration
FROM films;

-- Find the latest release_year
SELECT MAX(release_year) as latest_year
FROM films;

-- Find the duration of the shortest film
SELECT MIN(duration) as shortest_film
FROM films;