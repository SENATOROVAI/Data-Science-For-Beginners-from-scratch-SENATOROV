"""Magic methods, method overriding.

Inheritance.
"""

# # Special Methods in Python
#
# Python has many special methods used to define interactions with objects through standard operations and built-in functions. The process of defining these methods is called **operator overloading**.
#
# Special methods are enclosed with double underscores (`__`), such as `__init__`, which is a well-known special method.
#
# ## Common Special Methods
#
# ### Object Representation
# - `__repr__`: Called by the `repr()` function, Return a string representation of the object, useful for debugging and when objects are elements of a collection.
#
# ### Comparison Operations
# - `__lt__(self, other)`: `<`
# - `__le__(self, other)`: `<=`
# - `__eq__(self, other)`: `==`
# - `__ne__(self, other)`: `!=`
# - `__gt__(self, other)`: `>`
# - `__ge__(self, other)`: `>=`
#
# ### Callable Objects
# - `__call__(self, *args)`: Invoked when an object is called as a function.
#
# ### Collection-Like Behavior
# - `__getitem__(self, key)`: `self[key]`
# - `__setitem__(self, key, value)`: `self[key] = value`
# - `__delitem__(self, key)`: `del self[key]`
# - `__len__(self)`: Called by `len()`
# - `__contains__(self, item)`: Used with `in` operator
#
# ### Mathematical Operations
# - `__add__(self, other)`: `self + other`
# - `__sub__(self, other)`: `self - other`
# - `__mul__(self, other)`: `self * other`
# - `__matmul__(self, other)`: `self @ other`
# - `__truediv__(self, other)`: `self / other`
# - `__floordiv__(self, other)`: `self // other`
# - `__mod__(self, other)`: `self % other`
# - `__divmod__(self, other)`: `divmod(self, other)`
# - `__pow__(self, other)`: `self ** other`
# - `__lshift__(self, other)`: `self << other`
# - `__rshift__(self, other)`: `self >> other`
# - `__and__(self, other)`: `self & other`
# - `__xor__(self, other)`: `self ^ other`
# - `__or__(self, other)`: `self | other`
#
# ### Reflected (Right-Hand) Operations
# These methods handle cases where the operand order is reversed:
# - `__radd__(self, other)`: `other + self`
# - `__rsub__(self, other)`: `other - self`
# - `__rmul__(self, other)`: `other * self`
# - `__rtruediv__(self, other)`: `other / self`
# - `__rfloordiv__(self, other)`: `other // self`
# - `__rmod__(self, other)`: `other % self`
# - `__rpow__(self, other)`: `other ** self`
# - `__rlshift__(self, other)`: `other << self`
# - `__rrshift__(self, other)`: `other >> self`
# - `__rand__(self, other)`: `other & self`
# - `__rxor__(self, other)`: `other ^ self`
# - `__ror__(self, other)`: `other | self`
#
# ### In-Place Operations
# These methods modify the object itself:
# - `__iadd__(self, other)`: `self += other`
# - `__isub__(self, other)`: `self -= other`
# - `__imul__(self, other)`: `self *= other`
# - `__itruediv__(self, other)`: `self /= other`
# - `__ifloordiv__(self, other)`: `self //= other`
# - `__imod__(self, other)`: `self %= other`
# - `__ipow__(self, other)`: `self **= other`
# - `__ilshift__(self, other)`: `self <<= other`
# - `__irshift__(self, other)`: `self >>= other`
# - `__iand__(self, other)`: `self &= other`
# - `__ixor__(self, other)`: `self ^= other`
# - `__ior__(self, other)`: `self |= other`
#
# These special methods allow Python objects to behave like built-in types and participate in standard operations, making classes more intuitive and functional.
#

# +
# 1

# pylint: disable=C0302
# fmt: off
from math import sqrt
from typing import Union

# fmt: on


class Point:
    """A class representing a point on a 2D plane."""

    def __init__(self, x_coord: int, y_coord: int) -> None:
        """Initialize the point with given x and y coordinates."""
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, x_coord: int, y_coord: int) -> None:
        """Move the point by the given x and y coordinates."""
        self.x_coord += x_coord
        self.y_coord += y_coord

    def length(self, point: "Point") -> float:
        """Calculate the distance between this point and another point."""
        x_diff = self.x_coord - point.x_coord
        y_diff = self.y_coord - point.y_coord
        return round(
            sqrt(x_diff**2 + y_diff**2),
            2,
        )


# fmt: off

class PatchedPoint(Point):
    """A class representing a point on a 2D plane."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Initialize point with optional coordinates."""
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


# +
# 2

# fmt: off
class PatchedPointV2(Point):
    """A class representing a point on a 2D plane."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Initialize point with optional coordinates."""
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
        """Return string representation of the point."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Return string representation for debugging."""
        return f"PatchedPoint({self.x_coord}, {self.y_coord})"
# fmt: on


# +
# 3

