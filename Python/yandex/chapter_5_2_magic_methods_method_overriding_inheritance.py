"""Magic methods, method overriding, inheritance."""

# +
# 1


from __future__ import annotations

# pylint: disable=too-many-lines
import math


class Point:
    """Represent a point in 2D space."""

    def __init__(self, x_var: int, y_var: int) -> None:
        """Initialize a point with the given x and y coordinates."""
        self.x_var = x_var
        self.y_var = y_var

    def move(self, new_x: int | Point, new_y: int | None = None) -> None:
        """Translate the point by the given x and y offsets."""
        if isinstance(new_x, Point) and new_y is None:
            self.x_var += new_x.x_var
            self.y_var += new_x.y_var
        elif isinstance(new_x, int) and isinstance(new_y, int):
            self.x_var += new_x
            self.y_var += new_y
        else:
            raise TypeError("Invalid arguments for move")

    def length(self, point: Point) -> float:
        """Return the Euclidean distance to another point."""
        if not isinstance(point, Point):
            raise TypeError("Argument must be an instance of Point")
        result = math.hypot(point.x_var - self.x_var, point.y_var - self.y_var)
        return round(result, 2)


class PatchedPoint(Point):
    """A 2D point with flexible initialization options."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Initialize a point with stated coordinates."""
        if len(args) == 0:
            x_var, y_var = 0, 0
        elif len(args) == 1:
            if isinstance(args[0], tuple) and len(args[0]) == 2:
                x_var, y_var = args[0]
            else:
                raise TypeError("Single argument must be a tuple of two integers")
        elif len(args) == 2:
            if all(isinstance(arg, int) for arg in args):
                x_var, y_var = args  # type: ignore[assignment]
            else:
                raise TypeError("Both arguments must be integers")
        else:
            raise ValueError("Too many arguments")

        super().__init__(x_var, y_var)


point_1 = PatchedPoint()
print(point_1.x_var, point_1.y_var)
point_1.move(2, -3)
print(point_1.x_var, point_1.y_var)

# +
# 2


class PatchedPoint2(Point):
    """Represent a point in 2D space with flexible initialization."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Initialize a point with discretional coordinates."""
        if len(args) == 0:
            x_var, y_var = 0, 0

        elif len(args) == 1:
            arg = args[0]
            if (
                isinstance(arg, tuple)
                and len(arg) == 2  # noqa: W503
                and all(isinstance(i, int) for i in arg)  # noqa: W503
            ):
                x_var, y_var = arg
            else:
                raise TypeError(
                    "Single argument must be a tuple of two integers (x, y), "
                    "e.g., PatchedPoint2((1, 2))"
                )

        elif len(args) == 2:
            if all(isinstance(i, int) for i in args):
                x_var, y_var = args  # type: ignore[assignment]
            else:
                types = tuple(type(i).__name__ for i in args)
                raise TypeError(f"Both arguments must be integers, got {types}")
        else:
            raise ValueError(
                f"Too many arguments for PatchedPoint2 "
                f"(expected 0, 1, or 2, got {len(args)})"
            )

        super().__init__(x_var, y_var)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the point."""
        return f"({self.x_var}, {self.y_var})"

    def __repr__(self) -> str:
        """Return the formal representation of the point."""
        return f"PatchedPoint2({self.x_var}, {self.y_var})"


point_2 = PatchedPoint2()
print(point_2)
point_2.move(2, -3)
print(repr(point_2))

# +
# 3


class PatchedPoint3(Point):
    """Represent a point in 2D space with extended functionality."""

    def __init__(self, *args: int | tuple[int, int]) -> None:
        """Initialize a point with discretional coordinates."""
        if len(args) == 0:
            x_var, y_var = 0, 0

        elif len(args) == 1:
            arg = args[0]
            if (
                isinstance(arg, tuple)
                and len(arg) == 2  # noqa: W503
                and all(isinstance(i, int) for i in arg)  # noqa: W503
            ):
                x_var, y_var = arg
            else:
                raise TypeError("Single argument must be a tuple of two integers")

        elif len(args) == 2:
            a0, a1 = args
            if isinstance(a0, int) and isinstance(a1, int):
                x_var, y_var = a0, a1
            else:
                raise TypeError("Both arguments must be integers")

        else:
            raise ValueError(
                "Too many arguments for PatchedPoint3 "
                f"(expected 0, 1, or 2, got {len(args)})"
            )

        super().__init__(x_var, y_var)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the point."""
        return f"({self.x_var}, {self.y_var})"

    def __repr__(self) -> str:
        """Return the formal representation of the point."""
        return f"PatchedPoint3({self.x_var}, {self.y_var})"

    def __add__(self, other: PatchedPoint3 | tuple[int, int]) -> PatchedPoint3:
        """Return a new point by adding the certain coordinates."""
        if isinstance(other, PatchedPoint3):
            return PatchedPoint3(self.x_var + other.x_var, self.y_var + other.y_var)
        if (
            isinstance(other, tuple)
            and len(other) == 2  # noqa: W503
            and all(isinstance(i, int) for i in other)  # noqa: W503
        ):
            return PatchedPoint3(self.x_var + other[0], self.y_var + other[1])
        raise TypeError(
            f"Unsupported operand type(s) for +: 'PatchedPoint3' "
            f"and '{type(other).__name__}'"
        )

    def __iadd__(self, other: PatchedPoint3 | tuple[int, int]) -> PatchedPoint3:
        """Add the coordinates of another point or tuple to current point."""
        if isinstance(other, PatchedPoint3):
            self.move(other.x_var, other.y_var)
        elif isinstance(other, tuple) and len(other) == 2:
            self.move(other[0], other[1])
        else:
            raise TypeError(
                "Operand must be a PatchedPoint3 or a tuple of two integers"
            )
        return self


