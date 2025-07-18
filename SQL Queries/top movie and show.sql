WITH topShow AS (
    SELECT TOP 1
        title,
        type,
        yearr,
        ROUND(rating, 2) AS rating
    FROM netflix
    WHERE type = 'SHOW'
    ORDER BY rating DESC
),

topMovie AS (
    SELECT TOP 1
        title,
        type,
        yearr,
        ROUND(rating, 2) AS rating
    FROM netflix
    WHERE type = 'MOVIE'
    ORDER BY rating DESC
)

SELECT * FROM TopShow
UNION
SELECT * FROM TopMovie;
