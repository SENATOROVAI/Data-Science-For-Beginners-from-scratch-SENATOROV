"""3.3 List expressions."""

# ### Список квадратов
# [number ** 2 for number in range(a, b + 1)]

# ### Список квадратов 2
# [num ** 2 for num in (range(a, b + 1) if a <= b else range(a, b - 1, -1))]

# ### Основы фильтрации
# [number for number in range(a, b + 1) if number % d == 0]

# ### Множество нечетных чисел
# set(number for number in numbers if number % 2 != 0)

# ### Множество всех полных квадратов
# set(number for number in numbers if number == int(number ** 0.5) ** 2)

# ### Длины всех слов
# [len(word) for word in sentence.split()]

# ### Цифровая выжимка
# "".join(symbol for symbol in text if symbol.isdigit())

# ### Аббревиатура
# "".join(word[0].upper() for word in string.split())

# ### Преобразование в строку
# " - ".join(map(str, sorted(set(numbers))))

# ### Огласите список
# [word for word in words.split() if sum(1 for symbol in word if symbol.lower() in "аяуюоёэеиыaeiouy") >= 3]

# ### Выявление уникальности
# set(number for number in numbers if numbers.count(number) == 1)

# ### Максимальное произведение
# max(first * second for first in numbers for second in numbers if first != second)

# ### Словарный минимум
# min(sorted(data.items()), key=lambda x: sum(x[1]))[0]

# ### Поиск ошибок
# set(word for word, numbers in data.items() if len(numbers) != len(set(numbers)))

# ### Буквенная статистика
# {symbol: text.lower().count(symbol) for symbol in text.lower() if symbol.isalpha()}

# ### RLE наоборот
# "".join(symbol * count for symbol, count in rle)

# ### Таблица умножения 2.0
# [[n1 * n2 for n2 in range(1, n + 1)] for n1 in range(1, n + 1)]

# ### Делители
# {number: [d for d in range(1, number + 1) if number % d == 0] for number in numbers}

# ### Простое множество
# set(number for number in numbers if sum(1 for d in range(1, number + 1) if number % d == 0) == 2)

# ### Обобщение
# text = 'ехали медведи на велосипеде'
# {tuple(sorted((w1, w2))) for w1 in text.split() for w2 in text.split() if w1 < w2 and len(set(w1) & set(w2)) > 2}
