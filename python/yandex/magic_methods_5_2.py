"""Волшебные методы, переопределение методов. Наследование.

В этом параграфе вы познакомитесь с принципами наследования в Python и научитесь строить
производные классы на основе уже существующих. Вы разберётесь, как расширять и
переопределять методы базовых классов, а также узнаете, что такое множественное
наследование и как Python обрабатывает конфликты между родительскими классами.
"""

# ## Классная точка 3.0.
#
# - Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0» (предыдущий параграф).
# - Создайте класс PatchedPoint — наследника уже написанного вами Point.
# - Требуется реализовать следующие виды инициализации нового класса:
# - параметров не передано — координаты точки равны 0;
# - передан один параметр — кортеж с координатами точки;
# - передано два параметра — координаты точки.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.

# +
# pylint: disable=C0302
# fmt: off
from math import sqrt
from typing import Union

# fmt: on


class Point:
    """Точка в двумерном пространстве."""

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Инициализирует точку с координатами x и y.

        Args:
            x_coord: Координата X
            y_coord: Координата Y
        """
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, x_coord: int, y_coord: int) -> None:
        """Перемещает точку на dx, dy."""
        self.x_coord += x_coord
        self.y_coord += y_coord

    def length(self, point: "Point") -> float:
        """Вычисляет расстояние до другой точки."""
        x_diff = self.x_coord - point.x_coord
        y_diff = self.y_coord - point.y_coord
        return round(
            sqrt(x_diff**2 + y_diff**2),
            2,
        )


# fmt: off

class PatchedPoint(Point):
    """Улучшенная точка с гибкой инициализацией."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Инициализирует точку различными способами.

        Args:
            *args: Может быть пустым, кортежем (x,y) или двумя числами x,y
        """
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and isinstance(args[0], tuple):
            x_coord, y_coord = args[0]
            super().__init__(x_coord, y_coord)

        elif (len(args) == 2  # noqa: W503
              and isinstance(args[0], int)  # noqa: W503 
              and isinstance(args[1], int)):  # noqa: W503

            super().__init__(args[0], args[1])
# fmt: on


# -

# ## Классная точка 4.0.
#
# - А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str_ и _repr_.
# - При преобразовании в строку точка представляется в формате (x, y).
# - Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.

# fmt: off
class PatchedPointV2(Point):
    """Улучшенная точка с гибкой инициализацией."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Инициализирует точку различными способами.

        Args:
            *args: Может быть пустым, кортежем (x,y) или двумя числами x,y
        """
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and isinstance(args[0], tuple):
            x_coord, y_coord = args[0]
            super().__init__(x_coord, y_coord)
        elif (len(args) == 2  # noqa: W503
              and isinstance(args[0], int)  # noqa: W503 
              and isinstance(args[1], int)):  # noqa: W503

            super().__init__(args[0], args[1])

    def __str__(self) -> str:
        """Возвращает строковое представление точки."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление точки."""
        return f"PatchedPoint({self.x_coord}, {self.y_coord})"
# fmt: on


# ## Классная точка 5.0.
#
# - Согласитесь, что использовать операторы куда удобнее, чем обыкновенные методы. Давайте вспомним о реализованном нами методе move(x, y) и напишем ему альтернативу в виде операторов + и +=.
# - При выполнении кода point + (x, y), создаётся новая точка, которая отличается от изначальной на заданное кортежем расстояние по осям 
# x и y. При выполнении кода point += (x, y) производится перемещение изначальной точки. Напомним, что сейчас мы модернизируем только класс PatchedPoint.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.

# fmt: off
class PatchedPointV3(Point):
    """Улучшенная точка с гибкой инициализацией."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Инициализирует точку различными способами.

        Args:
            *args: Может быть пустым, кортежем (x,y) или двумя числами x,y
        """
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1 and isinstance(args[0], tuple):
            x_coord, y_coord = args[0]
            super().__init__(x_coord, y_coord)
        elif (len(args) == 2  # noqa: W503
              and isinstance(args[0], int)  # noqa: W503 
              and isinstance(args[1], int)):  # noqa: W503

            super().__init__(args[0], args[1])

    def __str__(self) -> str:
        """Возвращает строковое представление точки."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление точки."""
        return f"PatchedPoint({self.x_coord}, {self.y_coord})"

    def __add__(
        self, other: Union["PatchedPointV3", tuple[int, int]]
    ) -> "PatchedPointV3":
        """Добавляет координаты другой точки или кортежа к этой точке."""
        if isinstance(other, tuple):
            x_coord, y_coord = other
        else:
            x_coord, y_coord = other.x_coord, other.y_coord
        return PatchedPointV3(self.x_coord + x_coord, self.y_coord + y_coord)

    def __iadd__(
        self, other: Union["PatchedPointV3", tuple[int, int]]
    ) -> "PatchedPointV3":
        """Добавляет координаты другой точки или кортежа на месте."""
        if isinstance(other, tuple):
            x_coord, y_coord = other
        else:
            x_coord, y_coord = other.x_coord, other.y_coord
        self.move(x_coord, y_coord)
        return self
