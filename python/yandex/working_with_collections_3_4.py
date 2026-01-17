"""Встроенные возможности по работе с коллекциями.

В этом параграфе вы познакомитесь с расширенными возможностями Python для работы с
коллекциями. Вы научитесь использовать библиотеку itertools, чтобы эффективно обрабатывать
и комбинировать данные, даже если они приходят из разных источников. Разберётесь, как
создавать бесконечные итераторы, объединять и фильтровать коллекции, а также применять
функции enumerate() и zip() в практических задачах. Эти инструменты помогут писать более
компактный и читаемый код.
"""

# ## Автоматизация списка.
#
# - Эти задачи направлены на отработку применения встроенных инструментов Python для генерации, комбинирования и обработки коллекций.
# - Начнем с первой задачи. Не забывайте делать перерывы, если устали. Однако обязательно возвращайтесь к решению!
# - В жизни часто приходится составлять списки: продуктов, задач на день, дел.
# - Давайте автоматизируем это с помощью Python!
# - Напишите программу, которая превращает строку слов в нумерованный список — по одному элементу на строку.
# - Формат ввода
# - Вводится одна строка.
# - Формат вывода
# - Требуется вывести нумерованный список, составленный из её слов.

# +
import re
import sys
from collections.abc import Mapping
from itertools import (
    accumulate,
    chain,
    combinations,
    cycle,
    islice,
    permutations,
    product,
)

text_auto: str = input()
text_list: list[str] = text_auto.split()
for index, word_auto in enumerate(text_list, 1):
    print(f"{index}. {word_auto}")
# -

# ## Сборы на прогулку.
#
# - Воспитатель в детском саду устал тратить время, чтобы построить детей по парам. Он договорился с детьми, чтобы те делились на две, по возможности равные, группы.
# - Напишите программу, которая по списку двух шеренг составляет пары детей.
# - Формат ввода
# - Вводится две строки с именами детей, записанными через запятую и пробел.
# - Формат вывода
# - Требуется вывести список пар, которые можно составить, если последовательно брать из каждой шеренги по одному ребёнку.
# - Имена в парах выводить через дефис окружённый пробелами.
# - Примечание
# - В одной из групп может быть на одного ребенка больше, чем в другой.
# - Этот ребёнок при формировании пар не учитывается и идёт в паре с воспитателем.

group_1: str = input()
group_2: str = input()
group_list_1: list[str] = [name.strip() for name in group_1.split(",")]
group_list_2: list[str] = [name.strip() for name in group_2.split(",")]
for child_1, child_2 in zip(group_list_1, group_list_2):
    print(f"{child_1} - {child_2}")

# ## Рациональная считалочка.
#
# - Теперь потренируемся использовать бесконечные итераторы.
# - Напишите программу, которая выводит последовательность чисел по заданным параметрам — началу, концу и шагу.
# - Формат ввода
# - В одну строку через пробел вводятся 3 рациональных числа — начало счета, конец и шаг.
# - Формат вывода
# - Последовательность чисел с заданными параметрами.

# +
input_str: str = input()
values: list[str] = input_str.split()

start_count: float = float(values[0])
end_count: float = float(values[1])
step: float = float(values[2])

current: float = start_count
while current <= end_count:
    print(round(current, 2))
    current += step
# -

# ## Словарная ёлка.
#
# - Попробуем применить итератор к строкам, а не к числам.
# - Напишите программу, которая превращает строку слов в «ёлку» — с каждой строкой список становится длиннее.
# - Формат ввода
# - В одну строку через пробел вводятся слова разделенные пробелом.
# - Формат вывода
# - Несколько строк. В каждой следующей строке на одно слово больше.

text: list[str] = input().split()
for value in accumulate(text, lambda x, y: f"{x} {y}"):
    print(value)

# ## Список покупок.
#
# - Поход в магазин часто вызывает проблемы. Если не подготовить список, можно уйти за хлебом, а вернуться с десятком пакетов.
# - Напишите программу, которая собирает пожелания семьи (мамы, папы и дочки) в единый список и приводит его в порядок.
# - Формат ввода
# - В трёх строках записаны желаемые продукты (через запятую и пробел).
# - Формат вывода
# - Отсортированный по алфавиту список продуктов с нумерацией.
# - Примечание
# - Помните, что итераторы можно применять к другим итераторам.

# +
lines: list[str] = []
for _ in range(3):
    line: str = input().strip()
    lines.append(line)

lists_of_products: list[list[str]] = []
for line in lines:
    products: list[str] = [product.strip() for product in line.split(",")]
    lists_of_products.append(products)

