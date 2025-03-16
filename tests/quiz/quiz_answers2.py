# quiz2

# В VS Code можно включить автосохранение (Auto Save) следующим образом
# Способ 1 Через настройки UI
#
#     Открыть Файл → Настройки → Параметры (или нажать Ctrl + ,).
#     В поле поиска ввести Auto Save.
#     В разделе Files Auto Save выбрать один из вариантов
#         afterDelay – сохраняет файл автоматически через небольшой промежуток
# времени.
#         onFocusChange – сохраняет при переключении на другое окно.
#         onWindowChange – сохраняет при переключении на другое окно программы.
#         off – отключает автосохранение.
#
# Способ 2 Через settings.json
#
#     Открыть Файл → Настройки → Параметры → Открыть настройки (JSON).
#     Добавить строку
#
# files.autoSave afterDelay
#
# Можно заменить afterDelay на onFocusChange, onWindowChange или off,
# в зависимости от предпочтений.

# 2. Как настроить перенос строки
# В VS Code можно настроить автоматический перенос строк (Word Wrap)
# несколькими способами
# Способ 1 Через интерфейс настроек
#
#     Открыть Файл → Настройки → Параметры (Ctrl + ,).
#     В строке поиска ввести Word Wrap.
#     Найти параметр Editor Word Wrap и выбрать один из вариантов
#         off – отключено (строки не переносятся).
#         on – строки автоматически переносятся.
#         wordWrapColumn – перенос на заданной ширине.
#         bounded – перенос в пределах editor.wordWrapColumn.
#
# Способ 2 Через командную строку
#
#     Открыть командную строку (Ctrl + Shift + P).
#     Ввести Toggle Word Wrap и выбрать Editor Toggle Word Wrap (Alt + Z).
#
# Способ 3 Через settings.json
#
#     Открыть Файл → Настройки → Параметры → Открыть настройки (JSON).
#     Добавить параметр
#
# editor.wordWrap on
#
# Можно заменить on на off, wordWrapColumn или bounded в зависимости
# от предпочтений.

# 3. Сколько символов по pep8 разрешено на строке
#
# Согласно PEP 8, максимальная длина строки кода должна быть 79 символов.

# 4. Какие способы переноса строк показаны в видео
#
# 1 Коментарий с помощью решетки
# 2 Оборачиваем код в круглые скобки переносим код
# 3 Разбиваем строку на 2 переменых и в 3 переменной соеденяем
# методом конконтинации

# 4.1 Строки с использованием обратного слэша ()
#
# string_continued = This is a long string that we want to
#                    split across multiple lines.
# print(string_continued)

#
# 4.2 Тройные кавычки (''' или )
#
# multi_line_string = This is a string that spans
# multiple lines. You can write freely
# and it will keep the line breaks.
# print(multi_line_string)

# 4.3 Создание списка строк и объединение с помощью join
#
# strings = [
#     This is the first line.,
#     This is the second line.,
#     This is the third line.
# ]
# result = n.join(strings)  # Используем перенос строк 'n'
# print(result)

# 4.4 Использование круглых скобок для продолжения строки
# long_string = (
#     This is a very long string that I would like to
#     continue on the next line.
# )
# print(long_string)

# 4.5 Форматированные строки (f-строки) с использованием скобок
# letter_a = 5
# letter_b = 6
# product_ab = letter_a  letter_b
#
# message = (
#     fwhen {letter_a} is multiplied by {letter_b},
#     fthe result is {product_ab}
# )
# print(message)

# 4.6 Сложение строк с помощью +
#
# string_part1 = This is the first part,
# string_part2 = and this is the second part.
# full_string = string_part1 + string_part2
# print(full_string)

