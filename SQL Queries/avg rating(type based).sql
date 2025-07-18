SELECT 
	type,
	ROUND(AVG(rating), 2) as avg_rating
FROM netflix
GROUP BY type
ORDER BY avg_rating DESC