all_products: list[str] = list(chain.from_iterable(lists_of_products))
all_products.sort()

for index, product_by in enumerate(all_products, 1):
    print(f"{index}. {product_by}")
# -

# ## Колода карт.
#
# - Пора сыграть в карты — но без одной из мастей. Сгенерируйте колоду игральных карт (от двойки до туза), исключив масть, которую вводит пользователь.
# - Формат ввода
# - Название масти, которая должна быть выброшена, передаётся в том же падеже, в котором она выводится на экран: «пик», «треф», «бубен» и «червей».
# - Формат вывода
# - Список карт в колоде по увеличению номинала, затем масти (как в преферансе).

exclude_suit: str = input()
suits: list[str] = ["пик", "треф", "бубен", "червей"]
weights: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
suits.remove(exclude_suit)
deck: list[tuple[str, str]] = list(product(weights, suits))
deck.sort(key=lambda card: (weights.index(card[0]), suits.index(card[1])))
for card in deck:
    print(f"{card[0]} {card[1]}")

# ## Игровая сетка.
#
# - Ребята в классе решили устроить чемпионат по шашкам по принципу «каждый с каждым».
# - Напишите программу, которая составляет список всех возможных игр между учениками.
# - Формат ввода
# - В первой строке записано число учеников (N).
# - В каждой из последующих N строк записано одно имя.
# - Формат вывода
# - Список игр в формате:
# - <Игрок 1> - <Игрок 2>
# - Порядок игр не имеет значения.

pop: list[str] = []
numb: int = int(input())
for _ in range(numb):
    name: str = input()
    pop.append(name)
for pair in combinations(pop, 2):
    print(f"{pair[0]} - {pair[1]}")

# ## Меню питания 2.0.
#
# - В детском саду ежедневно подают новую кашу на завтрак.
# - Напишите программу, которая строит расписание каш на ближайшие дни на основе заданного меню.
# - Формат ввода
# - Вводится натуральное число M — количество каш в меню.
# - В каждой из последующих M строк записано одно название каши.
# - В конце передается натуральное число N — количество дней.
# - Формат вывода
# - Вывести список каш в порядке подачи.

count_porridge: int = int(input())
porridges: list[str] = []
for _ in range(count_porridge):
    porridge: str = input().strip()
    porridges.append(porridge)
count_day: int = int(input())
infinite_menu = cycle(porridges)
schedule: list[str] = list(islice(infinite_menu, count_day))
for porrige in schedule:
    print(porrige)

# ## Таблица умножения 3.0.
#
# - Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
# - Давайте поможем производителю.
# - Напишите программу, которая выводит таблицу умножения размером N×N — построчно, по одному ряду на строку.
# - Формат ввода
# - Вводится одно натуральное число — требуемый размер таблицы.
# - Формат вывода
# - Таблица умножения заданного размера.

numb_tab: int = int(input())
for i_tab, j_tab in product(range(1, numb_tab + 1), repeat=2):
    print(i_tab * j_tab, end=" " if j_tab < numb_tab else "\n")

# ## Мы делили апельсин 2.0.
#
# - Аня, Боря и Вова решили съесть апельсин. Подскажите ребятам, как им его разделить.
# - Разработайте программу, которая выводит все возможные способы разделить заданное количество долек апельсина между тремя детьми так, чтобы каждому досталось хотя бы по одной, и ничего не осталось.
# - Формат ввода
# - В единственной строке записано количество долек апельсина (N).
# - Формат вывода
# - Таблица вариантов разделения апельсина.
# - Примечания
# - Каждому ребёнку должна достаться хотя бы одна долька апельсина.
# - Ни одной дольки не должно остаться.
# - Выводить варианты в порядке увеличения количества долек у Ани, следом Бори и затем Вовы.

numb_div: int = int(input())
print("А Б В")
for anna in range(1, numb_div - 1):
    for borya in range(1, numb_div - anna):
        vova: int = numb_div - anna - borya
        if vova >= 1:
            print(f"{anna} {borya} {vova}")

# ## Числовой прямоугольник 3.0.
#
# - Ребята в детском саду вновь учатся считать, и воспитательница решила сделать так, чтобы им было проще освоить новый навык.
# - Для этого она хочет оформить список изучаемых чисел особым образом.
# - Дети справляются весьма быстро, поэтому ей требуется программа, которая способна строить числовые прямоугольники.
# - Напишите программу, которая строит числовой прямоугольник заданного размера, заполняя его числами по строкам.
# - Все столбцы должны быть одинаковой ширины — так прямоугольник будет выглядеть аккуратно.
# - Формат ввода
# - В первой строке записано число N — высота числового прямоугольника.
# - Во второй строке указано число M — ширина числового прямоугольника.
# - Формат вывода
# - Нужно вывести сформированный числовой прямоугольник требуемого размера.
# - Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.

