CREATE DATABASE zomato;
use zomato;
CREATE TABLE restaurants(

RestaurantID INT,

RestaurantName VARCHAR(100),

City VARCHAR(50),

Cuisine VARCHAR(100),

Rating FLOAT,

Votes INT,

AverageCost INT,

OnlineDelivery VARCHAR(10)

);

SELECT COUNT(*) FROM restaurants;

SELECT City,

COUNT(*) TotalRestaurants

FROM restaurants

GROUP BY City

ORDER BY TotalRestaurants DESC;

SELECT Cuisine,

COUNT(*)

FROM restaurants

GROUP BY Cuisine

ORDER BY COUNT(*) DESC;

SELECT AVG(Rating)

FROM restaurants;

SELECT RestaurantName,

Rating

FROM restaurants

ORDER BY Rating DESC

LIMIT 10;