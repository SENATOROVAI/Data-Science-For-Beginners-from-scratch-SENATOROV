Начнем с того что есть стандарт PEP-8.
Вот ссылка на него
[link](https://peps.python.org/pep-0008/)

В pep-8 очень много правил, но мы можем писать код согласно всем стандартам,
а нас будут поправлять и исправлять наш код в случае ошибок. Оказывается для этого служат
"Линтеры" которые находятся в файле `.pre-commit-config.yaml`

Этот файл нам позволяет запускать эти самые линтеры.

В официальном репозитории [cpython](https://github.com/python/cpython/blob/main/.pre-commit-config.yaml)
используется линтер - ruff
Но SENATOROV больше любит линтер pylint

Сперва найдем информацию про сам pre-commit (фреймворк для управления и поддержкой hooks для разных языков программирования)
Прежде чем запускать хуки, вам необходимо установить c помощью менеджера пакетов pip пакет pre-commit.
[link](https://pre-commit.com/#install)

зайдем в папку с проектом:

`cd C:\Users\auram\OneDrive\Документы\github\project`

активируем виртуальное окружение

`conda activate senatorov`

Используя pip устанавливаем в наше виртуальное окружение:

`pip  install  pre-commit`

`pre-commit --version` - что бы узнать версию установленного пакета

Затем в файл .pre-commit-config.yaml добавить следующее

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
```

Теперь нам нужно "поднять hook" (Install the git hook scripts)

`pre-commit install`

hook - это такой инструмент позволяющий запускать проверку линтерами на корректность.
и теперь pre-commit будет запускаться автоматически при git commit (когда мы будем создавать коммит)

И теперь, если мы напишем в файле lesson1.py не корректный код, и попытаемся сделать коммит, мы увидим ошибки и не сможем.

О линтере pylint
заменим содержимое файла .pre-commit-config.yaml на содержимое:
и посмотрим что тут можно настроить под себя

```yaml
- repo: https://github.com/nbQA-dev/nbQA                                                Эта строчка говорит что мы работает с файлами формата .ipynb (nbqa = ipynb)
    rev: 1.9.0
    hooks:
      - id: nbqa-pylint
        name: nbqa-pylint
        description: Run 'pylint' on a Jupyter Notebook
        entry: nbqa pylint
        language: python
        require_serial: true
        types_or: [jupyter, markdown]
        additional_dependencies: [pylint]
        args:                                                                           При настройке для себя обращаем внимание на аргументы args
          - --ignore=no_check*,__init__.py
          - --max-line-length=79
          - --const-naming-style=any
          - --disable=E0401,W0104,R0903,R1721,E1101,E0611,F0002,C0305,C0303,E2515       disable говорит о том какие ошибки мы хотим что бы линтер игнорировал


  - repo: https://github.com/pylint-dev/pylint                                          Эта строчка говорит что мы работает с файлами формата .py (где нет nbqa = py)
    rev: "v3.3.1"
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: python
        types: [python]
        args:
          [
            "--ignore=no_check*,__init__.py",
            "--max-line-length=79",
            "--const-naming-style=any",
            "--disable=E0401,W0104,R0903,R1721,E1101,E0611,F0002,C0305,line-too-long,C0303,E2515"
          ]
        additional_dependencies: [pylint]
```

Где можно посмотреть все эти коды есть pylint docs
[link](https://pylint.readthedocs.io/en/stable/tutorial.html)


О линтере black

добавим следующее содержимое в файл .pre-commit-config.yaml :


вариант, где ты указываешь repo: https://github.com/psf/black.git, обычно используется, когда тебе нужно явно привязаться к определённому репозиторию с хуками. Он удобен в таких случаях:

- Гарантированная версия хука Когда ты фиксируешь версию с rev: "24.10.0", это предотвращает неожиданные изменения в работе инструмента. Это полезно для командной работы, где важно, чтобы все пользовались одной версией

- Автоматическое получение хука При клонировании проекта с таким pre-commit конфигом хук будет загружен автоматически, даже если его нет в локальной системе.

- Использование готовых хуков из репозитория Некоторые инструменты предоставляют репозитории с уже настроенными хуками, и этот подход позволяет их использовать без ручной настройки.

```yaml
- repo: https://github.com/psf/black.git                      Эта строчка говорит что мы работает с файлами формата .py (где нет nbqa = py)
    rev: "24.10.0"
    hooks:
      - id: black

  - repo: https://github.com/nbQA-dev/nbQA                    Эта строчка говорит что мы работает с файлами формата .ipynb (nbqa = ipynb)
      rev: 1.9.0
      hooks:
        - id: nbqa-black
          name: nbqa-black
          description: Run 'black' on a Jupyter Notebook
          entry: nbqa black
          language: python
          require_serial: true
          types_or: [jupyter, markdown]
          additional_dependencies: [black]
```
Где можно посмотреть о литнтере black:
[link](https://black.readthedocs.io/en/stable/)


Еще мы хотим что бы наш код был строго типизированным, то есть этот линтер будет проверять, а все ли типы у нас указаны в коде.
Например:

```python
number: int = 1
name: str = "Senatorov"
```

Для таких проверок на строгую типизацию служит линтер mypy.
Есть документация на линтер mypy

[link](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#variables)
добавим следующее содержимое в файл .pre-commit-config.yaml :

```yaml
- repo: https://github.com/nbQA-dev/nbQA                  Эта строчка говорит что мы работает с файлами формата .ipynb (nbqa = ipynb)
    rev: 1.9.0
    hooks:
      - id: nbqa-mypy
        name: nbqa-mypy
        description: Run 'mypy' on a Jupyter Notebook
        entry: nbqa mypy
        language: python
        require_serial: true
        types_or: [jupyter, markdown]
        additional_dependencies:
          - mypy
          - pandas-stubs
          - git+https://github.com/numpy/numpy-stubs
          - mypy-extensions
          - types-requests
          - types-PyYAML
          - types-setuptools

        args:
          # - --cache-dir=/dev/null
          # - --cache-dir=nul
          # - --no-incremental
          - --non-interactive
          - --install-types
          - --explicit-package-bases
          - --ignore-missing-imports
          - --disallow-untyped-calls
          - --disallow-untyped-defs
          - --disallow-untyped-decorators
          - --strict
          - --extra-checks
          - --disallow-any-decorated
          - --disallow-any-generics
          - --local-partial-types
          - --pretty
          - --force-uppercase-builtins
          - --force-union-syntax
          - --warn-unreachable
          - --warn-redundant-casts
          - --warn-return-any
          - --disallow-any-explicit

  - repo: https://github.com/pre-commit/mirrors-mypy         Эта строчка говорит что мы работает с файлами формата .py (где нет nbqa = py)
    rev: v1.13.0
    hooks:
      - id: mypy
        args:
          # - --cache-dir=/dev/null
          # - --cache-dir=nul
          # - --no-incremental
          - --non-interactive
          - --install-types
          - --explicit-package-bases
          - --ignore-missing-imports
          - --disallow-untyped-calls
          - --disallow-untyped-defs
          - --disallow-untyped-decorators
          - --strict
          - --extra-checks
          - --disallow-any-decorated
          - --disallow-any-generics
          - --local-partial-types
          - --pretty
          - --force-uppercase-builtins
          - --force-union-syntax
          - --warn-unreachable
          - --warn-redundant-casts
          - --warn-return-any
          - --disallow-any-explicit


        additional_dependencies:
          - mypy
          - pandas-stubs
          - git+https://github.com/numpy/numpy-stubs
          - mypy-extensions
          - types-requests
          - types-PyYAML
          - types-setuptools
```


Пре коммит, может работать с линтерами которые вы установили локально, например используя команду pip install pylint , для этого надо указать явно в файле конфигурации, что вы хотите работать с линтерами которые стоят у вас локально. на сайт pre-commit, найдите в документации способ как это сделать, в ответ вставьте полную инструкцию, чтобы запускались локальные линтеры которые вы установили через pip
Локальная версия pylint используется, а не загружается из pre-commit.
что бы установить локальную версию

Установка pylint и nbQA для локальной версии запуска линтеров (то есть когда они запускаются у нас локально и установлены к нашем виртуальном окружении)

`pip install pylint nbqa`

Добавим nbqa-pylint в pre-commit, но так, чтобы он работал локально. nbQA позволяет запускать pylint на Jupyter Notebook (.ipynb файлах).

Сделаем новый файл .pre-commit-config.yaml со следующим содержимым
Добавляем nbqa-pylint как локальный хук:

```yaml
repos:
  - repo: local
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        require_serial: true
        args:
          - "--ignore=no_check*,__init__.py"
          - "--max-line-length=79"
          - "--const-naming-style=any"
          - "--disable=E0401,W0104,R0903,R1721,E1101,E0611,F0002,C0305,C0303,E2515"

      - id: nbqa-pylint
        name: nbqa-pylint
        entry: nbqa pylint
        language: system
        types: [jupyter]
        require_serial: true
        args:
          - "--ignore=no_check*,__init__.py"
          - "--max-line-length=79"
          - "--const-naming-style=any"
          - "--disable=E0401,W0104,R0903,R1721,E1101,E0611,F0002,C0305,C0303,E2515"
```

Локальный вариант установки линтеров (entry: pylint, language: system) удобен, когда ты их уже установил

теперь установим линтеры nbqa-black, black
black  форматирует обычные Python-файлы (.py).

nbqa-black запускает Black через nbQA, чтобы форматировать код внутри Jupyter-ноутбуков (.ipynb).

библиотека nbqa у нас уже установлена на предыдущем шаге

Как работает nbQA? nbQA позволяет запускать инструменты, которые обычно работают только с .py файлами, на .ipynb файлах. Он "извлекает" Python-код из ячеек ноутбука, применяет линтер или форматер, а затем возвращает исправленный код обратно.

Какие инструменты поддерживаются?

black → автоформатирование кода.

pylint → анализ качества кода.

flake8 → проверка соответствия PEP 8.

mypy → статическая проверка типов.

isort → сортировка импортов.

Пример использования:

```bash
nbqa black notebook.ipynb  # Форматирование кода в Jupyter-ноутбуке
nbqa pylint notebook.ipynb  # Запуск pylint для анализа кода
```

установим библиотеку black

`pip install black`

Добавим в файл .pre-commit-config.yaml со следующим содержимым

```yaml
      - id: black
        name: black
        entry: black
        language: system
        types: [python]
        require_serial: true

      - id: nbqa-black
        name: nbqa-black
        description: Run 'black' on a Jupyter Notebook
        entry: nbqa black
        language: python
        require_serial: true
        types_or: [jupyter, markdown]
        additional_dependencies: [black]
```

И осталось настроить линтер mypy.

`pip install mypy`

Добавим в файл .pre-commit-config.yaml

```yaml
      - id: mypy
        name: mypy
        description: Run 'mypy' for Python files
        entry: mypy
        language: python
        require_serial: true
        types: [python]
        additional_dependencies:
          - mypy
          - pandas-stubs
          - git+https://github.com/numpy/numpy-stubs
          - mypy-extensions
          - types-requests
          - types-PyYAML
          - types-setuptools

        args:
          - --non-interactive
          - --install-types
          - --explicit-package-bases
          - --ignore-missing-imports
          - --disallow-untyped-calls
          - --disallow-untyped-defs
          - --disallow-untyped-decorators
          - --strict
          - --extra-checks
          - --disallow-any-decorated
          - --disallow-any-generics
          - --local-partial-types
          - --pretty
          - --force-uppercase-builtins
          - --force-union-syntax
          - --warn-unreachable
          - --warn-redundant-casts
          - --warn-return-any
          - --disallow-any-explicit

      - id: nbqa-mypy
        name: nbqa-mypy
        description: Run 'mypy' on Jupyter notebooks
        entry: nbqa mypy
        language: python
        require_serial: true
        types_or: [jupyter, markdown]
        additional_dependencies:
          - mypy
          - pandas-stubs
          - git+https://github.com/numpy/numpy-stubs
          - mypy-extensions
          - types-requests
          - types-PyYAML
          - types-setuptools

        args:
          - --non-interactive
          - --install-types
          - --explicit-package-bases
          - --ignore-missing-imports
          - --disallow-untyped-calls
          - --disallow-untyped-defs
          - --disallow-untyped-decorators
          - --strict
          - --extra-checks
          - --disallow-any-decorated
          - --disallow-any-generics
          - --local-partial-types
          - --pretty
          - --force-uppercase-builtins
          - --force-union-syntax
          - --warn-unreachable
          - --warn-redundant-casts
          - --warn-return-any
          - --disallow-any-explicit
```


Для запуска линтеров 

`pre-commit run --all-files`

установим линтер black который служит для исправления форматирования кода, пряма при проверках, он может это делать
убирать/добавлять лишние/нужные пробелы, отступы. И что круто это происходит автоматически.

