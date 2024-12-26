"""Detailed explanation about issues in GitHub."""

# #### 1.Что такое Issues на GitHub и для чего они используются?
#
# Issues на GitHub — это инструмент для управления задачами и отслеживания ошибок в репозиториях. Они представляют собой систему тикетов, которая позволяет участникам проекта сообщать о проблемах, предлагать улучшения или новые функции, а также организовывать работу команды.

# #### 2. Чем Issues отличаются от других инструментов управления задачами?
#
# Issues встроены в экосистему GitHub, что позволяет ссылаться на конкретные строки кода, коммиты или ветки.
# Быстрота использования - так как она встроена в функционал GitHub вам не надо разбираться в других программах
# GitHub Issues идеально подходят для разработчиков и open-source проектов благодаря своей интеграции с кодовой базой, простоте и фокусу на разработке.
#

# #### 3. Какие основные компоненты (поля) есть у каждого Issue?
#
# * Заголовок (Title)
# * Описание (Description)
# * Метки (Labels)
# * Исполнитель (Assignees)
# * Проект (Projects)
# * Этап (Milestone)
# * Ссылки на Pull Requests (Linked Pull Requests)
# * Комментарии (Comments)
# * Автор (Author)
# * Состояние (State)
# * Номер Issue (#)

# #### 4. Как создать новое Issue в репозитории?
#
# 1. Перейдите в необходимый репозиторий
# 2. Перейдите во вкладку Issues > New Issues
# 3. Заполните поля Issues > Submit new issue  

# #### 5. Какие данные рекомендуется указывать в описании Issue для лучшего понимания задачи?
#
# Необходимо указать краткое описание проблемы и задачи
#
# Указать подробно как выглядит проблема и в каких случаях она появляется
#
# Поделитесь скриншотом экрана или ссылкой с записью экрана
#
# Укажите ожидаемое поведение, какой результат вы ожидаете
#
# Укажите фактическое поведение, что происходит на самом деле
#
# Укажите среду выполнения : браузер, язык программирования и тд
#
# Добавьте логи и сообщения об ошибках
#
#

# #### 6. Какие теги (labels) можно добавить к Issue? Какие из них стандартные?
#
# При создании нового репозитория на GitHub в нём уже присутствуют следующие стандартные метки:
#
# bug - ошибки
#
# documentation - обновление документации
#
# duplicate - проблема уже существует и указать ссылку на существующий issue
#
# enhancement - для улучшений или новых функций.
#
# good first issue - метка для простых задач, которые подходят для новичков в проекте.
#
# help wanted - необходима помощь с конкретной задачей
#
# invalid -  ошибочные данные или нерелевантны для проекта.
#
# question -  для вопросов или запросов на уточнение.
#
# wontfix - указывает, что данная задача или проблема не будет решена.
#
#
# #####  Кастомные метки (пользовательские)
#
# ##### По типу задачи
#
# feature: Для новых функций.
#
# refactor: Для задач, связанных с улучшением структуры или качества кода без изменения функциональности.
#
# tests: Для задач, связанных с тестированием.
#
# performance: Для задач, связанных с оптимизацией производительности.
#
# ##### По приоритету
#
# priority: high: Высокий приоритет.
#
# priority: medium: Средний приоритет.
#
# priority: low: Низкий приоритет.
#
# ##### По статусу задачи
#
# in progress: Задача в работе.
#
# blocked: Задача заблокирована и требует выполнения другой задачи.
#
# ready for review: Задача готова для проверки.
#
# ##### По области проекта
#
# frontend: Для задач, связанных с пользовательским интерфейсом.
#
# backend: Для задач, связанных с серверной частью.
#
# devops: Для задач, связанных с настройкой инфраструктуры.
#
# ##### Для конкретных процессов
#
# security: Для задач, связанных с уязвимостями и безопасностью.
#
# UX/UI: Для задач, связанных с дизайном или пользовательским опытом.
#
# localization: Для задач, связанных с переводом и локализацией.
#
#

# ####  7. Как прикрепить Assignees (ответственных) к Issue?
#
# На правой панели Issue (sidebar) вы увидите секцию "Assignees". Там вы  можете выбрать ответственных для этого issue

# #### 8. Как использовать Labels для классификации задач?
#
# Метки позволяют быстро находить, фильтровать и группировать Issues по категориям, типам, приоритету и другим характеристикам.

# #### 9. Для чего нужен Milestone, и как связать его с Issue?
#
# Milestone  на GitHub используется для группировки связанных задач (Issues и Pull Requests) в рамках общей цели или этапа проекта. Это инструмент для планирования и отслеживания прогресса разработки

# #### 10. Как привязать Issue к пул-реквесту (Pull Request)?
#
# Можно привязать при создании Pull Request при помощи # которая указывает на номер issue или же указать ссылку на прямую к issue

# #### 11. Как добавить комментарий к существующему Issue?
#
# Внизу каждого Issue есть поле для комментариев, там вы можете оставить свой комментарий.

