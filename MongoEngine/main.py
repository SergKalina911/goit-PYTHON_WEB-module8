"""  Отримання даних

​Залишилось написати скрипт отримання даних."""

# Імпортуємо модель Notes з файлу models.py,щоб мати доступ до структури даних нотаток і можливості
# виконувати запити до бази даних.
from models import Notes

# Імпортуємо модуль connect.py, щоб встановити з'єднання з базою даних MongoDB перед виконанням
# будь-яких операцій з нею. Це необхідно для того, щоб мати можливість виконувати запити до бази
# даних і отримувати дані.
import connect


print('--- All notes ---')
# Отримуємо всі нотатки з бази даних за допомогою методу objects() моделі Notes. Цей метод повертає
# список всіх документів, які відповідають моделі Notes, з бази данихи. Ми зберігаємо цей список у
# змінній notes. Потім ми проходимося по кожній нотатці в цьому списку і виводимо її id, name,
# created date, а також опис записів і назви тегів, які містяться в кожній нотатці. Для цього ми
# використовуємо генератори списків, щоб створити списки описів записів і назв тегів для кожної
# нотатки, і виводимо їх у форматі рядка.
notes = Notes.objects()
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with tag Fun ---')
# Отримуємо всі нотатки, які містять тег з назвою 'Fun', за допомогою методу objects() моделі Notes
# і використовуючи фільтр tags__name='Fun'. Цей фільтр дозволяє нам вибрати лише ті нотатки, які
# мають тег з назвою 'Fun'. Ми зберігаємо цей список у змінній notes. Потім ми проходимося по
# кожній нотатці в цьому списку і виводимо її id, name, created date, а також опис записів і назви
# тегів, які містяться в кожній нотатці, використовуючи той же підхід, що і раніше, з генераторами
# списків для створення списків описів записів і назв тегів для кожної нотатки, і виводимо їх у
# форматі рядка.
notes = Notes.objects(tags__name='Fun')
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with record description: Buying sausage ---')
# Отримуємо всі нотатки, які містять запис з описом 'Buying sausage', за допомогою методу objects()
# моделі Notes і використовуючи фільтр records__description='Buying sausage'. Цей фільтр дозволяє
# нам вибрати лише ті нотатки, які мають запис з описом 'Buying sausage'. Ми зберігаємо цей список
# у змінній notes. Потім ми проходимося по кожній нотатці в цьому списку і виводимо її id, name,
# created date, а також опис записів і назви тегів, які містяться в кожній нотатці, використовуючи
# той же підхід, що і раніше, з генераторами списків для створення списків описів записів і назв
# тегів для кожної нотатки, і виводимо їх у форматі рядка.
notes = Notes.objects(records__description='Buying sausage')
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

# Оновлення даних
_id = '69f7657762767a1c72d64347'
note = Notes.objects(id=_id)
note.update(name='New name')
print(f'Note with id {_id} was updated')

# Видалення:
_id = '69f7657762767a1c72d64347'
note = Notes.objects(id=_id).delete()
print(f'Note with id {_id} was deleted')

