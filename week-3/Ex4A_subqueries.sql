USE Northwind;

-- 1. What is the product name(s) of the most expensive products? 
SELECT ProductName,
       UnitPrice
FROM Products 
WHERE UnitPrice = (SELECT max(UnitPrice) FROM Products);

-- 2. What is the product name(s) and categories of the least expensive products?
SELECT p.ProductName, 
	   c.CategoryName,
       p.UnitPrice
FROM Products p 
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (SELECT min(UnitPrice) FROM Products);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"? 
SELECT OrderID,
       ShipName,
       ShipAddress
FROM Orders 
WHERE ShipVia = (SELECT ShipperID FROM Shippers WHERE CompanyName = 'Federal Shipping');

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `Order Details` 
WHERE ProductID = (SELECT ProductID FROM Products WHERE ProductName = 'Sasquatch Ale');
-- 5. What is the name of the employee that sold order 10266?
SELECT FirstName,
       LastName
FROM Employees
WHERE EmployeeID = (SELECT EmployeeID FROM Orders WHERE OrderID = 10266);

-- 6. What is the name of the customer that bought order 10266?
SELECT CompanyName AS 'Customer Name'
FROM Customers
WHERE CustomerID = (SELECT CustomerID FROM Orders WHERE OrderID = 10266);