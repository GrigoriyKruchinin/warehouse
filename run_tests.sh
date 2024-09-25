#!/bin/bash

set -e

echo -e "\n\n\nЗапуск тестов...\n\n\n"

docker-compose up -d test_db

pytest

docker-compose down

echo -e "\n\n\nТестирование завершено.\n\n\n"