# В VS Code панель Problems (Проблемы) находится внизу, в панели вывода.
# Как открыть панель Problems в VS Code
#
#     Через кнопку внизу
#         В нижней части редактора найдите вкладку Problems
# (значок 🚨 ошибкипредупреждения).
#         Если её нет, нажмите на значок Панель
# (или View Toggle Panel в командной строке).
#
#     Горячие клавиши
#         Ctrl + Shift + M (WindowsLinux).
#         Cmd + Shift + M (Mac).
#
#     Через меню
#         Открыть View (Вид) → Problems (Проблемы).
#
#     Через командную строку
#         Нажать Ctrl + Shift + P → ввести View Toggle Problems → нажать Enter.
#
# В панели Problems отображаются ошибки, предупреждения и рекомендации по коду.

# 6. Где в vscode находится клиент гита
#
# Как открыть клиент Git в VS Code
#
#     Боковая панель
#         Нажмите Ctrl + Shift + G (WindowsLinux) или Cmd + Shift + G (Mac).
#         Либо кликните на иконку Source Control
# (Источник) в левом боковом меню.
#
#     Терминал
#         Откройте терминал (Ctrl + `) и введите команды Git, например
#
#     git status
#     git add .
#     git commit -m Сообщение
#     git push
#
#     Командная палитра
#
#     Нажмите Ctrl + Shift + P → Введите Git
#     Здесь доступны все команды Git (например, Git Clone, Git Commit и т. д.).
#
#
#
#
#     Как сделать коммит в VS Code
#
#     Открыть панель Git
#         Нажмите Ctrl + Shift + G или кликните на вкладку
# Source Control в боковой панели.
#
#     Добавить файлы в коммит
#         Все изменённые файлы появятся в разделе Changes.
#         Нажмите + (Stage changes) рядом с файлом или используйте
# Stage All Changes (Иконка ✓ вверху).
#
#     Написать сообщение коммита
#         Внизу панели Source Control есть поле ввода.
#         Введите описание коммита (например, Исправил баг в коде).
#
#     Создать коммит
#         Нажмите на ✓ (Commit) или используйте сочетание Ctrl + Enter.
#
#     Отправить коммит на сервер (push)
#         Нажмите кнопку ↥ (Publish или Push), либо выполните
# в терминале git push
#
#
# Как принять домашку в Git
#
# Открыть терминал в VS Code (Ctrl + `)
#
#
# Перейти в нужную ветку (если нужно) git checkout main  # или другая ветка
#
# Получить последние изменения git pull
#
# Посмотреть, что изменилось
#
#     Открыть вкладку Source Control → посмотреть изменения.
#     Либо использовать команду git diff
#

# Что такое GIT
#
# GIT — это распределённая система контроля версий (VCS).
# Она используется для отслеживания изменений в коде,
# работы с разными версиями проекта и совместной разработки.
# Основные возможности GIT
#
#  Сохранение версий кода (можно вернуться к любому коммиту)
#  Работа в команде (несколько разработчиков могут работать над одним проектом)
#  Ветвление (branches) (можно создавать экспериментальные версии кода)
#  Слияние (merge) (объединение изменений из разных веток)
#  Удалённые репозитории (GitHub, GitLab, Bitbucket)
#
#
#  Git — локальный или нет
#
# Git — локальная система контроля версий, но при этом может работать
# с удалёнными репозиториями (например, GitHub, GitLab).
#
#     Локальный репозиторий (на твоём компьютере)
#     Удалённый репозиторий (на сервере, например, на GitHub)
#
# Ты можешь работать офлайн и коммитить изменения, а потом синхронизировать их
# с удалённым репозиторием командой git push
#
#
# Можно ли посмотреть историю изменений файлов
#
# Да! В Git можно увидеть все изменения и даже восстановить
# старую версию файла.
# Как посмотреть историю коммитов
#
# git log
#
# Это покажет список всех коммитов с их хэшами, авторами и датами.
#
# Сокращённый лог git log --oneline
#
# История изменений конкретного файла git log -- filename.txt
#
# Посмотреть, что изменилось в коммите  git show commit_id
# (где commit_id — хеш коммита, который можно взять из git log)
#
#
#
# Можно ли вернуться к любому коммиту
#
# Да! Git позволяет переключаться между версиями проекта.
# Как вернуть проект к старой версии
#
#     Переключиться на конкретный коммит (временное изменение)
#
# git checkout commit_id - В этом режиме ты не можешь коммитить, потому
# что окажешься в detached HEAD (отключённая голова).
#
# Вернуть файлы к состоянию конкретного коммита
# git reset --hard commit_id
#
# Создать новую ветку с этого коммита (чтобы не потерять данные)
# git checkout -b new_branch commit_id
#
#
#