height: int = int(input())
width: int = int(input())
total_numbers: int = height * width
max_width: int = len(str(total_numbers))
for i in range(height):
    start: int = i * width + 1
    end: int = start + width
    row: list[str] = [f"{num:>{max_width}}" for num in range(start, end)]
    print(" ".join(row))

# ## Список покупок 2.0.
#
# - Давайте вновь поможем человеку с покупками.
# - Разработайте программу, которая объединяет пожелания семьи в один аккуратный список продуктов.
# - Соберите все элементы в общий список, отсортируйте его по алфавиту и пронумеруйте.
# - Формат ввода
# - В первой строке задано натуральное число N — количество членов семьи. В следующих N строках записаны желаемые продукты (через запятую и пробел).
# - Формат вывода
# - Отсортированный по алфавиту список продуктов с нумерацией.

numb_l: int = int(input())
lines_l: list[str] = []
for _ in range(numb_l):
    line_l: str = input().strip()
    lines_l.append(line_l)
lists_of_products_2: list[list[str]] = []
for line_l in lines_l:
    products_: list[str] = [product.strip() for product in line_l.split(",")]
    lists_of_products_2.append(products_)
all_products_: list[str] = list(chain.from_iterable(lists_of_products_2))
all_products_.sort()
for index, product_ in enumerate(all_products_, 1):
    print(f"{index}. {product_}")

# ## Расстановка спортсменов.
#
# - Расстановка спортсменов на старте — дело несложное, если знать, как подойти к задаче.
# - Напишите программу, которая выводит все возможные расстановки участников, учитывая их имена.
# - Формат ввода
# - В первой строке задано натуральное число N — количество спортсменов. В следующих N строках записаны имена спортсменов.
# - Формат вывода
# - Отсортированный по алфавиту список расстановок.
# - Имена в каждой строке выводить через запятую и пробел.

numb_sp: int = int(input())
names_sp: list[str] = []
for _ in range(numb_sp):
    name_sp: str = input().strip()
    names_sp.append(name_sp)
all_permutations: list[tuple[str, ...]] = list(permutations(names_sp))
sorted_permutations: list[tuple[str, ...]] = sorted(all_permutations)
for perm in sorted_permutations:
    print(", ".join(perm))

# - Хорошо, спортсмены расставлены на старте. Вот только угадать финалистов практически невозможно.
# - Давайте напишем программу, которая выводит список возможных победителей — всех, кто может оказаться в числе призёров при любом раскладе.
# - Формат ввода
# - В первой строке задано натуральное число N — количество спортсменов.
# - В следующих N строках записаны имена спортсменов.
# - Формат вывода
# - Отсортированный по алфавиту список вариантов.
# - Имена в каждой строке выводить через запятую и пробел.

numb_sport: int = int(input())
names_sport: list[str] = []
for _ in range(numb_sport):
    name_sport: str = input().strip()
    names_sport.append(name_sport)
all_permutations_: list[tuple[str, ...]] = list(permutations(names_sport))
sorted_permutations_: list[tuple[str, ...]] = sorted(all_permutations_)
for perm in sorted_permutations_:
    print(", ".join(perm))

# ## Список покупок 3.0.
#
# - В этот раз семья договорилась, что в целях экономии они будут совершать в день только три покупки.
# - Напишите программу, которая готовит все возможные варианты списков таких покупок.
# - Формат ввода
# - В первой строке задано натуральное число N — количество членов семьи. В следующих N строках записаны желаемые продукты (через запятую и пробел).
# - Формат вывода
# - Варианты списков покупок в алфавитном порядке.

numb_list: int = int(input())
lines_list: list[str] = []
for _ in range(numb_list):
    line_list: str = input().strip()
    lines_list.append(line_list)
lists_of_products_ls: list[list[str]] = []
for line_ls in lines_list:
    products_ls: list[str] = [product.strip() for product in line_ls.split(",")]
    lists_of_products_ls.append(products_ls)
all_products_ls: list[str] = list(chain.from_iterable(lists_of_products_ls))
all_products_ls.sort()
for product_3 in permutations(all_products_ls, 3):
    prroduct_str: str = " ".join(product_3)
    print(prroduct_str)

