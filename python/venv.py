"""Learning log: виртуальное окружение."""

#  Что делает python -m venv venv?
# создает вирт окр для  со своими пакетами и настройками
#
#
# - pip list — список  пакетов
# - pip freeze > requirements.txt — сохраняет список пакетов в файл
# - pip install -r requirements.txt — утсновка пакетов с файла
#
#
# - conda env list — список окр
# - conda create -n env_name python=3.5 — создание вирт окр
# - conda env update -n env_name -f file.yml — обновление пакетов с файла
# - source activate env_name — активирует вирт окр
# - source deactivate — деактивация вирт окр
# - conda clean -a — очистка

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# pip indtsll пакет = установка пакета в venv
# conda install пакет = установка в conda

# PIP freeze > requirements.txt = загрузить пакеты в файл
# сonda env export > environment.yal = тоже самое в конде

# pip install -r = cкачать пакеты из файла requirements
# conda env freate -f = тоже в конде из environment

# pip list = cписок пакетов
# pip show = информация о пакете ее версия и тд
# conda list= список в конде

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# где по умолчанию больше пакетов в venv или в conde и почему ДС используют конду? = пакетов больше в venv,но для задач ДС лучше подходят пакеты из конды там готовые пакеты бинарки и допускает конфликт версии.

# ![image.png](attachment:image.png)

# Зачем нужно виртуально окружение? = это изолированое пространство проекта со своими настройками для удобства проекта
