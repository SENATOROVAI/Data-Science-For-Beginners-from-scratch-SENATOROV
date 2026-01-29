"""2026-01-29 [TASK] Виртуальное окружение."""

#
# 1. Что делает команда python -m venv venv?
#
#     - создаёт виртуальное окружение в папке venv в текущем проекте.
#
# 1.1 Что делает каждая команда в списке ниже?
#
# ![список1](img/command_python.png)
#
#     - pip list -> выводит список установленных пакетов в текущем окружении;
#     - pip freeze > requirements.txt -> выгружает в файл requirements.txt список всех установленных пакетов из окружения;
#     - pip install -r requirements.txt -> устанавливает все пакеты перечисленные в файле requirements.txt.
# 2. Что делает каждая команда в списке ниже?
#
# ![список2](img/command_conda.png)
#
#     - conda env list
#     - conda create -n env_name python=3.5
#     - conda env update -n env_name -f file.yml
#     - source activate env_name
#     - source deactivate
#     - conda clean -a
#
#
#     вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
#     Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
#     Что делают эти команды?
#     pip freeze > requirements.txt
#     conda env export > environment.yml
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
#     Что делают эти команды?
#     pip install -r requirements.txt
#     conda env create -f environment.yml.
#
#     Что делают эти команды?
#     pip list
#     pip show,
#     conda list
#
#     Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
#     вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
#     добавьте в .gitignore папку SENATOROV
#
#     Зачем нужно виртуально окружение?
#
#     С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#
#     Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
#
