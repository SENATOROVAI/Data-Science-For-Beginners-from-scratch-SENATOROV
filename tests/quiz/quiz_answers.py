"""This module contains the answers to the quiz tests."""

# 1) Как понять, что домашка пришла?
#
# 1.1 Проверить изменения на удалённом репозитории: git fetch
# Эта команда скачает обновления с удалённого репозитория, но не объединит их с твоими локальными изменениями.
#
# 1.2 Проверить статус ветки: git status
#
#

# 2) Как принять домашку? github 
#
# 2.1 Переключись на основную ветку (обычно main или master): git checkout Oleg14038
#
# 2.2  Обнови свою локальную копию: git pull origin Oleg14038
#
# 2.3 Убедись, что изменения появились (git log или git status)
#

# 3) Зачем нужна кнопка history и какие функции появляются при нажатии правой кнопки мыши на коммит?
#
# 3.1.1 Зачем нужна кнопка history и какие функции появляются при нажатии правой кнопки мыши на коммит?
#
# Кнопка "History" (История) в интерфейсе GitHub показывает историю коммитов в репозитории. Она позволяет:
#
#     Отслеживать изменения в коде.
#     Смотреть, кто и когда внёс изменения.
#     Видеть описание коммитов и изменения в файлах.
#     Переключаться на конкретные коммиты.
#
# 3.2.2 В GitHub Desktop доступны такие опции:
#     Amend Commit - используется для изменения последнего коммита, если ты: 
#
#     ЗАБЫЛ добавить файлы перед коммитом.
#     ХОЧЕШЬ исправить сообщение коммита.
#     ХОЧЕШЬ внести небольшие изменения, не создавая новый коммит.
#     
#     RESET TO COMMIT - используется для отката истории репозитория до указанного коммита
#
#     Основные случаи, когда используется reset to commit:
#
#     Откат последних коммитов (если ты сделал что-то лишнее).
#     
#     Исправление ошибок в истории (например, если закоммитил неправильные файлы).
#     
#     Удаление коммитов перед push, чтобы не засорять историю.
#     
#     Откат изменений перед слиянием веток (если обнаружены проблемы).
#
#     Типы git reset и их различия
#
#     git reset --soft <commit>
#         Откатывает коммиты, НО сохраняет изменения в файлах и индексе (git add).
#         Полезно, если хочешь переделать коммиты без потери данных.
#
#     git reset --mixed <commit> (по умолчанию)
#         Откатывает коммиты и удаляет git add, НО оставляет файлы без изменений.
#         Полезно, если хочешь пересобрать коммиты.
#
#     git reset --hard <commit>
#         Полностью удаляет коммиты и все изменения в файлах.
#         ⚠ Осторожно! Данные не восстановить, если они не были закоммичены
#
#
# Для чего нужен checkout commit?
#
# Команда git checkout <commit> используется для переключения на конкретный коммит в истории репозитория. 
# Это позволяет тебе просмотреть старое состояние кода или даже работать с ним без изменения основной ветки.
#
# Основные случаи использования checkout commit:
#
#     Просмотр старого кода:
#         Ты можешь переключиться на определённый коммит, чтобы посмотреть, как выглядел код в тот момент.
#
#     Тестирование состояния проекта на определённом коммите:
#         Если ты хочешь протестировать проект или исправление ошибки, сделанное в прошлом, можешь переключиться на нужный коммит и запустить проект.
#
#     Создание новой ветки от старого коммита:
#         Если нужно создать новую ветку на основе старого состояния репозитория, можно выполнить git checkout -b <new-branch-name> <commit-hash>.
#
#     Возврат к предыдущей версии проекта:
#         Иногда может потребоваться вернуться к старой версии кода и продолжить с ней работу (например, после неправильного слияния).
#
# Переключиться на конкретный коммит: git checkout <commit-hash>
#
# Создать новую ветку от старого коммита: git checkout -b <new-branch-name> <commit-hash>
#
# Для чего нужен reorder в Git? -order (перестановка коммитов) используется, когда тебе нужно изменить порядок коммитов в истории перед отправкой в удалённый репозиторий.
#
# Для чего нужна функция "Create Branch to Commit" в GitHub Desktop?
# Функция "Create Branch to Commit" в GitHub Desktop позволяет создать новую ветку из конкретного коммита. Это полезно, если ты хочешь начать новую работу или вносить изменения, начиная с какого-то определённого состояния проекта в истории
#
# Для чего нужен Create Tag в GitHub Desktop?
#
# Функция Create Tag используется для создания метки (тега) на определённом коммите в репозитории. Теги обычно применяются для:
#
#     Обозначения важного коммита (например, релиза или стабильной версии проекта).
#     Упрощения навигации по истории проекта.
#     Зафиксировать момент, когда завершена важная работа или когда выполнены релизные тесты.
#
#
# Revert This Commit – отменить коммит, создав обратный коммит.
#     Cherry-Pick Commit – применить этот коммит в другой ветке.
#     Copy SHA – скопировать хеш коммита.
#     View on GitHub – открыть коммит в браузере на GitHub.
#
#
#
# 3.1 Где брать ссылку на коммит? куда её отправлять? 
# де взять ссылку на коммит в GitHub Desktop?
#
#     Открой GitHub Desktop.
#     Переключись на вкладку "History" (История).
#     Найди нужный коммит.
#     Щёлкни правой кнопкой мыши по коммиту.
#     Выбери "View on GitHub" — коммит откроется в браузере.
#     Скопируй URL из адресной строки — это и есть ссылка на коммит.
#

