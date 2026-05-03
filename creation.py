""" Створення бази даних та колекції, а також додавання документів до колекції."""
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://kalinasergey911_db_user:OWW12HRdqXJtX2uK@cluster0.a23fjxm.mongodb.net/book?appName=Cluster0",
    server_api=ServerApi('1')
)
# Створюємо базу даних book та колекцію cats
db = client.book
# Додаємо документи до колекції cats
result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)
# Метод insert_one повертає об'єкт InsertOneResult, який містить інформацію про вставлений
# документ, включаючи його унікальний ідентифікатор (ObjectId). Ми можемо отримати цей
# ідентифікатор за допомогою атрибута inserted_id.
print(result_one.inserted_id)
# Метод insert_many дозволяє вставити кілька документів одночасно. Він приймає список документів
# і повертає об'єкт InsertManyResult, який містить інформацію про всі вставлені документи,
# включаючи їх унікальні ідентифікатори.
result_many = db.cats.insert_many(
    [
        {
            "name": "lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)
