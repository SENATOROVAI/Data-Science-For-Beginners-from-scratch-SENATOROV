"""This is a homework from Stepik.

8.2 conda:Пакетный менеджер для Data Science
"""

# **<h1>Gosha's Questions & Responses:</h1>**

# ![](1.png)
# 1. Shows a list of existing ENVs within conda on a PC
# 2. Creates a new ENV (flag `-n` stands for name, `python=x.x.x` - stands for a version of Python in the ENV)
# 3. Updates an ENV of conda with the name env_name by reading the file with dependencies
# 4. source is deprecated though, but, it has to be `conda activate ...`, which in turn activates an existing ENV
# 5. The same , but deactivate the current ENV.  `conda deactivate`

# ![](2.png)
# 1. Shows a list of installed dependencies
# 2. executes `pip freeze` which generates a list of needed dependencies for the current project and redirects the command's stdout to the file
# 3. Packet Manager `pip` installs all dependencies , which specified in `requirements.txt`

# <h3>The next task:</h1>

# **3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"**
#
#
# ![](3.png)
# <p>I did not activate venv, because it does not make sense while being in conda</p>
#

# **4.Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?**
#
# 1. conda install
# 2. pip install
# 3. uv pip install
#

# **5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости**
#
# ![](5.png)
#

# ### 6. Что делают эти команды?
# -`pip install -r requirements.txt`
#
# -`conda env create -f environment.yml`
#
#
# 1. Installing of the existing requirements drawning on the file in the project root
# 2. The same, but for conda

# ### 7. Что делают эти команды?
#
# - `pip list`
# - `pip show`
# - `conda list`
# <hr>
#
# - `pip list` - shows a list of installed packages in current env
# - `pip show` - shows a thorough info about a package
# - `conda list` - shows a list of installed packages in current conda env

# ### 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
#
#
# By default there are more packages in conda , and in Data Science they usually use  conda, since by default there are many DS packages

# ### 9. Bcтавьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
#
# ![](6.png)

# ### 10. Добавьте в .gitignore папку SENATOROV
#
# ![](7.png)

# ### 11. Зачем нужно виртуально окружение?
#
# Since it isolates you global interpreter from installation of a ton of packages, which you need in particular only for a single individual case

# ### 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#
# Yes

# ### 13. Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
#
# Done:
#
# ![](8.png)
