"""Task commits."""

# 1. Опишите своими словами назначение каждого из этих типов коммитов:
# feat, fix, docs, style, refactor, test, build, ci, perf, chore.
#
# коммит feat - при этом коммите разробочик сообщает что добовляеет новый
# функционал  (изменения стиля)
#
# коммит fix - при обнуружение ошибки кода разрабочик исправляет ошибку и
# отправляет коммит это показывает что он исправил - git commit -m "fix: неисправность........."
#
# docs: — указывает, что изменение связано с документацией (README,
# комментарии и т. д.).
# git commit -m "docs: обновлен README"
#
# style – при  изменениния или  форматирования кода и приведение кода к
# стилю PEP8 и линторам  (пробелы, запятые, отступы), не влияющие на
# работу кода.
#
# git commit -m "style: исправлено форматирование кода"
#
# refactor – улучшение структуры кода без изменения поведения.
# Когда использовать refactor?
#
#     Рефакторинг (переписывание) кода для повышения читаемости.
#     Разделение больших функций на более мелкие.
#     Удаление дублирующегося кода.
#     Переименование переменных и функций для большей ясности.
#     Улучшение архитектуры без изменения логики.
#
# git commit -m "refactor: вынесена логика вычислений в отдельную функцию"
#
# Когда использовать test?
#
#     Добавление новых тестов для новых функций или возможностей.
#     Обновление существующих тестов в связи с изменениями в логике программы.
#     Исправление ошибок в тестах (например, если тесты не прошли из-за
# изменений в коде).
#     Удаление устаревших или неактуальных тестов
#
# git commit -m "test: добавлены тесты для функции авторизации"
#
#
# build – изменения, связанные со сборкой проекта (например, зависимости).
# Когда использовать build?
#
#     Добавление, обновление или удаление зависимостей (например,
# в package.json или requirements.txt).
#     Обновление конфигураций сборки (например, Webpack, Gulp).
#     Изменения в процессах деплоя или подготовке кода для релиза.
#     Обновления скриптов сборки и настройки окружения.
#
# git commit -m "build: обновлены зависимости для улучшения сборки"
#
# ci – изменения в настройках CI/CD (например, конфигурация GitHub Actions).
# Когда использовать ci?
#
#     Изменение конфигурации для систем CI/CD (например, GitHub Actions,
# Jenkins, Travis CI).
#     Добавление или обновление скриптов для автоматизации тестов или деплоя.
#     Настройка этапов сборки и тестирования в конфигурационных файлах.
#     Исправление ошибок в пайплайнах CI/CD.
#
# git commit -m "ci: добавлена конфигурация для автоматической сборки на
# GitHub Actions"
#
#
# perf – оптимизация кода для повышения производительности.
#
#  Когда использовать perf?
#
#     Оптимизация алгоритмов для ускорения работы программы.
#     Снижение времени отклика или использования памяти.
#     Изменения, направленные на улучшение быстродействия системы.
#     Использование более эффективных методов или библиотек для
# выполнения задач.
#
# chore – технические изменения, не влияющие на код (обновление конфигураций,
# линтеров).
#
# Когда использовать chore?
#
#     Обновление зависимостей, которые не влияют напрямую на код (например,
# обновление версий линтеров или тестовых библиотек).
#     Изменения в конфигурациях (например, настройка ESLint, Prettier,
# обновление конфигов для сборки).
#     Очистка проекта от неиспользуемых файлов.
#     Обновление документации по настройке проекта.
#
# git commit -m "chore: обновлен конфиг для Prettier"
#

# 2 Пример фиктивного коммита с использованием типа fix для исправления бага в
# функции округления чисел:
#
# git commit -m "fix: исправлено округление чисел для корректного результата"
#
# Это сообщение соответствует стандарту Conventional Commits и четко описывает
# исправление бага, связанного с некорректным округлением чисел.
#
#

# 3 Добавление новой функциональности:
# Допустим, вы реализовали новую функцию generateReport в проекте. Сделайте
# фиктивный коммит с типом feat, отражающий добавление этой функциональности
#
# Пример фиктивного коммита с использованием типа feat для добавления новой
# функции generateReport:
#
# git commit -m "feat: добавлена функция generateReport для создания отчетов"
#

# 4 Модификация формата кода или стилей:
# Представьте, что вы поправили отступы и форматирование во всём проекте,
# не меняя логики кода. Сделайте фиктивный коммит с типом style
#
# Этот коммит отражает изменения, связанные с форматированием кода, без
# изменения его логики, что соответствует стандарту Conventional Commits.

# 5 Документация и тестирование:
#
# Сделайте фиктивный коммит с типом docs, добавляющий или улучшающий
# документацию для вашей новой функции.
# Сделайте фиктивный коммит с типом test, добавляющий тесты для этой же
# функции.
#
# Примеры фиктивных коммитов:
#
#     Документация (docs):git commit -m "docs: добавлена документация для
# функции generateReport"
#
# Тестирование (test):
#
# git commit -m "test: добавлены тесты для функции generateReport"
#
#

#

#

#

#