# 4 Что такое файл лога?
#
# Файл лога — это текстовый файл, в котором записываются события, действия и ошибки в системе или приложении. Лог-файлы используются для отслеживания работы программы или системы, анализа ошибок и диагностики.
#
# Файл лога — это текстовый файл, в котором записываются события, действия и ошибки в системе или приложении. Лог-файлы используются для отслеживания работы программы или системы, анализа ошибок и диагностики.
#
#
# 4.1 Когда нужно пушить файл лога?
#
# В Git обычно не рекомендуется пушить файлы логов в удалённый репозиторий по следующим причинам:
#
#     Часто меняющиеся данные — лог-файлы могут сильно изменяться в процессе работы приложения, и пушить их может быть неудобно.
#     Логи содержат временную информацию — логи часто включают данные, которые полезны только в момент локальной работы и не являются частью кода.
#     Размер файла — логи могут занимать много места, особенно если они записывают множество действий.
#
# Тем не менее, есть несколько случаев, когда пушить файлы логов может быть полезно:
# ✅ Когда можно пушить файл лога:
#
#     При отладке или тестировании:
#         Если ты работаешь над багом или тестируешь новую функциональность, лог-файлы могут содержать важную информацию для других разработчиков. В таком случае можно запушить их в репозиторий для совместного анализа.
#
#     Если лог-файл содержит важную информацию о релизе:
#         В некоторых случаях логи могут содержать детали о том, как был выполнен сборочный процесс или интеграция, и их можно сохранить для аналитики.
#
#     Для хранения логов в специфичных проектах:
#         Если проект требует отслеживания состояния на длительный период или если логи имеют структуру, которая может быть полезна другим участникам команды.

# 5 Что такое интерпретатор?
#
# Интерпретатор — это программа, которая выполняет код построчно, переводя его в машинный код или команды для исполнения на лету, без предварительного компилирования в отдельный исполнимый файл.

# 7) Что такое модуль Python ? 
# Модуль в Python — это файл, содержащий Python-код (функции, классы, переменные и т. д.), который можно импортировать в другие программы или модули для повторного использования кода.
#
# Модуль помогает организовывать код и разделять его на логические части, делая программы более удобными для разработки и поддержания.
# ✅ Основные особенности модулей в Python:
#
#     Файл с расширением .py:
#         Модуль — это, по сути, Python-файл, который может содержать функции, классы и переменные.
#
#     Повторное использование кода:
#         Модули позволяют избежать дублирования кода. Например, если у тебя есть часто используемая функция, ты можешь положить её в модуль и импортировать в другие проекты.
#
#     Подключение модулей:
#         Чтобы использовать функции или классы из модуля, нужно импортировать его в свой код.

