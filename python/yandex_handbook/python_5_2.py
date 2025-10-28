"""Yandex handbook "Python Basics" answers."""

# +
from __future__ import annotations

# pylint: disable=too-many-lines

# 1


class Point1:
    """Представляет точку в двумерном пространстве."""

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Инициализирует точку с заданными координатами x и y."""
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, new_x: int | Point1, new_y: int | None = None) -> None:
        """Перемещает точку на заданные смещения."""
        if isinstance(new_x, Point1) and new_y is None:
            self.x_coord += new_x.x_coord
            self.y_coord += new_x.y_coord
        elif isinstance(new_x, int) and isinstance(new_y, int):
            self.x_coord += new_x
            self.y_coord += new_y
        else:
            raise TypeError("Неверные аргументы для move")

    def length(self, other_point: Point1) -> float:
        """Возвращает евклидово расстояние до другой точки."""
        if not isinstance(other_point, Point1):
            raise TypeError("Аргумент должен быть экземпляром Point")
        dx = (other_point.x_coord - self.x_coord) ** 2
        dy = (other_point.y_coord - self.y_coord) ** 2
        result = (dx + dy) ** 0.5
        rounded_result: float = round(result, 2)
        return rounded_result


class PatchedPoint1(Point1):
    """Точка в 2D с гибкими вариантами инициализации."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Инициализирует точку с указанными координатами."""
        if len(args) == 0:
            x_coord, y_coord = 0, 0
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, tuple) and len(arg) == 2:
                x_coord, y_coord = arg
            else:
                raise TypeError("Единственный аргумент должен быть кортежем")
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, int) and isinstance(arg2, int):
                x_coord, y_coord = arg1, arg2
            else:
                raise TypeError("Оба аргумента должны быть целыми числами")
        else:
            raise ValueError("Слишком много аргументов")
        super().__init__(x_coord, y_coord)


# -

# 2
class PatchedPoint2(Point1):
    """Представляет точку в 2D с гибкой инициализацией."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Инициализирует точку с указанными координатами."""
        if len(args) == 0:
            x_coord, y_coord = 0, 0
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, tuple) and len(arg) == 2:
                if all(isinstance(i, int) for i in arg):
                    x_coord, y_coord = arg
                else:
                    raise TypeError(
                        "Аргумент должен быть кортежем двух целых чисел"
                    )
            else:
                raise TypeError(
                    "Аргумент должен быть кортежем двух целых чисел")
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, int) and isinstance(arg2, int):
                x_coord, y_coord = arg1, arg2
            else:
                types = (type(arg1).__name__, type(arg2).__name__)
                error_msg = (
                    f"Оба аргумента должны быть целыми, получено {types}"
                )
                raise TypeError(error_msg)
        else:
            error_msg = (
                f"Слишком много аргументов (ожидалось 0,1,2, получено "
                f"{len(args)})"
            )
            raise ValueError(error_msg)
        super().__init__(x_coord, y_coord)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление точки."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Возвращает формальное представление точки."""
        return f"PatchedPoint2({self.x_coord}, {self.y_coord})"


