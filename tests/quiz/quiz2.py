"""Quiz 2: задания по Git, VS Code и Python."""

#
#
# 1. **Как включить автосохранение данных в VSCode?**
#    - Слева сверху → `AutoSave`
#
# 2. **Как настроить перенос строки?**
#    - `settings → wrap`
#
# 3. **Сколько символов по PEP8 разрешено на строке?**
#    - 79 символов
#
# 4. **Какие способы переноса строк показаны в видео?**
#    - Комментарий
#    - Перенос с помощью круглых скобок
#    - Создание двух переменных и их объединение
#    - Обратный слэш:
#      ```python
#      string_continued = "This is a long string that we want to " \
#                         "split across multiple lines."
#      print(string_continued)
#      ```
#    - Тройные кавычки:
#      ```python
#      multi_line_string = """This is a string that spans
#      multiple lines. You can write freely
#      and it will keep the line breaks."""
#      print(multi_line_string)
#      ```
#    - Список и `join`:
#      ```python
#      strings = [
#          "This is the first line.",
#          "This is the second line.",
#          "This is the third line."
#      ]
#      result = "\n".join(strings)
#      print(result)
#      ```
#    - Скобки:
#      ```python
#      long_string = (
#          "This is a very long string that I would like to "
#          "continue on the next line."
#      )
#      print(long_string)
#      ```
#    - f-строки:
#      ```python
#      letter_a = 5
#      letter_b = 6
#      product_ab = letter_a * letter_b
#      message = (
#          f"when {letter_a} is multiplied by {letter_b}, "
#          f"the result is {product_ab}"
#      )
#      print(message)
#      ```
#    - Сложение строк:
#      ```python
#      string_part1 = "This is the first part, "
#      string_part2 = "and this is the second part."
#      full_string = string_part1 + string_part2
#      print(full_string)
#      ```
#
# 5. **Где находится кнопка Problems?**
#    - Вкладка `PROBLEMS | OUTPUT | DEBUG CONSOLE | TERMINAL`
#
# 6. **Где клиент Git в VSCode? Как сделать коммит? Как принять ДЗ?**
#    - Слева иконка с 3 кружочками
#    - Ввести название коммита → нажать `Commit`
#    - Для принятия → `Pull`
#
# 7. **Что такое Git?**
#    - Система контроля версий
#    - Работает локально
#    - История коммитов доступна через `GitLens`
#
# 8. **Как вставить картинку в Markdown?**
#    ```html
#    <img src="somepage.kz" alt="Описание" width="300">
#
# **Где посмотреть длину строки в VSCode?**
# - Внизу в `Status Bar`
# - Или открыть `.py` файл и смотреть в нём
#
# ---
#
# **Как поменять тип ячейки на Markdown?**
# - `Cell → Cell Type → Markdown`
# - Горячая клавиша: `Esc + M`
#
# ---
#
# **Как запустить все ячейки в Jupyter?**
# - Кнопка `Run All` вверху
#
# ---
#
# **Как изменить размер картинки в Jupyter? Нужно ли знать HTML?**
# - Да, использовать базовые HTML-теги
#
# ---
#
# **Хоткей: запустить ячейку и перейти вниз**
# - `Shift + Enter`
#
# ---
#
# **Как включить номера строк в Jupyter?**
# - `View → Appearance → Show Line Numbers`
#
# ---
#
# **Что такое Go To и как перейти на ошибочную ячейку?**
# - Показывает ошибку и при нажатии переносит к ячейке
#
# ---
#
# **Как очистить вывод всех ячеек?**
# - `Clear All Outputs`
#
# ---
#
# **Что такое Split в VSCode?**
# - Разделение экрана для одновременной работы в нескольких файлах
#
# ---
#
# **Как убрать левый сайдбар в VSCode?**
# - `Ctrl + B`
#
# ---
#
# **Иконка с двумя листочками**
# - Это `Explorer` — локальные файлы
#
# ---
#
# **Какая ошибка может появиться при запуске всех ячеек (DICT или LIST)?**
# - `TypeError: 'dict' object is not callable`
# - `TypeError: 'list' object is not callable`
#
# ---
#
# **Ознакомились с материалами?**
# - **Yes**
#
# ---
#
# **Что такое валидация?**
# - Проверка качества и правильности данных или модели
#
# ---
#
# **Что такое трассировка ошибки?**
# - Сообщение об ошибке с указанием причины и места в коде
#
# ---
#
# **Что значит "отвалился интерпретатор"?**
# - Python перестал работать во время выполнения программы
#

#