# #### 12. Как закрыть Issue вручную?
#
# На странице Issue найдите кнопку "Close issue". Нажмите на "Close issue". Статус Issue изменится на "Closed".

# #### 13. Можно ли автоматически закрыть Issue с помощью сообщения в коммите или пул-реквесте? Как это сделать?
#
# Да в описании коммита вы можете указать о закрытии Issue - Closes #issue-number 
#
# Так же при создании Pull-Request вы так же можете добавить в описание - Closes #issue-number
#

# #### 14. Как повторно открыть закрытое Issue, если работа ещё не завершена?
#
# На странице закрытого Issue найдите кнопку Reopen issue
#

# #### 15. Как найти все открытые или закрытые Issues в репозитории?
#
# На вкладке issues в вашей репозитории ниже поисковика вы можете найти две вкладки Open and Closed. Там вы можете выбрать как открытые так и закрытые issues

# #### 16. Как использовать фильтры для поиска Issues по меткам, исполнителям или другим критериям?
#
# Фильтрация по меткам (label)
#
# По исполнителям (assignees)
#
# По статусу (открытые или закрытые) - is:open или is:closed.
#
# По сроку выполнения (milestone)
#
# По автору (author) 
#
# По типу задачи (например, Pull Request или Issue)
#
# По датам (создания или обновления) - created: или updated:
#
#

# #### 17. Как сортировать Issues по приоритету, дате создания или другим параметрам?
#
#
# Сортировка по дате создания - is:open sort:created-desc
#
# Сортировка по дате последнего обновления - is:open sort:updated-desc
#
# Сортировка по приоритету (метки) - is:open label:"high priority" sort:created-desc
#
#

# #### 18. Как настроить автоматические уведомления о новых или изменённых Issues?
#
# Самый быстрый способ это нажать на кнопку Subscribe для любого Issues который вас интересует

# #### 19. Что такое Projects в контексте GitHub, и как связать их с Issues?
#
# GitHub Projects — это инструмент для организации и управления задачами в репозиториях. Он позволяет создавать доски с задачами, управлять рабочими процессами и отслеживать прогресс проектов
#
# Для связки с  Issues в правой части страницы, под разделом "Projects", выберите проект, к которому хотите добавить это Issue.

# #### 20. Какие сторонние инструменты можно использовать для автоматизации работы с Issues (например, боты, Webhooks)?
#
# GitHub Actions — это мощный инструмент для автоматизации рабочих процессов непосредственно внутри GitHub. С помощью Actions можно автоматизировать множество задач, таких как управление Issues, запуск тестов, деплой и тд.
#
# Probot — фреймворк для создания ботов, который позволяет автоматизировать работу с Issues, например, автоматически назначать исполнителей или добавлять метки.
#
# Mergify — бот для автоматизации процесса слияния Pull Requests и управления Issues, который может автоматически закрывать Issues при слиянии PR.
#
# Webhooks — это механизмы для отправки уведомлений о событиях в вашем репозитории на внешний сервер, который может обработать данные и выполнить автоматизированные действия
#

# #### 21. Как упомянуть другого пользователя в комментарии к Issue?
#
# В комментах @username 

# #### 22. Как запросить дополнительные данные или уточнения у автора Issue?
#
# Упомянуть автора в комментариях и вежливо запросить данные или уточняющие вопросы

# #### 23. Что делать, если Issue неактуально или его нужно объединить с другим?
#
# В неактуальном Issue оставьте комментарий, в котором укажете, что оно будет объединено с другим Issue, добавив ссылку на основное Issue и пояснение, что оно было объединено.
#

# #### 24. Как использовать шаблоны для создания Issues?
#
# Есть 4 видов issues: 
# Bug report  - сообщение об ошибке 
#
# Feature request - запрос новой фичи или улучшения
#
# Question - для всех остальных вопросов
#
# Telegram community - ссылка на группу в тг где вы можете задать вопрос

# #### 25. Что такое Linked Issues, и как создать связь между задачами?
#
# Linked Issues на GitHub — это способ создания связи между двумя или несколькими задачами (Issues), чтобы они были взаимосвязаны или зависели друг от друга. Это полезно для отслеживания связанных проблем, задач или функциональных требований, которые должны быть выполнены в определённой последовательности или в рамках одного процесса разработки.
#
# Для создания связи между задачами в теле issue добавьте комментарий с ссылкой на issue

# #### 26. Какие метрики (например, время выполнения) можно отслеживать с помощью Issues?
#
# Время выполнения задачи
#
# Время ответа
#
# Время решения
#
# Количество открытых и закрытых Issues
#
# Процент выполнения
#
# Частота обновлений 
#
# Количество Issues по типам
#
# Распределение задач между исполнителями (Assignees)
#
# Ожидаемая дата завершения 
#
#

# #### 27. Какие best practices рекомендуются при работе с Issues в команде?
#
# Используйте метки, четко описывайте структуру задачи и детальное описание, присвойте ответственных, ставьте четкие сроки, общайтесь с командой, используйте milestone