# 8. Как вставить картинку в маркдаун
#
# В Markdown картинку можно вставить с помощью следующего синтаксиса
#
# ![Альтернативный текст](ссылка_на_изображение)
#
#
# Картинка из интернета ![Логотип GitHub]
# (httpsgithub.githubassets.comimagesmoduleslogos_pageGitHub-Mark.png)
#
#
# Ссылка-картинка [![Описание](image.png)](httpsexample.com)
#

# 9. Где посмотреть длину строки в vs code
#
# В VS Code можно посмотреть длину строки несколькими способами
#
# 1. В строке состояния (внизу редактора)
#
#     Внизу окна VS Code есть статусная строка.
#     Справа показывается позиция курсора в формате
#
#     Ln 10, Col 25
#
# Если статусной строки нет
# Переключи её View → Appearance → Status Bar.
#
# 2. Через панель Selection (Выбор)
#
# Выдели строку → Внизу справа покажется Selected 42 characters
# (42 символа в строке).

# 10. Как поменять тип ячейки с питона на маркдаун
#
# Способы смены типа ячейки
# 1. Через меню
#
#     Выдели ячейку.
#     В верхнем меню нажми Cell → Cell Type → Markdown.
#
# 2. Быстрая команда в Jupyter Notebook
#
#     Выдели ячейку и нажми Esc, чтобы выйти из режима редактирования.
#
#     Нажми M (Markdown) или Y (Python).
#
# 3. В VS Code (если работаешь в .ipynb)
#
#     В панели инструментов над ячейкой выбери Markdown вместо Code.
#     Или нажми Ctrl + Shift + P, введи Change Cell to Markdown и
# выбери нужный вариант.

# 11. Как запустить сразу все ячейки в юпитере
#
# В VS Code (Jupyter Notebook, .ipynb) можно запустить сразу все ячейки
# несколькими способами
# 1. Через кнопку в интерфейсе
#
#     Вверху файла .ipynb есть панель с кнопками.
#     Нажми ▶ Run All (Запустить все ячейки).
#
# 2. Через командную палитру
#
#     Нажми Ctrl + Shift + P.
#     Введи Jupyter Run All Cells.
#     Выбери этот вариант и нажми Enter.
#
# 3. Горячие клавиши
#
#     Shift + Enter — запустить текущую ячейку и перейти к следующей.
#     Ctrl + Enter — запустить текущую ячейку, но не переходить.
#     Shift + Ctrl + Enter — запустить все ячейки выше текущей.
#     Shift + Alt + Enter — запустить все ячейки ниже текущей.
#
# 4. Через меню
#
#     Открыть Run → Выбрать Run All Cells.
#
#

# 12 Как изменить размер картинки в юпитере Нужно для этого знать HTML
#
# 1. С помощью Markdown (без HTML)
#
# Если вставляешь изображение в Markdown, можно изменить размер через HTML
#
# img src=image.png width=300
#
#     width=300 — задаёт ширину в пикселях.
#     Можно использовать height=200 для высоты.
#
#
# 2. Использование IPython display
#
# Если загружаешь картинку через IPython.display, можно задать размер так
#
#  from IPython.display import Image
#
# Image(image.png, width=300, height=200)
#
#

# 13. Какой хоткей чтобы запустить ячейку с смещением на следующую
#
# В Jupyter Notebook (VS Code), чтобы запустить ячейку и создать новую ниже,
# используй Горячая клавиша
#
# Shift + Alt + Enter
#
# Что делает этот хоткей
# Запускает текущую ячейку
#
# Создаёт новую ячейку сразу под текущей
#
# Перемещает курсор в новую ячейку
#
# Если нужно просто запустить и перейти дальше (без создания
#
# новой) Shift + Enter

