""" Створення моделей

​Тепер можна створити наші моделі даних. Абстракція MongoEngine заснована на класах, і всі створені
моделі є класами.

Оголошення деяких властивостей у класі еквівалентно створенню структури даних для збереження даних.
Ці класи прийнято зберігати у сценарії як модуль моделі застосунку, ми зробимо це просто у файлі
models.py. 

Тут у нас описані три схеми для документів Tag, Record та Notes. Причому схема документів Notes у
нашому випадку включає документи Tag і Record. """

from datetime import datetime
# Імпортуємо класи EmbeddedDocument і Document з модуля mongoengine. Клас Document використовується
# для створення основних документів, які будуть зберігатися в базі даних, тоді як EmbeddedDocument
# використовується для створення вкладених документів,які можуть бути включені в основні документи.
# Це дозволяє нам створювати складні структури даних, де один документ може містити інші документи
# як частину своєї структури.
from mongoengine import EmbeddedDocument, Document
# Імпортуємо типи полів, які нам потрібні для опису наших моделей даних (наприклад, StringField,
# DateTimeField, EmbeddedDocumentField тощо) з модуля mongoengine.fields. Ці типи полів дозволяють
# нам визначити структуру наших документів і вказати, які дані ми хочемо зберігати в кожному полі.
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Tag(EmbeddedDocument):
    """ Цей клас описує схему для тегів, які можуть бути прикріплені до нотаток. Він є вкладеним
    документом, оскільки теги будуть включені в основні документи нотаток."""
    name = StringField()


class Record(EmbeddedDocument):
    """ Цей клас описує схему для записів, які можуть бути прикріплені до нотаток. Він є вкладеним
    документом, оскільки записи будуть включені в основні документи нотаток."""
    description = StringField()
    done = BooleanField(default=False)


class Notes(Document):
    """ Цей клас описує схему для нотаток, які можуть містити теги та записи."""
    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}
