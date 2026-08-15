"""[TASK] Виртуальное окружение."""

# 1. Что делает команда python -m venv venv?
#
# Создает виртуальное окружение venv
#
# 1.1 Что делает каждая команда в списке ниже?
#
# pip list
# pip freeze > requirements.txt
# pip install -r requirements.txt
#
# pip list - выводит список установленных пакетов и их версии.
# pip freeze > requirements.txt - сохраняет список установленных пакетов и их версий в файл requirements.txt.
# pip install -r requirements.txt - устанавливает пакеты из файла requirements.txt.
#
# 2. Что делает каждая команда в списке ниже?
#
# conda env list
# conda create -n env_name python=3.5
# conda env update -n env_name -f file.yml
# source activate env_name
# source deactivate
# conda clean -a
#
#
# conda env list - выводит список виртуальных окружений conda.
# conda create -n env_name python=3.5 - создает виртуальное окружение с именем env_name и версией питона 3.5.
# conda env update -n env_name -f file.yml - обновляет виртуальное окружение env_name из файла file.yml.
# source activate env_name - активирует виртуальное окружение env_name.
# source deactivate - деактивирует текущее виртуальное окружение.
# conda clean -a - очищает кэш после удаления виртуальных окружений.
#
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
# - Активировать виртуальное окружение
# - pip install package_name для venv
#   conda install package_name для conda
#
# 5. Что делают эти команды?
#
# pip freeze > requirements.txt
# conda env export > environment.yml
#
# pip freeze > requirements.txt - сохраняет список установленных пакетов и их версий в файл requirements.txt
# conda env export > environment.yml - сохраняет данные окружения conda в файл environment.yml
#
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
#
# 6. Что делают эти команды?
#
# pip install -r requirements.txt
# conda env create -f environment.yml.
#
# pip install -r requirements.txt - устанавливает пакеты из файла requirements.txt
# conda env create -f environment.yml. - создает виртуальное окружение conda на основе файла environment.yml
#
# 7. Что делают эти команды?
#
# pip list
# pip show
# conda list
#
#
# pip list - выводит список установленных пакетов и их версии.
# pip show - выводит информацию об указанном пакете.
# conda list - выводит список установленных пакетов и их версии из conda окружения.
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
# В pip больше пакетов, но большинство из них для python разработчиков
# Дата сайнинисты используют обычно conda, она содержит множество пакетов для DS и упрощает установку больших DS пакетов с множеством зависимостей
#
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
# 10. добавьте в .gitignore папку SENATOROV
#
# Добавил
#
# 11. Зачем нужно виртуально окружение?
#
# Изолировать пакеты и зависимости, необходимые для текущего проекта.
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#
# Да
#
# 13. Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
#
# Удалил