point_3 = PatchedPoint3()
print(point_3)
new_point = point_3 + (2, -3)
print(point_3, new_point, point_3 is new_point)

# +
# 4


class Fraction1:
    """Represent a fraction and streamline it repeatedly."""

    def __init__(self, *args: str | int) -> None:
        """Initialize a Fraction object and streamline it."""
        if not args:
            raise ValueError("At least one argument required")

        if isinstance(args[0], str):
            parts = args[0].split("/")
            if len(parts) != 2:
                raise ValueError("String must be in format 'numerator/denominator'")
            num, den = map(int, parts)
        elif len(args) == 2 and all(isinstance(x, int) for x in args):
            num, den = args  # type: ignore[assignment]
        else:
            raise ValueError("Invalid arguments for Fraction")

        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        self.__num = num
        self.__den = den
        self.__reduction()

    @staticmethod
    def __gcd(a_var: int, b_var: int) -> int:
        """Compute the greatest common divisor (GCD) of two integers."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def __reduction(self) -> None:
        """Reduce the fraction and ensure the denominator is positive."""
        gcd = self.__gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd
        if self.__den < 0:
            self.__num *= -1
            self.__den *= -1

    def numerator(self, *args: int) -> int:
        """Get or set the numerator of the fraction."""
        if args:
            self.__num = args[0]
            self.__reduction()
        return self.__num

    def denominator(self, *args: int) -> int:
        """Get or set the denominator of the fraction."""
        if args:
            if args[0] == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.__den = args[0]
            self.__reduction()
        return self.__den

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self.__num}/{self.__den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction({self.__num}, {self.__den})"


fraction = Fraction1(3, 9)
print(fraction, repr(fraction))
fraction = Fraction1("7/14")
print(fraction, repr(fraction))

# +
# 5


class Fraction2:
    """A simplified fraction represented by a numerator and denominator."""

    def __init__(self, *args: str | int) -> None:
        """Create a Fraction object and streamline its value."""
        if not args:
            raise ValueError("At least one argument is required")

        if isinstance(args[0], str):
            parts = args[0].strip().split("/")
            if len(parts) != 2:
                raise ValueError("String must be in 'numerator/denominator' format")
            num, den = map(int, parts)
        elif len(args) == 2:
            num, den = args  # type: ignore[assignment]
        else:
            raise ValueError("Invalid number of arguments for Fraction")

        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        self.__num = num
        self.__den = den
        self.__reduction()

    def __sign(self) -> int:
        """Return sign of the fraction (-1 if negative, 1 if positive)."""
        return -1 if self.__num < 0 else 1

    @staticmethod
    def __gcd(a_var: int, b_var: int) -> int:
        """Compute the greatest common divisor (GCD) of two integers."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def __reduction(self) -> Fraction2:
        """Reduce the fraction and ensure the denominator is positive."""
        gcd = self.__gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = -self.__den
        return self

    def numerator(self, *args: int) -> int:
        """Get or set the numerator of the fraction."""
        if args:
            value = int(args[0])
            self.__num = abs(value) * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args: int) -> int:
        """Get or set the denominator of the fraction."""
        if args:
            value = int(args[0])
            if value == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.__den = abs(value)
            self.__reduction()
        return abs(self.__den)

    def __neg__(self) -> Fraction2:
        """Return negated fraction."""
        return Fraction2(-self.__num, self.__den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self.__num}/{self.__den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self.__num}/{self.__den}')"