# 3
class PatchedPoint3(Point1):
    """Представляет точку в 2D с расширенной функциональностью."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Инициализирует точку с указанными координатами."""
        if len(args) == 0:
            x_coord, y_coord = 0, 0
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, tuple) and len(arg) == 2:
                if all(isinstance(i, int) for i in arg):
                    x_coord, y_coord = arg
                else:
                    raise TypeError(
                        "Аргумент должен быть кортежем двух целых чисел")
            else:
                raise TypeError(
                    "Аргумент должен быть кортежем двух целых чисел")
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, int) and isinstance(arg2, int):
                x_coord, y_coord = arg1, arg2
            else:
                raise TypeError("Оба аргумента должны быть целыми числами")
        else:
            error_msg = (
                f"Слишком много аргументов (ожидалось 0,1,2, получено "
                f"{len(args)})"
            )
            raise ValueError(error_msg)
        super().__init__(x_coord, y_coord)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление точки."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Возвращает формальное представление точки."""
        return f"PatchedPoint3({self.x_coord}, {self.y_coord})"

    def __add__(self, other: PatchedPoint3 | tuple[int, int]) -> PatchedPoint3:
        """Возвращает новую точку путем сложения координат."""
        if isinstance(other, PatchedPoint3):
            new_x = self.x_coord + other.x_coord
            new_y = self.y_coord + other.y_coord
            return PatchedPoint3(new_x, new_y)
        if isinstance(other, tuple) and len(other) == 2:
            if all(isinstance(i, int) for i in other):
                new_x = self.x_coord + other[0]
                new_y = self.y_coord + other[1]
                return PatchedPoint3(new_x, new_y)
        raise TypeError(
            f"Неподдерживаемый тип операнда: {type(other).__name__}")

    def __iadd__(
        self, other: PatchedPoint3 | tuple[
            int, int]) -> PatchedPoint3:
        """Добавляет координаты другой точки или кортежа к текущей точке."""
        if isinstance(other, PatchedPoint3):
            self.move(other.x_coord, other.y_coord)
        elif isinstance(other, tuple) and len(other) == 2:
            self.move(other[0], other[1])
        else:
            raise TypeError("Операнд должен быть PatchedPoint3 или кортежем")
        return self


