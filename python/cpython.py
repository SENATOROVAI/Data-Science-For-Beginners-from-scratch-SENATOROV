"""This module demonstrates CPython interpreter functionality."""
from IPython.display import Image

# 1. Что такое CPython и чем он отличается от Python?
#
# CPython — это основная и наиболее распространённая реализация Python,
#  написанная на языке C.
#
#
# Отличия CPython от Python:
#
#     Python — это язык программирования, его спецификация описывает синтаксис и семантику.
#     
#     CPython — это конкретная реализация Python, написанная на C,
#      которая интерпретирует и выполняет Python-код.
#
# Особенности CPython:
#
#     Является официальной реализацией Python.
#     Использует интерпретатор и виртуальную машину на C.
#     Поддерживает GIL (Global Interpreter Lock), что ограничивает 
#     одновременное выполнение потоков.
#     Позволяет работать с расширениями на C, такими как NumPy и Pandas.
#
# Существуют и другие реализации Python, например:
#
#     PyPy — ускоренная версия с JIT-компиляцией.
#     Jython — реализация для JVM.
#     IronPython — для .NET.
#     MicroPython — для микроконтроллеров.
#
#

# +
image1 = "C:/Users/adm/Downloads/393432526"

image2="-325fd195-ad0d-4a3b-897f-2af536179877.png"

full_imag = image1+image2

img1 = Image(full_imag)

img1



# -

# Основные реализации Python:
#
#     CPython – стандартная и самая популярная реализация, написанная на C.
#     PyPy – альтернативная реализация с JIT-компилятором, ускоряющая выполнение кода.
#     Jython – реализация на Java для работы в JVM (Java Virtual Machine).
#     IronPython – версия Python для .NET и CLR (Common Language Runtime).
#     MicroPython – облегчённая версия Python для микроконтроллеров.
#     RustPython – экспериментальная реализация на языке Rust.
#     Brython – реализация для работы Python в браузере, заменяющая JavaScript.
#
#     CPython — основная и самая популярная реализация Python, используемая большинством разработчиков. Именно её вы скачиваете с официального сайта Python, и именно она используется в большинстве проектов.

# 4. На каком языке написан CPython?
#
# CPython написан на языке C. Именно поэтому он называется CPython — это стандартная реализация Python, написанная на C и использующая интерпретатор, также написанный на C.
#
# Кроме языка C, в CPython также используются:
#
#     Cython — для оптимизации производительности в некоторых модулях.
#     Assembly (Assembler) — в небольших частях для низкоуровневой оптимизации.
#     Python — сам Python используется для тестирования и вспомогательных инструментов.
#
# CPython — это официальная реализация Python, и именно она распространяется на python.org.

# 5. Кто создал CPython?
#
# CPython (и сам язык Python) был создан Гвидо ван Россумом (Guido van Rossum) в 1989 году. Первая версия Python 0.9.0 вышла в 1991 году.
#
# 6. Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?
#
# Хотя Python является интерпретируемым языком и в целом медленнее компилируемых языков (например, C или C++), он всё же считается достаточно быстрым благодаря:
#
#     Оптимизированной реализации CPython, использующей библиотеки на C.
#     Компиляции в байт-код, который выполняется быстрее, чем чистый исходный код.
#     Использованию высокопроизводительных библиотек, написанных на C/C++ (например, NumPy, Pandas).
#     JIT-компиляции в PyPy, которая ускоряет выполнение кода.
#
# 7. Путь к интерпретатору CPython на вашем компьютере
#
# C:\Users\ВашеИмя\AppData\Local\Programs\Python\PythonXX\python.exe
#
#
#

# Структура CPython
#
# 8. Что содержится в папке include в CPython?
#
# В папке include CPython находятся заголовочные файлы (.h), необходимые для компиляции и взаимодействия с ядром Python.
#
# Основные файлы в include содержат:
#
#     Python.h – главный заголовочный файл для работы с API Python из C.
#     object.h – описание базовой структуры объектов Python.
#     listobject.h, dictobject.h – структуры для списков и словарей.
#     eval.h – функции интерпретатора для выполнения кода.
#     pystate.h – управление состоянием интерпретатора Python.
#
# Эти файлы нужны для создания расширений на C и работы с Python C API.
#
# 9. Где можно найти исходный код CPython
# https://github.com/python/cpython
#

# Как работает интерпретатор CPython при выполнении кода

# 10. Как работает интерпретатор CPython при выполнении кода

