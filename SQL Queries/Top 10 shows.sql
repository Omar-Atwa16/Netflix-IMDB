SELECT TOP 10
	title,
	type,
	year,
	ROUND(rate, 2) rate
FROM netflixv4
WHERE type = 'SHOW'
ORDER BY rate DESC