# Yatube

## Описание проекта

Yatube - это сайт для создания и публикации личных блогов.
С помощью Yatube вы можете создать свои посты, делиться своими мыслями, опытом и знаниями со всем миром.
Также вы можете подписываться на интересных авторов и следить за их публикациями.
И не забудьте обсуждать понравившиеся посты в комментариях!

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Archi82123/api_final_yatube
```
```
cd api_final_yatube
```

2. Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```
```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

5. Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API

1. Получить список всех постов:

```
GET /api/v1/posts/
```

2. Создать новый пост:

```
POST /api/v1/posts/
```

Тело запроса:

```
{
    "text": "string"
}
```

3. Получить все комментарии к посту:

```
GET /api/v1/posts/{post_id}/comments/
```

4. Создать новый комментарий в посте:

```
POST /api/v1/posts/{post_id}/comments/
```

Тело запроса:

```
{
    "text": "string"
}
```

5. Получить все подписки пользователя, сделавшего запрос:

```
GET /api/v1/follow/
```

6. Подписаться на пользователя:

```
POST /api/v1/follow/
```

Тело запроса:

```
{
    "following": "string"
}
```
