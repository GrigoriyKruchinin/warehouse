# Warehouse API
***
## Описание проекта

Этот проект представляет собой API для управления складом. Он позволяет создавать и управлять заказами и продуктами с помощью RESTful интерфейса.
- Версия Python 3.12

***
## Установка и запуск

1. Клонируйте репозиторий:
```
git clone https://github.com/GrigoriyKruchinin/warehouse.git
```

2. Перейдите в директорию проекта:

```
cd warehouse
```

3. Создайте и активируйте виртуальное окружение:

```
python -m venv venv
```
```
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows

```
4. Установите зависимости:

```
pip install -r requirements.txt
```

5. Соберите и запустите контейнеры с помощью Docker Compose:

```
docker-compose up --build -d
```
6. После этого примените миграции:

```
docker-compose run app alembic upgrade head
```

7. Запустите приложение:

```
docker-compose up
```

8. Для удобства взаимодействия с API используйте интерактивную документацию, доступную в браузере по адресу:
```
http://0.0.0.0:8000/docs
```

***

## Тестирование

Запустите тесты с помощью команды:
```
pytest tests/
```

***

## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)

***