a_smpl = Fraction2(1, 3)
b_smpl = Fraction2(-2, -6)
c_smpl = Fraction2(-3, 9)
d_smpl = Fraction2(4, -12)
print(a_smpl, b_smpl, c_smpl, d_smpl)
print(*map(repr, (a_smpl, b_smpl, c_smpl, d_smpl)))

# +
# 6


class Fraction3:
    """Represent a reduced fraction with integer numerator and denominator."""

    def __init__(self, numerator: int | str, denominator: int | None = None) -> None:
        """Initialize a Fraction from 'a/b' string or two integers."""
        if isinstance(numerator, str):
            self._num, self._den = map(int, numerator.split("/"))
        else:
            if denominator is None:
                raise ValueError("Denominator required when numerator is int")
            self._num, self._den = numerator, denominator

        if self._den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self._reduce()

    def _sign(self) -> int:
        """Return sign of fraction (-1 if negative, 1 if positive)."""
        return -1 if self._num < 0 else 1

    @staticmethod
    def _gcd(a_var: int, b_var: int) -> int:
        """Compute the greatest common divisor (GCD) of two integers."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def _reduce(self) -> None:
        """Reduce the fraction using GCD and normalize the sign."""
        gcd = self._gcd(self._num, self._den)
        self._num //= gcd
        self._den //= gcd
        if self._den < 0:
            self._num = -self._num
            self._den = -self._den

    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self._num

    @numerator.setter
    def numerator(self, value: int) -> None:
        """Set the numerator and reduce the fraction."""
        abs_value = abs(value)
        self._num = -abs_value if value < 0 else abs_value
        self._reduce()

    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction."""
        return self._den

    @denominator.setter
    def denominator(self, value: int) -> None:
        """Set the denominator and reduce the fraction."""
        if value == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        abs_value = abs(value)
        self._den = abs_value
        self._reduce()

    def __neg__(self) -> Fraction3:
        """Return the negated fraction."""
        return Fraction3(-self._num, self._den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self._num}/{self._den}')"

    def __add__(self, other: Fraction3) -> Fraction3:
        """Add another fraction or integer to current fraction."""
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Fraction3(new_num, new_den)

    def __iadd__(self, other: Fraction3) -> Fraction3:
        """Execute instant addition with another fraction or integer."""
        self._num = self._num * other._den + other._num * self._den
        self._den = self._den * other._den
        self._reduce()
        return self

    def __sub__(self, other: Fraction3) -> Fraction3:
        """Subtract another fraction or integer from current fraction."""
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Fraction3(new_num, new_den)

    def __isub__(self, other: Fraction3) -> Fraction3:
        """Execute instant subtraction with another fraction or integer."""
        self._num = self._num * other._den - other._num * self._den
        self._den = self._den * other._den
        self._reduce()
        return self