# 4
class Fraction1:
    """Представляет дробь и упрощает ее."""

    def __init__(self, *args: str | int) -> None:
        """Инициализирует дробь и упрощает ее."""
        if not args:
            raise ValueError("Требуется хотя бы один аргумент")

        numerator_val: int
        denominator_val: int

        if isinstance(args[0], str):
            parts = args[0].split("/")
            if len(parts) != 2:
                raise ValueError(
                    "Строка должна быть в формате 'числитель/знаменатель'")
            numerator_val, denominator_val = map(int, parts)
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, int) and isinstance(arg2, int):
                numerator_val, denominator_val = arg1, arg2
            else:
                raise ValueError("Неверные аргументы для Fraction")
        else:
            raise ValueError("Неверные аргументы для Fraction")

        if denominator_val == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")

        self.__numerator = numerator_val
        self.__denominator = denominator_val
        self.__reduce()

    @staticmethod
    def __gcd(a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель двух целых чисел."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def __reduce(self) -> None:
        """Упрощает дробь и обеспечивает положительность знаменателя."""
        gcd_val = self.__gcd(self.__numerator, self.__denominator)
        self.__numerator //= gcd_val
        self.__denominator //= gcd_val
        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

    def numerator(self, *args: int) -> int:
        """Получает или устанавливает числитель дроби."""
        if args:
            self.__numerator = args[0]
            self.__reduce()
        return self.__numerator

    def denominator(self, *args: int) -> int:
        """Получает или устанавливает знаменатель дроби."""
        if args:
            if args[0] == 0:
                raise ZeroDivisionError("Знаменатель не может быть нулем")
            self.__denominator = args[0]
            self.__reduce()
        return self.__denominator

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction({self.__numerator}, {self.__denominator})"


# 5
class Fraction2:
    """Упрощенная дробь, представленная числителем и знаменателем."""

    def __init__(self, *args: str | int) -> None:
        """Создает дробь и упрощает ее."""
        if not args:
            raise ValueError("Требуется хотя бы один аргумент")

        numerator_val: int
        denominator_val: int

        if isinstance(args[0], str):
            parts = args[0].strip().split("/")
            if len(parts) != 2:
                raise ValueError(
                    "Строка должна быть в формате 'числитель/знаменатель'")
            numerator_val, denominator_val = map(int, parts)
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, int) and isinstance(arg2, int):
                numerator_val, denominator_val = arg1, arg2
            else:
                raise ValueError("Неверное количество аргументов")
        else:
            raise ValueError("Неверное количество аргументов")

        if denominator_val == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")

        self.__numerator = numerator_val
        self.__denominator = denominator_val
        self.__reduce()

    def __sign(self) -> int:
        """Возвращает знак дроби."""
        return -1 if self.__numerator < 0 else 1

    @staticmethod
    def __gcd(a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель двух целых чисел."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def __reduce(self) -> Fraction2:
        """Упрощает дробь и обеспечивает положительность знаменателя."""
        gcd_val = self.__gcd(self.__numerator, self.__denominator)
        self.__numerator //= gcd_val
        self.__denominator //= gcd_val
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        return self

    def numerator(self, *args: int) -> int:
        """Получает или устанавливает числитель дроби."""
        if args:
            value = int(args[0])
            self.__numerator = abs(value) * self.__sign()
            self.__reduce()
        return abs(self.__numerator)

    def denominator(self, *args: int) -> int:
        """Получает или устанавливает знаменатель дроби."""
        if args:
            value = int(args[0])
            if value == 0:
                raise ZeroDivisionError("Знаменатель не может быть нулем")
            self.__denominator = abs(value)
            self.__reduce()
        return abs(self.__denominator)

    def __neg__(self) -> Fraction2:
        """Возвращает отрицательную дробь."""
        return Fraction2(-self.__numerator, self.__denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self.__numerator}/{self.__denominator}')"


# 6
class Fraction3:
    """Представляет упрощенную дробь с целыми числителем и знаменателем."""

    def __init__(
        self,
        numerator: int | str,
        denominator: int | None = None
    ) -> None:
        """Инициализирует дробь из строки 'a/b' или двух целых чисел."""
        if isinstance(numerator, str):
            self._numerator, self._denominator = map(int, numerator.split("/"))
        else:
            if denominator is None:
                raise ValueError(
                    "Требуется знаменатель, когда числитель целый")
            self._numerator, self._denominator = numerator, denominator
        if self._denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")
        self._reduce()

    def _sign(self) -> int:
        """Возвращает знак дроби."""
        return -1 if self._numerator < 0 else 1

    @staticmethod
    def _gcd(a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель двух целых чисел."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def _reduce(self) -> None:
        """Упрощает дробь с помощью НОД и нормализует знак."""
        gcd_val = self._gcd(self._numerator, self._denominator)
        self._numerator //= gcd_val
        self._denominator //= gcd_val
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @property
    def numerator(self) -> int:
        """Возвращает числитель дроби."""
        return self._numerator

    @numerator.setter
    def numerator(self, value: int) -> None:
        """Устанавливает числитель и упрощает дробь."""
        abs_value = abs(value)
        self._numerator = -abs_value if value < 0 else abs_value
        self._reduce()

    @property
    def denominator(self) -> int:
        """Возвращает знаменатель дроби."""
        return self._denominator

    @denominator.setter
    def denominator(self, value: int) -> None:
        """Устанавливает знаменатель и упрощает дробь."""
        if value == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")
        abs_value = abs(value)
        self._denominator = abs_value
        self._reduce()

    def __neg__(self) -> Fraction3:
        """Возвращает отрицательную дробь."""
        return Fraction3(-self._numerator, self._denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: Fraction3) -> Fraction3:
        """Добавляет другую дробь или целое число к текущей дроби."""
        new_numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction3(new_numerator, new_denominator)

    def __iadd__(self, other: Fraction3) -> Fraction3:
        """Выполняет мгновенное сложение с другой дробью или целым числом."""
        self._numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __sub__(self, other: Fraction3) -> Fraction3:
        """Вычитает другую дробь или целое число из текущей дроби."""
        new_numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction3(new_numerator, new_denominator)

    def __isub__(self, other: Fraction3) -> Fraction3:
        """Выполняет мгновенное вычитание с другой дробью или целым числом."""
        self._numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self


# 7
class Fraction4:
    """Класс, представляющий дроби с арифметическими операциями."""

    def __init__(self, *args: int | str) -> None:
        """Инициализирует из строки 'num/den' или двух целых чисел."""
        if isinstance(args[0], str):
            parts = args[0].split("/")
            self._numerator = int(parts[0])
            self._denominator = int(parts[1])
        else:
            arg1, arg2 = args[0], args[1]
            self._numerator = int(arg1)
            self._denominator = int(arg2)
        self._reduce()

    def _sign(self) -> int:
        """Возвращает знак дроби."""
        return -1 if self._numerator < 0 else 1

    def _gcd(self, a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def _reduce(self) -> None:
        """Упрощает дробь до наименьшей формы."""
        gcd_val = self._gcd(self._numerator, self._denominator)
        self._numerator //= gcd_val
        self._denominator //= gcd_val
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    def numerator(self, value: int | None = None) -> int:
        """Получает или устанавливает числитель дроби."""
        if value is not None:
            self._numerator = value * self._sign()
            self._reduce()
        return abs(self._numerator)

    def denominator(self, value: int | None = None) -> int:
        """Получает или устанавливает знаменатель дроби."""
        if value is not None:
            self._denominator = value
            self._reduce()
        return abs(self._denominator)

    def __neg__(self) -> Fraction4:
        """Возвращает отрицательную дробь."""
        return Fraction4(-self._numerator, self._denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: Fraction4) -> Fraction4:
        """Добавляет другую дробь или целое число к текущей дроби."""
        term1 = self._numerator * other._denominator
        term2 = other._numerator * self._denominator
        numerator_new = term1 + term2
        denominator_new = self._denominator * other._denominator
        return Fraction4(numerator_new, denominator_new)

    def __sub__(self, other: Fraction4) -> Fraction4:
        """Вычитает другую дробь или целое число из текущей дроби."""
        term1 = self._numerator * other._denominator
        term2 = other._numerator * self._denominator
        numerator_new = term1 - term2
        denominator_new = self._denominator * other._denominator
        return Fraction4(numerator_new, denominator_new)

    def __iadd__(self, other: Fraction4) -> Fraction4:
        """Выполняет мгновенное сложение с другой дробью или целым числом."""
        term1 = self._numerator * other._denominator
        term2 = other._numerator * self._denominator
        self._numerator = term1 + term2
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __isub__(self, other: Fraction4) -> Fraction4:
        """Выполняет мгновенное вычитание с другой дробью или целым числом."""
        term1 = self._numerator * other._denominator
        term2 = other._numerator * self._denominator
        self._numerator = term1 - term2
        self._denominator = self._denominator * other._denominator
        self._reduce()
        return self

    def __mul__(self, other: Fraction4) -> Fraction4:
        """Умножает эту дробь на другую дробь или целое число."""
        numerator_new = self._numerator * other._numerator
        denominator_new = self._denominator * other._denominator
        return Fraction4(numerator_new, denominator_new)

    def __imul__(self, other: Fraction4) -> Fraction4:
        """Выполняет мгновенное умножение с другой дробью или целым числом."""
        self._numerator *= other._numerator
        self._denominator *= other._denominator
        self._reduce()
        return self

    def __truediv__(self, other: Fraction4) -> Fraction4:
        """Делит текущую дробь на другую дробь или целое число."""
        return self * other.reverse()

    def __itruediv__(self, other: Fraction4) -> Fraction4:
        """Выполняет мгновенное деление на другую дробь или целое число."""
        return self.__imul__(other.reverse())

    def reverse(self) -> Fraction4:
        """Возвращает обратную дробь (reciprocal)."""
        return Fraction4(self._denominator, self._numerator)


# 8
class Fraction5:
    """Класс Fraction, объединяющий лучшие функции из обеих реализаций."""

    def __init__(self, *args: str | int) -> None:
        """Инициализирует строкой 'num/den' или парой числитель/знаменатель."""
        if isinstance(args[0], str):
            parts = args[0].split("/")
            self._numerator = int(parts[0])
            self._denominator = int(parts[1]) if len(parts) > 1 else 1
        else:
            arg1, arg2 = args[0], args[1] if len(args) > 1 else 1
            self._numerator = int(arg1)
            self._denominator = int(arg2)
        self._reduce_fraction()

    def gcd(self, a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель двух целых чисел."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def _reduce_fraction(self) -> Fraction5:
        """Упрощает дробь и обеспечивает положительность знаменателя."""
        gcd_val = self.gcd(self._numerator, self._denominator)
        self._numerator //= gcd_val
        self._denominator //= gcd_val
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1
        return self

    def numerator(self, value: int | None = None) -> int:
        """Получает или устанавливает числитель дроби."""
        if value is not None:
            self._numerator = value
            self._reduce_fraction()
        return abs(self._numerator)

    def denominator(self, value: int | None = None) -> int:
        """Получает или устанавливает знаменатель дроби."""
        if value is not None:
            self._denominator = value
            self._reduce_fraction()
        return self._denominator

    def __neg__(self) -> Fraction5:
        """Возвращает отрицательную дробь."""
        return Fraction5(-self._numerator, self._denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: int | Fraction5) -> Fraction5:
        """Добавляет другую дробь или целое число к текущей дроби."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        numerator_new = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        denominator_new = self._denominator * other._denominator
        return Fraction5(numerator_new, denominator_new)._reduce_fraction()

    def __iadd__(self, other: int | Fraction5) -> Fraction5:
        """Выполняет мгновенное сложение с другой дробью или целым числом."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        return self._reduce_fraction()

    def __sub__(self, other: int | Fraction5) -> Fraction5:
        """Вычитает другую дробь или целое число из текущей дроби."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        numerator_new = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        denominator_new = self._denominator * other._denominator
        return Fraction5(numerator_new, denominator_new)._reduce_fraction()

    def __isub__(self, other: int | Fraction5) -> Fraction5:
        """Выполняет мгновенное вычитание с другой дробью или целым числом."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        return self._reduce_fraction()

    def __mul__(self, other: int | Fraction5) -> Fraction5:
        """Умножает эту дробь на другую дробь или целое число."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return Fraction5(
            self._numerator * other._numerator,
            self._denominator * other._denominator
        )._reduce_fraction()

    def __imul__(self, other: int | Fraction5) -> Fraction5:
        """Выполняет мгновенное умножение с другой дробью или целым числом."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._numerator *= other._numerator
        self._denominator *= other._denominator
        return self._reduce_fraction()

    def __truediv__(self, other: int | Fraction5) -> Fraction5:
        """Делит текущую дробь на другую дробь или целое число."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self * other.reverse()

    def __itruediv__(self, other: int | Fraction5) -> Fraction5:
        """Выполняет мгновенное деление на другую дробь или целое число."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self.__imul__(other.reverse())

    def __gt__(self, other: int | Fraction5) -> bool:
        """Проверяет, больше ли."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return (
            self._numerator * other._denominator > other._numerator * self._denominator
        )

    def __ge__(self, other: int | Fraction5) -> bool:
        """Проверяет, больше или равно."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return (
            self._numerator * other._denominator >= other._numerator * self._denominator
        )

    def __lt__(self, other: int | Fraction5) -> bool:
        """Проверяет, меньше ли."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return (
            self._numerator * other._denominator < other._numerator * self._denominator
        )

    def __le__(self, other: int | Fraction5) -> bool:
        """Проверяет, меньше или равно."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return (
            self._numerator * other._denominator <= other._numerator * self._denominator
        )

    def __eq__(self, other: object) -> bool:
        """Проверяет, равно ли."""
        if not isinstance(other, Fraction5):
            return NotImplemented
        return (
            self._numerator * other._denominator == other._numerator * self._denominator
        )

    def reverse(self) -> Fraction5:
        """Возвращает обратную дробь (reciprocal)."""
        return Fraction5(self._denominator, self._numerator)


# 9
class Fraction6:
    """Гибридный класс Fraction, объединяющий лучшие функции из обеих реализаций."""

    def __init__(self, *args: str | int) -> None:
        """Инициализирует строкой 'num/den' или парой числитель/знаменатель."""
        if isinstance(args[0], str):
            parts = args[0].split("/")
            self._numerator = int(parts[0])
            self._denominator = int(parts[1]) if len(parts) > 1 else 1
        else:
            arg1, arg2 = args[0], args[1] if len(args) > 1 else 1
            self._numerator = int(arg1)
            self._denominator = int(arg2)
        self._reduce_fraction()

    @staticmethod
    def gcd(a_val: int, b_val: int) -> int:
        """Вычисляет наибольший общий делитель двух целых чисел."""
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        return abs(a_val)

    def _reduce_fraction(self) -> Fraction6:
        """Упрощает дробь."""
        gcd_val = self.gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd_val
        self._denominator = self._denominator // gcd_val
        return self

    def numerator(self, value: int | None = None) -> int:
        """Получает или устанавливает числитель дроби."""
        if value is not None:
            self._numerator = value
            self._reduce_fraction()
        return abs(self._numerator)

    def denominator(self, value: int | None = None) -> int:
        """Получает или устанавливает знаменатель дроби."""
        if value is not None:
            self._denominator = value
            self._reduce_fraction()
        return self._denominator

    def __neg__(self) -> Fraction6:
        """Возвращает отрицательную дробь."""
        return Fraction6(-self._numerator, self._denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: int | Fraction6) -> Fraction6:
        """Добавляет другую дробь или целое число к текущей дроби."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        denominator_new = self._denominator * other._denominator
        numerator_new = (
            self._numerator * other._denominator + other._numerator * self._denominator
        )
        return Fraction6(numerator_new, denominator_new)._reduce_fraction()

    def __sub__(self, other: int | Fraction6) -> Fraction6:
        """Вычитает другую дробь или целое число из текущей дроби."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        denominator_new = self._denominator * other._denominator
        numerator_new = (
            self._numerator * other._denominator - other._numerator * self._denominator
        )
        return Fraction6(numerator_new, denominator_new)._reduce_fraction()

    def __isub__(self, other: int | Fraction6) -> Fraction6:
        """Выполняет мгновенное вычитание с другой дробью или целым числом."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        self._numerator = (
            self._numerator * other._denominator - other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        return self._reduce_fraction()

    def __iadd__(self, other: int | Fraction6) -> Fraction6:
        """Выполняет мгновенное сложение с другой дробью или целым числом."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        self._numerator = (
            self._numerator * other._denominator + other._numerator * self._denominator
        )
        self._denominator = self._denominator * other._denominator
        return self._reduce_fraction()

    def __mul__(self, other: Fraction6) -> Fraction6:
        """Умножает эту дробь на другую дробь или целое число."""
        numerator_new = self._numerator * other._numerator
        denominator_new = self._denominator * other._denominator
        return Fraction6(numerator_new, denominator_new)._reduce_fraction()

    def __imul__(self, other: Fraction6) -> Fraction6:
        """Выполняет мгновенное умножение с другой дробью или целым числом."""
        self._numerator *= other._numerator
        self._denominator *= other._denominator
        return self._reduce_fraction()

    def __truediv__(self, other: Fraction6) -> Fraction6:
        """Делит текущую дробь на другую дробь или целое число."""
        result = Fraction6(self._numerator, self._denominator)
        return result.__mul__(other.reverse())

    def __itruediv__(self, other: Fraction6) -> Fraction6:
        """Выполняет мгновенное деление на другую дробь или целое число."""
        return self.__imul__(other.reverse())

    def __gt__(self, other: int | Fraction6) -> bool:
        """Проверяет, больше ли."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return (
            self._numerator * other._denominator > other._numerator * self._denominator
        )

    def __ge__(self, other: int | Fraction6) -> bool:
        """Проверяет, больше или равно."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return (
            self._numerator * other._denominator >= other._numerator * self._denominator
        )

    def __lt__(self, other: int | Fraction6) -> bool:
        """Проверяет, меньше ли."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return (
            self._numerator * other._denominator < other._numerator * self._denominator
        )

    def __le__(self, other: int | Fraction6) -> bool:
        """Проверяет, меньше или равно."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return (
            self._numerator * other._denominator <= other._numerator * self._denominator
        )

    def __eq__(self, other: object) -> bool:
        """Проверяет, равно ли."""
        if not isinstance(other, Fraction6):
            return NotImplemented
        return (
            self._numerator * other._denominator == other._numerator * self._denominator
        )

    def reverse(self) -> Fraction6:
        """Возвращает обратную дробь (reciprocal)."""
        return Fraction6(self._denominator, self._numerator)


