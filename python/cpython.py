"""Ответы на вопросы по CPython."""

# **1. Что такое CPython и чем он отличается от Python?**
#
# CPython - это самый распространенный интрепретатор Python. Отличие в том, что Python - это сам язык, а CPython - один из инструментов, который позволяет писать и выполнять программы на этом языке.

# **3. Сколько существует реализаций Python, и какая из них самая популярная?**
#
# Всего существует 6 реализаций, самая популярная - CPython. Также существуют PyPy, Jython, IronPython, MicroPython, Brython

# **4. На каком языке написан CPython?**
#
# На языке программирования C

# **5. (опционально) Кто создал CPython?**
#
# Гвидо ван Россум

# **6. Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?**
#
# Потому как ядро Python на C, довольно много библиотек так же написаны на Python и хорошо оптимизированы

# **7. Напишите путь к Интерпретатору CPython на вашем компьютере**
#
# "C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe"

# **8.Что содержится в папке include в CPython?**
#
# Здесь содержатся заголовочные файлы (с расширением .h), необходимые для разработки и сборки C-расширений для Python

# **9.Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб**
#
# https://github.com/python/cpython

# **10.Как работает интерпретатор CPython при выполнении кода?**
#
# Инициализируется интрепретатор -> Код конвертируется в байт-код -> Интрепретатор выполняет инструкции байт-кода

# **11. Какая команда используется для запуска файла с помощью CPython?**
#
# python

# **12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему?**
#
# Да. Интрепретатор работает непосредственно с содержимым файла, игнорируя расширение

# **13. Как указать путь к интерпретатору и файлу для выполнения кода?**
#
# В терминале ввести <путь до интерпретатора> <путь до файла>

# **14. Чем PyPy отличается от CPython?**
#
# PyPy - это высокопроизводительная альтернативная реализация Python, использующая JIT-компиляцию (Just-in-Time), что делает её в 4–10 раз быстрее стандартного CPython в вычислительных задачах

# **15. Почему PyPy не может использоваться для всех проектов на Python?**
#
# Он плохо работает с библиотеками, написанными на C (например, numpy), потребляет много памяти и не так эффективен на коротких скриптах

# **16. Где можно скачать PyPy?**
#
# https://pypy.org

# **17. Как установить PyPy после скачивания?**
#
# Встроенного установщика нет, поэтому нужно распаковать архив

# **18. Как запустить файл с помощью PyPy?**
#
# В терминале ввести <путь до интерпретатора PyPy> <путь до файла>

# **19. Почему PyPy выполняет код быстрее, чем CPython?**
#
# PyPy работает быстрее CPython благодаря использованию JIT-компиляции. В отличие от интерпретатора CPython, который выполняет байт-код построчно, PyPy анализирует код во время выполнения и компилирует часто используемые участки (циклы) в машинный код, значительно ускоряя вычисления.

# ### Практические задания

# **Задание 1: Поиск и установка CPython**
# Проверьте, установлен ли CPython на вашем компьютере:
#     Используйте поиск в меню "Пуск" (Windows) или терминале (Linux/Mac).
#     Введите команду python --version или python3 --version в терминале.
# Если CPython не установлен, скачайте его с официального сайта Python https://www.python.org/downloads/ и установите.

# In[2]:
import os

# get_ipython().system("python --version")
# вывоб: 3.12.6


# **Задание 2: Исследование структуры CPython**
# Найдите папку, где установлен Python (например, через команду where python в терминале или свойства ярлыка).
# Откройте папку include и изучите её содержимое. Какое количество файлов на C там есть?
# Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython) и найдите файл README. Прочитайте информацию о проекте.


def count_h_files(directory: str) -> None:
    """Подсчитывает число файлов с расширением .h в каталоге и выводит
    результат."""
    count = 0
    for _, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".h"):
                count += 1
    print("Количество файлов на C в папке include:", count)


count_h_files("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\include")


# вывод: 215


# **Задание 3: Запуск файла с помощью CPython**
# Создайте текстовый файл example.txt с содержимым:
# print("Hello from CPython!")
# Запустите файл через команду python <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.

# In[ ]:


# !python "C:\Users\user\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\example.txt"
# вывод: Hello from Cpython!

# !python "C:\Users\user\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\example.py"
# вывод: Hello from Cpython!


# **Задание 4: Установка и использование PyPy**
#
# Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте подходящую версию для вашей операционной системы.
# Распакуйте скачанный архив в удобное место.
# Создайте файл example_pypy.py с кодом:
# print("Hello from pypy!")
#
# Запустите файл через PyPy
# pypy <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.

# In[ ]:


# !"C:\Users\user\Downloads\pypy3.11-v7.3.21-win64\pypy3.11-v7.3.21-win64\pypy.exe"
# "C:\Users\MikkyToto\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\example_pypy.py"
# вывод: Hello from pypy!


# In[ ]:


# !"C:\Users\user\Downloads\pypy3.11-v7.3.21-win64\pypy3.11-v7.3.21-win64\pypy.exe"
# "C:\Users\MikkyToto\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\example_pypy.txt"
# вывод: Hello from pypy!


# **Задание 5: Сравнение производительности CPython и PyPy**
#
# Создайте файл performance_test.py с кодом.
# Запустите этот файл сначала через CPython, а затем через PyPy. Запишите результаты времени выполнения для обоих интерпретаторов.
# Сделайте вывод о разнице в производительности.

# In[ ]:


# !python "C:\Users\user\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\performance_test.py"
# вывод: Result: 49999995000000
#        Execution time: 1.1002681255340576 seconds


# In[ ]:


# !"C:\Users\user\Downloads\pypy3.11-v7.3.21-win64\pypy3.11-v7.3.21-win64\pypy.exe"
# "C:\Users\user\Documents\GitHub\Data-Science-For-Beginners-from-scratch-SENATOROV\python\performance_test.py"
# вывод: Result: 49999995000000
#        Execution time: 0.0178983211517334 seconds
