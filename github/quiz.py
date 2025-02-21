"""Ответы на вопросы по контрибьютингу."""

<<<<<<< HEAD
# ## Список вопросов и ответов по теме контрибьютинг:
#
# ### GitHub
#
# 1. Что такое GitHub?
#
# GitHub -  это крупнейшее хранилище Git репозиториев, а так же центр сотрудничества для миллионов разработчиков и проектов.
#
# 1.2. Как GitHub связан с Git?
#
#  - Разработчики работают с локальными копиями репозиториев с использованием Git и могут пушить изменения на удаленные репозитории, находящиеся на GitHub.
#  - GitHub позволяет клонировать и форкать репозитории для работы с ними локально с помощью Git.
#  - Разработчики могут отправлять запросы на внесение изменений через GitHub, чтобы предложить свои изменения для включения в основной проект.
#
# 1.3. Чем отличается fork репозитория от его клонирования (clone)?
#
# Форк это копирование чужого репозитория к себе. Чтобы продолжить с ним работать локально, его необходимо склонировать к себе локально. То есть по сути клонирование проекта - это скачивание репозитория к себе на компьютер локально.
#
# 1.4. Зачем нужны и как работают pull requests?
#
# Pull Requests (PR) — это механизм в Git и GitHub, который позволяет разработчикам сотрудничать над проектами, предлагая изменения и внося улучшения в кодовую базу. Они помогают обеспечить качественный код и согласованность изменений.
#
# Как они работают: Разработчик форкает основной репозиторий, создавая свою копию на GitHub, и клонирует её на локальный компьютер и создает новую ветку. -> Разработчик вносит изменения в код, коммитит и пушит их. -> На странице форкнутого репозитория на GitHub разработчик создает новый Pull Request, указывая основную ветку (main или master) в качестве базовой и свою ветку с изменениями. -> Другие участники команды проверяют изменения, оставляют комментарии, предлагают улучшения и обсуждают код. -> После успешного ревью и одобрения PR сливается в основную ветку.
#
# 1.5. GitHub использует ваш почтовый адрес для привязки ваших Git коммитов к вашей учётной записи?
#
# Да, это позволяет GitHub правильно идентифицировать, кто совершил каждый коммит, и связывать его с соответствующей учетной записью на платформе.
#
# 1.6 Какая команда генерирует SSH ключ для Доступа по SSH к репозиторию (Рисунок 83)
#
# ```ssh-keygen``` - команда для генерации ssh-ключа. После того, как он будет сгенерирован, посмотреть его можно в папке ~/.ssh/id_rsa.pub. После этого заходим в настройки учетной записи на GitHub, переходим в SHH keys, нажимаем кнопку «Add an SSH key». В поле Title прописываем имя ключа, в поле Key вставляем сгенерированный ранее ssh-ключ. Далее нажимаем «Add key».
#
# ### Внесение собственного вклада в проекты
#
# 2. Создайте ишьюс и запомните его номер.
#
# DONE
#
# 2.1. Если вы хотите вносить свой вклад в уже существующие проекты, в которых у нас нет прав на внесения изменений путём отправки (push) изменений, вы можете создать своё собственное ответвление, что нужно сделать чтобы создать собственное ответвление (Рисунок 88)?
#
# Необходимо сделать форк репозитория.
#
# Сделайте ответвление https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV, и вставьте сюда ссылку на ваше ответвление.
#
# https://github.com/artistique1/Data-Science-For-Beginners-from-scratch-SENATOROV
#
# 2.2 создайте ветку dev в ФОРКЕ Data-Science-For-Beginners, вставьте сюда ссылку на вашу ветку dev
#
# https://github.com/artistique1/Data-Science-For-Beginners-from-scratch-SENATOROV/tree/dev
#
# 2.3 В README файле вашего ФОРКА, добавьте ссылку на мой телеграм канал https://t.me/RuslanSenatorov, сохраните коммит, название коммита - в тайтле название ишьюса (#номер_ишьюс), в дескрипшене - Closes #NUMBER-ISSUES номер возьмите из пункта 2
#
# DONE
#
# 2.4 Отправьте пул реквест из ФОРКА в основу В ВАШУ ВЕТКУ, тайтл пул реквеста скопируйте из ISSUES-TITLE, в дескрипшине пул реквеста напишите Closes #NUMBER-ISSUES вставьте номер из пункта 2
#
# DONE
#
# 2.5 Прокомментируйте ваш пул реквест перед слиянием, перейдите во вкладку(Рисунок 92) и напишите "ок", потом нажимайте сабмит ревью затем не выходя из этой вкладки, в файле README , добавьте туда ссылку на https://t.me/SENATOROVAI,
# => инструкция
#
# DONE
#
# 2.6 Выполните Merge pull request (Рисунок 116), вставьте сюда ссылку на ваш пул реквест
#
# https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV/pull/189
#
# 2.7 Вставьте сюда ссылку на закрытые пул реквесты в репозитории, найти можно тут
#
# https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV/pulls?q=is%3Apr+is%3Aclosed
#
# 2.8 Как посмотреть какие файлы были в репозитории на момент определенного коммита? вставьте сюда ссылку на любой коммит, где взять ссылку? подсказка:
#
# https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV/tree/9b4d2e8b320aaa621eff261c8ea58118569a7ef5
#
# 2.9 как открыть запрос слияния, указывающий на другой запрос слияния и зачем это нужно? (Рисунок 117)
#
# Если мы видим запрос слияния и у нас есть идея как его улучшить или мы не уверены, что это хорошая идея, или у нас просто нет прав записи в целевую ветку, то в таком случае мы можем открыть запрос слияния, указывающий на данный запрос. При открытии запроса на слияние вверху страницы мы увидим меню для выбора целевой и исходной веток. Если нажать кнопку Edit справа, то станет доступным выбор не только исходной ветки, а ещё и форка - здесь можно указать нашу новую ветку для слияния с другим запросом слияния или другим форком проекта.
#
# ### Рабочий процесс с использованием GitHub
#
# 3. Напишите 8 пунктов, которые нужно сделать, чтобы внести вклад в чужой проект.
#
#  1. Форкнуть репозиторий.
#  2. Склонировать его к себе на локальный компьютер.
#  3. Создать в нем новую ветку и запушить ее.
#  4. Внести изменения.
#  5. Сделать коммит изменений.
#  6. Запушить из на свою ветку в форкнутый репозиторий.
#  7. Создать pull request с описанием изменений, который мы внесли и какую пользу они несут.
#  8. Участвовать в обсуждении.
#
# 3.1. Какие практики принято соблюдать при создании Pull Request чтобы закрыть автоматический issues?
#
#  - Использование ключевых слов в описании pull request (closes, fixes, resolves).
#  - Четкое и подробное описание изменений, которые были внесены в проект, и как они решают связанный Issue.
#  - Включить ссылку на связанный Issue в описание pull request. Это сделает навигацию между pull request и Issue проще.
#  - Убедиться, что все тесты проходят успешно и они не нарушат работу проекта.
#  - Участие в обсуждениях и отзывах - внесение исправлений и доработок после обратной связи поможет ускорить процесс принятия PR.
#
# Какие практики принято соблюдать при создании commit чтобы закрыть автоматический issues?
#
#  - Использование ключевых слов в сообщении коммита, которые укажут GitHub на необходимость автоматического закрытия связанного Issue (closes, fixes, resolves). Желательно добавить название файлов или функций, в которых были сделаны изменения.
#  - Добавить ссылку на ишьюс в title, если коммит будет связан с конкретным ишьюс.
#  - Сообщение для коммита должно описывать связанные с ним изменения.
#  - В коммите должны быть только те файлы, который соответствуют названию коммита. Один коммит - один файл. Не должно быть лишних файлов.
#  - Регулярно делать коммиты - это поможет упростить отладку.
#  - Убедиться, что все тесты проходят успешно перед созданием коммита. Это гарантирует, что наши изменения не нарушат работу проекта.
#
# 3.2 Как отклонить/закрыть пул реквест? (предоставьте скриншот где это в гитхабе)
#
# ![screen](https://i.postimg.cc/tgzq0qbj/2025-02-16-172729.png)
#
# 3.3 Перед отправкой пул реквеста нужно ли создавать ишьюс?
#
# Создание Issues перед отправкой Pull Request (PR) необязательно, но является хорошей практикой, особенно в командной разработке и в крупных проектах. Так что здесь я бы ответила, что обязательно.
#
# 3.4 В какой вкладке можно посмотреть список изменений который был в пул реквесте? (Рисунок 92)
#
# Files changed
#
# 3.5 В какой вкладке находится страница обсуждений пул реквеста? (Рисунок 94)
#
# Conversation
#
# ### Создание запроса на слияние
#
# 4. Можно ли открыть пул реквест, если вы ничего не вносили в FORK?
#
# Нет, так как GitHub не будет иметь изменений для слияния.
#
# 4.1 Что нужно сделать чтобы открыть пул реквест? (Рисунок 90)
#
# Нажать на кнопку открытия запроса на слияние - Compare & pull request.
#
# 4.2 Что нужно сделать Если ваш Форк устарел?
#
#  - Через консоль: добавить оригинальный репозиторий как удаленный (`git remote add upstream "ссылка на оригинальный репозиторий"`) -> получить из него обновления с помощью `git fetch upstream` -> обновите локальную ветку `git checkout "название ветки"` - обычно это main или master -> объедините изменения из оригинального репозитория в вашу локальную ветку `git merge upstream/main` -> разрешить конфликты если они есть -> запушить изменения в наш форк.
#
#  - Через GitHub: перейти на страницу форкнутого репозитория -> перейти во вкладку Pull requests и нажать New pull request -> выбрать исходный (из которого будет пулить изменения) и целевой репозиторий (в который будем пулить изменения) -> нажать Create pull request -> подтвердить слияние, нажав на Merge pull request. Если возникнут конфликты, нужно будет нажать на Resolve conflicts и разрешить их вручную.
#
# 4.3 Что нужно сделать если в пул реквесте имеются конфликты слияния (Рисунок 96)
#
# Существует 2 варианта, как это сделать:
#
#  - Можно перебазировать свою ветку относительно целевой ветки (обычно, относительно master ветки исходного репозитория).
#  - Или слить целевую ветку в свою.
#
# Большинство разработчиков на GitHub выбирают последний вариант. Важна история и окончательное слияние, а перебазирование не принесёт ничего, кроме немного более чистой истории, при этом оно гораздо сложнее и может стать источником ошибок.
#
# ### Отрывки кода
#
# 5. Что нужно сделать Для добавления отрывка кода в комментарии к ишьюсу? (Рисунок 104)
#
# Выделяем строки кода, которые мы хотим прикрепить -> нажимаем на три точки и выбираем Copy permalink. Затем заходим  в Issue и в description вставляем эти строки кода. Либо это можно сделать вручную, скопировать код и вставить его внутрь обратных кавычек (```отрывок кода```). Если указать в кавычках название языка, то GitHub попробует применить к нему подсветку синтаксиса.
#
# 5.1 На какую клавишу нажать клавишу чтобы выделенный текст был включён как цитата в ваш комментарий?(Рисунок 105)
#
# Если в комментарии выделить текст и нажать клавишу r, то выделенный текст будет включён как цитата в наш комментарий. Либо перед цитируемой частью комментария поставить символ >.
#
# 5.2 Как вставить картинку в ишьюс? (Рисунок 108)
#
# Внизу комментария будет скрепка с надписью Paste, drop or click to add files. Выбираем картинку и прикрепляем ее в description нашего ишьюса.
#
# ### Поддержание GitHub репозитория в актуальном состоянии
#
# 6 Как понять что ваш форк устарел?
#
#  - При сравнении веток: перейти на страницу форкнутого репозитория -> нажать "Compare" или "Compare & pull request" -> выбрать оригинальный репозиторий и ветку для сравнения -> Если есть изменения, которых нет в нашем форке, это значит, что наш форк устарел.
#  - Выполнить команду git fetch upstream для получения изменений из оригинального репозитория -> git status, чтобы увидеть, есть ли какие-либо изменения, которых нет в нашем форке.
#  - Иногда GitHub уведомляет если наш форк отстает от оригинального репозитория. Это может быть отображено на странице нашего форка.
#
# 6.1 Как обновить форк?
#
#  1. Способ без конфигурации: перейти на ветку master в нашем форкнутом репозитории (`git checkout master`) -> спуллить с основной веткой оригинального репозитория (`git pull "url оригинального репозитория"`) -> отправить локальную ветку master в наш форк origin (`git push origin master`).
#  2. Используя конфигурацию: добавить исходный репозиторий как удалённый с другим именем (`git remote add progit "url оригинального репозитория"`) -> настроить локальную ветку master на получение изменений из удалённого репозитория
#  progit (`git branch --set-upstream-to=progit/master master`) -> установить origin как репозиторий по умолчанию для отправки (`git config --local remote.pushDefault origin`). После этого процесс становится гораздо проще:
#   - `git checkout master`
#   - `git pull`
#   - `git push`
#
# ### Добавление участников
#
# 7. Как добавить участников в ваш репозиторий, чтобы команда могла работать над одним репозиторием? (Рисунок 112)
#
# Заходим в Settings нашего репозитория, в панели слева в разделе Access нажимаем Collaborators и добавляем участников для совместной работы, нажав на Add people.
#
# ### Упоминания и уведомления
#
# 8. Какой символ нужен для упоминания кого-либо? (Рисунок 118)
#
# @
#
# 8.1 Где находится Центр уведомлений, напишите ссылку (Рисунок 121)
#
# https://github.com/notifications
#
# ### Особенные файлы
#
# 9. Что такое и зачем нужен файл README
#
# README для описания проекта и предоставления ключевой информации пользователям и разработчикам. Он включает в себя следующее:
#  - Для чего предназначен проект
#  - Инструкции по конфигурации и установке
#  - Примеры использования
#  - Используемую лицензию
#  - Правила участия в проекте
#
# 9.1 Что такое и зачем нужен файл CONTRIBUTING (Рисунок 122)
#
# В нем указаны конкретные вещи, которые мы хотим или не хотим видеть в новых запросах на слияние. Таким образом люди могут ознакомится с руководством, перед тем как создавать новый запрос на слияние.
#
# ### Управление проектом
#
# 10. Как изменить основную ветку (Рисунок 123)
#
# Заходим в Settings нашего репозитория, во вкладке General -> Default branch. Тут можно поменять ветку, к которой пользователи будут открывать запросы на слияние.
#
# 10.1 Как передать проект? какая кнопка? (рисунок 124)
#
# Заходим в Settings нашего репозитория, пролистываем вниз до Danger zone -> в Transfer ownership нажимаем на Transfer. Эта опция полезна, когда мы хотим отказаться от проекта, а кто-то другой хочет им заниматься, или когда наш проект растёт и мы хотим передать его какой-нибудь организации.
#
# 10.2 Что такое файл .gitignore?
#
# .gitignore — это специальный файл, используемый в системах контроля версий Git для указания файлов и директорий, которые Git должен игнорировать.
#

#