# 10
class Fraction7:
    """Представляет математические дроби с арифметическими операциями."""

    def __init__(self, *args: int | str) -> None:
        """Инициализирует дробь из указанных значений."""
        self._numerator: int = 0
        self._denominator: int = 1

        if len(args) == 1:
            if isinstance(args[0], str):
                parts = args[0].split("/")
                if len(parts) == 1:
                    self._numerator = int(parts[0])
                else:
                    self._numerator, self._denominator = map(int, parts)
            elif isinstance(args[0], int):
                self._numerator = args[0]
        elif len(args) == 2:
            arg1, arg2 = args
            self._numerator, self._denominator = int(arg1), int(arg2)
        else:
            raise ValueError("Неверные аргументы для конструктора Fraction")

        self._reduce_fraction((self._numerator, self._denominator))

    def _reduce_fraction(self, values: tuple[int, int]) -> None:
        """Упрощает дробь с использованием наибольшего общего делителя."""
        numerator_val, denominator_val = values
        if denominator_val == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")
        a_val, b_val = abs(numerator_val), abs(denominator_val)
        while b_val:
            a_val, b_val = b_val, a_val % b_val
        gcd_val = a_val
        numerator_val //= gcd_val
        denominator_val //= gcd_val
        if denominator_val < 0:
            numerator_val, denominator_val = -numerator_val, -denominator_val
        self._numerator, self._denominator = numerator_val, denominator_val

    @property
    def numerator(self) -> int:
        """Возвращает числитель дроби."""
        return self._numerator

    @numerator.setter
    def numerator(self, value: int) -> None:
        """Устанавливает числитель и упрощает дробь."""
        self._numerator = value
        self._reduce_fraction((self._numerator, self._denominator))

    @property
    def denominator(self) -> int:
        """Возвращает знаменатель дроби."""
        return self._denominator

    @denominator.setter
    def denominator(self, value: int) -> None:
        """Устанавливает знаменатель и упрощает дробь."""
        if value == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулем")
        self._denominator = value
        self._reduce_fraction((self._numerator, self._denominator))

    def __neg__(self) -> Fraction7:
        """Возвращает отрицательную дробь."""
        return Fraction7(-self._numerator, self._denominator)

    def __str__(self) -> str:
        """Возвращает удобное строковое представление дроби."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Возвращает формальное представление дроби."""
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __add__(self, other: Fraction7 | int) -> Fraction7:
        """Добавляет другую дробь или целое число к текущей дроби."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        term1 = self._numerator * other_frac._denominator
        term2 = other_frac._numerator * self._denominator
        numerator_new = term1 + term2
        denominator_new = self._denominator * other_frac._denominator
        return Fraction7(numerator_new, denominator_new)

    def __radd__(self, other: Fraction7 | int) -> Fraction7:
        """Правосторонняя версия операции сложения."""
        return self + other

    def __iadd__(self, other: Fraction7 | int) -> Fraction7:
        """Выполняет мгновенное сложение с другой дробью или целым числом."""
        result = self + other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __sub__(self, other: Fraction7 | int) -> Fraction7:
        """Вычитает другую дробь или целое число из текущей дроби."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        term1 = self._numerator * other_frac._denominator
        term2 = other_frac._numerator * self._denominator
        numerator_new = term1 - term2
        denominator_new = self._denominator * other_frac._denominator
        return Fraction7(numerator_new, denominator_new)

    def __rsub__(self, other: int | str) -> Fraction7:
        """Правосторонняя версия операции вычитания."""
        return Fraction7(other) - self

    def __isub__(self, other: Fraction7 | int) -> Fraction7:
        """Выполняет мгновенное вычитание с другой дробью или целым числом."""
        result = self - other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __mul__(self, other: Fraction7 | int) -> Fraction7:
        """Умножает эту дробь на другую дробь или целое число."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        numerator_new = self._numerator * other_frac._numerator
        denominator_new = self._denominator * other_frac._denominator
        return Fraction7(numerator_new, denominator_new)

    def __rmul__(self, other: Fraction7 | int) -> Fraction7:
        """Правосторонняя версия операции умножения."""
        return self * other

    def __imul__(self, other: Fraction7 | int) -> Fraction7:
        """Выполняет мгновенное умножение с другой дробью или целым числом."""
        result = self * other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __truediv__(self, other: Fraction7 | int) -> Fraction7:
        """Делит текущую дробь на другую дробь или целое число."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        if other_frac._numerator == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        numerator_new = self._numerator * other_frac._denominator
        denominator_new = self._denominator * other_frac._numerator
        return Fraction7(numerator_new, denominator_new)

    def __rtruediv__(self, other: int | str) -> Fraction7:
        """Правосторонняя версия операции деления."""
        return Fraction7(other) / self

    def __itruediv__(self, other: Fraction7 | int) -> Fraction7:
        """Выполняет мгновенное деление на другую дробь или целое число."""
        result = self / other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __eq__(self, other: object) -> bool:
        """Проверяет, равно ли."""
        if not isinstance(other, (Fraction7, int)):
            return NotImplemented
        other_frac = Fraction7(other) if isinstance(other, int) else other
        left_side = self._numerator * other_frac._denominator
        right_side = other_frac._numerator * self._denominator
        return left_side == right_side

    def __ne__(self, other: object) -> bool:
        """Проверяет, не равно ли."""
        if not isinstance(other, (Fraction7, int)):
            return NotImplemented
        return not self == other

    def __lt__(self, other: Fraction7 | int) -> bool:
        """Проверяет, меньше ли."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        left_side = self._numerator * other_frac._denominator
        right_side = other_frac._numerator * self._denominator
        return left_side < right_side

    def __le__(self, other: Fraction7 | int) -> bool:
        """Проверяет, меньше или равно."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        left_side = self._numerator * other_frac._denominator
        right_side = other_frac._numerator * self._denominator
        return left_side <= right_side

    def __gt__(self, other: Fraction7 | int) -> bool:
        """Проверяет, больше ли."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        left_side = self._numerator * other_frac._denominator
        right_side = other_frac._numerator * self._denominator
        return left_side > right_side

    def __ge__(self, other: Fraction7 | int) -> bool:
        """Проверяет, больше или равно."""
        other_frac = Fraction7(other) if isinstance(other, int) else other
        left_side = self._numerator * other_frac._denominator
        right_side = other_frac._numerator * self._denominator
        return left_side >= right_side

    def reverse(self) -> Fraction7:
        """Возвращает обратную дробь (reciprocal)."""
        if self._numerator == 0:
            raise ZeroDivisionError("Невозможно взять reciprocal от нуля")
        return Fraction7(self._denominator, self._numerator)

    def __float__(self) -> float:
        """Возвращает вещественное представление дроби."""
        return self._numerator / self._denominator

    def __int__(self) -> int:
        """Возвращает целую часть дроби."""
        return self._numerator // self._denominator
