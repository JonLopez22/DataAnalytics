USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells. (Hint: To help set up your query, look at the schema preview to see what column names belong to each table. Or use SELECT * to query all columns first, then refine your query to just the columns you want.)
SELECT ProductID, ProductName, UnitPrice
FROM Products;
SELECT *
FROM Products;

-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;

-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;

-- 4. Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry.
SELECT ProductID, ProductName, CategoryID
FROM Products;
SELECT CategoryID, CategoryName, Description
FROM Categories;
SELECT p.ProductID, p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';
-- 5. Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.
SELECT ProductID,ProductName, SupplierID
FROM Products;
SELECT SupplierID, CompanyName, Country
FROM Suppliers;
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';
SELECT p.ProductID, p.ProductName, s.SupplierID
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE s.CompanyName = 'Tokyo Traders';
-- 6. How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question.
SELECT EmployeeID, FirstName, LastName
FROM Employees;
SELECT EmployeeID, FirstName, LastName, Title
FROM Employees
WHERE Title = 'Sales Manager';