# fmt: on


# ## Дроби v0.1.
#
# - Возможно, вы уже заметили, что дробные числа (float) недостаточно точные для некоторых задач. Для более точных математических расчётов иногда прибегают к созданию правильных рациональных дробей, описываемых числителем и знаменателем.
# - Начнём разработку класса Fraction, который реализует предлагаемые дроби.
# - Предусмотрите возможность инициализации дроби с помощью двух целых чисел или строки в формате <числитель>/<знаменатель>.
# - В случаях наличия общего делителя у числителя и знаменателя, дробь следует сократить.
# - А также реализуйте методы:
# - numerator() — возвращает абсолютное значение числителя;
# - numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
# - denominator() – возвращает абсолютное значение знаменателя;
# - denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
# - __str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
# - __repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все числа в данной задаче будут положительными.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV1:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            self.num, self.den = self.__simplify((value, self.den))
        return self.num

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            self.num, self.den = self.__simplify((self.num, value))
        return self.den

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction({self.num}, {self.den})"


# ## Дроби v0.2.
#
# - Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# - Предусмотрите возможность задать отрицательные числитель и/или знаменатель. А также перепишите методы __str__ и __repr__ таким образом, чтобы информация об объекте согласовывалась с инициализацией строкой.
# - Далее реализуйте оператор математического отрицания — унарный минус.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV2:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV2":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV2(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"


# ## Дроби v0.3.
#
# - Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# - Реализуйте бинарные операторы:
# - + — сложение дробей, создаёт новую дробь;
# - - — вычитание дробей, создаёт новую дробь;
# - += — сложение дробей, изменяет дробь, переданную слева;
# - -= — вычитание дробей, изменяет дробь, переданную слева.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV8:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV8":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV8(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV8") -> "FractionV8":
        """Реализует оператор сложения (+)."""
        return FractionV8(
            self.num * other.den + other.num * self.den, self.den * other.den
        )

    def __iadd__(self, other: "FractionV8") -> "FractionV8":
        """Реализует оператор сложения с присваиванием (+=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.den + other.num * self.den, self.den * other.den)
        )
        return self

    def __sub__(self, other: "FractionV8") -> "FractionV8":
        """Реализует оператор вычитания (-)."""
        return FractionV8(
            self.num * other.den - other.num * self.den, self.den * other.den
        )

    def __isub__(self, other: "FractionV8") -> "FractionV8":
        """Реализует оператор вычитания с присваиванием (-=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.den - other.num * self.den, self.den * other.den)
        )
        return self


# ## Дроби v0.4.
#
# - Продолжим разработку класса Fraction, который реализует предлагаемые дроби.
# - Реализуйте бинарные операторы:
# - * — умножение дробей, создаёт новую дробь;
# - / — деление дробей, создаёт новую дробь;
# - *= — умножение дробей, изменяет дробь, переданную слева;
# - /= — деление дробей, изменяет дробь, переданную слева.
# - Также разработайте метод reverse, возвращающий дробь обратную данной.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV4:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV4":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV4(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор сложения (+)."""
        return FractionV4(
            self.num * other.den + other.num * self.den, self.den * other.den
        )

    def __iadd__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор сложения с присваиванием (+=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.den + other.num * self.den, self.den * other.den)
        )
        return self

    def __sub__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор вычитания (-)."""
        return FractionV4(
            self.num * other.den - other.num * self.den, self.den * other.den
        )

    def __isub__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор вычитания с присваиванием (-=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.den - other.num * self.den, self.den * other.den)
        )
        return self

    def __mul__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор умножения (*)."""
        return FractionV4(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор умножения с присваиванием (*=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den)
        )
        return self

    def __truediv__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор деления (/)."""
        return FractionV4(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: "FractionV4") -> "FractionV4":
        """Реализует оператор деления с присваиванием (/=)."""
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num)
        )
        return self

    def reverse(self) -> "FractionV4":
        """Переворачивает дробь, меняя числитель и знаменатель местами."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self


