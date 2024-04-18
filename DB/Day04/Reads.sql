-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
SELECT * from customers

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
SELECT * from products

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT name, jobTitle from employees

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT address from offices

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders ORDER BY orderDate desc LIMIT 10;

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where orderID = 3

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerID = 3

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
select decription from productlines

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where address = 'busan'

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where price BETWEEN 1000 and 2000

    

-- (1) **`orders`** 테이블에서 특정 고객의 모든 주문을 조회하세요.
select * from orders where customerID = 3
    
-- (2) **`orderdetails`** 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.
select * from orderdetails where productID = 3
    
-- (3) **`payments`** 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.
select * from payments where paymentDate BETWEEN '2024-01-01' and '2024-01-31'
    
-- (4) **`employees`** 테이블에서 특정 직급의 모든 직원을 조회하세요.
select * from employees where jobTitle = "marketing"
    
-- (5) **`offices`** 테이블에서 특정 국가의 모든 사무실을 조회하세요.
select * from offices where country = "korea"
    
-- (6) **`products`** 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.
select * from products where productLine = "Car"
    
-- (7) **`customers`** 테이블에서 최근에 가입한 5명의 고객을 조회하세요.
select * from customers ORDER BY createDate DESC LIMIT 5
    
-- (8) **`products`** 테이블에서 재고가 부족한 모든 제품을 조회하세요.
select * from products where quantity <= 0
    
-- (9) **`orders`** 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.
select * from orders where orderDate BETWEEN '2024-03-01' and '2024-03-31'
    
-- (10) **`orderdetails`** 테이블에서 특정 주문에 대한 총 금액을 계산하세요.
select SUM(price) from orderdetails where orderID = 3;

    
    
-- (1) **`customers`** 테이블에서 각 지역별 고객 수를 계산하세요.
select address, COUNT(*) from customers group by address;
    
-- (2) **`products`** 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.
select proudctLine, AVG(price) from products group by proudctLine;
    
-- (3) **`employees`** 테이블에서 각 부서별 직원 수를 계산하세요.
select department, count(*) from employees group by department

-- (4) **`offices`** 테이블에서 각 사무실별 평균 직원 연봉을 계산하세요.
select address, AVG(salary) from offices group by address

-- (5) **`orderdetails`** 테이블에서 가장 많이 팔린 제품 5개를 조회하세요.
SELECT productCode, SUM(quantityOrdered) AS totalOrdered FROM orderdetails
 GROUP BY productCode ORDER BY totalOrdered DESC LIMIT 5;