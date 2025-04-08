# db-hack

Эти скрипты автоматизируют исправление оценок, удаление замечаний и добавление похвалы.

## Функции:

- create_commendation (Добавляет похвалу)

- remove_chastisements (Удаляет все замечания для ученика)

- fix_marks (Исправляет плохие оценки)

- main():
    student_name - имя студента
    subject_for_commendation - предмет
## Как запустить?

1. Положить скрипт scipts.py возле manage.py

2. Запустить Django shell
```
python manage.py shell
```
3. Импортировать все функции
```
from scripts import main, get_student, create_commendation, remove_chastisements, fix_marks
```
4. Запустить 
```
main()
```