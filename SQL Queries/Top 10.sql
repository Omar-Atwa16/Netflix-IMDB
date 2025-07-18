SELECT TOP 10
	title,
	yearr,
	ROUND(rating, 2) rating
FROM netflix 
ORDER BY rating DESC