# 14. Как включить отображение номеров строк в юпитере(Cell line numbers)
# 1. Через меню (графический интерфейс)
#
#     Кликни на любую ячейку.
#     В верхнем меню выбери View → Toggle Line Numbers.
#     Номера строк появятся во всех ячейках.
#
# 2. Горячая клавиша (Jupyter Notebook)
#
#     Выбери ячейку.
#     Нажми Shift + L.
#     Включится или отключится нумерация строк.
#
# 3. Через настройки в VS Code
#
#     Открой командную палитру Ctrl + Shift + P.
#     Введи Jupyter Toggle Line Numbers.
#     Выбери и нажми Enter.

# 15. Что такое Go To чем это полезно Как перейти сразу на ошибочную ячейку
#
# Когда в Jupyter появляется ошибка, можно быстро найти ячейку с проблемой.
# 1. Через Go to Line (горячая клавиша)
#
#     Нажми Ctrl + G
#     Введи номер строки с ошибкой (из traceback)
#     Нажми Enter
#
# 2. Через Go to Next Problem (следующая ошибка)
#
#     Нажми F8 — переходит к следующей ошибке
#     Shift + F8 — переходит к предыдущей ошибке
#
# 3. Через журнал вывода ошибок (Problems panel)
#
#     Нажми Ctrl + Shift + M
#     Откроется вкладка Problems, где видны все ошибки
#     Кликни на ошибку, чтобы перейти к ячейке

# 16. Как очистить вывод ячеек которые уже запущены
#
# 1. Через меню
#
#     В верхнем меню выбери Cell → All Output → Clear.
#     Это очистит вывод для всех ячеек.
#
#     Для очистки вывода только одной ячейки выбери Clear Output
# для конкретной ячейки (клик правой кнопкой мыши по ячейке).
#
# 2. Горячие клавиши
#
#     Нажми Esc, чтобы выйти из режима редактирования.
#     Выбери ячейку с выводом, который нужно очистить.
#     Нажми O — это отключит вывод для ячейки.
#     (Нажми ещё раз, чтобы вернуть вывод).
#
# Через командную палитру
#
#     Нажми Ctrl + Shift + P.
#     Введи Clear Output.
#     Выбери нужный вариант Clear All Outputs или Clear Output
# для выбранной ячейки.

# 17. Как работать одновременно в нескольких файлах в VSCODE Что такое SPLIT
# В VS Code можно работать одновременно с несколькими файлами, используя
# возможности разделения окон и вкладок. Один из таких способов — это SPLIT.
# 1. Работа с несколькими файлами
#
# Чтобы работать с несколькими файлами одновременно, можно
#
#     Открыть несколько вкладок (каждый файл будет в своей вкладке).
#     Переключаться между вкладками с помощью Ctrl + Tab.
#
#
# 2. Использование SPLIT
#
# SPLIT — это функция разделения редактора на несколько панелей,
# чтобы открыть несколько файлов рядом.
# Как использовать Split (разделить экран)
#
#     Горячие клавиши
#         Ctrl +  — разделяет редактор на две части
# (горизонтально или вертикально).
#         Ctrl + 1, Ctrl + 2, и т.д. — переключение
# между разделёнными панелями.
#
#     Через контекстное меню
#         Открой файл, который хочешь разделить.
#         Правой кнопкой мыши по вкладке файла → Split Editor.
#         Откроется второй экземпляр редактора,
# в котором можно открыть другой файл.
#
#     Перетаскивание вкладок
#         Просто перетащи вкладку с файлом в одну из сторон экрана, и VS
# Code автоматически разделит окно.
#
# 3. Разделение на несколько частей
#
# В зависимости от конфигурации, можно разделить окно на две или более частей
#
#     Горизонтальное разделение два окна сверху и снизу.
#     Вертикальное разделение два окна слева и справа.
#
# В каждой части ты можешь работать с отдельным файлом, и даже редактировать
# один и тот же файл в разных частях экрана.
# Как использовать это эффективно
#
#     Это удобно, когда нужно работать с несколькими файлами одновременно,
# например
#         Просматривать документацию или примеры кода.
#         Сравнивать разные части проекта.
#         Работать с несколькими конфигурационными файлами.
#
# 4. Работа с несколькими терминалами
#
# Также в VS Code можно открыть несколько терминалов с помощью
#
#     Ctrl + Shift + ' — откроет новый терминал.
#     Переключаться между терминалами можно с помощью кнопок в панели или
# через Ctrl + ~ (открывает терминал).
#