# 8) Как создать и отправить коммит?
#
# 1. Создание коммита:
# Шаг 1: Добавление файлов в индекс (staging area)
#
# Для того чтобы Git знал, какие файлы ты хочешь коммитить, их нужно сначала добавить в индекс с помощью команды git add. Это делает изменения готовыми для коммита.
#
# Чтобы добавить конкретный файл: git add filename.py
#
# Чтобы добавить все изменённые файлы: git add .
#
# Создаём коммит: git commit -m "Сообщение коммита"
#
# Отправляем изменения на удалённый репозиторий: git push origin Oleg14038
#
#

# 9) Как посмотреть что коммит точно отправлен и находится в github? 
#
# Проверка с помощью команды git log:
#
#     Открой терминал и перейди в каталог с репозиторием.
#
#     Выполни команду для просмотра локальной истории коммитов: git log
#
# В выводе ты увидишь список всех коммитов с их уникальными идентификаторами (hash), автором, датой и сообщением коммита
#
# commit 9fcb5a0b8b923a11a6e9b5df378bd8a6a2b5fbc6 (HEAD -> main, origin/main)
# Author: John Doe <john.doe@example.com>
# Date:   Thu Mar 7 15:47:39 2025 +0000
#
#     Исправил ошибку в функции calculate()
#
#
# 2. Проверка через GitHub (веб-интерфейс):
#
#     Перейди на GitHub и открой репозиторий, в который ты отправлял коммит.
#
#     Перейди во вкладку "Commits" (или на главную страницу репозитория, если она настроена для отображения последних коммитов).
#
#     Там ты увидишь список последних коммитов с их хешами, сообщениями и датами. Если твой коммит был успешно отправлен, он должен быть в этом списке
#
#  3. Использование команды git fetch и git log для синхронизации с удалённым репозиторием:
#
#     Чтобы убедиться, что локальная копия репозитория синхронизирована с удалённой, используй команду: git fetch
#
# После этого снова можешь использовать команду git log, чтобы увидеть, появились ли новые коммиты, отправленные на GitHub.
#
#
# 4. Проверка через графический интерфейс (например, GitHub Desktop):
#
# Если ты используешь GitHub Desktop:
#
#     Открой приложение GitHub Desktop.
#     Перейди в репозиторий, с которым работаешь.
#     В разделе "History" ты увидишь список всех коммитов, как локальных, так и тех, которые были отправлены на GitHub. Убедись, что твой коммит присутствует в этом списке.
#
# Если ты следовал этим шагам

# 10) Какая команда показывает что код не прошёл проверки на ошибки?
#
# pre-commit — это инструмент, который позволяет автоматически запускать различные проверки (например, линтеры или тесты) перед каждым коммитом. Если проверки не проходят, коммит не будет выполнен.

# 23.6 Практические примеры использования стэша.  
#
# В Git stash позволяет временно сохранять изменения в рабочем каталоге, не создавая коммит. Это полезно, если нужно переключиться на другую ветку или отложить текущую работу.
#
# 1. Сохранение изменений в стэше
#
# Допустим, у вас есть несохранённые изменения, но нужно срочно переключиться на другую ветку: git stash
#
# 2. Просмотр сохранённых изменений
#
# Чтобы увидеть список всех отложенных изменений: git stash list
# stash@{0}: On Oleg14038: Example
#
# 3. Восстановление изменений из стэша
#
# Чтобы вернуть последние сохранённые изменения: git stash pop
#
# При этом запись из стэша удалится. Если нужно оставить изменения в стэше, используйте: git stash apply
#
# 4. Восстановление конкретного стэша
#
# Если в стэше несколько сохранений, можно восстановить определённое: git stash apply stash@{1}
#
# 5. Удаление стэша
#
# Чтобы удалить последнее сохранённое изменение:git stash drop
#
# Чтобы удалить все сохранённые изменения: git stash clear
#
# 6. Сохранение изменений с сообщением
#
# Можно добавить описание при сохранении: git stash save "Исправления в логике"
#
# 7. Сохранение изменений без удаления индекса
#
# Если нужно сохранить только изменённые файлы, а проиндексированные оставить: git stash push --keep-index
#
# 8. Сохранение только конкретных файлов git stash push -m "Частичный стэш" -- path/to/file
#
#