# ## Расклад таков...
#
# - Можно налить себе чай перед следующей задачей — и снова в бой! Виталий любит играть в карты. Он решил выяснить, какие есть вариации вытащить из колоды определённые тройки карт. Напишите программу, которая выводит список подходящих троек в лексикографическом порядке с учётом заданных условий.
# - Формат ввода
# - В первой строке записана масть, которая должна присутствовать в тройке.
# - Во второй строке записан достоинство, которого не должно быть в тройке.
# - Формат вывода
# - Выведите на экран первые 10 получившихся троек.
# - Карты в каждой комбинации должны быть отсортированы лексикографически (по строке названия карты). Карты комбинации выводятся через запятую с пробелом после неё.
# - Комбинации между собой также должны быть отсортированы в лексикографическом порядке по строке, представляющей комбинацию целиком.
# - Примечание
# - Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше, чем «2 ...», а бубны младше, чем пики.
# - Масти в именительном и родительном падежах:

required_suit: str = input().strip()
excluded_weight: str = input().strip()
suit_cases: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
suits_: list[str] = ["пик", "треф", "бубен", "червей"]
weights_: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
if required_suit in suit_cases:
    required_suit_genitive: str = suit_cases[required_suit]
else:
    required_suit_genitive = required_suit
deck_: list[str] = []
for weight in weights_:
    for suit in suits_:
        card_: str = f"{weight} {suit}"
        deck_.append(card_)
deck_.sort()
count: int = 0
for combo in combinations(deck_, 3):
    cards: list[str] = list(combo)
    has_required_suit: bool = any(required_suit_genitive in card_ for card_ in cards)
    has_excluded_weight: bool = any(f"{excluded_weight}" in card_ for card_ in cards)
    if has_required_suit and not has_excluded_weight:
        cards_sorted: list[str] = sorted(cards)
        print(", ".join(cards_sorted))
        count += 1
        if count >= 10:
            break

# ## А есть ещё варианты?
#
# - Давайте вновь поможем Виталию — теперь его интересует, какой вариант расклада идёт сразу после уже полученного.
# - Напишите программу, которая находит следующий подходящий вариант тройки карт, соответствующий условиям.
# - Формат ввода
# - В первой строке записана масть, которая должна присутствовать в тройке.
# - Во второй строке записан достоинство, которого не должно быть в тройке.
# - В третьей строке записан предыдущий вариант полученный Виталием.
# - Формат вывода
# - Выведите следующий вариант расклада.
# - Примечание
# - Обратите внимание: валет-дама-король-туз лексикографически упорядочены. Но «10 ...» лексикографически младше, чем «2 ...», а бубны младше, чем пики.

required_suit_: str = input().strip()
excluded_weight_: str = input().strip()
previous_combo_str: str = input().strip()
suit_cases_: dict[str, str] = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
required_suit_genitive_: str = suit_cases_.get(required_suit_, required_suit_)
suits_2: list[str] = ["пик", "треф", "бубен", "червей"]
weights_2: list[str] = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "валет",
    "дама",
    "король",
    "туз",
]
deck_2: list[str] = [f"{w} {s}" for w in weights_2 for s in suits_2]
deck_2.sort()
prev_csrds: list[str] = sorted(previous_combo_str.split(", "))
found: bool = False
for combo in combinations(deck_2, 3):
    cards_2: list[str] = sorted(combo)
    has_suit: bool = any(required_suit_genitive_ in card for card in cards_2)
    no_excluded: bool = not any(
        card.startswith(excluded_weight_ + " ") for card in cards_2
    )
    if has_suit and no_excluded:
        if found:
            print(", ".join(cards_2))
            break
        if cards_2 == prev_csrds:
            found = True

# ## Таблица истинности.
#
# - Вся современная электронно-вычислительная техника строится на Булевой алгебре, которая оперирует истинностью и ложностью высказываний (в Python это and, or, not).
# - Разработайте программу, которая для введённого логического выражения от переменных a, b, c строит таблицу истинности — то есть перебирает все возможные комбинации значений и вычисляет результат.
# - Формат ввода
# - Вводится логическое выражение от трех переменных (a, b, c) валидное для языка Python.
# - Формат вывода
# - Выведите таблицу истинности данного выражения.

exp: str = input().strip()
print("a b c f")
for a_t, b_t, c_t in product([0, 1], repeat=3):
    result_table: bool = eval(  # pylint: disable=eval-used
        exp, {"a": a_t, "b": b_t, "c": c_t}
    )
    result_int_: int = 1 if result_table else 0
    print(f"{a_t} {b_t} {c_t} {result_int_}")

