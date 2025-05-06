-- Lists all bands with Glam rock as main style, ranked by their lifespan until 2022
SELECT band_name,
       IF(split IS NULL OR split = 0, 2022 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
