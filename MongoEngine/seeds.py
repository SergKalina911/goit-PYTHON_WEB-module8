""" Додаємо дані

​Далі напишемо скрипт seeds.py, щоб наповнити даними нашу БД. Підключаємо всі моделі та імпортуємо
модуль connect.py, для підключення до нашої хмарної БД MongoDB. Інші коментарі є в коді файлу
seeds.py """
# Імпортуємо модель Notes,а також Record і Tag з файлу models.py,щоб мати доступ до структури даних
# нотаток,записів і тегів,і можливості створювати об'єкти цих класів для збереження їх у базі даних
from models import Notes, Record, Tag
# Імпортуємо модуль connect.py, щоб встановити з'єднання з базою даних MongoDB перед виконанням
# будь-яких операцій з нею. Це необхідно для того, щоб мати можливість виконувати запити до бази
# даних і зберігати дані в ній.
import connect

# спочатку - створити об'єкт Tag
tag = Tag(name='Purchases')
# потім - створення об'єктів Record
record1 = Record(description='Buying sausage')
record2 = Record(description='Buying milk')
record3 = Record(description='Buying oil')
#  Останнє - створюємо об'єкт Note і зберігаємо його
Notes(name='Shopping', records=[record1, record2, record3], tags=[tag, ]).save()
# Також можна створити об'єкт Note і зберегти його в один рядок, не створюючи окремо об'єкти Tag і
# Record. У цьому випадку ми передаємо всі необхідні дані безпосередньо в конструктор Notes, і він
# автоматично створить вкладені документи для тегів і записів.
Notes(name='Going to the movies', records=[Record(description='Went to see the Avengers'), ], tags=[Tag(name='Fun'), ]).save()
