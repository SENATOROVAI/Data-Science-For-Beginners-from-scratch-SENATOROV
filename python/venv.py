"""Virtual environment task answers."""

# **Question 1.** What does the command `python -m venv venv` do?
#
# **Answer:** It creates a virtual environment in a folder named `venv`.
#
# Breaking it down:
# - `python -m venv` runs Python's built-in `venv` module.
# - The second `venv` is the name of the folder where the environment will be created (you could name it anything, e.g. `python -m venv myenv`).
#
# The command creates an isolated environment with its own Python interpreter and its own `site-packages` directory, separate from the global Python installation. Once activated, any packages you install go into this folder instead of the system-wide Python, keeping the project's dependencies isolated.

# **Question 1.1.** What does each command in the list below do?
#
# **Answer:**
#
# - **`pip list`** - shows all packages installed via pip in the active environment, along with their versions.
#
# - **`pip freeze > requirements.txt`** (#1) - outputs the installed pip packages with their exact versions and writes them into the `requirements.txt` file, so the dependencies can be saved and shared.
#
# - **`pip install -r requirements.txt`** (#2) - reads the `requirements.txt` file and installs all the packages listed in it into the active environment.

# **Question 2.** What does each command in the list below do?
#
# **Answer:**
#
# - **`conda env list`** (#1) - lists all conda environments on the system, showing their names and paths. The currently active environment is marked with an asterisk (`*`).
#
# - **`conda create -n env_name python=3.5`** (#2) - creates a new conda environment named `env_name` with Python 3.5 installed.
#
# - **`conda env update -n env_name -f file.yml`** (#3) - updates the environment `env_name` according to the specification in `file.yml`, adding or updating packages to match the file.
#
# - **`source activate env_name`** (#4) - activates the environment `env_name`. This is the older syntax; the modern equivalent is `conda activate env_name`.
#
# - **`source deactivate`** (#5) - deactivates the current environment and returns to base. The modern equivalent is `conda deactivate`.
#
# - **`conda clean -a`** - removes unused conda data (cached package tarballs, index caches, unused packages) to free up disk space.

# **Question 3.** Insert a screenshot of your terminal where you first activated venv, then conda. Name the environment "SENATOROV".
#
# **Answer:** Below is a screenshot of the terminal showing both environments activated in sequence, both named "SENATOROV":
#
# 1. `.\SENATOROV\Scripts\Activate.ps1` - activates the **venv**. The prompt shows `(SENATOROV) (base)`.
# 2. `deactivate` - deactivates the venv, returning to `(base)`.
# 3. `conda activate SENATOROV` - activates the **conda** environment. The prompt shows `(SENATOROV)`.
#
# The two are distinguishable: venv appears as `(SENATOROV) (base)` (nested), conda as just `(SENATOROV)`.
#
# ![Terminal activating venv then conda](./images/q3_venv_conda.png)

# **Question 4.**  How do you install the required packages inside a virtual environment for conda/venv?
#
# **Answer:** First activate the environment, then install packages into it.
#
# **For venv (using pip):**
# 1. Activate the venv: `.\SENATOROV\Scripts\Activate.ps1`
# 2. Install a package: `pip install package_name` (e.g. `pip install numpy pandas`)
#
# **For conda:**
# 1. Activate the environment: `conda activate SENATOROV`
# 2. Install a package: `conda install package_name` (e.g. `conda install numpy pandas`)
#
# In both cases, activating the environment first ensures the packages are installed into that isolated environment rather than the global system. With conda you can also install from a specific channel using `conda install -c channel_name package_name` (e.g. `conda install -c conda-forge package_name`).

# **Question 5.** What do these commands do? `pip freeze > requirements.txt` and `conda env export > environment.yml`
#
# **Answer:** Both commands export the dependencies of the current environment into a file, so the environment can be recreated later.
#
# - **`pip freeze > requirements.txt`** - lists all packages installed via pip in the active environment, with their exact versions, and writes them to `requirements.txt`. This is the standard dependency file for venv/pip projects.
#
# - **`conda env export > environment.yml`** - exports the full specification of the active conda environment to `environment.yml`. This is more complete than `pip freeze`: it includes the Python version, all conda packages with versions, the channels they come from, and any pip-installed packages as well.
#
# The key difference: `requirements.txt` captures only pip packages, while `environment.yml` captures the entire conda environment (Python version, conda + pip packages, and channels).

# **Question 5.1.** Insert a screenshot showing the VENV folder in your repository, as well as the dependency files `requirements.txt` and `environment.yml`. The files must contain dependencies.
#
# **Answer:** The screenshot below shows the `SENATOROV` venv folder in the repository, along with both dependency files containing their packages - `requirements.txt` (from `pip freeze`) and `environment.yml` (from `conda env export`).
#
# ![VENV folder with requirements.txt and environment.yml](./images/q5.1_venv_deps.png)

