-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
INSERT into customers (name, address) VALUES ('name1', 'busan');
-- (2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT into products (name, price) VALUES ('name1', '5000');
-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT into employees (name, address) VALUES ('name1', 'busan');
-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT into offices (name, address) VALUES ('name1', 'busan');
-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT into orders (orderID, productName) VALUES ('1234', 'apple');
-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
INSERT into orderdetails (orderID, productName) VALUES ('1234', 'apple');
-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT into payments (paymentID, price) VALUES ('123213', '5000');
-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
INSERT into productlines (productLine, productName) VALUES ('linename', 'productname');
-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT into customers (name, address) VALUES ('name2', 'seoul');
-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT into products (name, price, category) VALUES ('name12', '54000', 'fruit');


-- (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
INSERT into customers (name, address)
VALUES ('name2', 'seoul'),
       ('name23', 'busan');

-- (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
INSERT into products (name, price)
VALUES ('name1', '5000'),
       ('name2', '6000');

-- (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
INSERT into employees (name, address)
VALUES ('name1', 'busan'),
        ('name2', 'seoul');

-- (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.
INSERT into orders (orderID, productName) VALUES ('1234', 'apple'); 
INSERT INTO orderdetails(orderID, productName) VALUES ('1234', 'apple')

-- (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.
INSERT INTO payments (paymentID, price)
VALUES ('1', '5000'),
        ('2', '5000');

-- (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.
INSERT INTO customers (name, address) VALUES ('name2', 'seoul');
INSERT INTO orders (orderID, productName, customorID)
VALUES ('3', 'banana', LAST_INSERT_ID());

-- (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.
INSERT INTO employees (name, address) VALUES ('name1', 'busan');
UPDATE employees SET jobTitle = 'Marketing rep' WHERE employeeID = LAST_INSERT_ID();

-- (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
INSERT into products (name, price) VALUES ('name1', '5000');
UPDATE products SET count = '50' WHERE productID = LAST_INSERT_ID();

-- (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
INSERT into offices (name, address) VALUES ('name1', 'busan');
INSERT into employees (name, address) VALUES ('name12', LAST_INSERT_ID());

-- (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.
INSERT INTO productlines (productLine, productName) VALUES ('linename', 'proname');
UPDATE products SET lineName = LAST_INSERT_ID()


-- (1) **`customers`** 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.
INSERT INTO customers (name, address, customerID) VALUES ("name1", "busan", "34512");
INSERT INTO orders (orderID, productName, customorID) VALUES ("adsf", "applemango", LAST_INSERT_ID());

-- (2) **`employees`** 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이트하세요.
INSERT INTO employees (name, address) VALUES ("name1", "busan");
UPDATE employees SET manager = "manager1" WHERE employees.name = "name1"

UPDATE employees SET reportsTo = (SELECT employeeNumber FROM employees WHERE lastName = 'Johnson')
WHERE name = "name1"

-- (3) **`products`** 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.
INSERT INTO products (name, price) VALUES ('productname', 5000);
INSERT INTO orders (orderID, productID) VALUES (1234, LAST_INSERT_ID());

-- (4) **`orders`** 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.
INSERT INTO orders (orderID, productID) VALUES ('prName', 12345);
INSERT INTO payments (paymentID, cutomerID, quantity) VALUES (325, 1234, 5);

-- (5)**`orderdetails`** 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.
INSERT INTO orderdetails (orderID, productID, quantityOrdered) VALUES (1,2,3);
UPDATE products SET quantity = quantity - 3 WHERE productID = 2;