# ## Дроби v0.5.
#
# - Следующим этапом разработки будет реализация методов сравнения: >, <, >=, <=, ==, !=.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV5:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV5":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV5(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор сложения (+)."""
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV5(num, den)

    def __iadd__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор сложения с присваиванием (+=)."""
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор вычитания (-)."""
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV5(num, den)

    def __isub__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор вычитания с присваиванием (-=)."""
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор умножения (*)."""
        return FractionV5(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор умножения с присваиванием (*=)."""
        num = self.num * other.num
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __truediv__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор деления (/)."""
        return FractionV5(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: "FractionV5") -> "FractionV5":
        """Реализует оператор деления с присваиванием (/=)."""
        num = self.num * other.den
        den = self.den * other.num
        self.num, self.den = self.__simplify((num, den))
        return self

    def reverse(self) -> "FractionV5":
        """Переворачивает дробь, меняя числитель и знаменатель местами."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: "FractionV5") -> bool:
        """Реализует оператор больше (>)."""
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: "FractionV5") -> bool:
        """Реализует оператор больше или равно (>=)."""
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: "FractionV5") -> bool:
        """Реализует оператор меньше (<)."""
        return self.num / self.den < other.num / other.den

    def __le__(self, other: "FractionV5") -> bool:
        """Реализует оператор меньше или равно (<=)."""
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Реализует оператор равенства (==)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Реализует оператор неравенства (!=)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den


# ## Дроби v0.6.
#
# - Надо было, наверное, раньше об этом подумать...
# - Эти слова так и срываются с губ при разработке какого-либо программного обеспечения.
# - Все же понимают, что целые числа тоже являются дробями?! Следовательно, нам требуется изменить систему инициализации, чтобы она могла воспринимать и целые числа (причём и в виде строк). Ну и естественно, требуется переработать операторы арифметических действий и сравнения.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV6:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        if len(values) == 1:
            values += (1,)
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV6":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV6(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор сложения (+)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV6(num, den)

    def __iadd__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор сложения с присваиванием (+=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор вычитания (-)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV6(num, den)

    def __isub__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор вычитания с присваиванием (-=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор умножения (*)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return FractionV6(self.num * other.num, self.den * other.den)

    def __imul__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор умножения с присваиванием (*=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.num
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __truediv__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор деления (/)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return FractionV6(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Реализует оператор деления с присваиванием (/=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den
        den = self.den * other.num
        self.num, self.den = self.__simplify((num, den))
        return self

    def reverse(self) -> "FractionV6":
        """Переворачивает дробь, меняя числитель и знаменатель местами."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: Union[int, "FractionV6"]) -> bool:
        """Реализует оператор больше (>)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: Union[int, "FractionV6"]) -> bool:
        """Реализует оператор больше или равно (>=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: Union[int, "FractionV6"]) -> bool:
        """Реализует оператор меньше (<)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den < other.num / other.den

    def __le__(self, other: Union[int, "FractionV6"]) -> bool:
        """Реализует оператор меньше или равно (<=)."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Реализует оператор равенства (==)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Реализует оператор неравенства (!=)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den


# ## Дроби v0.7.
#
# - "Остался последний штрих!" Правда звучит как издевательство?
# - Мы «научили» наши дроби работать с целыми числами и вот теперь надо провернуть обратное действие. Реализуйте функционал, который позволит производить все арифметические операции с дробями и числами, независимо от их положения (слева или справа) в операторе.
# - Примечание
# - Будем считать, что пользователь знает о запрете деления на ноль.
# - Все поля и методы, не требуемые в задаче, следует инкапсулировать (называть с использованием ведущих символов нижнего подчёркивания).
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class FractionV7:
    """Класс для представления дроби с автоматическим упрощением."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь с помощью наибольшего общего делителя (НОД)."""
        if len(values) == 1:
            values += (1,)
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализирует объект Fraction и упрощает его."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Возвращает или устанавливает числитель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Возвращает или устанавливает знаменатель дроби."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((self.num, abs(value)))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                num, den = self.__simplify((abs(self.num), abs(value)))
                self.num, self.den = num, den
                self.num = -self.num if value > 0 else self.num
        return self.den

    def __neg__(self) -> "FractionV7":
        """Реализует унарное отрицание (-Fraction)."""
        return FractionV7(-self.num, self.den)

    def __str__(self) -> str:
        """Возвращает дробь в строковом формате."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Возвращает строковое представление дроби для отладки."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор сложения (+)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __radd__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор обратного сложения (+)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __iadd__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор сложения с присваиванием (+=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор вычитания (-)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __rsub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор обратного вычитания (-)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = other.num * self.den - self.num * other.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __isub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор вычитания с присваиванием (-=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор умножения (*)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.num, self.den * other.den)

    def __rmul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор обратного умножения (*)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор умножения с присваиванием (*=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den)
        )
        return self

    def __truediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор деления (/)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализоует оператор обратного деления (/)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.den * other.num, self.num * other.den)

    def __itruediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Реализует оператор деления с присваиванием (/=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num)
        )
        return self

    def reverse(self) -> "FractionV7":
        """Переворачивает дробь, меняя числитель и знаменатель местами."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: "FractionV7 | int") -> bool:
        """Реализует оператор больше (>)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: "FractionV7 | int") -> bool:
        """Реализует оператор больше или равно (>=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: "FractionV7 | int") -> bool:
        """Реализует оператор меньше (<)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den < other.num / other.den

    def __le__(self, other: "FractionV7 | int") -> bool:
        """Реализует оператор меньше или равно (<=)."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Реализует оператор равенства (==)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Реализует оператор неравенства (!=)."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den


#