# fmt: off
class PatchedPointV3(Point):
    """A class representing a point on a 2D plane."""

    def __init__(self, *args: Union[int, tuple[int, int]]) -> None:
        """Initialize point with optional coordinates."""
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
        """Return string representation of the point."""
        return f"({self.x_coord}, {self.y_coord})"

    def __repr__(self) -> str:
        """Return string representation for debugging."""
        return f"PatchedPoint({self.x_coord}, {self.y_coord})"

    def __add__(
        self, other: Union["PatchedPointV3", tuple[int, int]]
    ) -> "PatchedPointV3":
        """Add coordinates of another point or tuple to this point."""
        if isinstance(other, tuple):
            x_coord, y_coord = other
        else:
            x_coord, y_coord = other.x_coord, other.y_coord
        return PatchedPointV3(self.x_coord + x_coord, self.y_coord + y_coord)

    def __iadd__(
        self, other: Union["PatchedPointV3", tuple[int, int]]
    ) -> "PatchedPointV3":
        """Add coordinates of another point or tuple to this point in place."""
        if isinstance(other, tuple):
            x_coord, y_coord = other
        else:
            x_coord, y_coord = other.x_coord, other.y_coord
        self.move(x_coord, y_coord)
        return self
# fmt: on
# -

#

# +
# 4


class FractionV1:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            self.num, self.den = self.__simplify((value, self.den))
        return self.num

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
        if value:
            self.num, self.den = self.__simplify((self.num, value))
        return self.den

    def __str__(self) -> str:
        """Return the string representation of the fraction."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the official string representation of the fraction."""
        return f"Fraction({self.num}, {self.den})"


# +
# 5