# 18. Каким сочетанием убирается левый сайдбар
#
# Чтобы скрыть или показать левый сайдбар в VS Code, используй следующее
# сочетание клавиш
# Сочетание клавиш
#
#     Ctrl + B — скрывает или показывает боковую панель (сайдбар).
#
# Это поможет быстро освободить место на экране, если тебе нужно больше
# пространства для работы с кодом. 🚀

# 19. Кнопка два листочка это наши локальные файлы
#
# Да, кнопка с двумя листочками в VS Code обычно относится к панели Explorer,
# которая отображает локальные файлы и папки твоего проекта.

# 20. Какая ошибка появилась в трассировке при запуске всех ячеек DICT или LIST
#
# 1. TypeError 'dict' object is not callable
#
#     Описание ошибки Эта ошибка может появиться, если ты пытаешься вызвать
# объект типа dict как функцию, например
#
#  my_dict = {'a' 1, 'b' 2}
# result = my_dict()  # Ошибка, так как dict не может быть вызван
#
# 2. TypeError 'list' object is not callable
#
# Описание ошибки Эта ошибка возникает, если ты пытаешься вызвать объект
# типа list как функцию
#
# my_list = [1, 2, 3]
# result = my_list()  # Ошибка, так как list не может быть вызван
#
# Решение Убедись, что не используешь имя list как переменную и не пытаешься
# вызывать его как функцию.
#
# 3. IndexError list index out of range
#
#     Описание ошибки Возникает, если ты пытаешься обратиться к элементу
# списка по индексу, который выходит за пределы списка
#
# my_list = [1, 2, 3]
# print(my_list[5])  # Ошибка индекс выходит за пределы
#
#
# 4. KeyError 'key'
#
#     Описание ошибки Ошибка возникает, если ты пытаешься получить значение из
# словаря по ключу, которого нет в словаре
#
# my_dict = {'a' 1, 'b' 2}
# print(my_dict['c'])  # Ошибка, так как ключ 'c' не существует
#
# Решение Используй метод .get() для безопасного доступа к ключам словаря,
# например value = my_dict.get('c', 'default_value')
#
#

# 22. Что такое валидация
#
# Валидация — это процесс проверки данных на соответствие определённым
# правилам или стандартам. В контексте программирования валидация
# применяется для того, чтобы убедиться, что введённые или полученные
# данные правильные и соответствуют ожиданиям.
# Типы валидации
#
#     Валидация данных пользователя
#         Проверка, что введённые пользователем данные имеют правильный формат.
# Например
#             Проверка, что email содержит символ @.
#             Проверка, что пароль достаточно сложный.
#             Проверка, что возраст не меньше 18 лет.
#
#     Валидация данных в API
#         Проверка, что данные, отправленные на сервер, соответствуют
# требуемому формату. Например
#             Проверка, что JSON содержит все обязательные поля.
#             Проверка правильности типов данных
# (например, строка вместо числа).
#
#     Валидация данных в базе данных
#         Проверка, что данные, сохраняемые в базу данных, не нарушают
# ограничения (например, уникальность значения, ограничения по длине и типу).
#
# Зачем нужна валидация
#
#     Предотвращение ошибок Валидация помогает предотвратить ошибки,
# которые могут возникнуть из-за некорректных данных.
#     Безопасность Защищает от атак, таких как SQL-инъекции или XSS
# (кросс-сайтовый скриптинг).
#     Пользовательский опыт Позволяет пользователю быстро понять, если что-то
# введено неправильно, и помогает избежать дальнейших ошибок при обработке.

