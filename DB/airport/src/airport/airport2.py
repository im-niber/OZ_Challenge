from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy import Table, text, exc
from faker import Faker
import time
import yaml
import random

engine = create_engine("mysql+pymysql://root:rbwo8160@localhost/airportdb?charset=utf8mb4")
fake = Faker()

metadata_obj = MetaData()
metadata_obj.reflect(engine)

conn = engine.connect()

def truncate_table(table):
    query = "TRUNCATE TABLE {}".format(table)
    conn.execute(text(query))

# yaml 파일 생성 함수
def generate_yaml():
    tables = metadata_obj.tables

    with open('dummy.yaml', 'w') as f:
        for table in tables:
            dummy_dict = {}

            print(table, "의 더미데이터 생성기")
            is_truncated = input("기존 데이터를 삭제하시겠습니까? (y/n): ") == "y"
            count = int(input("추가할 더미데이터 갯수를 지정해주세요: "))
            dummy_dict = {table: { "count": count, "is_truncated": is_truncated } }
            yaml.dump(dummy_dict, f)

# 타입에 맞는 데이터 생성 함수
str_list = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
def generate_type_data(type_str, enum_data=[]):
    if "DECIMAL" in type_str:
        decimal = list(map(int, type_str.split("(")[1].split(")")[0].split(",")))
        if len(decimal) == 1:
            return random.randrange(-1 * (10**decimal[0]) + 1, 10**decimal[0] - 1)

        else:
            num = (10 ** (decimal[0]) -1) * 10 ** -decimal[1]
            return round(random.uniform(-num, num), decimal[1] )
    
    # char varchar
    if "(" in type_str and "CHAR" in type_str:
        size = int(type_str.split("(")[1].split(")")[0])
        type_str = type_str.split("(")[0]

        if "CHAR" == type_str:
            return "".join(fake.random_choices(elements=str_list, length=size))

        size = random.randrange(1, size)
        return fake.sentence()[:size]

    if "TEXT" in type_str:
        return fake.sentence()

    if type_str == "TINYINT":
        return random.choice([0, 1])

    if type_str == "SMALLINT":
        return random.randrange(1, 32000)

    if type_str == "MEDIUMINT":
        return random.randrange(1, 32000)
    
    if type_str == "INTEGER":
        return random.randrange(0, 2 ** 31 - 1)

    if type_str == "DATETIME":
        return fake.date_between(start_date='-365d', end_date='+365d').strftime('%Y-%m-%d %H:%M:%S'),
    
    if type_str == "DATE":
        return fake.date_between(start_date='-365d', end_date='+365d').strftime('%Y-%m-%d')
    
    if type_str == "TIMESTAMP":
        return fake.date_between(start_date='-365d', end_date='+365d')

    if type_str == "TIME":
        return fake.time_object(end_datetime=False)

    return random.choice(enum_data)

def generate_col_dummy_data(table, col_arr, count):
    table = Table(table, metadata_obj)
    col_stmt = {}

    for _ in range(count):
        for col in col_arr:
            # 성별의 경우 제 생각엔, 따로 데이터를 넣어도 괜찮아보여서 이렇게 진행했슴니다
            if col[0] == 'sex':
                col_stmt[col[0]] = random.choice(['M', 'F'])
                continue

            col_stmt[col[0]] = generate_type_data(col[1], col[2])

        try:
            stmt = insert(table).values(col_stmt)
            conn.execute(stmt)
        except exc.IntegrityError:
            print("IntegrityError")


# 테이블에 맞는 col_arr를 생성 후 더미데이터까지 만드는 함수.
def generate_dummy_data(table_name, count=10, is_truncated = True):
    tables = metadata_obj.tables

    if is_truncated:
        truncate_table(table_name)
        print(f"{table_name} truncated")

    columns = tables[table_name].columns
    col_arr = []

    for col in columns:
        if col.autoincrement is True:
            continue

        col_type = str(col.type)
        try:
            col_arr.append((col.name, col_type, col.type.enums))

        except: 
            col_arr.append((col.name, col_type, []))

    generate_col_dummy_data(table_name, col_arr, count)

if __name__ == '__main__':
    start = time.time()

    generate_yaml()

    with open('dummy.yaml') as f:
        file = yaml.full_load(f)
        for item in file:
            generate_dummy_data(item, file[item]['count'], file[item]['is_truncated'])

    end = time.time()
    print(end - start)

    conn.commit()
    conn.close()