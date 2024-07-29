# Personal Business Card

## Описание проекта

"Personal Business Card" - это веб-приложение, которое позволяет пользователям создавать и управлять своими персональными визитными карточками. Приложение построено с использованием FastAPI, SQLAlchemy и PostgreSQL, и предоставляет RESTful API для взаимодействия с системой.

## Технологии

- Python 3.12+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (для миграций базы данных)
- Pydantic (для валидации данных)
- Uvicorn (ASGI сервер)

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/yourusername/personal-business-card.git
cd personal-business-card
```

### Установка зависимостей

`pip install -r requirements.txt`

### Настройка окружения

```DB_URL=postgresql+asyncpg://username:password@localhost/dbname
DB_URL=postgresql+asyncpg://user:pass@hostname/dbname
SECRET_KEY=xxx
ALGORITHM=HS256
```

### Запуск проекта

`uvicorn app.main:app --reload`