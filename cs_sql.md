<link rel="stylesheet" href="styles.css">

### COMMANDS
SHOW DATABASES;
SHOW TABLES;
INSERT INTO table1 (field1, field2) VALUES (value1, value2);   NOTE THAT STRING MUST BE in ' '
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
UPDATE table1 SET field1=new_value1 WHERE condition;
DELETE FROM table_name WHERE condition;
ALTER TABLE scores REMOVE COLUMN 'old' to 'new'; (NOT NEED FOR '')

### Sql_0
SELECT DISTINCT
    CITY
FROM
    STATION
WHERE
    LOWER(SUBSTRING(CITY, -1, 1)) NOT IN ('a', 'e', 'u', 'i', 'o') AND
    LOWER(SUBSTRING(CITY, 1, 1)) NOT IN ('a', 'e', 'u', 'i', 'o')"
	
### Sql_0
SELECT
    FLOAT(LONG_W, 10, 4)
WHERE
    LAT_N > 38.7780
FROM
    STATION"

### Sql_0
SELECT
    ROUND(LONG_W, 4)
FROM
    STATION
WHERE
    LAT_N > 38.7780
ORDER BY
    LAT_N
LIMIT 1

### Sql_0
SET @a := (SELECT MIN(LAT_N ) FROM STATION);
SET @b := (SELECT MAX(LAT_N ) FROM STATION);

SET @c := (SELECT MIN(LONG_W ) FROM STATION);
SET @d := (SELECT MAX(LONG_W ) FROM STATION);

SET @distance = SQRT(POWER(@b - @a, 2) + POWER(@d - @c, 2));
SELECT ROUND(@distance, 4);

### Sql_0
SELECT
    LAT_N as t
FROM
    STATION
WHERE
    (SELECT COUNT(LAT_N) FROM STATION WHERE COUNT(LAT_N) > LAT_N) =
    (SELECT COUNT(LAT_N) FROM STATION WHERE COUNT(LAT_N) < LAT_N)
	
### Sql_0
SELECT
    (months * salary) AS max_earning,
    COUNT(*)
FROM 
    Employee
GROUP BY 1
ORDER BY
    max_earning DESC
LIMIT 1;

### Sql_0
SET @max_salary =
(
    SELECT
        MAX(months * salary)
    FROM
        Employee
);
SET @count_max_salary =
(
    SELECT COUNT(*)
    FROM Employee
    WHERE months * salary = @max_salary
);

SELECT CONCAT(@max_salary, ""  "", @count_max_salary)

### Sql_0
SELECT
    CITY.NAME
FROM
    CITY
INNER JOIN
    COUNTRY
ON
    CITY.COUNTRYCODE=COUNTRY.CODE &&
    COUNTRY.CONTINENT='Africa'"

### Sql_0
SELECT
    SUM(CITY.POPULATION)
FROM
    CITY
INNER JOIN
    COUNTRY
ON
    CITY.COUNTRYCODE=COUNTRY.CODE &&
    COUNTRY.CONTINENT='Asia'
	
### Sql_0
CREATE TABLE people (name VARCHAR(100), birthdate DATE, birthtime TIME, birthdt DATETIME);
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Padma', '1983-11-11', '10:07:35', '1983-11-11 10:07:35');
 
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Larry', '1943-12-25', '04:10:42', '1943-12-25 04:10:42');
 
SELECT * FROM people;

### Sql_0
SELECT title, released_year FROM books WHERE released_year >= 2004 && released_year <= 2015;
 
SELECT title, released_year FROM books 
WHERE released_year BETWEEN 2004 AND 2015;
 
SELECT title, released_year FROM books 
WHERE released_year NOT BETWEEN 2004 AND 2015;
 
SELECT CAST('2017-05-02' AS DATETIME);
 
show databases;
 
use new_testing_db;
 
SELECT name, birthdt FROM people WHERE birthdt BETWEEN '1980-01-01' AND '2000-01-01';
 
SELECT 
    name, 
    birthdt 
FROM people
WHERE 
    birthdt BETWEEN CAST('1980-01-01' AS DATETIME)
    AND CAST('2000-01-01' AS DATETIME);
	
### Sql_0
show databases();
use book_shop;
 
SELECT 
    title, 
    author_lname 
FROM books
WHERE author_lname='Carver' OR
      author_lname='Lahiri' OR
      author_lname='Smith';
 
SELECT title, author_lname FROM books
WHERE author_lname IN ('Carver', 'Lahiri', 'Smith');
 
SELECT title, released_year FROM books
WHERE released_year IN (2017, 1985);
 
SELECT title, released_year FROM books
WHERE released_year != 2000 AND
      released_year != 2002 AND
      released_year != 2004 AND
      released_year != 2006 AND
      released_year != 2008 AND
      released_year != 2010 AND
      released_year != 2012 AND
      released_year != 2014 AND
      released_year != 2016;

### Sql_0
SELECT title, released_year FROM books
WHERE released_year NOT IN 
(2000,2002,2004,2006,2008,2010,2012,2014,2016);
 
### Sql_0
SELECT title, released_year FROM books
WHERE released_year >= 2000
AND released_year NOT IN 
(2000,2002,2004,2006,2008,2010,2012,2014,2016);

### Sql_0 
SELECT title, released_year FROM books
WHERE released_year >= 2000 AND
released_year % 2 != 0;

