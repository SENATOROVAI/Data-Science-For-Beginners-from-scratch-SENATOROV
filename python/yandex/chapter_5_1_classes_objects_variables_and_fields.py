"""Python Object Model.

Classes, Fields, and Methods.
"""

# +
# 1
from math import sqrt


class Point:
    """A class representing a point on a 2D plane."""

    def __init__(self, x_coord: float, y_coord: float) -> None:
        """Initialize the point with given x and y coordinates."""
        self.x_coord = x_coord
        self.y_coord = y_coord


# +
# 2


class Point2:
    """A class representing a point on a 2D plane."""

    def __init__(self, x_coord: float, y_coord: float) -> None:
        """Initialize the point with given x and y coordinates."""
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, x_coord: float, y_coord: float) -> None:
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


# +
# 3


class RedButton:
    """A class of a red button that counts clicks and triggers an alarm."""

    def __init__(self) -> None:
        """Initialize the red button with a click count of 0."""
        self.clicks_count = 0

    def click(self) -> None:
        """Trigger the alarm and increment the click count."""
        print("Тревога!")
        self.clicks_count += 1

    def count(self) -> int:
        """Return the total number of clicks."""
        return self.clicks_count


# +
# 4


class Programmer:
    """A class representing a programmer with defined fields."""

    SALARY = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self, name: str, position: str) -> None:
        """Initialize the programmer with given parameters."""
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.base_salary = self.SALARY[position]
        self.senior_bonus = 0
        self.total_salary = 0

    def work(self, time: int) -> None:
        """Increment the hours worked and update the total salary."""
        self.hours_worked += time
        self.total_salary += time * (self.base_salary + self.senior_bonus)

    def rise(self) -> None:
        """Promote the programmer to the next level and increase salary."""
        if self.position == "Junior":
            self.position = "Middle"
            self.base_salary = self.SALARY["Middle"]
        elif self.position == "Middle":
            self.position = "Senior"
            self.base_salary = self.SALARY["Senior"]
        elif self.position == "Senior":
            self.senior_bonus += 1

    def info(self) -> str:
        """Return a string with the programmer's information."""
        return f"{self.name} {self.hours_worked}ч. {self.total_salary}тгр."


# +
# 5


class Rectangle:
    """A class representing a rectangle with two corners."""

    def __init__(self, corn1: tuple[int, int], corn2: tuple[int, int]) -> None:
        """Initialize the rectangle with given corners."""
        self.x1_coord, self.y1_coord = corn1
        self.x2_coord, self.y2_coord = corn2

    def width(self) -> int:
        """Return the width of the rectangle."""
        return abs(self.x2_coord - self.x1_coord)

    def height(self) -> int:
        """Return the height of the rectangle."""
        return abs(self.y2_coord - self.y1_coord)

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return round(2 * (self.width() + self.height()), 2)

    def area(self) -> float:
        """Return the area of the rectangle."""
        return round(self.width() * self.height(), 2)


# +
# 6


class Rectangle1:
    """A class representing a rectangle with two corners."""

    def __init__(
        self, corner1: tuple[float, float], corner2: tuple[float, float]
    ) -> None:
        """Initialize the rectangle with given corners."""
        self.x1__coord, self.y1__coord = min(corner1[0], corner2[0]), max(
            corner1[1], corner2[1]
        )
        self.x2__coord, self.y2__coord = max(corner1[0], corner2[0]), min(
            corner1[1], corner2[1]
        )

    def width(self) -> float:
        """Return the width of the rectangle."""
        return round(abs(self.x2__coord - self.x1__coord), 2)

    def height(self) -> float:
        """Return the height of the rectangle."""
        return round(abs(self.y2__coord - self.y1__coord), 2)

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return round(2 * (self.width() + self.height()), 2)

    def area(self) -> float:
        """Return the area of the rectangle."""
        return round(self.width() * self.height(), 2)

    def get_pos(self) -> tuple[float, float]:
        """Return the position of the rectangle."""
        return round(self.x1__coord, 2), round(self.y1__coord, 2)

    def get_size(self) -> tuple[float, float]:
        """Return the size of the rectangle."""
        return self.width(), self.height()

    def move(self, dx: float, dy: float) -> None:
        """Move the rectangle by the given x and y coordinates."""
        self.x1__coord += dx
        self.y1__coord += dy
        self.x2__coord += dx
        self.y2__coord += dy

    def resize(self, width: float, height: float) -> None:
        """Resize the rectangle by the given width and height."""
        self.x2__coord = self.x1__coord + width
        self.y2__coord = self.y1__coord - height