# 24) Где посмотреть что есть конфликт в файлах? 
#
# 1. Проверка конфликтов при слиянии
#
# Если возникает конфликт, в GitHub Desktop появится предупреждение, например:
# 🚨 "Merge Conflict Detected"
# Как найти файлы с конфликтами:
#
#     Открыть GitHub Desktop.
#     На вкладке Changes (Изменения) появятся файлы с пометкой ⚠️ Conflicted.
#     Нажмите на файл – появится кнопка "Open in Editor" (Открыть в редакторе).
#
# 2. Ручное исправление конфликта
#
#     Если открыть файл в редакторе (например, VS Code или Notepad++), внутри него можно увидеть конфликтные секции:
#
#     <<<<<<< HEAD
# Текущая версия кода
# =======
# Версия из другой ветки
# >>>>>>> feature-branch
#
# Выберите нужный вариант, удалите маркеры (<<<<<<<, =======, >>>>>>>).
#
# 3. Завершение слияния
#
# После исправления конфликта:
#
#     Вернитесь в GitHub Desktop.
#     Отметьте файл как исправленный, нажав кнопку "Mark as Resolved".
#     Нажмите "Commit merge" и затем "Push" для отправки изменений.
#
# Дополнительно
#
# Если хотите увидеть файлы с конфликтами через терминал, используйте: git status
#
# git diff --name-only --diff-filter=U Это покажет список конфликтных файлов. 🚀
#
# 24.1 Когда он появляется?
#
# Когда появляется конфликт в Git?
#
# 1. При слиянии (git merge)
#
# Если две ветки изменили один и тот же участок кода, Git не может решить, какая версия верная. Например: git merge feature-branch
#
# Если в main и feature-branch изменена одна и та же строка, Git выдаст конфликт.
#
# 2. При перемотке (git rebase)
#
# Команда git rebase переносит коммиты одной ветки на другую. Если изменения пересекаются, возникает конфликт: git rebase main
#
# Git остановит процесс и потребует вручную исправить конфликт.
#
# 3. При cherry-pick
#
# Если применить коммит из одной ветки в другую (git cherry-pick), а в файле уже есть изменения, будет конфликт:git cherry-pick <commit_hash>
#
# 4. При stash pop
#
# Если у вас есть несохранённые изменения в рабочем каталоге, а в stash сохранены другие изменения для тех же строк, конфликт может появиться после команды:
#
# git stash pop
#
# 5. При pull (если есть локальные изменения)
#
# Если у вас изменённый файл локально, а удалённый репозиторий (origin) содержит другие изменения в этом же файле, конфликт возникнет при git pull: git pull origin main
#
# Git не сможет автоматически объединить изменения.
#
# Как решить?
#
#     Открыть файлы с конфликтами (git status или GitHub Desktop).
#     Вручную выбрать нужный вариант (через редактор или GitHub Desktop).
#     Добавить исправленный файл (git add file.txt).
#     Завершить процесс (git commit или git rebase --continue).
#
#     Если нужно отменить слияние: git merge --abort
#
# Если хотите отменить rebase: git rebase --abort
#
#
#

# 25) Как решить конфликт в файлах?
#
# VS Code предлагает кнопки:
#
#     Accept Current Change – оставить локальные изменения (синие).
#     Accept Incoming Change – принять изменения с GitHub (зелёные).
#     Accept Both Changes – объединить оба варианта.
#     Compare Changes – сравнить отличия.
#
# После исправления удалите конфликтные маркеры (<<<<<<<, =======, >>>>>>>), сохраните файл, выполните:
#
# git add file.txt
# git commit -m "Исправлен конфликт"
#

# 26) Напишиие правильное утверждение
#
# Зелёный (Incoming Change) – изменения, пришедшие с GitHub (из удалённого репозитория).
# Синий (Current Change) – ваши локальные изменения.
#
# Как это выглядит в VS Code?
#
# При открытии файла с конфликтом в VS Code появятся две секции
#
# <<<<<<< HEAD
# (Синее) Ваши локальные изменения
# =======
# (Зелёное) Изменения из удалённого репозитория (GitHub)
# >>>>>>> origin/main
#

