"""5.2 Method overriding inheritance."""

from functools import total_ordering
from typing import Union

# +
# Классная точка 3.0, 4.0, 5.0


class Point:
    """Класс для представления точки."""

    def __init__(self, coord_x: int, coord_y: int) -> None:
        """Инициализация точки."""
        self.x = coord_x
        self.y = coord_y

    def move(self, delta_x: int, delta_y: int) -> None:
        """Перемещение точки."""
        self.x += delta_x
        self.y += delta_y

    def length(self, other_point: "Point") -> float:
        """Расстояние до точки."""
        x_delta = self.x - other_point.x
        y_delta = self.y - other_point.y

        return float(round((x_delta**2 + y_delta**2) ** 0.5, 2))


class PatchedPoint(Point):
    """Класс-наследник Point."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Инициализация класса-наследника."""
        if not args:
            Point.__init__(self, 0, 0)

        elif len(args) == 1 and isinstance(args[0], tuple):
            coord_x, coord_y = args[0]
            Point.__init__(self, coord_x, coord_y)

        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            Point.__init__(self, args[0], args[1])

    def __str__(self) -> str:
        """Строка."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Репрезентация."""
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other: tuple[int, int]) -> "PatchedPoint":
        """Создает новую точку на основе изначальной точки и кортежа."""
        coord_x, coord_y = other
        return PatchedPoint(self.x + coord_x, self.y + coord_y)

    def __iadd__(self, other: tuple[int, int]) -> "PatchedPoint":
        """Изменяет текущаю точку на основе изначальной точки и кортежа."""
        coord_x, coord_y = other
        self.move(coord_x, coord_y)
        return self


# -


@total_ordering
class Fraction:
    """Класс для представления дроби."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Упрощает дробь."""
        if len(values) == 1:
            values += (1,)
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Инициализатор."""
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

    def __neg__(self) -> "Fraction":
        """Унарное отрицание."""
        return Fraction(-self.num, self.den)

    def __str__(self) -> str:
        """Строка."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Репрезентация."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "Fraction | int") -> "Fraction":
        """Сложение."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other: "Fraction | int") -> "Fraction":
        """Вычитание."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __iadd__(self, other: "Fraction | int") -> "Fraction":
        """Сложение с присваиванием."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __isub__(self, other: "Fraction | int") -> "Fraction":
        """Сложение с вычитанием."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: "Fraction | int") -> "Fraction":
        """Умножение."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: "Fraction | int") -> "Fraction":
        """Деление."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        return Fraction(self.num * other.den, self.den * other.num)

    def __imul__(self, other: "Fraction | int") -> "Fraction":
        """Умножение с присваиванием."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den)
        )
        return self

    def __itruediv__(self, other: "Fraction | int") -> "Fraction":
        """Деление с присваиванием."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num)
        )
        return self

    def reverse(self) -> "Fraction":
        """Обращение дроби."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __eq__(self, other: object) -> bool:
        """Равенство."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __lt__(self, other: "Fraction | int") -> bool:
        """Меньше."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        return self.num / self.den < other.num / other.den

    def __radd__(self, other: "Fraction | int") -> "Fraction":
        """Правостороннее сложение."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __rsub__(self, other: "Fraction | int") -> "Fraction":
        """Правостороннее вычитание."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        num = other.num * self.den - self.num * other.den
        den = self.den * other.den
        return Fraction(num, den)

    def __rmul__(self, other: "Fraction | int") -> "Fraction":
        """Правостороннее умножение."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        return Fraction(self.num * other.num, self.den * other.den)

    def __rtruediv__(self, other: "Fraction | int") -> "Fraction":
        """Правостороннее деление."""
        if not isinstance(other, Fraction):
            other = Fraction(str(other))
        return Fraction(self.den * other.num, self.num * other.den)
