# DataCenter Management System

Это руководство содержит инструкции по запуску и использованию проекта DataCenter Management System.

## Описание проекта

DataCenter Management System - это веб-приложение для управления доступом и отслеживания активности в центре обработки данных. С его помощью администраторы могут управлять пропусками, контролировать доступ к хранилищам и отслеживать активность сотрудников в здании.

## Требования

Для запуска проекта вам понадобятся следующие компоненты:

- Python (рекомендуемая версия: 3.6 и выше)
- Django (установится автоматически при следовании инструкциям)

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Rokyl59/django-orm-watching-storage.git
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Настройка

1. Создайте файл `.env` в корне проекта и заполните его данными о настройке проекта, например:

```
ENGINE=django.db.backends.postgresql
HOST=localhost
PORT=5432
NAME=mydatabase
USER=mydatabaseuser
PASSWORD=mypassword
SECRET_KEY=mysecretkey
DEBUG=True
ROOT_URLCONF=project.urls
LANGUAGE_CODE=language
TIME_ZONE=zone
DEFAULT_AUTO_FIELD=django.db.models.BigAutoField
```

## Запуск

1. Запустите сервер

```bash
python manage.py runserver
```

2. Теперь проект доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Использование

* Просмотр активных пропусков: [http://127.0.0.1:8000](http://127.0.0.1:8000)

* Информация о хранилище: [http://127.0.0.1:8000/storage_information](http://127.0.0.1:8000/storage_information)

* Информация о пропуске: [http://127.0.0.1:8000/passcard_info/uuid:passcode](http://127.0.0.1:8000/passcard_info/uuid:passcode)