# 23. Что такое трассировка ошибки
#
# Трассировка ошибки (или traceback) — это подробная информация, которая
# выводится при возникновении ошибки в программе. Она показывает
# последовательность вызовов функций и местоположения в коде, где
# произошла ошибка. Трассировка позволяет разработчикам понять,
# как программа дошла до места ошибки, что помогает быстро
# обнаружить и устранить проблему.
# Как выглядит трассировка ошибки
#
# Трассировка обычно содержит следующие элементы
#
#     Тип ошибки — Например, ValueError, TypeError, IndexError.
#     Сообщение об ошибке — Описание самой ошибки, например,
# list index out of range или division by zero.
#     Местоположение ошибки — Указывает, в каком файле и
# на какой строке возникла ошибка.
#     Стек вызовов — Список функций, которые были вызваны до того,
# как произошла ошибка. Каждая строка в трассировке соответствует
# вызову функции.
#
#     Пример трассировки ошибки в Python
#
#     Traceback (most recent call last)
#   File example.py, line 5, in module
#     result = my_list[10]  # Ошибка индекс выходит за пределы
# IndexError list index out of range
#
# Traceback (most recent call last) Начало трассировки, показывающее,
# что ошибка произошла в последнем вызове.
#
# File example.py, line 5 Ошибка произошла в файле example.py, на строке 5.
# my_list[10] Это место в коде, где произошла ошибка.
#
# IndexError list index out of range Тип ошибки — это IndexError, и сообщение —
# индекс выходит за пределы.
#

# 24. Что значит отвалился интерпритатор
#
# огда говорят, что отвалился интерпретатор, это обычно означает, что
# интерпретатор Python (или другой язык программирования) внезапно прекратил
# свою работу или не может выполнить задачу.
#
# Это может произойти по нескольким причинам
# 1. Ошибка в коде, которая вызывает сбой интерпретатора
#
#     Например, бесконечный цикл, который использует все ресурсы процессора,
# или неправильное использование памяти (например,
# создание слишком больших объектов).
#     Пример
#
#     while True
#         pass  # Это может привести к отвалу интерпретатора
#
# 2. Недостаток ресурсов
#
#     Если программа требует слишком много памяти или процессорных ресурсов,
# интерпретатор может выйти из строя.
#     Пример Попытка загрузить в память очень большой файл или создание
# бесконечных рекурсий.
#
# 3. Ошибка в сторонних библиотеках
#
#     Иногда сторонние библиотеки или зависимости, с которыми работает твой
# код, могут привести к сбою интерпретатора.
#     Пример Использование неустойчивых или плохо написанных
# сторонних пакетов, которые не корректно обрабатывают ошибки.
#
# 4. Прерывание процесса
#
#     Интерпретатор может завершить работу, если его принудительно завершить
# (например, с помощью команды Ctrl + C или через задачу
# в операционной системе).
#
# 5. Проблемы с самим интерпретатором
#
#     Бывают случаи, когда сам интерпретатор или его установка повреждены
# (например, из-за ошибок в системе или при установке Python).
#
# 6. Ошибки в настройках среды
#
#     Если настройка среды (например, IDE, виртуального окружения) или
# несовместимость версий пакетов приводит к сбою.
#
# Что делать, если интерпретатор отвалился
#
#     Перезапуск интерпретатора Закрой текущую сессию и перезапусти
# интерпретатор.
#     Проверка ошибок в коде Изучите код на наличие циклов, рекурсий или
# больших данных, которые могут привести к сбою.
#     Посмотреть логи Внимательно посмотри на трассировку ошибки
# (если она есть), чтобы найти источник проблемы.
#     Использование отладчика Попробуй использовать отладчик, чтобы шаг за
# шагом пройти по коду и выявить место, где возникает ошибка.
