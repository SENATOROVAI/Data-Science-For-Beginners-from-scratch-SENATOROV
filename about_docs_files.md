# Как пример оформления GitHub репозитория посмотрим

1) [kandinsky_модель_генерации_видео_по_тексту_видео_аудио](https://github.com/ai-forever/Kandinsky-4/blob/main/README.md)

2) [DeepSeek_Математика](https://github.com/deepseek-ai/DeepSeek-Math/blob/main/README.md)

В файл README.md нужно добавлять информацию о нашем проекте, если это учебный репозиторий, так и напишем, можно показать структуру проекта в формате

project_root/
├── requirements.txt          # зависимости проекта
├── setup.py                  # (если проект - пакет)
├── README.md                 # описание проекта
└── LICENSE                   # лицензия

Далее идет пример README.md в дальнейшем нужно изменять этот файл под наш проект, а пока пусть будет "болванка".

## 🚀 Как работать с этим репозиторием

### 📦 Установка

#### Клонируйте репозиторий:

`git clone https://github.com/USERNAME/REPO_NAME.git`

`cd REPO_NAME`

#### (Рекомендуется) создайте виртуальное окружение:

`python -m venv venv`

`source venv/bin/activate`  # Windows: venv\Scripts\activate

#### Установите зависимости

`pip install -r requirements.txt`

### 🧪 Запуск тестов (если есть)

`pytest`

### 📚 Генерация документации (Sphinx)

`cd docs` - Перейдите в папку документации:

`make html` - Сгенерируйте HTML-документацию:

Откройте в браузере:
`open _build/html/index.html`  # Windows: `start _build/html/index.html`

### 🚀 Авто-публикация документации

Документация автоматически собирается и публикуется на GitHub Pages при каждом коммите в ветку main.

Ссылка на документацию:
👉 https://USERNAME.github.io/REPO_NAME/

### 🛠️ Основные команды разработки

Установка зависимостей `pip install -r requirements.txt`
Запуск тестов `pytest`
Сборка документации `cd docs && make html`
Локальный просмотр доков открыть `docs/_build/html/index.html`

## Генератор документации Sphinx [link_doc](https://sphinx-ru-ng.readthedocs.io/ru/latest/sphinx.html#ltx-label)

Установка

`pip install sphinx` - c помощью pip:

`easy_install sphinx` - c помощью easy_install:

`sudo apt-get install python3-sphinx` - В стандартном репозитории Ubuntu 14.10 есть пакеты python-sphinx и python3-sphinx.

Sphinx для авто-документирования на проекте
Ознакомься с

1) [статья_habr_1](https://habr.com/ru/companies/otus/articles/799687/)

2) [статья_habr_2](https://habr.com/ru/articles/750968/)

3) [doc_sphinx](https://sphinx-ru-ng.readthedocs.io/ru/latest/sphinx.html#id3)

Pandas
Библиотека Python для обработки и анализа данных, которая использует Sphinx для создания своей обширной документации, включающей справочные материалы, руководства и учебные пособия.

NumPy
Библиотека для научных вычислений на Python, которая широко использует Sphinx для создания своей документации. Это подтверждает статус Sphinx как стандартного инструмента для документации в научной и академической среде Python.

Создаем файл .github/workflows/docs.yml в репозитории GitHub. Файл будет содержать инструкции для автоматизации генерации документации, вставьте всю инструкцию с сайта(1*) в ответ:

Ознакомься с:

1) https://habr.com/ru/companies/rostelecom/articles/570098/ (MkDocs)
Пошаговая инструкция как использовать MkDocs для создания сайта с документацией продукта

ветка или бренч -  представляет собой отдельное направление разработки, чаще всего вы будете видеть ветку dev, в неё сначала коммитят, потом сливаются с main, это сделано в первую очередь для безопасности.