# 27) Если мы работаем в одном файле, можно ли принять pull после того как вы спрячете в стэш свои изменения? 
#
# Если у вас есть несохранённые изменения в файле, но нужно сделать git pull, вы можете сохранить их в стэш, выполнить pull и затем вернуть изменения обратно.
#
# Как это сделать?
#
# 1️⃣ Сохраните изменения в стэш: git stash
#
# Теперь рабочий каталог чист, и вы можете принять pull.
#
# 2️⃣ Выполните git pull: git pull origin main
#
# Git обновит ваш локальный репозиторий.
#
# 3️⃣ Верните изменения из стэша: git stash pop
#
# Это восстановит ваши изменения поверх обновлённого кода.
#
# 🔹 Если после stash pop снова возник конфликт, исправьте его вручную и завершите процесс (git add . → git commit). 
#
#

# 27.1 Что может произойти когда stash восстановите после принятия pull?
#
# 1. Нет конфликтов — всё прошло успешно ✅
#
# Если ваши изменения не пересекались с обновлениями из pull, Git просто применит их поверх обновлённого кода - git stash pop
#
# Вы получите сообщение: Dropped refs/stash@{0} (stash)
# Ваши изменения вернулись, и всё работает.
#
#
# 2. Возник конфликт ⚠️
#
# Если изменения из stash затрагивают те же строки, что и pull, Git покажет конфликт.
#
# Сообщение Git:Auto-merging file.txt
# CONFLICT (content): Merge conflict in file.txt
#
# Как исправить?
#
#     Откройте файл с конфликтом (file.txt), найдите маркеры <<<<<<<, =======, >>>>>>>.
#     Вручную выберите нужный код.
#     Добавьте файл в индекс:
#
# Как исправить?
#
#     Откройте файл с конфликтом (file.txt), найдите маркеры <<<<<<<, =======, >>>>>>>.
#     Вручную выберите нужный код.
#     Добавьте файл в индекс:
#
#
# git add file.txt
#
# Завершите процесс: git commit -m "Исправлен конфликт после стэша"
#
#
#
# 3. Ошибки при восстановлении стэша ❌
#
# Если Git не может применить stash, он покажет ошибку: error: Your local changes to the following files would be overwritten by merge:
#
# Что делать?
#
#     Использовать git stash apply вместо pop (так стэш не удалится, если что-то пойдёт не так): git stash apply
#
# Если изменения не накладываются, можно применить их вручную из стэша, используя git stash show -p stash@{0}
#

# Что делает кнопка "Complete Merge" в GitHub Desktop?
#
# 🔹 Кнопка "Complete Merge" в GitHub Desktop завершает процесс слияния (merge).
# Когда она появляется?
#
#     Когда есть конфликты при слиянии (merge).
#     Вы разрешили все конфликты вручную.
#     Файлы с исправлениями добавлены в индекс (git add).
#
# Что происходит после нажатия?
#
#     Git фиксирует изменения и завершает слияние.
#     Создаётся новый коммит с результатом слияния.
#     Вы можете отправить (push) изменения в репозиторий.
#

# 31 Что такое FORK? Зачем его делают? 
#
# Что такое Fork?
#
# Fork — это операция в GitHub (и других платформах, таких как GitLab или Bitbucket), которая создаёт копию репозитория в вашем собственном аккаунте. Это даёт вам возможность вносить изменения в проект, не влияя на оригинальный репозиторий, а затем предложить изменения обратно через pull request.
#
# Зачем делают Fork?
#
#     Работа с чужими проектами:
#     Когда вы хотите внести изменения в чужой репозиторий, вы не можете напрямую изменить его, если у вас нет прав. В этом случае вы можете форкнуть репозиторий. Это создаёт его копию в вашем аккаунте, и вы можете вносить изменения в неё.
#
#     Внесение предложений и исправлений:
#     После внесения изменений в форк, вы можете создать pull request, чтобы предложить эти изменения владельцу оригинального репозитория. Это используется для исправлений ошибок, улучшения функционала или добавления новых возможностей.
#
#     Изучение и эксперименты:
#     Вы можете форкнуть проект, чтобы изучить его код, поэкспериментировать с новыми фичами или попробовать сделать изменения без риска повредить основной проект.
#
#     Разработка в отдельной ветке:
#     Fork позволяет вам работать над проектом в своей ветке и интегрировать изменения обратно, только если они готовы и протестированы.

