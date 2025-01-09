"""set_theory_basics."""

# # Теория множеств
# # Конспект по книге "Элементарный курс теории вероятностей" до стр. 29
#
# """
# # 1. Множества выборочного пространства
#
# ## Основные определения:
#
# - Множество - математическая структура, представляющая собой совокупность различных объектов,
#   рассматриваемых как единое целое. Важно: элементы не могут повторяться!
#   Пример: множество студентов в классе, множество целых чисел.
#
# - Выборочное пространство (Ω) - полная совокупность всех возможных элементарных исходов
#   рассматриваемого эксперимента или явления.
#   Пример: при бросании монеты Ω = {орел, решка}
#
# - Точка выборочного пространства (ω) - отдельный элементарный исход или элемент множества.
#   Пример: при бросании кубика ω может быть числом от 1 до 6
#
# - Размер множества |S| - количество элементов (точек) в множестве. Может быть конечным или бесконечным.
#   Пример: |{1,2,3}| = 3
#
# - Пустое множество ∅ - множество, не содержащее ни одного элемента. |∅| = 0
#
# ## Обозначения и их смысл:
#
# - ω ∈ S - элемент ω является членом (принадлежит) множества S
# - ω ∉ S - элемент ω не является членом (не принадлежит) множества S
# - A ⊂ B - все элементы множества A содержатся в множестве B (включение)
# - A = B - множества A и B состоят в точности из одних и тех же элементов (равенство множеств)
#
# # 2. Операции над множествами
#
# ## Основные операции:
#
# 1. Дополнение (Ac) - множество всех элементов пространства Ω, не входящих в A
#    Пример: если Ω = {1,2,3,4,5} и A = {1,2}, то Ac = {3,4,5}
#
# 2. Объединение (A ∪ B) - множество элементов, принадлежащих хотя бы одному из множеств A или B
#    Пример: {1,2} ∪ {2,3} = {1,2,3}
#
# 3. Пересечение (A ∩ B) - множество элементов, принадлежащих одновременно обоим множествам
#    Пример: {1,2,3} ∩ {2,3,4} = {2,3}
#
# 4. Разность (A \ B) - множество элементов, принадлежащих A, но не принадлежащих B
#    Пример: {1,2,3} \ {2,3} = {1}
#
# 5. Симметрическая разность (A △ B) - элементы, принадлежащие только одному из множеств
#    Пример: {1,2,3} △ {2,3,4} = {1,4}
#
# ## Основные законы и их интерпретация:
#
# 1. Коммутативные законы - порядок множеств не важен:
#    - A ∪ B = B ∪ A
#    - A ∩ B = B ∩ A
#
# 2. Ассоциативные законы - порядок выполнения операций не важен:
#    - (A ∪ B) ∪ C = A ∪ (B ∪ C)
#    - (A ∩ B) ∩ C = A ∩ (B ∩ C)
#
# 3. Дистрибутивные законы - правила раскрытия скобок:
#    - (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C)
#    - (A ∩ B) ∪ C = (A ∪ C) ∩ (B ∪ C)
#
# 4. Законы де Моргана - правила для дополнений:
#    - (A ∪ B)c = Ac ∩ Bc  # дополнение объединения есть пересечение дополнений
#    - (A ∩ B)c = Ac ∪ Bc  # дополнение пересечения есть объединение дополнений
#
# # 3. Индикаторы множеств
#
# ## Определение:
# Индикатор (характеристическая функция) множества A - это функция IA(ω), которая:
# IA(ω) = 1, если ω ∈ A  (элемент принадлежит множеству)
# IA(ω) = 0, если ω ∉ A  (элемент не принадлежит множеству)
#
# ## Основные свойства индикаторов:
#
# 1. IA∩B = IA ∧ IB = IA · IB
#    # индикатор пересечения равен минимуму или произведению индикаторов
#
# 2. IA∪B = IA ∨ IB
#    # индикатор объединения равен максимуму индикаторов
#
# 3. IAc = 1 - IA
#    # индикатор дополнения
#
# 4. IA+B = IA + IB (если A ∩ B = ∅)
#    # для непересекающихся множеств индикатор суммы равен сумме индикаторов
#
# 5. IA△B = IA + IB (по модулю 2)
#    # индикатор симметрической разности
# """
