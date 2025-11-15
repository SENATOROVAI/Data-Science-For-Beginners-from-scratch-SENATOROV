"""[TASK] Виртуальное окружение  #7."""

# 1. Что делает команда python -m venv venv?
#     - Создает виртуальное окружение в папке venv
#
# 1.1 Что делают команды:
#
#     - pip list - отображает список установленных модулей в текущем окружении
#     - pip freeze > requirements.txt - выгрузка установленных модулей в текущем окружении в файл requirements.txt
#     - pip install -r requirements.txt - установка модулей, записанных в файле requirements.txt
#
# 2. Что делают команды:
#     - conda env list - показывает список виртуальных сред conda
#     - conda create -n env_name python=3.5 - создает виртуальную среду с именем env_name и версией питона 3.5
#     - conda env update -n env_name -f file.yml - настройка виртуальной среды из файла file.yml
#     - source activate env_name (conda activate env_name) - переключение на виртуальную среду env_name
#     - source deactivate (conda deactivate) - отключение виртуальной среды
#     - conda clean -a - очистка кэша conda
#
# 3. Вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
#     ![image.png](attachment:image.png)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#     1. Активировать окружение
#     2. Установить пакеты через conda/pip install
#     3. Для venv можно загрузить пакеты из фала зависимостей pip install -r requirements.txt
#
# 5. Что делают эти команды?
#     - pip freeze > requirements.txt - выгрузка зависимостей в requirements.txt
#     - conda env export > environment.yml - экспорт виртуального окружения в environment.yml
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории, а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#     ![image-2.png](attachment:image-2.png)
#
# 6. Что делают эти команды?
#     - pip install -r requirements.txt - устанавливает пакеты из requirements.txt
#     - conda env create -f environment.yml - создает виртуальную среду из environment.yml
#
# 7. Что делают эти команды?
#     - pip list - выводит список всех установленных пакетов в виртуальном окружении
#     - pip show имя пакета - показывает подробную информацию об указанном пакете
#     - conda list - показывает список всех установленных пакетов в conda
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#     - pip имеет доступ к большему количеству пакетов
#     - в conda есть предварительно собранные пакеты для работы в ДС и она более удобная
#
# 9. Вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
#     ![image-3.png](attachment:image-3.png)
#
# 10. Добавьте в .gitignore папку SENATOROV
#     - echo SENATOROV/ >> .gitignore
#
# 11. Зачем нужно виртуальное окружение?
#     - Чтобы пакеты и их различные версии не конфликтовали друг с другом в разных проектах
#     - Удобство
#     - Для тестирования разных версий и конфигураций
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#     - ✓
#
#

#
