"""Closes https://github.com/SENATOROVAI/intro-cs/issues/7."""

# 1. Что делает команда python -m venv venv?
# - создает переменную окружения venv в проекте
#
# 1.1 Что делает каждая команда в списке ниже?
# - pip list # выводит список библиотек и их зависимостей venv в терминал
# - pip freeze > requirements.txt # экспортирует библиотеки и зависимости из текущей venv в файл requirements.txt
# - pip install -r requirements.txt # импортирует либы из requirements.txt в venv или в глобальный python
#
# 2. Что делает каждая команда в списке ниже?
# - conda env list # выводит список либ и зависимостей проекта в менеджере пакетов и venv conda
# - conda create -n env_name python=3.5 # создание нового окружения env_name и установка в него python 3.5
# - conda env update -n env_name -f file.yml # обновление окружения по yml файлу
# - source activate env_name # активация venv env_name
# - source deactivate # выход из venv
# - conda clean -a # очистка кжша conda и освобождение места на диске
#
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
# ![Активация окружений](images/activate_venv_conda.png)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
# - conda env update -f environment.yml
# - pip install -r requirements.txt
#
# 5. Что делают эти команды?
# pip freeze > requirements.txt # экспортирует все библиотеки текущей venv и их зависимости в файл requirements.txt пакетным менеджером pip
#
# conda env export > environment.yml # экспортирует все библиотеки текущего окружения Conda и их зависимости в файл requirements.txt менеджером пакетов и окружений в файл environment.yml
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
# ![VENV](images/venv_screen.png)
#
# 6. Что делают эти команды?
# pip install -r requirements.txt # устанавливает либы и зависимости из файла requirements.txt в текущий venv при помощи пакетного менеджера pip.
#
# conda env create -f environment.yml. # создает новое окружение с именем env и устанавливает либы и зависимости из файла requirements.txt в текущее окружение Conda при помощи менеджера пакетов и окружения conda.
#
# 7. Что делают эти команды?
# pip list # выводят список библиотек, инсталлированных pip в текущем окружении
# pip show # показывает сведения о конкретной библиотеке
# conda list # показывает все все установленные пакеты в Conda-окружении, установленные через condа и многие установленные через pip.
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
# - по умолчанию пакетов больше в conda. DS используют conda, ибо в ней предустановлены основные бибилиотеки для исследований, такие как numpy, pandas и 20+ др.
#
#
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
# ![Interpreter](images/conda-interpreter.png)
#
# 10. добавьте в .gitignore папку SENATOROV
# ![gitignore-dir](images/adding-gitignore.png)
#
# 11. Зачем нужно виртуально окружение?
# - это изолированная среда Python, которая позволяет каждому проекту использовать свою версию Python и свой набор библиотек без влияния на глобальную систему и другие проекты.
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
# ДА!
#
# Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
# - Анигилировал

#
