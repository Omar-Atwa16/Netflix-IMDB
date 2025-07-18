SELECT 
  type,
  STDEV(rating) AS stddev_rating
FROM netflix
GROUP BY type
ORDER BY stddev_rating ASC;