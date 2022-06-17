SELECT Users.name AS name, 
IF(SUM(Rides.distance) IS NULL, 0, SUM(Rides.distance)) AS travelled_distance
FROM
Users LEFT JOIN Rides
ON Users.id = Rides.user_id
GROUP BY Rides.user_id
ORDER BY travelled_distance DESC, name ASC;