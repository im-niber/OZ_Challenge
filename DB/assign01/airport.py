from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy import Table, text
from faker import Faker
import random
import time

engine = create_engine("mysql+pymysql://root:rbwo8160@localhost/airportdb?charset=utf8mb4")
tables = []
fake = Faker()

metadata_obj = MetaData()
metadata_obj.reflect(engine)

conn = engine.connect()

def truncate_table(table):
    query = "TRUNCATE TABLE {}".format(table.name)
    conn.execute(text(query))

def generate_airport_data(count=10, is_truncated = False):
    table = Table('airport', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'iata': fake.unique.bothify(text='???'),
                'icao': fake.unique.bothify(text='????'),
                'name': fake.unique.city()[:50]})
            conn.execute(stmt)
        except:
            pass


def generate_airline_data(count=10, is_truncated=False):
    table = Table('airline', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    unique_iata = set()
    for _ in range(count):
       iata = fake.bothify(text='??')
       try:
            if iata in unique_iata: 
                raise
            unique_iata.add(iata)

            stmt = insert(table).values({
                'iata': fake.bothify(text='??'),
                'airlinename': fake.unique.city()[:30],
                'base_airport': random.randint(1, 32000)
                })
            
            conn.execute(stmt)
       except:
            pass


def generate_airplane_type_data(count=10, is_truncated=False):
    table = Table('airplane_type', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'identifier': fake.unique.bothify(text='????'),
                'description': fake.sentence()
            })
            conn.execute(stmt)
        except:
            pass

def generate_airplane_data(count=10, is_truncated=False):
    table = Table('airplane', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'capacity': random.randint(100, 500),
                'type_id': random.randint(1, 10),
                'airline_id': random.randint(1, 32000)
            })
            conn.execute(stmt)
        except:
            pass

def generate_airport_geo_data(count=10, is_truncated=False):
    table = Table('airport_geo', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'airport_id': random.randint(1, 32000),
                'name': fake.unique.city(),
                'city': fake.city(),
                'country': fake.country(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude()
            })
            conn.execute(stmt)
        except:
            pass

def generate_booking_data(count=10, is_truncated=False):
    table = Table('booking', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")
        
    for _ in range(count):
        try:
            stmt = insert(table).values({
                'flight_id': random.randint(1, 32000),
                'seat': fake.unique.bothify(text='??##'),
                'passenger_id': random.randint(1, 10),
                'price': round(random.uniform(50, 500), 2)
            })
            conn.execute(stmt)
        except:
            pass

def generate_employee_data(count=10, is_truncated=False):
    table = Table('employee', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'firstname': fake.first_name(),
                'lastname': fake.last_name(),
                'birthdate': fake.date_of_birth().strftime('%Y-%m-%d'),
                'sex': random.choice(['M', 'F']),
                'street': fake.street_address(),
                'city': fake.city(),
                'zip': random.randint(0, 32000),
                'country': fake.country(),
                'emailaddress': fake.email(),
                'telephoneno': fake.phone_number(),
                'salary': round(random.uniform(20000, 100000), 2),
                'department': random.choice(['Marketing', 'Buchhaltung', 'Management', 'Logistik', 'Flugfeld']),
                'username': fake.user_name()[:20],
                'password': fake.password(length=10)
            })
            conn.execute(stmt)
        except:
            pass

