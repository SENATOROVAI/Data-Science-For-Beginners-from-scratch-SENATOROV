"""[TASK] Виртуальное окружение."""

# 1. Что делает команда python -m venv venv?
#     - создает виртуальное окружение
# 1.1 Что делает каждая команда в списке ниже?
#     - pip list - список установленных библиотек в виде таблицы
#     - pip freeze > requirements.txt - записать в файл requirements.txt установленные библиотеки
#     - pip install -r requirements.txt - установить зависимости из файла requirements.txt
# 2. Что делает каждая команда в списке ниже?
#     - conda env list - показывает список всех существующих окружений
#     - conda create -n env_name python=3.5 - создает виртуальное окружение для python=3.5
#     - conda env update -n env_name -f file.yml - обновляет окружение env_name на основе файла file.yml
#     - source activate env_name - активировать виртуальное окружение
#     - source deactivate - деактивировать виртуальное окружение
#     - conda clean -a - Удаляет все временные файлы, кэшированные пакеты, логи и т.д., чтобы освободить место
# 3. Вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#     ![image.png](attachment:image.png)
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#     - активировать виртуальное окружение, conda activate venv/source activate
#     - устанавливаешь пакеты с помощью conda install/pip install, conda install numpy pandas/pip install numpy
# 5. Что делают эти команды?
#     - pip freeze > requirements.txt, Сохраняет список всех установленных пакетов (и их версий) в файл requirements.txt
#     - conda env export > environment.yml, Экспортирует текущее окружение Conda в YAML-файл environment.yml
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#     - ![image-2.png](attachment:image-2.png)
# 6. Что делают эти команды?
#     - pip install -r requirements.txt - Устанавливает пакеты, перечисленные в файле requirements.txt
#     - conda env create -f environment.yml. - Создаёт новое окружение Conda из YAML-файла environment.yml
# 7. Что делают эти команды?
#     - pip list - Показывает все установленные пакеты
#     - pip show - Показывает подробную информацию об одном конкретном пакете
#     - conda list - Аналог команды pip list, но для Conda
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#     - В conda больше, т.к. по умолчанию установлены библиотеки дял дата сайнс
# 9. Вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#     - ![image-3.png](attachment:image-3.png)
# 10. Добавьте в .gitignore папку SENATOROV
#     - % cat .gitignore| grep SENATOROV
#     - SENATOROV
# 11. Зачем нужно виртуально окружение?
#     - Помогает работать с разными версиями пакетов на разных проектах
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#     - Да
# 13. Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
#     - % rm -fr venv
#
