import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rbwo8160',
                             db='classicmodels',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        connection.commit()

try:
    # SELECT
    result = execute_query(connection, "SELECT * FROM customers")
    print("SELECT RESULT:")
    for row in result:
        print(row)

    # INSERT
    execute_query(connection, "INSERT INTO customers (customerNumber, customerName) VALUES (%s, %s)", ('232232', 'hikim'))
    print("INSERT.")

    # UPDATE
    execute_query(connection, "UPDATE customers SET customerName=%s WHERE customerNumber=%s", ('byekim', '12030'))
    print("UPDATE.")

    # DELETE
    execute_query(connection, "DELETE FROM customers WHERE customerNumber=%s", ('12030'))
    print("DELETE.")

finally:
    connection.close()