e_smpl = Fraction3(1, 3)
f_smpl = Fraction3(1, 2)
g_smpl = e_smpl + f_smpl
print(e_smpl, f_smpl, g_smpl, e_smpl is g_smpl, f_smpl is g_smpl)

# +
# 7


class Fraction4:
    """
    A class representing mathematical fractions with integer numerator and denominator.

    Supports basic arithmetic operations (+, -, *, /) and their in-place variants.
    Automatically reduces fractions to their simplest form.
    """

    def __init__(self, *args: int | str) -> None:
        """Initialize from string 'num/den' or two integers (num, den)."""
        if isinstance(args[0], str):
            self._num, self._den = (int(c) for c in args[0].split("/"))
        else:
            self._num = int(args[0])
            self._den = int(args[1])
        self._reduction()

    def _sign(self) -> int:
        """Return sign of fraction (-1 if negative, 1 if positive)."""
        return -1 if self._num < 0 else 1

    def _gcd(self, a_var: int, b_var: int) -> int:
        """Calculate greatest common divisor."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def _reduction(self) -> None:
        """Reduce fraction to simplest form."""
        gcd = self._gcd(self._num, self._den)
        self._num //= gcd
        self._den //= gcd

        if self._den < 0:
            self._num = -self._num
            self._den = -self._den

    def numerator(self, value: int | None = None) -> int:
        """Get or set the numerator of the fraction."""
        if value is not None:
            self._num = value * self._sign()
            self._reduction()
        return abs(self._num)

    def denominator(self, value: int | None = None) -> int:
        """Get or set the denominator of the fraction."""
        if value is not None:
            self._den = value
            self._reduction()
        return abs(self._den)

    def __neg__(self) -> Fraction4:
        """Return negated fraction."""
        return Fraction4(-self._num, self._den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self._num}/{self._den}')"

    def __add__(self, other: Fraction4) -> Fraction4:
        """Add another fraction or integer to current fraction."""
        num = self._num * other._den + other._num * self._den
        den = self._den * other._den
        return Fraction4(num, den)

    def __sub__(self, other: Fraction4) -> Fraction4:
        """Subtract another fraction or integer from current fraction."""
        num = self._num * other._den - other._num * self._den
        den = self._den * other._den
        return Fraction4(num, den)

    def __iadd__(self, other: Fraction4) -> Fraction4:
        """Execute instant addition with another fraction or integer."""
        self._num = self._num * other._den + other._num * self._den
        self._den = self._den * other._den
        self._reduction()
        return self

    def __isub__(self, other: Fraction4) -> Fraction4:
        """Execute instant subtraction with another fraction or integer."""
        self._num = self._num * other._den - other._num * self._den
        self._den = self._den * other._den
        self._reduction()
        return self

    def __mul__(self, other: Fraction4) -> Fraction4:
        """Multiply this fraction by another fraction or integer."""
        num = self._num * other._num
        den = self._den * other._den
        return Fraction4(num, den)

    def __imul__(self, other: Fraction4) -> Fraction4:
        """Execute instant multiplication with another fraction or integer."""
        self._num *= other._num
        self._den *= other._den
        self._reduction()
        return self

    def __truediv__(self, other: Fraction4) -> Fraction4:
        """Divide the current fraction by another fraction or an integer."""
        return self * other.reverse()

    def __itruediv__(self, other: Fraction4) -> Fraction4:
        """Execute instant division by another fraction or integer."""
        return self.__imul__(other.reverse())

    def reverse(self) -> Fraction4:
        """Return reversed fraction (reciprocal)."""
        return Fraction4(self._den, self._num)


h_smpl = Fraction4(1, 3)
i_smpl = Fraction4(1, 2)
j_smpl = h_smpl * i_smpl
print(h_smpl, i_smpl, j_smpl, h_smpl is j_smpl, i_smpl is j_smpl)

# +
# 8


class Fraction5:
    """Hybrid Fraction class combining best features from both implementations."""

    def __init__(self, *args: str | int) -> None:
        """Initialize with either string 'num/den' or numerator/denominator pair."""
        if isinstance(args[0], str):
            parts = args[0].split("/")
            self._num = int(parts[0])
            self._den = int(parts[1]) if len(parts) > 1 else 1
        else:
            self._num = int(args[0])
            self._den = int(args[1]) if len(args) > 1 else 1
        self._reduce_fraction()

    def gcd(self, a_var: int, b_var: int) -> int:
        """Compute the greatest common divisor (GCD) of two integers."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def _reduce_fraction(self) -> Fraction5:
        """Reduce fraction and ensure denominator is positive."""
        gcd_value = self.gcd(self._num, self._den)
        self._num //= gcd_value
        self._den //= gcd_value
        if self._den < 0:
            self._num *= -1
            self._den *= -1
        return self

    def numerator(self, value: int | None = None) -> int:
        """Get or set the numerator of the fraction."""
        if value is not None:
            self._num = value
            self._reduce_fraction()
        return abs(self._num)

    def denominator(self, value: int | None = None) -> int:
        """Get/set denominator with proper Optional type hint."""
        if value is not None:
            self._den = value
            self._reduce_fraction()
        return self._den

    def __neg__(self) -> Fraction5:
        """Return negated fraction."""
        return Fraction5(-self._num, self._den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self._num}/{self._den}')"

    def __add__(self, other: int | Fraction5) -> Fraction5:
        """Add another fraction or integer to current fraction."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        numerator = self._num * other._den + other._num * self._den
        denominator = self._den * other._den
        return Fraction5(numerator, denominator)._reduce_fraction()

    def __iadd__(self, other: int | Fraction5) -> Fraction5:
        """Execute instant addition with another fraction or integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._num = self._num * other._den + other._num * self._den
        self._den = self._den * other._den
        return self._reduce_fraction()

    def __sub__(self, other: int | Fraction5) -> Fraction5:
        """Subtract another fraction or integer from current fraction."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        numerator = self._num * other._den - other._num * self._den
        denominator = self._den * other._den
        return Fraction5(numerator, denominator)._reduce_fraction()

    def __isub__(self, other: int | Fraction5) -> Fraction5:
        """Execute instant subtraction with another fraction or integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._num = self._num * other._den - other._num * self._den
        self._den = self._den * other._den
        return self._reduce_fraction()

    def __mul__(self, other: int | Fraction5) -> Fraction5:
        """Multiply this fraction by another fraction or integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return Fraction5(
            self._num * other._num, self._den * other._den
        )._reduce_fraction()

    def __imul__(self, other: int | Fraction5) -> Fraction5:
        """Execute instant multiplication with another fraction or integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        self._num *= other._num
        self._den *= other._den
        return self._reduce_fraction()

    def __truediv__(self, other: int | Fraction5) -> Fraction5:
        """Divide the current fraction by another fraction or an integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self * other.reverse()

    def __itruediv__(self, other: int | Fraction5) -> Fraction5:
        """Execute instant division by another fraction or integer."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self.__imul__(other.reverse())

    def __gt__(self, other: int | Fraction5) -> bool:
        """Check if greater than."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self._num * other._den > other._num * self._den

    def __ge__(self, other: int | Fraction5) -> bool:
        """Check if greater than or equal."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self._num * other._den >= other._num * self._den

    def __lt__(self, other: int | Fraction5) -> bool:
        """Check if less than."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self._num * other._den < other._num * self._den

    def __le__(self, other: int | Fraction5) -> bool:
        """Check if less than or equal."""
        if isinstance(other, int):
            other = Fraction5(other, 1)
        return self._num * other._den <= other._num * self._den

    def __eq__(self, other: object) -> bool:
        """Check if equal."""
        if not isinstance(other, Fraction5):
            return NotImplemented
        return self._num * other._den == other._num * self._den

    def reverse(self) -> Fraction5:
        """Return reversed fraction (reciprocal)."""
        return Fraction5(self._den, self._num)


k_smpl = Fraction5(1, 3)
l_smpl = Fraction5(1, 2)
print(
    k_smpl > l_smpl,
    k_smpl < l_smpl,
    k_smpl >= l_smpl,
    k_smpl <= l_smpl,
    k_smpl == l_smpl,
    k_smpl >= l_smpl,
)

# +
# 9


class Fraction6:
    """Hybrid Fraction class combining best features from both implementations."""

    def __init__(self, *args: str | int) -> None:
        """Initialize with either string 'num/den' or numerator/denominator pair."""
        if isinstance(args[0], str):
            parts = args[0].split("/")
            self._num = int(parts[0])
            self._den = int(parts[1]) if len(parts) > 1 else 1
        else:
            self._num = int(args[0])
            self._den = int(args[1]) if len(args) > 1 else 1
        self._reduce_fraction()

    @staticmethod
    def gcd(a_var: int, b_var: int) -> int:
        """Calculate greatest common divisor of two integers."""
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        return abs(a_var)

    def _reduce_fraction(self) -> Fraction6:
        gcd_value = self.gcd(self._num, self._den)
        self._num = self._num // gcd_value
        self._den = self._den // gcd_value
        return self

    def numerator(self, value: int | None = None) -> int:
        """Get or set the numerator of the fraction."""
        if value is not None:
            self._num = value
            self._reduce_fraction()
        return abs(self._num)

    def denominator(self, value: int | None = None) -> int:
        """Get/set denominator with proper Optional type hint."""
        if value is not None:
            self._den = value
            self._reduce_fraction()
        return self._den

    def __neg__(self) -> Fraction6:
        """Return negated fraction."""
        return Fraction6(-self._num, self._den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self._num}/{self._den}')"

    def __add__(self, other: int | Fraction6) -> Fraction6:
        """Add another fraction or integer to current fraction."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        denominator = self._den * other._den
        numerator = self._num * other._den + other._num * self._den
        return Fraction6(numerator, denominator)._reduce_fraction()

    def __sub__(self, other: int | Fraction6) -> Fraction6:
        """Subtract another fraction or integer from current fraction."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        denominator = self._den * other._den
        numerator = self._num * other._den - other._num * self._den
        return Fraction6(numerator, denominator)._reduce_fraction()

    def __isub__(self, other: int | Fraction6) -> Fraction6:
        """Execute instant subtraction with another fraction or integer."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        self._num = self._num * other._den - other._num * self._den
        self._den = self._den * other._den
        return self._reduce_fraction()

    def __iadd__(self, other: int | Fraction6) -> Fraction6:
        """Execute instant addition with another fraction or integer."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        self._num = self._num * other._den + other._num * self._den
        self._den = self._den * other._den
        return self._reduce_fraction()

    def __mul__(self, other: Fraction6) -> Fraction6:
        """Multiply this fraction by another fraction or integer."""
        numerator = self._num * other._num
        denominator = self._den * other._den
        return Fraction6(numerator, denominator)._reduce_fraction()

    def __imul__(self, other: Fraction6) -> Fraction6:
        """Execute instant multiplication with another fraction or integer."""
        self._num *= other._num
        self._den *= other._den
        return self._reduce_fraction()

    def __truediv__(self, other: Fraction6) -> Fraction6:
        """Divide the current fraction by another fraction or an integer."""
        result = Fraction6(self._num, self._den)
        return result.__mul__(other.reverse())

    def __itruediv__(self, other: Fraction6) -> Fraction6:
        """Execute instant division by another fraction or integer."""
        return self.__imul__(other.reverse())

    def __gt__(self, other: int | Fraction6) -> bool:
        """Check if greater than."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return self._num * other._den > other._num * self._den

    def __ge__(self, other: int | Fraction6) -> bool:
        """Check if greater than or equal."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return self._num * other._den >= other._num * self._den

    def __lt__(self, other: int | Fraction6) -> bool:
        """Check if less than."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return self._num * other._den < other._num * self._den

    def __le__(self, other: int | Fraction6) -> bool:
        """Check if less than or equal."""
        if isinstance(other, int):
            other = Fraction6(other, 1)
        return self._num * other._den <= other._num * self._den

    def __eq__(self, other: object) -> bool:
        """Check if equal."""
        if not isinstance(other, Fraction6):
            return NotImplemented
        return self._num * other._den == other._num * self._den

    def reverse(self) -> Fraction6:
        """Return reversed fraction (reciprocal)."""
        return Fraction6(self._den, self._num)