# **Question 6.** What do these commands do? `pip install -r requirements.txt` and `conda env create -f environment.yml`
#
# **Answer:** Both commands recreate an environment's dependencies from a file - they are the reverse of the export commands.
#
# - **`pip install -r requirements.txt`** - reads the `requirements.txt` file and installs all the listed pip packages (with their specified versions) into the **currently active** environment. It does not create a new environment; it installs into whatever environment is active.
#
# - **`conda env create -f environment.yml`** - creates a **new** conda environment from the specification in `environment.yml`, installing the defined Python version, channels, and all packages. The environment name is taken from the `name:` field inside the file.
#
# The key difference: `pip install -r` installs packages into an existing/active environment, while `conda env create -f` builds a brand-new conda environment from scratch based on the file.

# **Question 7.** What do these commands do? `pip list`, `pip show`, `conda list`
#
# **Answer:** All three display information about installed packages.
#
# - **`pip list`** - shows all packages installed via pip in the active environment, along with their versions, as a simple list.
#
# - **`pip show package_name`** - shows detailed information about one specific package: its version, summary, author, license, dependencies (Requires), what depends on it (Required-by), and its install location.
#
# - **`conda list`** - shows all packages installed in the active conda environment, with their versions, build strings, and the channel each came from.
#
# The difference: `pip list` and `conda list` give an overview of all installed packages (pip-only vs. the full conda environment respectively), while `pip show` gives detailed information about a single named package.

# **Question 8.** Where are there more packages by default, venv/pip or conda? And why do data scientists use conda?
#
# **Answer:**
#
# **Which has more packages:** pip has access to more packages overall. PyPI (the Python Package Index, used by pip) hosts far more packages than the default conda channels - virtually every Python package is published to PyPI, while conda channels contain a curated subset. (Conda can be extended with channels like `conda-forge`, which greatly expands its available packages, but by default pip/PyPI still covers more.)
#
# **Why data scientists use conda:**
#
# 1. **Manages non-Python dependencies.** Conda installs not just Python packages but also system-level libraries written in C/C++/Fortran (e.g. BLAS, LAPACK, MKL, CUDA toolkits). Many scientific libraries depend on these, and conda handles them automatically.
#
# 2. **Pre-compiled binaries.** Conda provides packages like NumPy, SciPy, TensorFlow, and PyTorch as ready-built binaries, so you avoid compiling from source and the build errors that often come with pip on Windows.
#
# 3. **Better dependency resolution.** Conda's solver checks for version conflicts across the whole environment before installing, reducing "dependency hell."
#
# 4. **Full environment management.** Conda can manage the Python version itself (not just packages) and create isolated environments with different Python versions easily.
#
# In short: pip/PyPI wins on raw package count, but data scientists prefer conda because it reliably installs complex scientific stacks (with their non-Python dependencies) without compilation headaches.

# **Question 9.** Insert a screenshot showing the selection of the Python interpreter (conda) in VS Code/Cursor.
#
# **Answer:** The screenshot below shows the conda `SENATOROV` environment selected as the Python interpreter in Cursor, with its path pointing to `anaconda3\envs\SENATOROV\python.exe`.
#
# ![Selecting the conda Python interpreter in Cursor](./images/q9_interpreter_conda.png)

# **Question 10.** Add the SENATOROV folder to .gitignore.
#
# **Answer:** Added the following line to the `.gitignore` file in the repository root: SENATOROV/

# **Question 11.** Why do you need a virtual environment?
#
# **Answer:** A virtual environment is an isolated environment that lets you install and use dependencies (libraries, packages) separately for each project, without affecting the global system or other projects. The main reasons it's needed:
#
# 1. **Dependency isolation.** Different projects may require different versions of the same library. A virtual environment keeps each project's dependencies separate so they don't conflict with each other.
#
# 2. **Keeps the global Python clean.** Packages are installed into the environment instead of the system-wide Python, avoiding clutter and version conflicts at the system level.
#
# 3. **Reproducibility.** The environment can be exported (`requirements.txt` / `environment.yml`) and recreated exactly on another machine, so the project runs the same way for everyone.
#
# 4. **Easier collaboration and deployment.** Teammates can recreate the identical environment from the dependency files, ensuring the code behaves consistently across different setups.
#
# In short: a virtual environment guarantees that each project has its own controlled, reproducible set of dependencies, independent of other projects and the global system.

# **Question 12.** From this point on, you need to work in the conda virtual environment. Have you learned to export dependencies and work with environments?
#
# **Answer:** Yes. I have learned to:
#
# - Create environments with both venv (`python -m venv SENATOROV`) and conda (`conda create -n SENATOROV python=3.13`).
# - Activate and deactivate environments (`conda activate SENATOROV` / `conda deactivate`, and the venv activate script).
# - Install packages into an environment (`pip install` for venv, `conda install` for conda).
# - Export dependencies to files (`pip freeze > requirements.txt` and `conda env export > environment.yml`).
# - Recreate environments from those files (`pip install -r requirements.txt` and `conda env create -f environment.yml`).
# - Inspect installed packages (`pip list`, `pip show`, `conda list`).
# - Select the conda interpreter in Cursor and exclude the environment folder from Git via `.gitignore`.
#
# From now on I will work inside the conda `SENATOROV` environment (or another conda environment as needed).

# **Question 13.** Delete the VENV folder - it's no longer needed, we're not developers, we only need conda.
#
# **Answer:** Deleted the `SENATOROV` venv folder from the repository, since the workflow will use the conda environment only: Remove-Item -Recurse -Force SENATOROV
