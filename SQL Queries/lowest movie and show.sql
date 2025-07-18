WITH lowShow AS (
    SELECT TOP 1
        title,
        type,
        yearr,
        ROUND(rating, 2) AS rating
    FROM netflix
    WHERE type = 'SHOW'
    ORDER BY rating ASC
),

lowMovie AS (
    SELECT TOP 1
        title,
        type,
        yearr,
        ROUND(rating, 2) AS rating
    FROM netflix
    WHERE type = 'MOVIE'
    ORDER BY rating ASC
)

SELECT * FROM lowShow
UNION
SELECT * FROM lowMovie;
