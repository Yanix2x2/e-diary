# Редактирование школьного дневника

Скрипт позволяет исправлять оценки, удалять замечания и создавать похвалу для учеников.

## Функции

### fix_marks(schoolkid_name)
Исправляет плохие оценки (2 и 3) на отличные (5) для указанного ученика.

Пример:
```bash
fix_marks("Фролов Иван")
```
### remove_chastisements(schoolkid_name)
Удаляет все замечания для указанного ученика.

Пример:
```bash
remove_chastisements("Фролов Иван")
```

### create_commendation(schoolkid_name, subject_title)
Добавляет случайную похвалу для ученика по указанному предмету.

Пример:
```bash
create_commendation("Фролов Иван", "Математика")
```

## Запуск
1. Скачайте и поместите файл `crud.py` в корень [проекта](https://github.com/devmanorg/e-diary).  
2. Окройте интерактивный режим `Django shell`:
```bash
python manage.py shell
```
3. Импортируйте все функции в `Django shell`:
```bash
from crud import *
```
4. Вызывайте и используйте любые функции, как в примерах выше.
