"""Работа с виртуальным окружением Venv."""

# 1) Что делает команда python -m venv venv?
# - создает виртуальное окружение(ставит Python в отедльной папке)
# 2) Что делает каждая команда в списке ниже?
# ![image.png](attachment:image.png)
# - pip list - показывает установленные пакеты
# - pip freeze > requirements.txt - выгружает список зависимостей
# в файл requirements.txt
# - pip install -r requirements.txt скачивает все зависимости из файла
# requirements.txt
# 3) Что делает каждая команда в списке ниже?
# ![image-2.png](attachment:image-2.png)
# - conda env list - показывает все существующие окружения conda
# - conda create -n env_name python=3.5 - создаёт окружение conda с именем
# env_name и версией python = 3.5
# - conda env update -n env_name -f file.yml - создает(если окружение есть то обновляет его)
# окружение env_name в соответствии с зависимостями, перечисленных в файле file.yml
# - source activate env_name - активирует окружение env_name
# - source deactivate - деактивирует текущее окружение
# - conda clean -a - очищает все ненужные файлы из кэша Conda
# вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
# ![image-3.png](attachment:image-3.png)
# - conda activate SENATOROV
# 4) Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#  - для venv pip install <необходимый пакет> или уже с готовым файлом с
# зависимостями написать pip install -r requirements.txt
# - для conda используем conda install <имя_пакета> или
# conda env -n update -f environment.yml
# 5) Что делают эти команды?
# - pip freeze -> requirements.txt - выгружают зависимости в файл requirements.txt
# - conda env export -> environment.yml - выгружают зависимости в файл
# environment.ymlpip freeze -> requirements.txt
# conda env export -> environment.yml
# 6) вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
# - conda ё(![image-4.png](attachment:image-4.png))
# - venv (![image-5.png](attachment:image-5.png))
# 7) Что делают эти команды?
# - pip install -r requirements.txt - Устанавливают зависимости в текущее окружение
# - conda env create -f environment.yml. - создает окружение с зависимостями из файла environment.yml
# 8) Что делают эти команды?
# - pip list - показывает список установленных пакетов
# - pip show, - выводит полную информацию об одном указанном пакете, установленном через pip
# - conda list - выводит список всех установленных пакетов в текущем conda-окружении
# 9) Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
# 10) вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
# - ![image-6.png](attachment:image-6.png)
# 11) добавьте в .gitignore папку SENATOROV
# - добавил
# 12) Зачем нужно виртуально окружение?
# - изолировать зависимости разных проектов, фиксировать версии пакетов,
# работать с разными версиями Python одновременно, не засорять глобальный
# интерпретатор
# 13) С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
# - да
# 14) Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
# - сделано

#