m_smpl = Fraction6(1)
n_smpl = Fraction6("2")
o_smpl, p_smpl = map(Fraction6.reverse, (m_smpl + 2, n_smpl - 1))
print(m_smpl, n_smpl, o_smpl, p_smpl)
print(m_smpl > n_smpl, o_smpl > p_smpl)
print(m_smpl >= 1, n_smpl >= 1, o_smpl >= 1, p_smpl >= 1)

# +
# 10


class Fraction7:
    """Represent mathematical fractions with arithmetic operations."""

    def __init__(self, *args: int | str) -> None:
        """Initialize a fraction from certain values."""
        self._num: int = 0
        self._den: int = 1

        if len(args) == 1:
            if isinstance(args[0], str):
                parts = args[0].split("/")
                if len(parts) == 1:
                    self._num = int(parts[0])
                else:
                    self._num, self._den = map(int, parts)
            elif isinstance(args[0], int):
                self._num = args[0]
        elif len(args) == 2:
            self._num, self._den = int(args[0]), int(args[1])
        else:
            raise ValueError("Invalid arguments to Fraction constructor.")

        self._reduce_fraction((self._num, self._den))

    def _reduce_fraction(self, values: tuple[int, int]) -> None:
        """Simplify a fraction using the greatest common divisor (GCD)."""
        num, den = values
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        a_var, b_var = abs(num), abs(den)
        while b_var:
            a_var, b_var = b_var, a_var % b_var
        gcd = a_var
        num //= gcd
        den //= gcd
        if den < 0:
            num, den = -num, -den
        self._num, self._den = num, den

    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self._num

    @numerator.setter
    def numerator(self, value: int) -> None:
        """Set the numerator and reduce the fraction."""
        self._num = value
        self._reduce_fraction((self._num, self._den))

    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction."""
        return self._den

    @denominator.setter
    def denominator(self, value: int) -> None:
        """Set the denominator and reduce the fraction."""
        if value == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        self._den = value
        self._reduce_fraction((self._num, self._den))

    def __neg__(self) -> Fraction7:
        """Return negated fraction."""
        return Fraction7(-self._num, self._den)

    def __str__(self) -> str:
        """Return the user-friendly string representation of the fraction."""
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        """Return the formal representation of the fraction."""
        return f"Fraction('{self._num}/{self._den}')"

    def __add__(self, other: Fraction7 | int) -> Fraction7:
        """Add another fraction or integer to current fraction."""
        other = Fraction7(other) if isinstance(other, int) else other
        numerator = self._num * other._den + other._num * self._den
        denominator = self._den * other._den
        return Fraction7(numerator, denominator)

    def __radd__(self, other: Fraction7 | int) -> Fraction7:
        """Right-hand version of adding operation."""
        return self + other

    def __iadd__(self, other: Fraction7 | int) -> Fraction7:
        """Execute instant addition with another fraction or integer."""
        result = self + other
        self._num, self._den = result._num, result._den
        return self

    def __sub__(self, other: Fraction7 | int) -> Fraction7:
        """Subtract another fraction or integer from current fraction."""
        other = Fraction7(other) if isinstance(other, int) else other
        numerator = self._num * other._den - other._num * self._den
        denominator = self._den * other._den
        return Fraction7(numerator, denominator)

    def __rsub__(self, other: int | str) -> Fraction7:
        """Right-hand version of subtracting operation."""
        return Fraction7(other) - self

    def __isub__(self, other: Fraction7 | int) -> Fraction7:
        """Execute instant subtraction with another fraction or integer."""
        result = self - other
        self._num, self._den = result._num, result._den
        return self

    def __mul__(self, other: Fraction7 | int) -> Fraction7:
        """Multiply this fraction by another fraction or integer."""
        other = Fraction7(other) if isinstance(other, int) else other
        return Fraction7(self._num * other._num, self._den * other._den)

    def __rmul__(self, other: Fraction7 | int) -> Fraction7:
        """Right-hand version of multiplying operation."""
        return self * other

    def __imul__(self, other: Fraction7 | int) -> Fraction7:
        """Execute instant multiplication with another fraction or integer."""
        result = self * other
        self._num, self._den = result._num, result._den
        return self

    def __truediv__(self, other: Fraction7 | int) -> Fraction7:
        """Divide the current fraction by another fraction or an integer."""
        other = Fraction7(other) if isinstance(other, int) else other
        if other._num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Fraction7(self._num * other._den, self._den * other._num)

    def __rtruediv__(self, other: int | str) -> Fraction7:
        """Right-hand version of dividing operation."""
        return Fraction7(other) / self

    def __itruediv__(self, other: Fraction7 | int) -> Fraction7:
        """Execute instant division by another fraction or integer."""
        result = self / other
        self._num, self._den = result._num, result._den
        return self

    def __eq__(self, other: object) -> bool:
        """Check if equal."""
        if not isinstance(other, (Fraction7, int)):
            return NotImplemented
        other = Fraction7(other) if isinstance(other, int) else other
        return self._num * other._den == other._num * self._den

    def __ne__(self, other: object) -> bool:
        """Check if not equal."""
        if not isinstance(other, (Fraction7, int)):
            return NotImplemented
        return not self == other

    def __lt__(self, other: Fraction7 | int) -> bool:
        """Check if less than."""
        other = Fraction7(other) if isinstance(other, int) else other
        return self._num * other._den < other._num * self._den

    def __le__(self, other: Fraction7 | int) -> bool:
        """Check if less than or equal."""
        other = Fraction7(other) if isinstance(other, int) else other
        return self._num * other._den <= other._num * self._den

    def __gt__(self, other: Fraction7 | int) -> bool:
        """Check if greater than."""
        other = Fraction7(other) if isinstance(other, int) else other
        return self._num * other._den > other._num * self._den

    def __ge__(self, other: Fraction7 | int) -> bool:
        """Check if greater than or equal."""
        other = Fraction7(other) if isinstance(other, int) else other
        return self._num * other._den >= other._num * self._den

    def reverse(self) -> Fraction7:
        """Return reversed fraction (reciprocal)."""
        if self._num == 0:
            raise ZeroDivisionError("Cannot take reciprocal of zero.")
        return Fraction7(self._den, self._num)

    def __float__(self) -> float:
        """Return the float representation of the fraction."""
        return self._num / self._den

    def __int__(self) -> int:
        """Return the integer part of the fraction."""
        return self._num // self._den


q_smpl = Fraction7(1)
r_smpl = Fraction7("2")
s_smpl, t_smpl = map(Fraction7.reverse, (2 + q_smpl, -1 + r_smpl))
print(q_smpl, r_smpl, s_smpl, t_smpl)
print(q_smpl > r_smpl, s_smpl > t_smpl)
print(q_smpl >= 1, r_smpl >= 1, s_smpl >= 1, t_smpl >= 1)