# 32 Как скачать форкнутый репозиторий на локальный компьютер?
#
# 1. Склонируйте репозиторий
#
#     Перейдите в свой форк репозитория на GitHub/GitLab и скопируйте URL репозитория (кнопка Code).
#
#         HTTPS: https://github.com/ВАШ_АККАУНТ/РЕПОЗИТОРИЙ.git
#
#         SSH: git@github.com:ВАШ_АККАУНТ/РЕПОЗИТОРИЙ.git
#
#     Откройте терминал и выполните: git clone [URL-репозитория]
#
# 2. Перейдите в папку репозитория cd forked-repo
#
# 3. (Опционально) Добавьте связь с исходным репозиторием
#
# Чтобы синхронизироваться с изменениями из оригинального репозитория: git remote add upstream [URL-исходного-репозитория]
#
# 4. Проверьте настройки
#
# Убедитесь, что удалённые репозитории настроены: git remote -v
#
# Вывод должен содержать: git remote -v
#
# Вывод должен содержать:
#
# origin    [URL-вашего-форка] (fetch/push)
# upstream  [URL-исходного-репозитория] (fetch/push)
#
# Теперь вы можете работать с локальной копией форкнутого репозитория. Чтобы обновить его с изменениями из исходного репозитория:
#
# git fetch upstream
# git merge upstream/main  # или другая ветка

# 34 Как создать файл в vs code? 
#
# Чтобы создать файл в Visual Studio Code (VS Code), выполните следующие шаги:
#
#     Откройте VS Code.
#
#     Создайте новый файл:
#         Перейдите в меню File (Файл) в верхней панели и выберите New File (Новый файл), или
#         Используйте сочетание клавиш Ctrl+N (Windows/Linux) или Cmd+N (Mac), чтобы создать новый файл.
#
#     Сохраните файл:
#         После создания нового файла, выберите File > Save As (Сохранить как) или используйте сочетание клавиш Ctrl+S (Windows/Linux) или Cmd+S (Mac).
#         Выберите место для сохранения файла и введите имя файла, включая расширение (например, index.html, script.js, style.css и т.д.).
#
#     Редактируйте и используйте файл:
#         Теперь вы можете редактировать файл и работать с ним в VS Code.

# Дополнительные вопросы:
# 1 Какая команда конвертирует файл в py из ipynb? 
#
# Чтобы конвертировать файл из формата .ipynb (Jupyter Notebook) в .py (Python script), используйте команду: jupyter nbconvert --to script имя_файла.ipynb
#
# Эта команда создаст Python-скрипт с расширением .py из вашего Jupyter Notebook.
#
# Замените имя_файла.ipynb на имя вашего файла. После выполнения команды файл с расширением .py будет создан в той же директории, где находится ваш исходный файл .ipynb.
#

