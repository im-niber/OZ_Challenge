-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set address = 'seoul' where customerID = 12

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
update products set price = 10000 where productID = 4

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
update employees SET jobTitle = 'senior' WHERE employeeID = 13;

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices set phone = '123-456-7891' WHERE officeID = 123;

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET status = 'Shipped' WHERE orderID = 12

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails SET quantityOrdered = 3 WHERE orderID = 1325

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET amount = 3000 WHERE customerID = 1 AND paymentDate = '2024-03-01';

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET description = 'description1' WHERE productLine = 'Car';

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET email = 'john_updated@email.com' WHERE customerID = 1;

-- (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET price = 4000;


-- (1) **`employees`** 테이블에서 여러 직원의 부서를 한 번에 갱신하세요.
update employees set department = 'sales'

-- (2) **`offices`** 테이블에서 여러 사무실의 위치를 한 번에 갱신하세요.
update offices set address = 'seoul'

-- (3) **`orders`** 테이블에서 지난 달의 모든 주문의 배송 상태를 갱신하세요.
update orders set status = 'shipped' where orderDate BETWEEN '2024-03-01' and '2024-03-31'

-- (4) **`orderdetails`** 테이블에서 여러 주문 상세의 가격을 한 번에 갱신하세요.
update orderdetails set price = 19492

UPDATE orderdetails SET priceEach = priceEach * 0.9 WHERE orderID IN
(SELECT orderID FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-01-31');

-- (5) **`payments`** 테이블에서 특정 고객의 모든 지불 내역을 갱신하세요.
update payments set paid = False where customerID = 1

-- (6) **`productlines`** 테이블에서 여러 제품 라인의 설명을 한 번에 갱신하세요.
update productlines set decription = "hi" where productID in ('car', 'boat')

-- (7) **`customers`** 테이블에서 특정 지역의 모든 고객의 연락처를 갱신하세요.
update customers set contact = '01012341234' where address = 'busan'

-- (8) **`products`** 테이블에서 특정 카테고리의 모든 제품 가격을 갱신하세요.
update products set price = price + 3000 where productLine = 'car'

-- (9) **`employees`** 테이블에서 특정 직원의 모든 정보를 갱신하세요.
update employees set salary = salary + 5000, address = 'seoul', ... where employeeID = 3

-- (10) **`offices`** 테이블에서 특정 사무실의 모든 정보를 갱신하세요.
update offices set address = 'seoul', ... where officeID = 5



-- (1) **`orders`** 테이블에서 지난 해의 모든 주문 상태를 갱신하세요.
update orders set status = '1 years ago' where orderDate BETWEEN '2023-01-01' and '2023-12-31'

-- (2) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 갱신하세요.
update orderdetails set price = price * 1.1, orderDate = '2024-01-01', ...
where orderID = 32

-- (3) **`payments`** 테이블에서 지난 달의 모든 지불 내역을 갱신하세요.
update payments set ~~ where paymentDate BETWEEN '2024-03-01' and '2024-03-31'

-- (4) **`productlines`** 테이블에서 모든 제품 라인의 정보를 갱신하세요.
update productlines set ~~

UPDATE productlines SET textDescription = 'New updated description' WHERE productLine IN
(SELECT productLine FROM products WHERE quantityInStock < 10);

-- (5) **`customers`** 테이블에서 모든 고객의 주소를 갱신하세요.
update customers set address = 'busan'