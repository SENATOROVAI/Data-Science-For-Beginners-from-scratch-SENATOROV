"""[TASK] Виртуальное окружение."""

# 1. Что делает команда python -m venv venv?
#
# Ответ:
# Создает виртуальное окружение в папке venv
#
# 1.1 Что делает каждая команда в списке ниже?
# pip list
# pip freeze > requirements.txt
# pip install -r requirements.txt
#
# Ответ:
# pip list - выводит список установленных пакетов Python с их версиями.
# pip freeze > requirements.txt - сохраняет список установленных пакетов и их версий в файл requirements.txt.
# pip install -r requirements.txt - устанавливает пакеты и версии, перечисленные в requirements.txt.
#
# 2. Что делает каждая команда в списке ниже?
#    conda env list
#    conda create -n env_name python=3.5
#    conda env update -n env_name -f file.yml
#    source activate env_name
#    source deactivate
#
# conda clean -a
#
# Ответ:
#
# conda env list - выводит список всех созданных conda-окружений и указывает активное.
# conda create -n env_name python=3.5 - создает новое окружение с именем env_name и Python 3.5.
# conda env update -n env_name -f file.yml - обновляет окружение env_name зависимостями из YAML-файла.
# source activate env_name - активирует окружение env_name.
# source deactivate - деактивирует текущее окружение.
# conda clean -a - удаляет кеш conda, неиспользуемые пакеты и индексные файлы для освобождения места.
#
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
# Ответ:
#
# venv: ![image.png](attachment:image.png)
#
# conda: ![image-2.png](attachment:image-2.png)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
# Ответ:
#
# venv:
#
# 1. Активируйте окружение (Windows: `venv\Scripts\activate`, Linux/macOS: `source venv/bin/activate`)
# 2. Используйте pip: `pip install имя_пакета`
#
# conda:
#
# 1. Активируйте окружение: `conda activate env_name` (или `source activate env_name` на Linux/macOS)
# 2. Используйте conda: `conda install имя_пакета` или pip: `pip install имя_пакета`
#
# 5. Что делают эти команды?
#    pip freeze > requirements.txt
#    conda env export > environment.yml
#
# Ответ:
#
# pip freeze > requirements.txt - сохраняет все зависимости виртуального/глобального проекта в файл requirements.txt
# conda env export > environment.yml - сохраняет все зависимости для Data Science виртуального/глобального проекта в файл environment.yml
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
# Ответ:
# ![image-3.png](attachment:image-3.png)
#
# 6. Что делают эти команды?
#    pip install -r requirements.txt
#    conda env create -f environment.yml.
#
# Ответ:
#
# pip install -r requirements.txt - устанавливает через pip зависимости из файла requirements.txt
# conda env create -f environment.yml. - создает виртуальное окружение с помощью conda основанное на описание из environment.yml
#
# 7. Что делают эти команды?
#    pip list
#    pip show,
#    conda list
#
# Ответ:
#
# pip list - выводит список всех установленных пакетов Python с их версиями в текущем окружении.
# pip show имя_пакета - выводит подробную информацию о конкретном пакете.
# conda list - выводит список всех установленных пакетов в текущем conda-окружении с их версиями и источниками установки.
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
# Ответ:
#
# Обычно в conda, так как это уже готовая сборка под DS
# дата сайнинисты используют обычно conda из-за того, что она специально настроена и имеет нужные пакеты для работы с DS
#
#
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
# Ответ: ![image-4.png](attachment:image-4.png)
#
# 10. добавьте в .gitignore папку SENATOROV
#
# Ответ: Добавил
#
# 11. Зачем нужно виртуально окружение?
#
# Ответ:
# Для изолированной работы от глобального окружения, в виртуальном окружении связанным непосредственно с текущим проектом и его задачами.
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#
# Ответ: Да
#
# 13. Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
#
# Ответ: Удалил
#
