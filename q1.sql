show variables like 'event%';

show databases;
use world;

select * from country;
select distinct(Continent), count(Continent) as Count from country group by Continent;
select count(distinct(Continent)) from country;
select * from countrylanguage;
select * from city;

SELECT Code,Name,Continent
FROM country
WHERE Code NOT IN (SELECT CountryCode FROM city);

SELECT A.code,A.Name, A.Continent
FROM country as A 
WHERE NOT EXISTS (SELECT 1 FROM city B WHERE A.Code = B.CountryCode);

SELECT A.code,A.Name, A.Continent
FROM country as A
LEFT JOIN city as B ON A.Code = B.CountryCode
WHERE B.CountryCode IS NULL;

-- The reason why the first query returns extra null row values is because of the way NOT IN clause works.

-- When you use NOT IN clause, it checks if the value is not present in the list of values returned by the subquery. However, if the subquery returns a null value, the NOT IN clause will return null for all rows, because null is not equal to any value, including null.

-- In your case, the subquery (SELECT CountryCode FROM city) might be returning null values, which are then being compared to the Code column in the country table. Since null is not equal to any value, the NOT IN clause is returning null for all rows where the Code column is not present in the list of values returned by the subquery.

-- On the other hand, the NOT EXISTS clause and the LEFT JOIN with IS NULL condition do not have this issue, because they are checking for the existence of a matching row, rather than checking if a value is not present in a list.

-- In the NOT EXISTS clause, the subquery is checking if there exists a row in the city table where the CountryCode matches the Code column in the country table. If no such row exists, the NOT EXISTS clause returns true, and the row is included in the result set.

-- Similarly, in the LEFT JOIN with IS NULL condition, the join is checking if there is a matching row in the city table where the CountryCode matches the Code column in the country table. If no such row exists, the IS NULL condition returns true, and the row is included in the result set.

-- So, to summarize, the NOT IN clause can return null values if the subquery returns null values, while the NOT EXISTS clause and the LEFT JOIN with IS NULL condition do not have this issue.