### Sql_0
SELECT title, released_year FROM books
WHERE released_year >= 2000 AND
released_year % 2 != 0 ORDER BY released_year;"
"SELECT title, released_year,
       CASE 
         WHEN released_year >= 2000 THEN 'Modern Lit'
         ELSE '20th Century Lit'
       END AS GENRE
FROM books;

### Sql_0 
SELECT title, stock_quantity,
    CASE 
        WHEN stock_quantity BETWEEN 0 AND 50 THEN '*'
        WHEN stock_quantity BETWEEN 51 AND 100 THEN '**'
        ELSE '***'
    END AS STOCK
FROM books;
 
### Sql_0
SELECT title,
    CASE 
        WHEN stock_quantity BETWEEN 0 AND 50 THEN '*'
        WHEN stock_quantity BETWEEN 51 AND 100 THEN '**'
        ELSE '***'
    END AS STOCK
FROM books;

### Sql_0
SELECT title, stock_quantity,
    CASE 
        WHEN stock_quantity BETWEEN 0 AND 50 THEN '*'
        WHEN stock_quantity BETWEEN 51 AND 100 THEN '**'
        WHEN stock_quantity BETWEEN 101 AND 150 THEN '***'
        ELSE '****'
    END AS STOCK
FROM books;

### Sql_0 
SELECT title, stock_quantity,
    CASE 
        WHEN stock_quantity <= 50 THEN '*'
        WHEN stock_quantity <= 100 THEN '**'
        ELSE '***'
    END AS STOCK
FROM books;

### Sql_0SELECT 10 != 10;
 
### Sql_0
SELECT 15 > 14 && 99 - 5 <= 94;

### Sql_0 
SELECT 1 IN (5,3) || 9 BETWEEN 8 AND 10;
-- true
 
SELECT title, released_year FROM books WHERE released_year < 1980;
 
SELECT title, author_lname FROM books WHERE author_lname='Eggers' OR author_lname='Chabon';
 
SELECT title, author_lname FROM books WHERE author_lname IN ('Eggers','Chabon');
 
SELECT title, author_lname, released_year FROM books WHERE author_lname = 'Lahiri' && released_year > 2000;
 
SELECT title, pages FROM books WHERE pages >= 100 && pages <=200;
 
SELECT title, pages FROM books WHERE pages BETWEEN 100 AND 200;
 
### Sql_0
SELECT 
    title, 
    author_lname 
FROM books 
WHERE 
    author_lname LIKE 'C%' OR 
    author_lname LIKE 'S%';
 
SELECT 
    title, 
    author_lname 
FROM books 
WHERE 
    SUBSTR(author_lname,1,1) = 'C' OR 
    SUBSTR(author_lname,1,1) = 'S';
 
SELECT title, author_lname FROM books 
WHERE SUBSTR(author_lname,1,1) IN ('C', 'S');

### Sql_0
SELECT 
    title, 
    author_lname,
    CASE
        WHEN title LIKE '%stories%' THEN 'Short Stories'
        WHEN title = 'Just Kids' OR title = 'A Heartbreaking Work of Staggering Genius' THEN 'Memoir'
        ELSE 'Novel'
    END AS TYPE
FROM books;

### Sql_0
SELECT author_fname, author_lname,
    CASE 
        WHEN COUNT(*) = 1 THEN '1 book'
        ELSE CONCAT(COUNT(*), ' books')
    END AS COUNT
FROM books 
GROUP BY author_lname, author_fname;"
"

### Sql_0
-- IMPLICIT INNER JOIN
SELECT * FROM customers, orders 
WHERE customers.id = orders.customer_id;
-- IMPLICIT INNER JOIN

SELECT first_name, last_name, order_date, amount
FROM customers, orders 
    WHERE customers.id = orders.customer_id;
   
### Sql_0   
-- EXPLICIT INNER JOINS

SELECT * FROM customers
JOIN orders
    ON customers.id = orders.customer_id;
    
SELECT first_name, last_name, order_date, amount 
FROM customers
JOIN orders
    ON customers.id = orders.customer_id;

### Sql_0	
SELECT *
FROM orders
JOIN customers
    ON customers.id = orders.customer_id;"
"SELECT
    CONCAT(name, '(', SUBSTR(occupation, 1, 1), ')')
FROM
    OCCUPATIONS
ORDER BY
    name;

### Sql_0	
SELECT
    CONCAT('There are a total of ', count(occupation), ' ', LOWER(occupation), 's.')
FROM
    OCCUPATIONS
GROUP BY
    occupation
ORDER BY
    count(occupation),
    occupation"
"SELECT
    N as node_number, 
    CASE
        WHEN P IS NULL THEN ' Root'
        WHEN 0 = (SELECT COUNT(N) FROM BST WHERE P = XXX.N) THEN ' Leaf'
        ELSE ' Inner'
    END
FROM
    BST AS XXX
ORDER BY
    N"
"SELECT
    N as node_number, 
    CASE
        WHEN P IS NULL THEN ' Root'
        WHEN N IN (SELECT DISTINCT P FROM BST) THEN ' Inner'
        ELSE ' Leaf'
    END
FROM
    BST AS XXX
ORDER BY
    N"
"SELECT * FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id;
SELECT first_name, last_name, order_date, amount
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id; 
SELECT 
    first_name, 
    last_name,
    IFNULL(SUM(amount), 0) AS total_spent
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_spent;"

### Sql_0
SELECT ROUND(LAT_N, 4) FROM STATION AS XXX WHERE
    (
        (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > XXX.LAT_N) =
        (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < XXX.LAT_N)
    )
LIMIT 1
___
# The end