"""Quiz 2."""

# Выполнение заданий по Питону
#
# Список вопросов к видео https://youtu.be/Si9MfV8uJ-0?si=JXHe-tsgOEwSTI5E (НАСТРОЙКА VSCODE, перенос строк, линтеры, работа с ячейками):
#
#
# (По желанию)В ответе подробно всё опишите и обязательно нужно указывать тайм код из видео где я это сказал, по желанию, дополнительно прикладываем скриншот из видео.
#
# Если вы знаете ответы на вопросы из Вашего опыта, то таймкоды из видео не надо указывать и т.д.
#
#
# 1. Как включить автосохранение данных в VSCODE?
#
#
# File - Auto Save
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&t=14
#
#
# 2. Как настроить перенос строки?
#
#
# Preferences-Settings, в поисковую строку пишем wrap, в поле Editor в контекстном меню выбираем WordWrapColumn, длина строки 79, нажимаем Enter.
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&t=34
#
#
# 3. Сколько символов по pep8 разрешено на строке?
#
#
# 79
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=1m28s
#
#
# 4. Какие способы переноса строк показаны в видео:
#
#
# Вариант 1.
#
# перенос комментариев - с помощью #
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ?=1m55s
#
# перенос кода - взять в скобки ( )
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=2m36s
#
# Вариант 2.
#
# длинную переменную разбить на две переменные, затем “склеить" их, например,  name_sum=name_1+name_2
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=4m
#
#
# 4.1 Строки с использованием обратного слэша (\)
#
#
# string_continued = "This is a long string that we want to " \
#
#                    "split across multiple lines."
#
# print(string_continued)
#
#
#
# 4.2 Тройные кавычки (''' или """)
#
#
# multi_line_string = """This is a string that spans
#
# multiple lines. You can write freely
#
# and it will keep the line breaks."""
#
# print(multi_line_string)
#
#
# 4.3 Создание списка строк и объединение с помощью join
#
#
# strings = [
#
#     "This is the first line.",
#
#     "This is the second line.",
#
#     "This is the third line."
#
# ]
#
# result = "\n".join(strings)  # Используем перенос строк '\n'
#
# print(result)
#
#
# 4.4 Использование круглых скобок для продолжения строки
#
# long_string = (
#
#     "This is a very long string that I would like to "
#
#     "continue on the next line."
#
# )
#
# print(long_string)
#
#
# 4.5 Форматированные строки (f-строки) с использованием скобок
#
# letter_a = 5
#
# letter_b = 6
#
# product_ab = letter_a * letter_b
#
#
# message = (
#
#     f"when {letter_a} is multiplied by {letter_b}, "
#
#     f"the result is {product_ab}"
#
# )
#
# print(message)
#
#
# 4.6 Сложение строк с помощью +
#
#
# string_part1 = "This is the first part, "
#
# string_part2 = "and this is the second part."
#
# full_string = string_part1 + string_part2
#
# print(full_string)
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=3m55s
#
#
# 5. Проверка на ошибки c помощью кнопки problems, где она находится?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=4m49s
#
# Находится внизу окна редактора, слева.
#
#
# 6. Где в vscode находится клиент гита? как в нём отправить коммит? как принять домашку?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=6m24s
#
# Клиент находится в левой части окна(три кружочка)
#
# Чтобы отправить коммит, пишем коммит, затем нажимаем Commit
#
# Домашка принимается с помощью кнопки Pull.
#
#
# 7. Что такое GIT? он локальный? В нём можно посмотреть историю изменений файлов и вернуться к любому коммиту?
#
#
# Git - это контроль версий. да, можно посмотреть
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=7m12s
#
#
# 8. Как вставить картинку в маркдаун?
#
#
# С помощью сочетания клавиш Ctrl+V
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=8m03s
#
#
# 9. Где посмотреть длину строки в vs code?
#
# Скопировать строку в файл с расширением .py,  внизу справа показывается количество символов.
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=1m25s
#
#
#
# 10. Как поменять тип ячейки с питона на маркдаун?
#
# По умолчанию создается тип ячейки Code. Нажать на тип Python и выбрать в ниспадающем меню Markdown.
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=8m08s
#
#
# 11. Как запустить сразу все ячейки в юпитере?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=8m36s
#
#
# Нажать Run All - запуск всех ячеек одновременно.
#
#
# 12. Как изменить размер картинки в юпитере? Нужно для этого знать HTML?
#
# img are,  ссылка на картинку и её размер
#
# Да, нужно знать.
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=8m21s
#
#
# 13. Какой хоткей чтобы запустить ячейку с смещением на следующую?
#
#
# Shift+Enter
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=8m49s
#
#
# 14. Как включить отображение номеров строк в юпитере(Cell line numbers)?
#
# Нажимаем на три точки в правом нижнем углу окна редактора и выбираем Show Cell line Number.
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=9m17s
#
#
# 15. Что такое "Go To" чем это полезно? Как перейти сразу на ошибочную ячейку?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=9m41s
#
# Показывает, в какой ячейке ошибка. Схватываем проблемную ячейку и тащим вниз, нажимаем “Go To”
#
#
# 16. Как очистить вывод ячеек которые уже запущены?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=10m51s
#
# Нужно нажать Clear All Outputs.
#
#
# 17. Как работать одновременно в нескольких файлах в VSCODE? Что такое SPLIT?
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=11m03s
#
# Split Editor позволяет работать одновременно в нескольких файлах.
#
#
# 18. Каким сочетанием убирается левый сайдбар?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=11m23s
#
# Ctrl+B, либо просто нажимаем на активное окно.
#
#
# 19. Кнопка два листочка это наши локальные файлы?
#
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=11m36s
#
# Да
#
#
# 20. Какая ошибка появилась в трассировке при запуске всех ячеек DICT или LIST?
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=9m23s
#
#
# 21. Вы ознакомились с https://t.me/c/1937296927/832/19307? и  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet?
#
#
# Ознакомилась
#
#
# 22. Что такое валидация?
#
#
# Это проверка соответствия программного кода определённым правилам.
#
#
# 23. Что такое трассировка ошибки?
#
#
# Трассировка - это визуализация ошибки
#
# https://youtu.be/Si9MfV8uJ-0?si=U4yGy8-OCkDu1cRZ&=10m05s
#
#
# 24. Что значит отвалился интерпретатор?
#
# Это означает,  что интерпритатор перестал работать или быть доступным, из-за чего программный код, который от него зависел, не может запуститься, выполнить команды или выдать ошибку.
#
#