# 10.1 Чтение исходного кода
#
# Файл .py загружается в память, а интерпретатор читает его как обычный текс

# 10.2 Лексический и синтаксический анализ (парсинг)
#
#     Код разбивается на токены (слова и символы).
#     Из токенов строится абстрактное синтаксическое дерево (AST), отражающее структуру программы.

# 10.3 Компиляция в байт-код
#
#     AST преобразуется в байт-код – последовательность инструкций для виртуальной машины Python (PVM).
#     Байт-код может кэшироваться в .pyc файлах (__pycache__).

# 10.4 Исполнение байт-кода на PVM
#
#     Виртуальная машина Python (PVM) интерпретирует байт-код, выполняя его команду за командой.
#     PVM использует стек, регистры и память для выполнения операций.

# 10.5 Управление памятью и выполнение кода
#
#     Объекты создаются и хранятся в памяти.
#     Работает сборщик мусора (GC), удаляя неиспользуемые объекты.
#     Глобальная таблица имен отслеживает переменные и функции.

# 11. Какая команда используется для запуска файла с помощью CPython

# Для запуска Python-файла с помощью CPython используется команда:  
#
# python filename.py
#
# python3 filename.py
#
# python3.11 filename.py
#

# 12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему? 
#
# Нет, обычные текстовые файлы (.txt) нельзя запускать через интерпретатор Python, потому что они не содержат исполняемый Python-код.
#
# Почему?
#
#     Python ожидает, что файл содержит синтаксически корректный код на Python.
#     Текстовый файл содержит произвольный текст, который не соответствует правилам Python.
#
# Если попытаться запустить текстовый файл, например: python file.txt интерпретатор выдаст ошибку SyntaxError
#

# 13. Как указать путь к интерпретатору и файлу для выполнения кода
#
# C:\Users\adm\AppData\Local\Programs\Python\Python39\python.exe C:\path\to\script.py - Windows 
#
# /usr/bin/python3 /home/user/script.py - Linux/macOS
#
#
#  

# 14. Основные отличия PyPy от CPython
#
# 14.1 PyPy отличается от CPython тем, что использует JIT-компиляцию (Just-In-Time), которая позволяет значительно ускорять выполнение кода, тогда как CPython интерпретирует байт-код построчно. Это делает PyPy быстрее в большинстве случаев, особенно в вычислительно сложных задачах.
#
# 14.2 CPython поддерживает все C-расширения, такие как NumPy и TensorFlow, без ограничений, тогда как PyPy может испытывать сложности с некоторыми из них.
#
# 14.3 В управлении памятью CPython использует счетчик ссылок, что может приводить к накладным расходам, в то время как PyPy применяет более эффективный механизм сборки мусора без счетчика ссылок, что снижает нагрузку на систему.
#
# 14.4 PyPy также более экономно использует память по сравнению с CPython, но из-за особенностей JIT-компиляции он может потреблять больше ресурсов в начале работы программы.
#

# 15. Почему PyPy не может использоваться для всех проектов на Python?
#
#     Ограниченная поддержка C-расширений
#     Многие популярные библиотеки, такие как NumPy, SciPy и TensorFlow, зависят от модулей, написанных на C. PyPy поддерживает не все C-расширения или может работать с ними медленнее, чем CPython.
#
#     Выше потребление памяти в некоторых случаях
#     Хотя PyPy эффективно управляет памятью, его JIT-компилятор может потреблять больше ресурсов в начале работы программы, что делает его менее подходящим для маломощных устройств.
#
#     Медленный старт программы
#     JIT-компиляция ускоряет выполнение долгих задач, но на старте программы может происходить дополнительная нагрузка на процессор. Это делает PyPy менее эффективным для небольших скриптов и командных утилит.
#
#     Не всегда 100% совместимость с CPython
#     Хотя PyPy старается поддерживать стандарт Python, его внутренняя реализация может вести себя немного иначе, что иногда вызывает несовместимость с кодом, написанным для CPython.
#
#     Ограниченная поддержка от разработчиков библиотек
#     Большинство библиотек разрабатываются и тестируются с учетом CPython, а PyPy рассматривается как второстепенная платформа, что может привести к неожиданным проблемам.
#
# Из-за этих ограничений PyPy лучше всего подходит для вычислительных задач, но не всегда удобен для проектов, активно использующих C-расширения и быстрый запуск.

# 16. Где можно скачать PyPy?
# https://pypy.org/download.html

