"""Quiz 4."""

# 1. Что такое CPython и чем он отличается от Python?
# Python - это язык программирования, а CPython - это и язык программирования, и интерпретатор одновременно.
# 3. Сколько существует реализаций Python, и какая из них самая популярная?
# Существует 6 реализаций Python, самая популярная из них-CPython
# 4. На каком языке написан CPython?
# CPython написан на языке С.
# 5. (опционально) Кто создал CPython?
# CPython создал голландский программист Гвидо ван Россум.
#
# 6. Почему Python считается быстрым, несмотря на то, что это интерпретируемый язык?
# Потому что ядро CPython написано на языке С, и он вызывает инструкции из С.
#
# 7. Напишите путь к Интерпретатору CPython на вашем компьютере
# C:\Users\user\anaconda3\python.exe
#
# 8. Что содержится в папке include в CPython?
# В папке include в CPython находятся заголовочные файлы на языке С.
#
# 9. Где можно найти исходный код CPython дайте ссылку на репозиторий гитхаб.
# Ссылка на репозиторий гитхаб: https://github.com/python/cpython
#
# 10. (опционально) Как работает интерпретатор CPython при выполнении кода?
# Интерпретатор CPython выполняет код пошагово, преобразуя его в машинные инструкции для компьютера.
#
# 11. Какая команда используется для запуска файла с помощью CPython?
# python filename
#
# 12. Можно ли запускать текстовые файлы через интерпретатор Python? Почему?
# Можно, так как интерпретатору неважно, какие файлы запускать, главное – валидный пайтон-код.
#
# 13. Как указать путь к интерпретатору и файлу для выполнения кода?
# Через абсолютный или относительный путь.
#
# 14. Чем PyPy отличается от CPython?
# Этот интерпретатор работает в 10 раз быстрее, чем CPython.
#
# 15. Почему PyPy не может использоваться для всех проектов на Python?
# Это достаточно новый интерпретатор, и он ещё не совместим со всеми проектами на Python.
#
# 16. Где можно скачать PyPy?
# По ссылке: https://pypy.org/download.html
#
# 17. Как установить PyPy после скачивания?
# Извлечь папку и прописать пути в переменных средах.
#
# 18. Как запустить файл с помощью PyPy?
# В командной строке Windows ввести абсолютный путь до интерпретатора, пробел, абсолютный путь до файла, нажать Enter.
#
# 19. Почему PyPy выполняет код быстрее, чем CPython?
# PyPy использует Just-In-Time компилятор для компиляции Python в машинный код во время выполнения, что ускоряет работу.
#
# Практические задания
# Задание 1: Поиск и установка CPython
# Проверьте, установлен ли CPython на вашем компьютере:
#     Используйте поиск в меню "Пуск" (Windows) или терминале (Linux/Mac).
#     Введите команду python --version или python3 --version в терминале.
# Если CPython не установлен, скачайте его с официального сайта Python https://www.python.org/downloads/ и установите.
#
# C:\Users\user>python --version
# Python 3.13.9
#
#
# Задание 2: Исследование структуры CPython
# Найдите папку, где установлен Python (например, через команду where python в терминале или свойства ярлыка).
# Откройте папку include и изучите её содержимое. Какое количество файлов на C там есть?
# Перейдите на [GitHub-репозиторий CPython](https://github.com/python/cpython) и найдите файл README. Прочитайте информацию о проекте.
#
# В папке include количество файлов на C: 77.
#
# C:\Users\user>where python
# C:\Users\user\anaconda3\python.exe
# C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
# C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe
# C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#
# C:\Users\user>
#
# Задание 3: Запуск файла с помощью CPython
# Создайте текстовый файл example.txt с содержимым:
# print("Hello from CPython!")
# Запустите файл через команду python <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
# C:\Users\user>C:\Users\user\anaconda3\Scripts\ipython3.exe C:\Users\user\Desktop\Test1\example.txt
# Hello from CPython!
#
# C:\Users\user>C:\Users\user\anaconda3\Scripts\ipython3.exe
# C:\Users\user\Desktop\Test1\example.py
# Hello from CPython!
#
#
# Задание 4: Установка и использование PyPy
# Перейдите на [официальный сайт PyPy](https://www.pypy.org/) и скачайте подходящую версию для вашей операционной системы.
# Распакуйте скачанный архив в удобное место.
# Создайте файл example_pypy.py с кодом:
# print("Hello from pypy!")
# Запустите файл через PyPy
# pypy <путь_до_файла> (замените <путь_до_файла> на фактический путь к вашему файлу).
# Проверьте, что выводится на экран. Попробуйте изменить расширение файла на .py и повторите запуск.
# Вывод:
# C:\Users\user>C:\Users\user\Downloads\pypy3.11-v7.3.20-win64\pypy.exe C:\Users\user\Desktop\Test1\example_pypy.py
# Hello from PyPy
# C:\Users\user>
# Задание 5: Сравнение производительности CPython и PyPy
# Создайте файл performance_test.py с кодом:
#     import time
#     start_time = time.time()
#     total = 0
#     for i in range(1, 10000000):
#         total += i
#     end_time = time.time()
#
#     print("Result:", total)
#     print("Execution time:", end_time - start_time, "seconds")
# Запустите этот файл сначала через CPython, а затем через PyPy. Запишите результаты времени выполнения для обоих интерпретаторов.
# Сделайте вывод о разнице в производительности.
#
# Результат запуска через PyPy:
# C:\Users\user>C:\Users\user\Downloads\pypy3.11-v7.3.20-win64\pypy.exe C:\Users\user\Desktop\Test1\performance_test.py
# Result: 49999995000000
# Execution time: 0.015625715255737305 seconds
#
# Результат запуска через iPython:
# C:\Users\user>C:\Users\user\anaconda3\Scripts\ipython.exe C:\Users\user\Desktop\Test1\ performance_test.py
# Result: 49999995000000
# Execution time: 2.2144627571105957 seconds
# Вывод:  Время выполнения через интерпретатор iPython в 142 раза больше.
#
