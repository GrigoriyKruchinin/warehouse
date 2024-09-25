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
python -m venv .venv
source .venv/bin/activate
```

Или используйте встроенные возможности создания и активации виртуального окружения вашей IDE.

4. Установите необходимые зависимости:

```
pip install -r requirements.txt
```

5. Создайте файл .env и ознакомьтесь с его содержимым:

```
cp .env.example .env
```

В некоторых системах и IDE может потребоваться перезапустить терминал, что бы приложение начало считывать переменные окружения.

6. Убедитесь, что скрипты инициализации приложения и запуска тестов имеют исполняемые права. Для этого используйте команды:

```
chmod +x initial_setup.sh
chmod +x run_tests.sh
```

7. Запустите начальную настройку проекта:

```
./initial_setup.sh
```

В итоге, скрипт соберет и запустит докер контейнеры, установит миграции и запустит приложение.

8. Для удобства взаимодействия с API используйте интерактивную документацию, доступную в браузере по адресу:

```
http://localhost:8000/docs
```

9. При следующих запусках приложения достаточно использовать команду:

```
docker-compose up db app
```

***

## Тестирование

Для запуска тестов используйте скрипт:

```
./run_tests.sh
```

***

## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)

***