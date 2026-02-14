"""[TASK] Виртуальное окружение."""

# Ответы
# 1. Создает виртуальное окружение в папке с названием venv
# 1.1 pip list: Выводит список всех установленных в текущем
# окружении пакетов и их версии.
#     pip freeze > requirements.txt: Сохраняет список всех
# установленных библиотек с их точными версиями в текстовый файл.
#     pip install -r requirements.txt: Устанавливает все
# библиотеки, перечисленные в указанном текстовом файле.
#
# 2. conda env list: Показывает список всех созданных виртуальных
# окружений Conda и путь к ним.
#     conda create -n env_name python=3.5: Создает новое окружение
# с именем env_name и устанавливает в него Python версии 3.5.
#     conda env update -n env_name -f file.yml: Обновляет пакеты в
# окружении env_name, используя список зависимостей из файла конфигурации .yml.
#     source activate env_name: Активирует виртуальное окружение
# (переключает терминал на работу внутри него).
#     source deactivate: Выходит из текущего виртуального окружения в базовое.
#     conda clean -a: Удаляет неиспользуемые пакеты, кэш загрузок и
# временные файлы для очистки места на диске.
#
# 3.  1) ![image-2.png](attachment:image-2.png)
#     2) ![image-3.png](attachment:image-3.png)
#
# 4. venv:
#         1. Активируйте окружение (Windows: `venv\Scripts\activate`,
# Linux/macOS: `source venv/bin/activate`)
#         2. Используйте pip: `pip install имя_пакета`
#     conda:
#         1. Активируйте окружение: `conda activate env_name`
# (или `source activate env_name` на Linux/macOS)
#         2. Используйте conda: `conda install имя_пакета`
# или pip: `pip install имя_пакета`
#
# 5.  pip freeze > requirements.txt - сохраняет все зависимости
# виртуального/глобального проекта в файл requirements.txt
#     conda env export > environment.yml - сохраняет все зависимости
# для Data Science виртуального/глобального проекта в файл environment.yml
# 5.1 ![image.png](attachment:image.png)
#
# 6.  pip install -r requirements.txt - устанавливает через pip
# зависимости из файла requirements.txt
#     conda env create -f environment.yml. - создает виртуальное
# окружение с помощью conda основанное на описание из environment.yml
#
# 7.  pip list - выводит список всех установленных пакетов
# Python с их версиями в текущем окружении.
#     pip show имя_пакета - выводит подробную информацию о конкретном
# пакете.
#     conda list - выводит список всех установленных пакетов
# в текущем conda-окружении с их версиями и источниками установки.
#
# 8. Обычно в conda, так как это уже готовая сборка под DS
# дата сайнинисты используют обычно conda из-за того, что она
# специально настроена и имеет нужные пакеты для работы с DS
#
# 9. ![image-4.png](attachment:image-4.png)
#
# 10. ![image-5.png](attachment:image-5.png)
#
# 11. Для изолированной работы от глобального окружения, в
# виртуальном окружении связанным непосредственно с текущим
# проектом и его задачами.
# 12. Да
# 13. Удалил
