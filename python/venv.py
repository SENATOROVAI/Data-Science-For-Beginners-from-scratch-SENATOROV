"""Virtual environment."""

# Что делает команда python -m venv venv?
# * создает новое виртуальное окружение
#
# 1.1 Что делает каждая команда в списке ниже?
#
# ![image.png](attachment:image.png)

# pip list -> выводить в консоль всех установленных пакетов
#
# pip freeze > requiremens.txt ->  выгружает всех установленных пакетов  в файл requiremens.txt
#
# pip install -r requiremens.txt ->  устанавливает всех пакетов и зависимостей из файла requiremens.txt
#

# 2. Что делает каждая команда в списке ниже?
# conda env list - показывает все созданные среды
#
# conda create -n env_name python=3.5 -  создаёт новую виртуальную среду env_name  и устанавливает пайтон версию 3.5
#
# conda env update -n env_name -f file.yml - обновляет или создаёт новую среду  согласно файлу file.yml
#
# source activate env_name -  активирует среду env_name , делая её текущей
#
# source deactivate - Деактивирует текущую среду и возвращает в base
#
# conda clean -a - Очищает кэш и временные файлы conda

# вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"

# ![{855EB9ED-9BE2-4AD6-AADF-3E1B1B719F15}.png](attachment:{855EB9ED-9BE2-4AD6-AADF-3E1B1B719F15}.png)

# ![{055D1AD3-A0D7-483A-BDAB-6EFBB124B489}.png](attachment:{055D1AD3-A0D7-483A-BDAB-6EFBB124B489}.png)

# ![{FF3B54CF-1169-4D77-9244-2AA2570D24A0}.png](attachment:{FF3B54CF-1169-4D77-9244-2AA2570D24A0}.png)

# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
# pip install package_name
#
# conda install package_name

# 5. Что делают эти команды?
# pip freeze > requirements.txt
# conda env export > environment.yml
#
#  выгружает всех установленных пакетов  в файл requiremens.txt/environment.yml

#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости

# ![{96AD9824-6C0E-4D56-87A2-CCF73B1D6699}.png](attachment:{96AD9824-6C0E-4D56-87A2-CCF73B1D6699}.png)

# ![{EB637F20-C170-4F0C-8971-7E5A40FD9EDF}.png](attachment:{EB637F20-C170-4F0C-8971-7E5A40FD9EDF}.png)

# 6.   Что делают эти команды?
#  pip install -r requirements.txt ->
#  устанавливает пакеты которые находятся в файле requirements.txt
#
# conda env create -f environment.yml  ->
#  создаёт новую среду из файла environment.yml

# Что делают эти команды?
# pip list
# conda list
# * выводить в консоль всех установленных пакетов  в виртуальной окружении
# pip show
# * выводит информацию про установленном пакете (имя, версия, описание, путь файла и т.д)
#

#
# 8.  Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнтисты используют conda?
# conda -  здесь большинство  необходимые пакеты уже установлены и именно предназначено для data science

# 9.  вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
# ![{EA4FDD4E-90C3-4D61-8FEE-1444A827498A}.png](attachment:{EA4FDD4E-90C3-4D61-8FEE-1444A827498A}.png)

# 10.  добавьте в .gitignore папку SENATOROV
# ✅
# 11. Зачем нужно виртуальное окружение?
# Виртуальное окружение нужно для изоляции пакетов и зависимостей — чтобы каждый проект имел свои собственные версии библиотек, не конфликтующие с другими проектами
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?  Да, научилься пользоваться с базовыми командами
# 13.
# Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
# ✅
