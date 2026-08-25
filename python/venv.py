# %% [markdown]
# 1. Что делает команда python -m venv venv?  
# создаёт виртуальное окружение под названием venv
# 1.1. Что делает каждая команда в списке ниже?  
# pip list - список загруженных библиотек
# pip freeze > requirements.txt - записать все загруженные библиотеки в файл requirements.txt
# pip install -r requirements.txt - установить все библиотеки из файла requirements.txt
# 2.
# conda env list - показывает все виртуальные окружения conda
# conda create -n env_name python=3.5 - создать виртуальное окружение conda
# conda env update -n env_name -f file.yml - доавить в виртуальное окружение библиотеки, записанные в file.yml
# source activate env_name - активировать виртуальную среду
# source deactivate - деактивировать виртуальную среду
# conda clean -a - очистить все временные файлы conda 
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
# https://drive.google.com/file/d/10odLejOH5pezPcFEp3c7KwBXqCyf5w3Y/view?usp=drive_link
# 
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#  conda install lib_name / pip install lib_name
# 5. Что делают эти команды?
# pip freeze > requirements.txt  записывает зависимости в файл requirements.txt
# conda env export > environment.yml  записывает зависимости в файл environment.yml
# 
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
# https://drive.google.com/file/d/1L8DCmBEfFWujOb-7oM1JQFzyXuw1qajg/view?usp=drive_link
# 6. Что делают эти команды?
# pip install -r requirements.txt  устанавливает библиотеки, написанные в файле requirements.txt
# conda env create -f environment.yml  устанавливает библиотеки, написанные в файле environment.yml
# 
# 7. Что делают эти команды?
# pip list - список всех установленных библиотек
# pip show lib_name краткая информация про библиотеку
# conda list - список всех установленных библиотек conda
# 
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
# в conda. потому что заранеее предустановлены если не все, то большинство библиотек, необходимых дата саентисту
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
# https://drive.google.com/file/d/1XXj7UYY_YYALGNImDkuOddU_AjokNTeX/view?usp=drive_link
# 10. Зачем нужно виртуальное окружение?
# виртуальное окружение необходимо, чтобы можно было комфортно использовать различные версии одних и тех же библиотек для разных 
# проектов, а также для избегания конфликтов между разными версиями библиотек
# 11. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
# да