# 2) Что такое пакетный менеджер? Вы пользуетесь пакетным менеджером conda или pip? Какой лучше использовать для дата сайнс?
#
# 1. Что такое пакетный менеджер?
#
# Пакетный менеджер — это инструмент для автоматизации установки, обновления, удаления и управления зависимостями программных пакетов. Он упрощает работу с библиотеками, фреймворками и другими компонентами проекта, обеспечивая:
#
#     Установку пакетов из репозиториев (например, PyPI для Python).
#
#     Разрешение зависимостей (автоматический подбор совместимых версий пакетов).
#
#     Создание изолированных окружений (чтобы проекты не конфликтовали друг с другом).
#
# Примеры пакетных менеджеров: pip (Python), conda (кроссплатформенный), apt (Debian/Ubuntu), npm (JavaScript).
#
#
# 2 Пакетный менеджер  conda 
#
# 3. Conda vs pip: что лучше для Data Science?
# Conda
#
#     Плюсы:
#
#         Управляет не только Python-пакетами, но и бинарными зависимостями (C/C++ библиотеки, CUDA и т.д.), что критично для работы с ML-библиотеками (TensorFlow, PyTorch).
#
#         Создает изолированные окружения с контролем версий Python и других программ.
#
#         Имеет собственный репозиторий (Anaconda Cloud), где многие пакеты оптимизированы под Data Science.
#
#     Минусы:
#
#         Меньше пакетов по сравнению с PyPI.
#
#         Требует установки дистрибутива (Miniconda или Anaconda).
#
# pip
#
#     Плюсы:
#
#         Стандартный менеджер для Python, интегрирован с PyPI (крупнейший репозиторий Python-пакетов).
#
#         Подходит для простых проектов без сложных системных зависимостей.
#
#     Минусы:
#
#         Не умеет работать с не-Python зависимостями.
#
#         Для изоляции окружений требуется virtualenv или venv.
#
# Рекомендация для Data Science
#
#     Используйте conda, если:
#
#         Работаете с библиотеками, требующими компиляции (NumPy, SciPy, TensorFlow).
#
#         Нужны разные версии Python или системные зависимости.
#
#         Хотите избежать проблем с установкой CUDA или других низкоуровневых компонентов.
#
#     Используйте pip, если:
#
#         Проект использует только чистые Python-пакеты (например, Flask, requests).
#
#         Пакет недоступен в репозиториях conda (например, Hugging Face Transformers).

# 3 Почему расширение py лучше чем ipynb?
#
# Расширение .py имеет несколько преимуществ перед .ipynb:
#
#     Производительность: Скрипты Python (.py) выполняются быстрее, так как они не требуют использования Jupyter Notebook для запуска кода. В то время как .ipynb файлы создают дополнительные накладные расходы при выполнении через Jupyter.
#
#     Простота использования: Скрипты .py можно легко запускать в любых средах, включая текстовые редакторы, IDE и командную строку. В отличие от .ipynb, для которых требуется наличие Jupyter, что не всегда удобно.
#
#     Чистота кода: Python-скрипты не содержат "мусорных" ячеек, как в Jupyter Notebook. Это упрощает код и делает его более структурированным.
#
#     Гибкость: Скрипты Python можно интегрировать в другие системы и автоматизировать выполнение. Их можно запускать как часть более крупных проектов, в то время как .ipynb файлы обычно используются для исследовательского анализа и визуализаций.
#
#     Контроль версий: .py файлы легче отслеживать в системах контроля версий (например, Git), так как они представляют собой чистый текст, тогда как .ipynb файлы могут включать метаданные, что затрудняет сравнение версий.

