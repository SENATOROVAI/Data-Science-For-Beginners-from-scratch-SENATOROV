# Environment

Файл .env (от слова environment — "среда") — это текстовый файл, в котором хранятся переменные окружения. Такие переменные часто используются в проектах, чтобы:

1) хранить настройки (например, DEBUG=true);
2) задавать пути к файлам или сервисам (например, DATABASE_URL=postgres://...);
3) скрывать секретные данные, такие как API-ключи, пароли и токены.

Пример .env файла:

```ini
DEBUG=true
PORT=8000
SECRET_KEY=my-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/mydb
```

Как пользоваться:

1) Создай файл .env в корне проекта.
2) Добавь туда переменные в формате ИМЯ=значение.
3) Загрузи переменные в коде проекта. load_dotenv()

На Python (например, с помощью библиотеки python-dotenv):
Установка:

`pip install python-dotenv` - установка библиотеки python-dotenv

Загрузка .env:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

# Теперь можно получить их
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")
```

Почему это важно?

1) Безопасность: секретные данные не попадают в репозиторий.
2) Гибкость: легко менять параметры без переписывания кода.
3) Удобство: переменные можно подставлять в разные среды (разработка, продакшн и т.д.)

## Создаем проект! :)

Telegram-бот на Python (с использованием библиотеки python-telegram-bot):

## Создай файл в папке github/project/.env

Токен можно получить у него @BotFather

```ini
TELEGRAM_TOKEN=123456789:ABCdefGhIJKlmNOPqrSTUvwxYZ
DEBUG=True
```

## Создай файл в папке github/project/app.py и добавь туда код

```python
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os


# Загрузка переменных из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DEBUG = os.getenv("DEBUG") == 'True'

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))

    print(f"Бот запущен. DEBUG = {DEBUG}")
    app.run_polling()
```

Создай виртуальное окружение и активируй его

`python -m venv venv`

Активируем виртуальное окружение

`venv\Scripts\activate`

## Установим библиотеку которая будет работать с .env

`pip install python-dotenv`

Установим библиотеку для работы с телеграм (telegram)

`pip install python-telegram-bot`

Выгрузим зависимости

`pip freeze > requirements.txt`

## ⚠️ Безопасность

Никогда не загружай .env в публичные репозитории!

Обязательно добавь в .gitignore:

```gitignore
.env
```

## Для текстов с разметкой нам нужно указать языки для подсветки синтаксиса в markdown файлах

[Поддерживаемые в markdown языки программирования](https://github.com/jincheng9/markdown_supported_languages?tab=readme-ov-file#heres-a-full-list-of-supported-languages)
Это проект jincheng9 / markdown_supported_languages
