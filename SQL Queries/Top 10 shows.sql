SELECT TOP 10
	title,
	type,
	yearr,
	ROUND(rating, 2) rating
FROM netflix 
WHERE type = 'SHOW'
ORDER BY rating DESC