# 4 Что такое pep8? 
#
# PEP 8 (Python Enhancement Proposal 8) — это стиль кодирования для Python, который описывает рекомендации по написанию чистого, читаемого и поддерживаемого кода. Он включает в себя правила и соглашения по следующим аспектам:
#
#     Отступы: Рекомендуется использовать 4 пробела для каждого уровня отступа.
#     Длина строки: Строки не должны превышать 79 символов (или 72 для строк документации).
#     Импорт: Импорты должны быть на отдельных строках и расположены в определённом порядке (стандартные библиотеки, сторонние библиотеки, локальные модули).
#     Именование: Стиль именования должен соответствовать соглашениям (например, snake_case для переменных и функций, CamelCase для классов).
#     Докстринги: Описание функций и классов должно быть оформлено в виде строк документации, соблюдая формат PEP 257.
#     Пробелы: Использование пробелов в выражениях и после запятых.
#
# 4.1 линтеры проверяют на соблюдение pep8?
#
# Да, линтеры, такие как Pylint, Flake8 и PyLint, могут проверять код на соответствие PEP 8. Они анализируют код и предупреждают о нарушениях стиля, таких как:
#
#     Несоответствие отступов.
#     Превышение максимальной длины строки.
#     Неправильное именование переменных или функций.
#     Отсутствие пробелов после запятой или перед/после оператора.
#     Нарушения в структуре импорта и другие проблемы.
#
# Линтеры могут быть настроены для строгого соблюдения PEP 8 или для проверки только определённых правил. Это позволяет автоматизировать процесс проверки кода и улучшать его качество, особенно в больших проектах с несколькими разработчиками.
#
# 4.2 Какая нотация используется для создания переменных? 
#
# В Python для создания переменных используется нотация snake_case. Это означает, что:
#
#     Имя переменной состоит из строчных букв.
#     Слова разделяются нижним подчеркиванием (_).
#
# user_name = "Alice"
# total_amount = 100
#
# Для классов используется нотация CamelCase, где каждое слово начинается с заглавной буквы, без пробелов и подчёркиваний:
#
# class UserAccount:
#     pass
#
# Для констант (значений, которые не меняются) принято использовать UPPER_CASE_WITH_UNDERSCORES:
#
# 4.3 Может ли переменная состоять из одной буквы например андерскор  "_"
# Один подчеркивание (_): Это специальная переменная, которая часто используется в Python для обозначения значения, которое не имеет важности или будет игнорироваться. Например, в цикле или в функциях:
#
#     for _ in range(5):
#     print("Hello")
#
# Одиночные буквы (например, x, y, z): Переменные с одной буквой тоже допустимы. Это часто используется для временных переменных или индексов в циклах:
# x = 10
# y = 20
# result = x + y
#
# Особенность _ в интерпретаторе: В интерактивной сессии Python переменная _ используется для хранения последнего вычисленного значения. Например:
#
# >>> 10 + 5
# 15
# >>> _
# 15
#
#
# 4.4 Зачем и где мы используем андерскор _ 
#
# 1. Игнорирование значения
#
# Когда вы хотите игнорировать значение, которое не имеет значения для вашего кода, используйте один символ подчеркивания (_).
#
# Примеры:
#
#     В цикле for, если вам не нужно использовать индекс:
#     for _ in range(5):
#     print("Hello")
#
# Когда функция возвращает несколько значений, но вам нужно только одно:
#  x, _ = some_function()
#
# 2. Последнее вычисленное значение (в интерактивной сессии)
#
# В интерактивной оболочке Python символ _ хранит последнее вычисленное значение.
#
# Пример в интерактивной сессии Python: >>> 3 + 5
# 8
# >>> _  # Выводит последнее значение
# 8
#
#
#
# 3. Одно или два подчёркивания перед именем
#
#     Один подчеркивание перед именем (например, _var): Это соглашение указывает, что переменная или метод являются "приватными" и не должны использоваться напрямую за пределами класса или модуля. Однако это всего лишь соглашение, а не строгая защита (Python не запрещает доступ к таким переменным).
#
#     class MyClass:
#     def __init__(self):
#         self._private_variable = 42
#
#
# Два подчеркивания перед именем (например, __var): Это вызывает механизмы "name mangling", что изменяет имя переменной, делая его уникальным внутри класса и предотвращая прямой доступ к нему. Это используется для защиты от случайных конфликтов имён в наследуемых классах. 
#
# class MyClass:
#     def __init__(self):
#         self.__private_variable = 42
#
#
# Здесь переменная будет называться _MyClass__private_variable внутри класса.
#
# 4. Одно подчеркивание в конце имени (например, class_)
#
# Когда имя переменной или функции конфликтует с ключевым словом Python, используется подчеркивание в конце. Это помогает избежать конфликтов с зарезервированными словами.
#
# Пример: class_ = "MyClass"
#
#
# 5. Использование в библиотеках и фреймворках
#
# В некоторых библиотеках (например, в Django) символ _ может использоваться для обозначения функций или переменных, которые выполняют специфические задачи, такие как международная локализация (перевод) через gettext:
#
# from django.utils.translation import gettext as _
# print(_("Hello, World!"))
#
# 6. Для представлений и других случаев
#
# Символ _ может использоваться и в других случаях, например, для обозначения временных переменных, которые не должны использоваться в дальнейшем, или в тех местах, где это улучшает читаемость и соответствие стилю кода.
#
# В целом, _ часто используется как вспомогательный элемент для улучшения структуры кода, его читаемости и предотвращения конфликтов имен.
#
#  По PEP8 допустима переменная в одну букву?
#
# Да, согласно PEP 8, переменные с именем в одну букву допустимы, но они должны использоваться в особых случаях, когда это оправдано контекстом. Например:
#
#     Индексы в циклах: Когда переменная используется как индекс в цикле, обычно предпочтительны такие имена, как i, j, k, и т. п.

#