# +
# 7


class Rectangle2:
    """A class representing a rectangle with two corners."""

    def __init__(
        self, corner1: tuple[float, float], corner2: tuple[float, float]
    ) -> None:
        """Initialize the rectangle with given corners."""
        self.x1_coord, self.y1_coord = min(corner1[0], corner2[0]), max(
            corner1[1], corner2[1]
        )
        self.x2_coord, self.y2_coord = max(corner1[0], corner2[0]), min(
            corner1[1], corner2[1]
        )

    def width(self) -> float:
        """Return the width of the rectangle."""
        return round(abs(self.x2_coord - self.x1_coord), 2)

    def height(self) -> float:
        """Return the height of the rectangle."""
        return round(abs(self.y2_coord - self.y1_coord), 2)

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return round(2 * (self.width() + self.height()), 2)

    def area(self) -> float:
        """Return the area of the rectangle."""
        return round(self.width() * self.height(), 2)

    def get_pos(self) -> tuple[float, float]:
        """Return the position of the rectangle."""
        return round(self.x1_coord, 2), round(self.y1_coord, 2)

    def get_size(self) -> tuple[float, float]:
        """Return the size of the rectangle."""
        return self.width(), self.height()

    def move(self, dx: float, dy: float) -> None:
        """Move the rectangle by the given x and y coordinates."""
        self.x1_coord += dx
        self.y1_coord += dy
        self.x2_coord += dx
        self.y2_coord += dy

    def resize(self, width: float, height: float) -> None:
        """Resize the rectangle by the given width and height."""
        self.x2_coord = self.x1_coord + width
        self.y2_coord = self.y1_coord - height

    def turn(self) -> None:
        """Turn the rectangle 90 degrees clockwise."""
        center_x = (self.x1_coord + self.x2_coord) / 2
        center_y = (self.y1_coord + self.y2_coord) / 2
        new_half_width = self.height() / 2
        new_half_height = self.width() / 2
        self.x1_coord = center_x - new_half_width
        self.x2_coord = center_x + new_half_width
        self.y1_coord = center_y + new_half_height
        self.y2_coord = center_y - new_half_height

    def scale(self, factor: float) -> None:
        """Scale the rectangle by the given factor."""
        center_x = (self.x1_coord + self.x2_coord) / 2
        center_y = (self.y1_coord + self.y2_coord) / 2
        new_half_width = (self.width() * factor) / 2
        new_half_height = (self.height() * factor) / 2
        self.x1_coord = center_x - new_half_width
        self.x2_coord = center_x + new_half_width
        self.y1_coord = center_y + new_half_height
        self.y2_coord = center_y - new_half_height


# +
# 8


class Cell:
    """A class representing a cell on a board."""

    def __init__(self, status: str) -> None:
        """Initialize the cell with given status."""
        self._status = status

    def status(self) -> str:
        """Return the status of the cell."""
        return self._status


class Checkers:
    """A class representing a checkers board."""

    def __init__(self) -> None:
        """Initialize the checkers board."""
        self.board = {}
        for row in range(8):
            for col in range(8):
                pos = chr(ord("A") + col) + str(8 - row)
                if row < 3 and (col + row) % 2 == 1:
                    self.board[pos] = Cell("B")
                elif row > 4 and (col + row) % 2 == 1:
                    self.board[pos] = Cell("W")
                else:
                    self.board[pos] = Cell("X")

    def move(self, f_coord: str, t_coord: str) -> None:
        """Move a piece from one cell to another."""
        self.board[t_coord] = self.board[f_coord]
        self.board[f_coord] = Cell("X")

    def get_cell(self, p_coord: str) -> Cell:
        """Return the cell at the given position."""
        return self.board[p_coord]


# +
# 9


class Queue:
    """A class representing a queue."""

    def __init__(self) -> None:
        """Initialize the queue."""
        self.items: list[str | int | float] = []

    def push(self, item: str | int | float) -> None:
        """Add an item to the queue."""
        self.items.append(item)

    def pop(self) -> str | int | float | None:
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0


# +
# 10


class Stack:
    """A class representing a stack."""

    def __init__(self) -> None:
        """Initialize the stack."""
        self.items: list[str | int | float] = []

    def push(self, item: str | int | float) -> None:
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self) -> str | int | float | None:
        """Remove and return the item at the top of the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0
