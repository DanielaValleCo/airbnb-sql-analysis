# Airbnb NYC SQL Analysis

## Objective
Analyze Airbnb listing data in New York City to identify patterns in pricing, availability, and listing behavior.

---

## Tools used
- PostgreSQL
- pgAdmin
- Python (pandas, SQLAlchemy)
  
## Dataset
Public dataset of Airbnb listings (NYC, 2019) obtained from Kaggle.

Main variables:
- price
- neighbourhood_group
- room_type
- availability_365
- number_of_reviews

---

## Key Questions
- Which areas are the most expensive?
- What type of property is most common?
- Is there a relationship between price and availability?
- Which areas have the highest activity (reviews)?

---

## Approach
SQL queries were used to aggregate and analyze the data, focusing on:
- GROUP BY
- AVG()
- COUNT()
- Filtering and ranking

## Question 1 : How many listings are there?

SELECT COUNT(id) AS num_listings
FROM airbnb;

RESULT: 48,895 listings found in the dataset.
The dataset represents a large and competitive Airbnb market in New York City.

## How many unique hosts are there?

SELECT COUNT (DISTINCT host_id)
FROM airbnb;

RESULT: There are 37,457 unique hosts.
The high number of unique hosts suggest a decentralized market with many individual participants.

## How many different types of property are there?

SELECT COUNT(DISTINCT room_type) AS total_tipos_propiedades
FROM airbnb;

RESULT: There are 3 different types of property: Entire home/apt, shared room and private room.

## How many listings are there in total in Manhattan?
SELECT COUNT(name)
FROM airbnb
WHERE neighbourhood_group = 'Manhattan';

RESULT: There are 21,652 listings in Manhattan.

## All listings with a price greater than 200 
SELECT name
FROM airbnb
WHERE price::NUMERIC > 200;

RESULT: There are 8,384 listings with a price greater than 200
INSIGHT: Approximately **17% of listings** are priced above 200, indicating that while premium listings exist, the majority of the market is concentrated in lower price ranges.

## Listings in Brooklyn priced under 100
SELECT name AS listings_brooklyn_priceunder100
FROM airbnb
WHERE price::NUMERIC < 100 AND neighbourhood_group = 'Brooklyn';

RESULT: There are 10,904 listings in Brooklin priced under 100

## Listings priced between 50 and 150
SELECT COUNT(id) AS priced_50_150
FROM airbnb
WHERE price BETWEEN 50 AND 150;

RESULT: There are 28,930 listings priced between 50 and 150

## Listings whose name contains the word “park”
SELECT name 
FROM airbnb
WHERE name LIKE '%park%';

RESULT: There are 337 listings with the word park in its name.
Listings referencing "park" may highlight proximity to green areas, which can be a selling point.

## Listings where the name does NOT contain “room”
SELECT name
FROM airbnb 
WHERE name NOT LIKE '%room%';

RESULT: There are 35,810 listings that not contain the word "room" in its name.

## Average price of all listings
SELECT ROUND(AVG(price), 2)
FROM airbnb
WHERE price IS NOT NULL;

RESULT: The average price of all listings where the price is not null is 152.72

## Average price per room type
SELECT room_type, ROUND(AVG(price), 2)
FROM airbnb
WHERE price IS NOT NULL
GROUP BY room_type;

RESULT:
<img width="383" height="148" alt="image" src="https://github.com/user-attachments/assets/7219c454-1c5a-4312-8563-0f5c43e30b8d" />

## Number of listings per area (neighbourhood_group)
SELECT neighbourhood_group, COUNT(id)
FROM airbnb
GROUP BY neighbourhood_group;

RESULT:
<img width="318" height="205" alt="image" src="https://github.com/user-attachments/assets/2dd87a68-605c-4380-8ac1-9bb4283c4e78" />

## Top 5 areas with the most listings
SELECT neighbourhood, COUNT(id) 
FROM airbnb
GROUP BY neighbourhood
ORDER BY COUNT(id) DESC
LIMIT 5;

RESULT: 
<img width="376" height="208" alt="image" src="https://github.com/user-attachments/assets/7227183a-bebc-4e0e-883a-84a31fa8e1ef" />

## Most expensive area on average
SELECT neighbourhood AS most_expensive_peraverage, ROUND(AVG(price))
FROM airbnb
GROUP BY neighbourhood
ORDER BY ROUND(AVG(price)) DESC
LIMIT 1;

RESULT:
<img width="378" height="87" alt="image" src="https://github.com/user-attachments/assets/b1454374-0ac2-43fc-8cc0-937d6c56321b" />
The most expensive area is Fort Wadsworth priced 800 on average.

## Most common type of property
SELECT room_type AS most_common_typeroom, COUNT(id) AS num_listings
FROM airbnb
GROUP BY room_type
ORDER BY COUNT(id) DESC;

RESULT: 
<img width="393" height="145" alt="image" src="https://github.com/user-attachments/assets/4d41b0c2-4ecf-4390-9750-37cc007509f0" />
The most common type of property is Entire home/apartment with 25,409 listings


## Conclusion: 

I analyzed an Airbnb dataset using SQL, focusing on pricing distribution, listing concentration by aream and host behavior. I also identified that around 17% of listings belong to the premium segment, while the majority of the market is concentrated in more affordable ranges.
