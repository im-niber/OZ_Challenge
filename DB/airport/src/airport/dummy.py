from sqlalchemy import create_engine, MetaData, insert, values, delete
from sqlalchemy import Table, Column, Integer, String, text
from faker import Faker
import random
import time

engine = create_engine("mysql+pymysql://root:rbwo8160@localhost/alchemyproj?charset=utf8mb4")

metadata_obj = MetaData()

tables = []
faker_obj = Faker()

# 더미 테이블 14개 생성
for i in range(1, 15):
    table_name = f"dummy_table_{i}"
    table = Table(
        table_name,
        metadata_obj,
        Column(f"{table_name}_id", Integer, primary_key=True),
        Column(f"{table_name}_name", String(20), nullable=False),
        Column(f"{table_name}_description", String(200)),
    )
    tables.append(table)
    
metadata_obj.create_all(engine)

for table in tables:
    start = time.time()
    rand_num = random.randrange(1000, 10000)
    
    table_name = table.name + '_name'
    table_description = table.name + '_description'

    print(table, rand_num)
    print(table_name, table_description)

    if random.randint(0, 1) == 1:
        print("truncating...")

        with engine.connect() as conn:
            query = "TRUNCATE TABLE {}".format(table.name)
            conn.execute(text(query))

    for i in range(0, rand_num):
        fake_table_name = faker_obj.word()
        fake_table_description = faker_obj.paragraph(nb_sentences = 2)

        stmt = insert(table).values({
            table_name: fake_table_name, table_description: fake_table_description 
            })
        
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()

    end = time.time()
    print(f"end, {end - start}")