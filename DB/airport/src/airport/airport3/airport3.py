from sqlalchemy import create_engine, MetaData
from sqlalchemy import inspect, Table, URL
from sqlalchemy.schema import CreateTable
import yaml

engine = None
insp = None
conn = None
metadata_obj = MetaData()
schema = ""

# DB 연결하는 함수
def conn_db(db_url:str):
    global engine, insp, conn, metadata_obj

    engine = create_engine(db_url)
    metadata_obj.reflect(engine)
    insp = inspect(engine)

    conn = engine.connect()

# 조회할 스키마로 url을 만들어서 새로 연결하는 함수
def set_schema():
    global schema
    schema = input("조회할 스키마 이름을 입력해주세요.")
    url = engine.url

    new_url = URL.create(
        drivername=url.drivername,
        username=url.username,
        password=url.password,
        host=url.host,
        port=url.port,
        database=schema,
        query=url.query
    )

    conn_db(new_url)

def get_schemas() -> list[str]:
    return insp.get_schema_names()

def get_tables() -> list[str]:
    return insp.get_table_names(schema)

def get_views() -> list[str]:
    return insp.get_view_names(schema)

def get_columns_and_comments(name:str):
    columns = insp.get_columns(name)
    comments = insp.get_table_comment(name)

    return columns, comments

def get_tables_and_column_comment():
    tables = get_tables()
    print(tables)

    for table in tables:
        print(table)
        (col, comment) = get_columns_and_comments(table)
        
        print(col)
        print(comment)

def get_views_and_column_comment():
    views = get_views()
    print(views)

    for view in views:
        print(view)
        (col, comment) = get_columns_and_comments(view)

        print(col)
        print(comment)

def get_table_ddl(name: Table):
    global engine
    return CreateTable(name).compile(engine)


if __name__ == '__main__':
    db_list = {}

    with open('config.yaml') as f:
        file = yaml.full_load(f)
        for db in file:
            db_list[db] = file[db]

    while True:

        print(""" 0: 조회할 DB 입력 \n 1: 스키마 목록 조회\n 2: 스키마 설정 \n 3: 테이블 목록 조회 \n 4: 뷰 목록 조회 \n 5: 테이블 목록 및 컬럼 코멘트 조회
 6: 뷰 목록 및 컬럼 코멘트 조회 \n 7: 특정 테이블의 컬럼 코멘트 조회 \n 8: 테이블 DDL 조회 \n 9: 종료 """)
        
        inp = input()

        if inp == "0":
            print(db_list.keys())
            db_name = input("접속할 DB를 입력해주세요")
            conn_db(db_list[db_name])

        elif inp == "1":
            print(get_schemas())

        elif inp == "2":
            set_schema()

        elif inp == "3":
            print(get_tables())

        elif inp == "4":
            print(get_views())
        
        elif inp == "5":
            get_tables_and_column_comment()

        elif inp == "6":
            get_views_and_column_comment()

        elif inp == "7":
            table = input("조회할 테이블 명을 입력해주세요")
            print(get_columns_and_comments(table))

        elif inp == "8":
            table_name = input("조회할 테이블 명을 입력해주세요")
            table = Table(table_name, metadata_obj)
            print(get_table_ddl(table))

        elif inp == "9":
            break

    conn.close()