# ## Таблица истинности 2.
#
# - Продолжим работу с таблицами истинности.
# - Теперь выражения могут содержать переменное количество переменных, обозначенных заглавными латинскими буквами.
# - Напишите программу, которая строит таблицу истинности для заданного логического выражения.
# - Формат ввода
# - Вводится логическое выражение от нескольких переменных валидное для языка Python. Все переменные заданы заглавными латинскими буквами.
# - Формат вывода
# - Выведите таблицу истинности данного выражения

# +
expression: str = input().strip()
variables_: list[str] = sorted(set(re.findall(r"[A-Z]", expression)))

if not variables_:
    print("F")
    print("1" if eval(expression) else "0")  # pylint: disable=eval-used
    sys.exit()

header: str = " ".join(variables_) + " F"
print(header)

for combination in product([0, 1], repeat=len(variables_)):
    var_dict: dict[str, int] = dict(zip(variables_, combination))
    try:
        result: bool = eval(expression, var_dict)  # pylint: disable=eval-used
        result_value: str = "1" if result else "0"
    except ValueError:
        result_value = "E"
    values_str: str = " ".join(str(v) for v in combination)
    print(f"{values_str} {result_value}")
# -

# ## Таблица истинности 3.
#
# - На этот раз придётся справиться с выражением, в котором встречаются нестандартные логические операции: импликация, строгая дизъюнкция и эквивалентность. Они не поддерживаются в Python напрямую, но вы сможете реализовать их самостоятельно.
# - Напишите программу, которая для заданного логического выражения строит таблицу истинности, включая поддержку следующих операций:
# - -> — импликация
# - ^ — строгая дизъюнкция
# - ~ — эквивалентность
# - Формат ввода
# - Вводится логическое выражение от нескольких переменных.
# - Возможное содержание выражения:
# - Заглавная латинская буква — переменная;
# - not — отрицание;
# - and — конъюнкция;
# - or — дизъюнкция;
# - ^ — строгая дизъюнкция;
# - -> — импликация;
# - ~ — эквивалентность;
# - () — логические скобки.
# - Формат вывода
# - Выведите таблицу истинности данного выражения.

# +
OPERATORS: dict[str, str] = {
    "not": "not",
    "and": "and",
    "or": "or",
    "^": "!=",
    "->": "<=",
    "~": "==",
}
PRIORITY: dict[str, int] = {
    "not": 0,
    "and": 1,
    "or": 2,
    "^": 3,
    "->": 4,
    "~": 5,
    "(": 6,
}


def parse_expression(expr: str, variables: list[str]) -> list[str]:
    """parse_expression."""
    stack: list[str] = []
    result_9: list[str] = []
    expr = expr.replace("(", "( ").replace(")", " )")
    for token in expr.split():
        if token in variables:
            result_9.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                result_9.append(OPERATORS[stack.pop()])
            stack.pop()
        elif token in OPERATORS:
            while stack and PRIORITY[token] >= PRIORITY.get(stack[-1], 100):
                result_9.append(OPERATORS[stack.pop()])
            stack.append(token)
    while stack:
        result_9.append(OPERATORS[stack.pop()])
    return result_9


def evaluate(rpn_expr: list[str], v_dict: Mapping[str, int | bool]) -> int:
    """evaluate."""
    stack: list[int | bool] = []
    for token in rpn_expr:
        if token in v_dict:
            stack.append(v_dict[token])
        elif token == "not":
            operand = stack.pop()
            stack.append(not operand)
        else:
            rhs = stack.pop()
            lhs = stack.pop()
            if token == "and":
                result_ev = lhs and rhs
            elif token == "or":
                result_ev = lhs or rhs
            elif token == "!=":
                result_ev = lhs != rhs
            elif token == "<=":
                result_ev = (not lhs) or rhs  # implication
            elif token == "==":
                result_ev = lhs == rhs
            else:
                raise ValueError(f"Unknown operator: {token}")
            stack.append(result_ev)
    return int(stack.pop())


log_expr: str = input().strip()
vars_in_expr: list[str] = sorted({ch for ch in log_expr if ch.isupper()})
rpn: list[str] = parse_expression(log_expr, vars_in_expr)
print(*vars_in_expr, "F")
for bool_values in product([0, 1], repeat=len(vars_in_expr)):
    value_pairs = zip(vars_in_expr, (bool(v) for v in bool_values))
    val_map: dict[str, bool] = dict(value_pairs)
    result_10: int = evaluate(rpn, val_map)
    print(*bool_values, result_10)