def generate_flight_log_data(count=10, is_truncated=False):
    table = Table('flight_log', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")
        
    for _ in range(count):
        past_date = fake.date_between(start_date='-365d', end_date='now')
        try:
            stmt = insert(table).values({
                'log_date': fake.date_between(start_date='-100d', end_date='now').strftime('%Y-%m-%d'),
                'user': fake.user_name(),
                'flight_id': random.randint(1, 32000),
                'flightno_old': fake.bothify(text='??####'),
                'flightno_new': fake.bothify(text='??####'),
                'from_old': random.randint(1, 32000),
                'to_old': random.randint(1, 32000),
                'from_new': random.randint(1, 32000),
                'to_new': random.randint(1, 32000),
                'departure_old': past_date.strftime('%Y-%m-%d %H:%M:%S'),
                'arrival_old': past_date.strftime('%Y-%m-%d %H:%M:%S'),
                'departure_new': fake.date_between(start_date=past_date, end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                'arrival_new': fake.date_between(start_date=past_date, end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                'airplane_id_old': random.randint(1, 32000),
                'airplane_id_new': random.randint(1, 32000),
                'airline_id_old': random.randint(1, 32000),
                'airline_id_new': random.randint(1, 32000),
                'comment': fake.sentence()
            })
            conn.execute(stmt)
        except:
            pass

def generate_flight_data(count=10, is_truncated=False):
    table = Table('flight', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'flightno': fake.bothify(text='??####'),
                'from': random.randint(1, 32000),
                'to': random.randint(1, 32000),
                'departure': fake.date_time_between(start_date='-300d', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
                'arrival': fake.date_time_between(start_date='now', end_date='+300d').strftime('%Y-%m-%d %H:%M:%S'),
                'airline_id': random.randint(1, 32000),
                'airplane_id': random.randint(1, 32000)
            })
            conn.execute(stmt)
        except:
            pass

def generate_flightschedule_data(count=10, is_truncated=False):
    table = Table('flightschedule', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'flightno': fake.bothify(text='??####'),
                'from': random.randint(1, 32000),
                'to': random.randint(1, 32000),
                'departure': fake.time(pattern='%H:%M:%S'),
                'arrival': fake.time(pattern='%H:%M:%S'),
                'airline_id': random.randint(1, 32000),
                'monday': random.choice([0, 1]),
                'tuesday': random.choice([0, 1]),
                'wednesday': random.choice([0, 1]),
                'thursday': random.choice([0, 1]),
                'friday': random.choice([0, 1]),
                'saturday': random.choice([0, 1]),
                'sunday': random.choice([0, 1])
            })
            conn.execute(stmt)
        except:
            pass

def generate_passenger_data(count=10, is_truncated=False):
    table = Table('passenger', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'passportno': fake.unique.bothify(text='######??'),
                'firstname': fake.first_name(),
                'lastname': fake.last_name()
            })
            conn.execute(stmt)
        except: 
            pass

def generate_weatherdata_data(count=10, is_truncated=False):
    table = Table('weatherdata', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'log_date': fake.date_between(start_date='-1y', end_date='today'),
                'time': fake.time_object(end_datetime=False),
                'station': random.randint(1, 32000),
                'temp': round(random.uniform(-10, 40), 1),
                'humidity': round(random.uniform(0, 100), 1),
                'airpressure': round(random.uniform(900, 1100), 2),
                'wind': round(random.uniform(0, 50), 2),
                'weather': random.choice(['Nebel-Schneefall', 'Schneefall', 'Regen', 'Regen-Schneefall', 'Nebel-Regen', 'Nebel-Regen-Gewitter', 'Gewitter', 'Nebel', 'Regen-Gewitter']),
                'winddirection': random.randint(0, 360)
            })
            conn.execute(stmt)
        except:
            pass

def generate_passengerdetails_data(count=10, is_truncated=False):
    table = Table('passengerdetails', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")

    for _ in range(count):
        try:
            stmt = insert(table).values({
                'passenger_id': random.randint(1, 32000),
                'birthdate': fake.date_of_birth().strftime('%Y-%m-%d'),
                'sex': random.choice(['M', 'F']),
                'street': fake.street_address(),
                'city': fake.city(),
                'zip': random.randint(1, 32000),
                'country': fake.country(),
                'emailaddress': fake.email(),
                'telephoneno': fake.phone_number()
            })
            conn.execute(stmt)
        except:
            pass


def generate_airport_reachable_data(count=10, is_truncated=False):
    table = Table('airport_reachable', metadata_obj)

    if is_truncated:
        truncate_table(table)
        print(f"{table} truncated")
        
    for _ in range(count):
        try:
            stmt = insert(table).values({
                'airport_id': random.randint(1, 32000),
                'hops': random.randint(1, 32000)
            })
            conn.execute(stmt)
        except:
            pass

# 추가하고 싶은 테이블 관련 함수 호출 (데이터 수, truncate 여부)
if __name__ == '__main__':
    start = time.time()
    generate_airport_data(10000, True)
    generate_airline_data(10000, True)
    generate_airplane_type_data(10000, True)
    generate_employee_data(10000, True)
    generate_airport_geo_data(10000, True)
    generate_passenger_data(10000, True)
    generate_airport_reachable_data(10000, True)
    generate_passengerdetails_data(10000, True)
    generate_booking_data(10000, True)
    generate_flight_data(10000, True)
    generate_flight_log_data(10000, True)
    generate_airplane_data(10000, True)
    generate_flightschedule_data(10000, True)
    generate_weatherdata_data(10000, True)

    end = time.time()
    print(end - start)
    conn.commit()
    conn.close()