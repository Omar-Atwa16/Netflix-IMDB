SELECT '50s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_50s
UNION
SELECT '60s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_60s
UNION
SELECT '70s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_70s
UNION
SELECT '80s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_80s
UNION
SELECT '90s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_90s
UNION
SELECT '2000s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_00s
UNION
SELECT '2010s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_10s
UNION
SELECT '2020s' AS era, ROUND(AVG(rating), 2) AS avg_rating FROM Netflix_20s
ORDER BY avg_rating DESC