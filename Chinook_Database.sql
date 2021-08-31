SELECT Genre.Name AS Genre_Name,
	COUNT(Track.TrackId) AS Number_Purchased -- InvoiceLine.InvoiceId
FROM Track
	INNER JOIN Genre ON Track.GenreId = Genre.GenreId
	INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
WHERE Track.UnitPrice < 1
GROUP BY Genre.GenreId
HAVING COUNT(Track.TrackId) >= 10
ORDER BY Number_Purchased DESC;
-- One Genre has multiple tracks bought
-- How to order by multiple purchases
-- SELECT * FROM InvoiceLine;