class FractionV2:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV2(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"


# +
# 6


class FractionV8:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV8(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV8") -> "FractionV8":
        """Implement addition (+) operator."""
        return FractionV8(
            self.num * other.den + other.num * self.den, self.den * other.den
        )

    def __iadd__(self, other: "FractionV8") -> "FractionV8":
        """Implement in-place addition (+=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.den + other.num * self.den, self.den * other.den)
        )
        return self

    def __sub__(self, other: "FractionV8") -> "FractionV8":
        """Implement subtraction (-) operator."""
        return FractionV8(
            self.num * other.den - other.num * self.den, self.den * other.den
        )

    def __isub__(self, other: "FractionV8") -> "FractionV8":
        """Implement in-place subtraction (-=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.den - other.num * self.den, self.den * other.den)
        )
        return self


# +
# 7


class FractionV4:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV4(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV4") -> "FractionV4":
        """Implement addition (+) operator."""
        return FractionV4(
            self.num * other.den + other.num * self.den, self.den * other.den
        )

    def __iadd__(self, other: "FractionV4") -> "FractionV4":
        """Implement in-place addition (+=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.den + other.num * self.den, self.den * other.den)
        )
        return self

    def __sub__(self, other: "FractionV4") -> "FractionV4":
        """Implement subtraction (-) operator."""
        return FractionV4(
            self.num * other.den - other.num * self.den, self.den * other.den
        )

    def __isub__(self, other: "FractionV4") -> "FractionV4":
        """Implement in-place subtraction (-=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.den - other.num * self.den, self.den * other.den)
        )
        return self

    def __mul__(self, other: "FractionV4") -> "FractionV4":
        """Implement multiplication (*) operator."""
        return FractionV4(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV4") -> "FractionV4":
        """Implement in-place multiplication (*=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den)
        )
        return self

    def __truediv__(self, other: "FractionV4") -> "FractionV4":
        """Implement division (/) operator."""
        return FractionV4(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: "FractionV4") -> "FractionV4":
        """Implement in-place division (/=) operator."""
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num)
        )
        return self

    def reverse(self) -> "FractionV4":
        """Reverses the fraction by swapping numerator and denominator."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self


# +
# 8


class FractionV5:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV5(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV5") -> "FractionV5":
        """Implement addition (+) operator."""
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV5(num, den)

    def __iadd__(self, other: "FractionV5") -> "FractionV5":
        """Implement in-place addition (+=) operator."""
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: "FractionV5") -> "FractionV5":
        """Implement subtraction (-) operator."""
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV5(num, den)

    def __isub__(self, other: "FractionV5") -> "FractionV5":
        """Implement in-place subtraction (-=) operator."""
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: "FractionV5") -> "FractionV5":
        """Implement multiplication (*) operator."""
        return FractionV5(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV5") -> "FractionV5":
        """Implement in-place multiplication (*=) operator."""
        num = self.num * other.num
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __truediv__(self, other: "FractionV5") -> "FractionV5":
        """Implement division (/) operator."""
        return FractionV5(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: "FractionV5") -> "FractionV5":
        """Implement in-place division (/=) operator."""
        num = self.num * other.den
        den = self.den * other.num
        self.num, self.den = self.__simplify((num, den))
        return self

    def reverse(self) -> "FractionV5":
        """Reverses the fraction by swapping numerator and denominator."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: "FractionV5") -> bool:
        """Implement greater than (>) operator."""
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: "FractionV5") -> bool:
        """Implement greater than or equal to (>=) operator."""
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: "FractionV5") -> bool:
        """Implement less than (<) operator."""
        return self.num / self.den < other.num / other.den

    def __le__(self, other: "FractionV5") -> bool:
        """Implement less than or equal to (<=) operator."""
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Implement equality (==) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Implement inequality (!=) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den


# +
# 9


class FractionV6:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        if len(values) == 1:
            values += (1,)
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV6(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement addition (+) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV6(num, den)

    def __iadd__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement in-place addition (+=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement subtraction (-) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV6(num, den)

    def __isub__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement in-place subtraction (-=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement multiplication (*) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return FractionV6(self.num * other.num, self.den * other.den)

    def __imul__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement in-place multiplication (*=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.num
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __truediv__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement division (/) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return FractionV6(self.num * other.den, self.den * other.num)

    def __itruediv__(self, other: Union[int, "FractionV6"]) -> "FractionV6":
        """Implement in-place division (/=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        num = self.num * other.den
        den = self.den * other.num
        self.num, self.den = self.__simplify((num, den))
        return self

    def reverse(self) -> "FractionV6":
        """Reverses the fraction by swapping numerator and denominator."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: Union[int, "FractionV6"]) -> bool:
        """Implement greater than (>) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: Union[int, "FractionV6"]) -> bool:
        """Implement greater than or equal to (>=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: Union[int, "FractionV6"]) -> bool:
        """Implement less than (<) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den < other.num / other.den

    def __le__(self, other: Union[int, "FractionV6"]) -> bool:
        """Implement less than or equal to (<=) operator."""
        if not isinstance(other, FractionV6):
            other = FractionV6(str(other))
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Implement equality (==) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Implement inequality (!=) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den


# +
# 10


class FractionV7:
    """A class to represent a fraction and simplify it automatically."""

    def __simplify(self, values: tuple[int, ...]) -> tuple[int, int]:
        """Simplifies a fraction using the greatest common divisor (GCD)."""
        if len(values) == 1:
            values += (1,)
        num, den = values
        while den:
            num, den = den, num % den
        return values[0] // num, values[1] // num

    def __init__(self, *args: Union[str, int]) -> None:
        """Initialize a Fraction object and simplifies it."""
        if isinstance(args[0], str):
            coordinates = tuple(map(int, args[0].split("/")))
            self.num, self.den = self.__simplify(coordinates)
        else:
            self.num, self.den = self.__simplify(tuple(int(x) for x in args))

    def numerator(self, value: int = 0) -> int:
        """Return or sets the numerator of the fraction."""
        if value:
            if self.num > 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value < 0 else self.num
            elif self.num < 0:
                self.num, self.den = self.__simplify((abs(value), self.den))
                self.num = -self.num if value > 0 else self.num
        return abs(self.num)

    def denominator(self, value: int = 0) -> int:
        """Return or sets the denominator of the fraction."""
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
        """Implement unary negation (-Fraction)."""
        return FractionV7(-self.num, self.den)

    def __str__(self) -> str:
        """Return the fraction as a string format."""
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        """Return the string representation of the fraction for debugging."""
        return f"Fraction('{self.num}/{self.den}')"

    def __add__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement addition (+) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __radd__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement reverse addition (+) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __iadd__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement in-place addition (+=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __sub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement subtraction (-) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __rsub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement reverse subtraction (-) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = other.num * self.den - self.num * other.den
        den = self.den * other.den
        return FractionV7(num, den)

    def __isub__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement in-place subtraction (-=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        self.num, self.den = self.__simplify((num, den))
        return self

    def __mul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement multiplication (*) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.num, self.den * other.den)

    def __rmul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement reverse multiplication (*) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.num, self.den * other.den)

    def __imul__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement in-place multiplication (*=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.num, self.den * other.den)
        )
        return self

    def __truediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement division (/) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement reverse division (/) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return FractionV7(self.den * other.num, self.num * other.den)

    def __itruediv__(self, other: "FractionV7 | int") -> "FractionV7":
        """Implement in-place division (/=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        self.num, self.den = self.__simplify(
            (self.num * other.den, self.den * other.num)
        )
        return self

    def reverse(self) -> "FractionV7":
        """Reverses the fraction by swapping numerator and denominator."""
        self.num, self.den = self.__simplify((self.den, self.num))
        return self

    def __gt__(self, other: "FractionV7 | int") -> bool:
        """Implement greater than (>) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den > other.num / other.den

    def __ge__(self, other: "FractionV7 | int") -> bool:
        """Implement greater than or equal to (>=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other: "FractionV7 | int") -> bool:
        """Implement less than (<) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den < other.num / other.den

    def __le__(self, other: "FractionV7 | int") -> bool:
        """Implement less than or equal to (<=) operator."""
        if not isinstance(other, FractionV7):
            other = FractionV7(str(other))
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other: object) -> bool:
        """Implement equality (==) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den == other.num / other.den

    def __ne__(self, other: object) -> bool:
        """Implement inequality (!=) operator."""
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.num / self.den != other.num / other.den
