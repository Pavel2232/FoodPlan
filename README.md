# 🍧🍳🥐🦑FoodPlan
## Ценности:
- Для клиента:
Избавиться от фрустрации при выборе блюда.
Планирование бюджета.
Авторасчёт списка покупок: больше ничего не забудут в магазине.
Подбор блюд под диету или аллергию.
Чувство единения/помощи блогерам. 
- Для владельца приложения:
Заработать на ежемесячной подписке
Использовать как канал привлечения новых подписчиков/клиенто


## Как запустить:
1. Вполните командку 
```
git clone https://github.com/Pavel2232/FoodPlan
```
2. Установите зависимости ``` poetry install ```
3. Заполните .env
```
SECRET_KEY=ВАШ SECRET_KEY
DATABASE_URL=psql://username:password@host/dbname
```

4. Выполните:
- ```./manage.py makemigrations```
- ```./manage.py migrate```
- ```./manage.py collectstatic```
- ```./manage.py runserver```

## Подключение к remote db
`DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME`