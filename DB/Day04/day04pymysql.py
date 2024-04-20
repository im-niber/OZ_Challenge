import pymysql
from faker import Faker
import random

# Faker 객체 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='***',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Products 테이블을 위한 더미 데이터 생성
def generate_product_data(n):
    for _ in range(n):
        product_name = fake.word().capitalize() + ' ' + fake.word().capitalize()
        price = round(random.uniform(10, 100), 2)
        stock_quantity = random.randint(10, 100)
        create_date = fake.date_time_this_year()
        yield (product_name, price, stock_quantity, create_date)

# Customers 테이블을 위한 더미 데이터 생성
def generate_customer_data(n):
    for _ in range(n):
        customer_name = fake.name()
        email = fake.email()
        address = fake.address()
        create_date = fake.date_time_this_year()
        yield (customer_name, email, address, create_date)

# Orders 테이블을 위한 더미 데이터 생성
def generate_order_data(n, customer_ids):
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        order_date = fake.date_time_this_year()
        total_amount = round(random.uniform(20, 500), 2)
        yield (customer_id, order_date, total_amount)

# 데이터베이스에 데이터 삽입
with conn.cursor() as cursor:
    # Products 데이터 삽입
    products_sql = "INSERT INTO Products (productName, price, stockQuantity, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_product_data(10):
        cursor.execute(products_sql, data)
    conn.commit()

    # Customers 데이터 삽입
    customers_sql = "INSERT INTO Customers (customerName, email, address, createDate) VALUES (%s, %s, %s, %s)"
    for data in generate_customer_data(5):
        cursor.execute(customers_sql, data)
    conn.commit()

    # Orders 데이터 삽입
    # Customers 테이블에서 ID 목록을 얻어옵니다.
    cursor.execute("SELECT customerID FROM Customers")
    customer_ids = [row['customerID'] for row in cursor.fetchall()]
    
    orders_sql = "INSERT INTO Orders (customerID, orderDate, totalAmount) VALUES (%s, %s, %s)"
    for data in generate_order_data(15, customer_ids):
        cursor.execute(orders_sql, data)
    conn.commit()

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        connection.commit()

# 1. **새로운 제품 추가**: Python 스 크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
execute_query(conn, "insert into Products (productName, price, stockQuantity) VALUES ('Python Book', 10000, 10)")

# 2. **고객 목록 조회**: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
data = execute_query(conn, "select * from customers")
print(data)

# 3. **제품 재고 업데이트**: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
execute_query(conn, "update products set stockQuantity = stockQuantity - 1 WHERE productID = 1")

# 4. **고객별 총 주문 금액 계산**: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
data = execute_query(conn, "select customerID, SUM(totalAmount) from Orders group by customerID")
print(data)

# 5. **고객 이메일 업데이트**: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
execute_query(conn, "update Customers set email = 'newemail22@naver.com' where customerID = %s", 1)

# 6. **주문 취소**: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
execute_query(conn, "delete from Orders where orderID = 1")

# 7. **특정 제품 검색**: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
print(execute_query(conn, 'select productName from Products'))
print(execute_query(conn, 'select * from Products where productName LIKE %s', '%Book%'))

# 8. **특정 고객의 모든 주문 조회**: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
print(execute_query(conn, 'select * from Orders where customerID = 2'))

# 9. **가장 많이 주문한 고객 찾기**: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
print(execute_query(conn, """
                    select customerID, COUNT(*) as orderCount 
                    from Orders group by customerID 
                    order by orderCount desc
                    """))


# 데이터베이스 연결 종료
conn.close()
