from pymongo import MongoClient

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"}
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client["local"]
    collection = db['books']
    query = {"genre": "fantasy"}
    books = collection.find(query)

    for book in books:
        print(book)

    collection = db['movies']
    pipeline = [
        {"$group": {"_id": "$director", "aver_rating": {"$avg": "$rating"}}},
        {"$sort": {"aver_rating": -1}}
    ]

    results = collection.aggregate(pipeline)
    for result in results:
        print(result)

    collection = db['user_actions']
    query = {"user_id": 1}

    actions = collection.find(query).sort('timestamp', -1).limit(5)
    for action in actions:
        print(action)

    collection = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    results = collection.aggregate(pipeline)
    for result in results:
        print(result)
        
    collection = db.user_actions
    query ={"user_id": 1, "action": "view", "timestamp": { "$lt": "2023-04-15" }}
    update = {"$set": {"action": "seen"}}
    
    results = collection.update_many(query, update)
    print(results.modified_count)

