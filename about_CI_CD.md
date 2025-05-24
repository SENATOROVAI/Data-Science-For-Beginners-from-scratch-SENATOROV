# Фундаментальная база по CI/CD

Если у нас работает команда, каждый может писать код по разному, и мы не можем проконтролировать, использует человек линтеры или нет, но нам это и не нужно, ведь у нас есть инструмент github Actions с его помощью мы можем на стороне github проверять качество кода каждого разработчика.

Можем создать новый репозиторий, с именем test_CI_CD
В нем жмем -> Actions -> затем в поиске ищем pylint (для примера) -> Configure на нем, 
и откроется конфигурация pylint.yaml файл. Соответственно код в github будет проверятся этим линтером.

```yaml
name: Pylint

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10"]
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
    - name: Analysing the code with pylint
      run: |
        pylint $(git ls-files '*.py')
```

Эту конфигурацию (по умолчанию) можно редактировать в соответствии с нужным нам поведением.
жмем -> Commit changes и затем Sign off commit changes

Вот так выглядит конфигурация линтера pylint в проекте scratch-SENATOROV файл .github/workflows/pylint.yml

```yaml
name: "SENATOROV"                          # Так выглядит доработанный файл линтера pylint для ipynb и py файлов

permissions:
  contents: write  # Grant write access to the repository contents
on:
  push:
    branches:
      - "**"
   
  schedule:
    - cron: "0 0 * * *" # Run every day
  workflow_dispatch:
  create:
  delete:
  release:
  issues:
 
jobs:
  pylint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        allow-prereleases: true
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install "nbqa[toolchain]" pylint nbqa
    - name: Pylint
      run: |                                            # Внимание!!! В файле .pre-commit.yaml должны быть точно такие же коды ошибок, чтобы линтеры работали синхронно.
        pylint --max-line-length=79 --const-naming-style=any --disable=R1721,R0903,C0303,E1101,R1716,E0401,W1514,C0200,C0114,C0301,E0602,W0104,C0302,R0801,E1136,line-too-long,C0305,E2515 --disable=import-error $(git ls-files '*.py' '*.ipynb')
        nbqa pylint --max-line-length=79 --const-naming-style=any --disable=R1721,R0903,E2515,C0303,E1101,R1716,E0401,W1514,C0200,C0114,C0301,E0602,W0104,C0302,R0801,E1136,C0305,E2515 --disable=import-error $(git ls-files '*.py' '*.ipynb')
```

Теперь благодаря github Actions невозможно будет сделать push в удаленный репозиторий если код не пройдет проверки линтера pylint. Github Actions позволяет разработчикам автоматизировать рабочие процессы (workflows) непосредственно в репозитории, используя файлы конфигурации в формате YAML

Чтение документации - очень важный навык.

GitHub Actions documentation

[link](https://docs.github.com/en/actions)

Workflow syntax for GitHub Actions

[link](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)

Универсальный линтер, для тех кому лень что-то настраивать
Super-Linter
[Репозиторий:](https://github.com/github/super-linter)

Описание: Объединяет множество линтеров для различных языков в одном действии.

```yaml
- name: Run Super-Linter
  uses: github/super-linter@v4
  env:
    VALIDATE_ALL_CODEBASE: true
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

CI: Continuous Integration workflows
Deployments: Deployment workflows
Automation: Automating workflows
Code Scanning: Code Scanning workflows
Pages: Pages workflows

CI - простыми словами, это мы с вами коммитим в гитхаб, и в гитхабе есть такая штука которая автоматический запускает линтеры, и другие тесты, которые проверяют наш код, Github Actions это он есть.

CD - простыми словами это уже происходит после процедуры проверки кодом линтерами, мы код отправили на гитхаб, его проверили линтеры там, потом этот код с помощью специальных механизмов отправляется на ваш VPS, так вот автоматическая отправка кода с вашего гитхаб на VPS это и есть CD

Основные возможности GitHub Actions:

Непрерывная интеграция (CI): автоматическая сборка и тестирование кода при каждом коммите или pull request.

Непрерывное развертывание (CD): автоматическое развертывание приложения на сервер или в облако после успешного тестирования.

Автоматизация задач: выполнение задач, таких как линтинг, форматирование кода, обновление зависимостей и многое другое.

Поддержка различных операционных систем: возможность запуска рабочих процессов на виртуальных машинах с Linux, Windows и macOS.
