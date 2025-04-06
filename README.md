# db-hack

Эти скрипты автоматизируют исправление оценок, удаление замечаний и добавление похвалы.

## Функции:

- create_commendation (Добавляет похвалу)

- remove_chastisements (Удаляет все замечания для ученика)

- fix_marks (Исправляет плохие оценки)

## Использование

1. Положить файл в корневую папку сайта

2. Запустите Django shell:
```
python manage.py shell
```

3. Импортироваь функции:
```
from scripts import create_commendation, remove_chastisements, fix_marks
```
 
4. Вызов функции:

```
create_commendation("Фролов Иван", "Музыка")
```
```
remove_chastisements("Фролов Иван")
```
```
from datacenter.models import Schoolkid
child = Schoolkid.objects.get(full_name__contains="Фролов Иван")
fix_marks(child)
```