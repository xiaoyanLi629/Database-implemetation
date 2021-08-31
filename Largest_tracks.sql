SELECT upper(Artist.Name) AS UPPER_NAME,
	MAX(Track.Bytes) AS MEMORY_SIZE -- Track.Bytes also works
FROM Artist
	INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
	INNER JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Artist.ArtistId -- GROUP BY Artist.ArtistId HAVING MAX(Track.Bytes)
ORDER BY Bytes DESC
LIMIT 10;