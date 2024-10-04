# Kitten Exhibition API

## Описание

Проект представляет собой REST API для онлайн выставки котят, где пользователи
могут добавлять, редактировать, удалять информацию о котятах, а также
просматривать и оценивать котят других пользователей. Приложение использует
Django и Django REST Framework, а для аутентификации пользователей применяется
JWT.

## Технологический стек

- **Django 5.1.1**
- **Django REST Framework**
- **PostgreSQL** для хранения данных
- **JWT аутентификация**
- **Docker** и **Docker Compose** для контейнеризации

## Установка и запуск

### Предварительные требования

Для запуска проекта вам понадобятся:

- **Docker** и **Docker Compose**: Убедитесь, что у вас установлены эти
  инструменты. Если нет, установите их с официального
  сайта [Docker](https://www.docker.com/).

### Запуск проекта

1. **Склонируйте репозиторий:**

   ```bash
   git clone https://github.com/AwakeGit/kitten_exhibition.git
   cd kitten-exhibition

2. **Создайте .env файл:**

   ```bash
   DB_ENGINE=django.db.backends.postgresql
   POSTGRES_DB=kitten_exhibition_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=12345

   DB_HOST=db
   DB_PORT=5432

   SECRET_KEY=your-secret-key

   DJANGO_DEBUG_VALUE=False

   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [ip] [domain]
   ```

3. **Запустите Docker Compose для сборки и запуска контейнеров:**

   ```bash
   docker-compose up -d --build
   ```
4. **Создать миграции:**

   ```bash
   docker exec -it kitten_exhibition-backend-1 python manage.py makemigrations
   ```

5. **Примените миграции:**

   ```bash
   docker exec -it kitten_exhibition-backend-1 python manage.py migrate
   ```

6. **Создать суперпользователя:**

   ```bash
   docker exec -it kitten_exhibition-backend-1 python manage.py createsuperuser
   ```

7. **Наполнить базу данных начальными данными:**

   ```bash
   docker exec -it kitten_exhibition-backend-1 python manage.py populate_data
   ```

8. **Доступ к приложению**

   ```bash
   Приложение будет доступно по адресу http://localhost:8000.

   Для доступа к админке используйте: http://localhost:8000/admin/
   ```

9. **Запустить тесты:**

   ```bash
   docker exec -it kitten_exhibition-backend-1 pytest
   ```

10. Удалить данные из базы данных:

```bash
docker exec -it kitten_exhibition-backend-1 python manage.py clear_data
```

### Api

* Для получения Swagger-документации перейдите
  по http://localhost:8000/swagger/

   ```bash
   1. Получение списка пород
      * Endpoint: /api/breeds/
      * Метод: GET

      Возвращает список всех доступных пород котят.

   2. Получение списка всех котят
      * Endpoint: /api/kittens/
      * Метод: GET

    Возвращает список всех котят.

   3. Получение котят определенной породы
      * Endpoint: /api/kittens/?breed=<breed_id>
      * Метод: GET

    Возвращает список котят указанной породы.

  4. Получение детальной информации о котенке
        * Endpoint: /api/kittens/<id>/
        * Метод: GET
      
   Возвращает детальную информацию о конкретном котенке по его id.

  5. Добавление информации о котенке
        * Endpoint: /api/kittens/
        * Метод: POST
   
   Требуется аутентификация: JWT Token
   Добавляет информацию о новом котенке.

  6. Изменение информации о котенке
        * Endpoint: /api/kittens/<id>/
        * Метод: PUT
   
   Требуется аутентификация: JWT Token
   Изменяет информацию о котенке, если пользователь является владельцем котенка.

  7. Удаление информации о котенке
        * Endpoint: /api/kittens/<id>/
        * Метод: DELETE
   
   Требуется аутентификация: JWT Token
   Удаляет информацию о котенке, если пользователь является владельцем котенка.

  8. Оценка котят
           * Endpoint: /api/kittens/<id>/rate/
           * Метод: POST
   
   Требуется аутентификация: JWT Token
   Позволяет пользователям оценивать котят других пользователей.
   ```