-- Jonathan Lopez
-- April 20, 2026
-- SHOW DATABASES;

USE northwind;
SHOW TABLES;
SELECT ProductName, UnitPrice
FROM Products;
SELECT *
FROM Products;
SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock As 'Stock'
FROM Products;
-- Retrieve all CompanyName, City, and Country for Germany
SELECT CompanyName, City, Country
FROM Customers
WHERE Country = 'Germany';
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;
SELECT OrderID, CustomerID, ShipCountry, Freight
FROM Orders
WHERE ShipCountry = 'France';
SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;
SELECT OrderID, Freight 
FROM Orders
WHERE freight >= 100;
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;
SELECT CompanyName, Country
FROM customers
WHERE country = 'UK' OR 'Ireland';
SELECT categoryID, UnitPrice
FROM Products
WHERE ( CategoryID = 1 OR CategoryID = 2 )
AND UnitPrice < 20;
SELECT CompanyName, Country
FROM Customers
WHERE Country != 'U.S.A';
SELECT ProductName
FROM Products
WHERE Discontinued != 1;
SELECT CompanyName, Country
FROM Customers
WHERE Country IN ( 'France' , 'Germany' , 'Spain');
SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN ( 1,2,3);
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;
SELECT OrderID, CustomerId, ShipRegion
FROM Orders
WHERE ShipRegion is NULL;
SELECT FirstName, LastName, Region
FROM Employees
WHERE Region is NOT NULL;
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';
SELECT OrderID, CustomerID, OrderDate
FROM Orders
WHERE OrderDate = '1997-01-01';
SELECT OrderID, OrderDate
FROM Orders
WHERE YEAR(OrderDate) = 1997 AND MONTH(OrderDate) = 6;
SELECT ProductName, UnitPrice
FROM Products
ORDER BY ProductName AND UnitPrice DESC;
SELECT CompanyName, Country, City
FROM Customers
ORDER BY Country ASC, CompanyName ASC;
SELECT ProductName, UnitPrice
FROM Products
order by UnitPrice DESC
LIMIT 5;
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5, 5;
SELECT DISTINCT Country
FROM Customers
ORDER BY Country;
SELECT distinct Country, City
from Customers
order by Country, City;
select concat(FirstName, ' ', LastName) AS 'Full Name',
Title
from Employees;
select ProductName, UnitPrice AS 'Original Price', UnitPrice*0.90 AS '10% Discount'
from Products
Order by ProductName ASC;