-- Part B

USE northwind;

-- Question 1
SELECT productID,
       productname,
       unitprice,
       unitsinstock
FROM products
ORDER BY unitprice DESC;

-- Question 2
SELECT customerid,
       companyname,
       contactname,
       country
FROM customers
ORDER BY country ASC, companyname ASC;

-- Question 3
SELECT categoryid,
		count(productid) AS productcount
FROM products 
GROUP BY categoryid
ORDER BY productcount DESC;

-- Question 4
SELECT orderid,
		round(sum(unitprice * quantity * (1 - discount)),2) AS revenue
FROM `order details`
GROUP BY orderid
ORDER BY revenue DESC;

-- Question 5
SELECT employeeid,
		count(orderid) AS ordercount
FROM orders
GROUP BY employeeid
HAVING count(orderid) > 50
ORDER BY ordercount DESC;

-- Question 6 
SELECT shipvia AS shipperid,
		count(orderid) AS ordercount
FROM orders
GROUP BY shipvia
ORDER BY shipvia ASC;

-- Question 7
SELECT p.productid, p.productname, c.categoryname
FROM products AS p
JOIN Categories AS c ON p.categoryid = c.categoryid
ORDER BY c.categoryname ASC, p.productname ASC;

-- Question 8
SELECT o.orderid, o.orderdate, c.companyname
FROM orders AS o
JOIN customers as c ON o.customerid = c.customerid
ORDER BY o.Orderdate DESC;

-- Question 9
SELECT c.categoryname, round(avg(p.unitprice),2) AS avgprice
FROM products AS p
JOIN categories AS c ON p.categoryid = c.categoryid
GROUP BY c.categoryid, c.categoryname
HAVING avg(p.unitprice) > 20
ORDER BY avgprice DESC;

-- Question 10
SELECT e.employeeid,
		e.firstname + ' ' + e.lastname as FullName,
        count(o.orderID) AS OrderCount
FROM employees AS e
JOIN orders AS o ON e.employeeid = o.employeeid
GROUP BY e.employeeid, e.firstname, e.lastname
HAVING count(o.orderid) >= 70
ORDER BY ordercount DESC, FullName ASC;