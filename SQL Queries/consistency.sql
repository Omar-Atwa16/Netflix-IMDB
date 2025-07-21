SELECT 
	type,
	STDEV(rate) AS std_rating
FROM netflixv4
GROUP BY type
ORDER BY std_rating