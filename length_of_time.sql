SELECT Artist.Name,
	sum(Milliseconds) / 1000.00 AS TotalTime
FROM (
		Artist
		INNER JOIN (
			Album
			INNER JOIN Track ON Album.AlbumId = Track.AlbumId
			AND Track.Milliseconds >= 180 * 1000 -- WHERE Track.Milliseconds < 180*1000
		) ON Artist.ArtistId = Album.ArtistId
	)
GROUP BY Artist.Name
HAVING Artist.Name LIKE '%C%'
ORDER BY TotalTime ASC;