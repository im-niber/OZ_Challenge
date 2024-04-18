-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
delete from customers where cutomerID = 3
    
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE productID = 1;

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE employeeID = 1;

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE officeID = 1
    
-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
DELETE FROM orders WHERE orderID = 1;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderID = 1;

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE customerID = 1;

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productLine = 'Classic Cars';

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE city = 'San Francisco';

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE productLine = 'Classic Cars';


-- (1) **`employees`** 테이블에서 특정 부서의 모든 직원을 삭제하세요.
DELETE FROM employees WHERE department = 'Sales';

-- (2) **`offices`** 테이블에서 특정 국가의 모든 사무실을 삭제하세요.
DELETE FROM offices WHERE country = 'USA';

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문을 삭제하세요.
DELETE FROM orders WHERE orderDate BETWEEN '2022-12-01' AND '2022-12-31';

-- (4) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 삭제하세요.
DELETE FROM orderdetails WHERE orderID = 2;

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 삭제하세요.
DELETE FROM payments WHERE customerID = 2;

-- (6) **`productlines`** 테이블에서 여러 제품 라인을 한 번에 삭제하세요.
DELETE FROM productlines WHERE productLine IN ('Motorcycles', 'Planes');

-- (7) **`customers`** 테이블에서 가장 오래된 5명의 고객을 삭제하세요.
delete from customers order by createDate LIMIT 5;

DELETE FROM customers WHERE customerNumber IN 
(SELECT customerNumber FROM customers ORDER BY customerNumber LIMIT 5);
    
-- (8) **`products`** 테이블에서 재고가 없는 모든 제품을 삭제하세요.
delete from products where quantity <= 0
    
-- (9) **`employees`** 테이블에서 특정 직급의 모든 직원을 삭제하세요.
DELETE FROM employees WHERE jobTitle = 'Sales Rep';
    
-- (10)**`offices`** 테이블에서 가장 작은 사무실을 삭제하세요.
delete from offices order by size limit 1;
    

    
-- (1) **`orders`** 테이블에서 지난 해의 모든 주문을 삭제하세요.
delete from orders where orderDate BETWEEN '2023-01-01' and '2023-12-31'
    
-- (2) **`orderdetails`** 테이블에서 가장 적게 팔린 제품의 모든 주문 상세를 삭제하세요.
delete from orderdetails where orderID in
(select orderID, count(*) as total from orders group by orderID
order by total limit 1);

DELETE FROM orderdetails WHERE productID IN
(SELECT productID FROM products ORDER BY quantityInStock LIMIT 5);

-- (3) **`payments`** 테이블에서 특정 금액 이하의 모든 지불 내역을 삭제하세요.
delete from payments where price < 5000;
    
-- (4) **`productlines`** 테이블에서 제품이 없는 모든 제품 라인을 삭제하세요.
delete from productlines where productID NOT IN
(select productID from products)
    
DELETE FROM productlines WHERE productLine NOT IN 
(SELECT DISTINCT productLine FROM products);

-- (5) **`customers`** 테이블에서 최근 1년 동안 활동하지 않은 모든 고객을 삭제하세요.
delete from customers where lastDate < '2023-04-18'