# 17. Как установить PyPy после скачивания?
#
#     Скачивание: Перейдите на официальный сайт PyPy и загрузите версию, соответствующую вашей операционной системе.
#
#     Распаковка:
#         Windows: Распакуйте загруженный архив в удобное для вас место, например, C:\pypy.
#         Linux и macOS: Распакуйте архив в выбранную директорию, например, /opt/pypy.
#
#     Настройка переменной PATH (опционально):
#         Windows:
#             Добавьте путь к директории pypy в системную переменную PATH.
#             Для этого перейдите в "Панель управления" → "Система" → "Дополнительные параметры системы" → "Переменные среды" и добавьте путь, например, C:\pypy, в переменную PATH.
#         Linux и macOS:
#             Добавьте путь к pypy в файл ~/.bashrc или ~/.zshrc:
#
#             export PATH=/opt/pypy/bin:$PATH
#
# Затем примените изменения командой source ~/.bashrc или source ~/.zshrc.
#

# 18. Как запустить файл с помощью PyPy?
#
#     Через командную строку:
#         Откройте терминал или командную строку.
#         Перейдите в директорию с вашим скриптом: 
#         
#         cd путь/к/вашему/скрипту
#

# Запустите скрипт с помощью PyPy:
#
# pypy ваш_скрипт.py
#
#
#

# Если вы не добавили PyPy в переменную PATH, укажите полный путь к исполняемому файлу pypy:
#
# /путь/к/pypy/bin/pypy ваш_скрипт.py
#

# 19.  Почему PyPy выполняет код быстрее, чем CPython?
#
# PyPy достигает более высокой производительности по сравнению с CPython благодаря использованию JIT-компиляции (Just-In-Time). JIT-компилятор анализирует исполняемый код во время выполнения и оптимизирует его, компилируя часто используемые части кода непосредственно в машинный код. Это позволяет значительно ускорить выполнение программ, особенно тех, которые содержат интенсивные вычисления или часто повторяющиеся операции.
#
# В отличие от CPython, который интерпретирует код построчно, PyPy компилирует горячие участки кода в машинный код, что снижает накладные расходы на интерпретацию и повышает общую скорость выполнения программ.
#
# Однако стоит отметить, что выигрыш в производительности может варьироваться в зависимости от конкретного приложения и его характера. В некоторых случаях, особенно при использовании C-расширений или ввода-вывода, разница в скорости может быть менее заметной.

# Практика 1 
#  python --version 

# +

ima = Image("C:/Users/adm/Pictures/2025-02-10_15-33-19.png") 
ima
# -

# Практика2 
# Для выполнения указанных вами действий, выполните следующие шаги:
#
# 1. Найдите папку, где установлен Python:
#
#     Для Linux:
#         Откройте терминал.
#         Введите команду: which python
#         или, если используете Python 3:
#         which python3
# Для Windows:
#
#     Нажмите Win + R, введите cmd и нажмите Enter.
#     Введите команду: where python
#     where python3
#
# Откройте папку include и изучите её содержимое:
# Для Linux:
#
#     Перейдите в директорию include внутри установленного Python - cd $(dirname $(which python))/../include
#
# Для подсчёта количества файлов на C в этой директории используйте команду: ls *.h | wc -l - Эта команда выведет количество файлов с расширением .h, которые обычно содержат объявления функций и структур на C.
#
# Для Windows:
#
#     Перейдите в директорию include внутри установленного Python - cd \path\to\python\include
# Для подсчёта количества файлов на C в этой директории используйте команду: dir *.h /b | find /c /v ""
#
# 3. Перейдите на GitHub-репозиторий CPython и найдите файл README:
#
#     Перейдите по ссылке: https://github.com/python/cpython.
#     В корне репозитория вы найдёте файл README.rst.
#     Откройте его, чтобы ознакомиться с информацией о проекте.
#
# Обратите внимание, что количество файлов на C в директории include может варьироваться в зависимости от версии Python и операционной системы.
#

ima1 = Image("C:/Users/adm/Downloads/2025-02-11_08-30-38.png")
ima1

# +
ima3= Image("C:/Users/adm/Downloads/2025-02-11_08-47-52.png")

ima3
# -

ima4 = Image("C:/Users/adm/Downloads/2025-02-11_08-52-52.png")
ima4

ima5 = Image("C:/Users/adm/Downloads/2025-02-11_08-59-59.png")
ima5
