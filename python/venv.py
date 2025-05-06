"""
Ответы на вопросы по теме: "Виртуальное окружение".
"""

# %% [markdown]
# Что делает команда python -m venv venv?
# 
#     Создает виртуальное окружение с именем venv в текущей директории.

# %% [markdown]
# pip list – Показывает список установленных пакетов Python в текущем окружении.
# pip freeze > requirements.txt – Создает файл requirements.txt, записывая в него список установленных пакетов и их версии.
# pip install -r requirements.txt – Устанавливает все пакеты, перечисленные в requirements.txt.

# %% [code]
# !pip list

# %% [code]
# !conda env list

# %% [markdown]
# ![alt text](screensdhots/Screenshot_1.png)

# %% [markdown]
# Что делает каждая команда в списке ниже?
# 
#     conda env list –   
#     Выводит список всех Conda-окружений, доступных в системе.
# 
#     conda create -n env_name python=3.5 – 
#     Создает новое Conda-окружение с названием env_name и устанавливает в него Python версии 3.5.
# 
#     conda env update -n env_name -f file.yml – 
#     Обновляет окружение env_name согласно зависимостям, указанным в файле file.yml.
# 
#     source activate env_name – 
#     Активирует окружение env_name.
# 
#     source deactivate – 
#     Деактивирует текущее Conda-окружение.
# 
#     conda clean -a – 
#     Очищает кеш Conda, удаляя временные файлы, устаревшие пакеты и другие ненужные данные.

# %% [markdown]
# Вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"

# %% [markdown]
# ![alt text](screensdhots/Screenshot_2.png)

# %% [markdown]
# ![alt text](screensdhots/image.png)

# %% [markdown]
# Что делают эти команды?
# pip freeze > requirements.txt
#     Сохраняет установленные pip packages в requirements.txt
# conda env export > environment.yml
#     Экспортирует текущие Conda configuration и packages environment в environment.yml

# %% [markdown]
# вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости

# %% [markdown]
# ![alt text](screensdhots/Screenshot_4.png)

# %% [markdown]
# Что делают эти команды?
# pip install -r requirements.txt
#     Устанавливает все пакеты, перечисленные в файле requirements.txt, с помощью pip.
# conda env create -f environment.yml.
#     Создает новую виртуальную среду Conda на основе конфигурации, указанной в файле environment.yml

# %% [markdown]
# Что делают эти команды?
# - pip list: Список всех пакетов, установленных через pip.
# - pip show: Подробная информация о конкретном пакете.
# - conda list: Список всех пакетов в текущей Conda-среде.

# %% [markdown]
# Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
# 
#     По количеству пакетов pip (PyPI) значительно превосходит conda. Однако conda предоставляет высококачественные, предкомпилированные пакеты для задач, связанных с data science. Есть специальные packages (NumPy, Pandas, SciPy)

# %% [markdown]
# вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor

# %% [markdown]
# ![alt text](screensdhots/Screenshot_5.png)

# %% [markdown]
# добавьте в .gitignore папку SENATOROV

# %% [markdown]
# ![alt text](screensdhots/Screenshot_6.png)

# %% [markdown]
# Зачем нужно виртуальное окружение?
# 
#     Виртуальное окружение в Python используется для изоляции зависимостей проекта. Это особенно важно при работе с несколькими проектами, чтобы избежать конфликтов между версиями библиотек.

# %% [markdown]
# С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
# 
#     +

# %% [markdown]
# Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
# 
#         done