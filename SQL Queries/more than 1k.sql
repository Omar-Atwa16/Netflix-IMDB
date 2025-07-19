SELECT 'Less than 1000 votes' Category,
COUNT(id) count
FROM netflix
WHERE votes < 1000

UNION ALL

SELECT 
	'1000 or more votes',
	COUNT(id)
FROM netflix
WHERE votes >= 1000;
