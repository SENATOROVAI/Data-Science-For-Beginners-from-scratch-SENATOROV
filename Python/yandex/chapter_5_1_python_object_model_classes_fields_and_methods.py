"""Python object model. Classes, fields and methods."""

# +
# 1


from collections import deque
from typing import Union


class Point1:
    """Represent a point in a two-dimensional space."""

    def __init__(self, x_pos: float, y_pos: float) -> None:
        """Create a point using specified x and y coordinates."""
        self.x_pos = x_pos
        self.y_pos = y_pos


point = Point1(3, 5)
print(point.x_pos, point.y_pos)

# +
# 2


class Point2:
    """Defines a point in a two-dimensional coordinate system."""

    def __init__(self, x_pos: float, y_pos: float) -> None:
        """Create a point with specified x and y positions."""
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, x_pos: float, y_pos: float) -> None:
        """Shift the point by the given x and y positions."""
        self.x_pos += x_pos
        self.y_pos += y_pos

    def length(self, point_: "Point2") -> float:
        """Return the distance from this point to another point."""
        result = (
            (point_.x_pos - self.x_pos) ** 2 + (point_.y_pos - self.y_pos) ** 2
        ) ** 0.5
        return float(round(result, 2))


point_2 = Point2(3, 5)
print(point_2.x_pos, point_2.y_pos)
point_2.move(2, -3)
print(point_2.x_pos, point_2.y_pos)

# +
# 3


class RedButton:
    """Represent a red button that tracks clicks and sounds an alarm."""

    def __init__(self) -> None:
        """Set up the button with the initial click count at zero."""
        self.counter = 0

    def click(self) -> None:
        """Sound an alarm and increase the click counter by one."""
        self.counter += 1
        print("Тревога!")

    def count(self) -> int:
        """Return how many times the button has been clicked."""
        return self.counter


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())

# +
# 4


class Programmer:
    """Represent a programmer with certain characteristics."""

    _base_wages = {
        "Junior": 10,
        "Middle": 15,
        "Senior": 20,
    }

    def __init__(self, name: str, position: str) -> None:
        """Initialize a programmer with a given name and position."""
        self.name = name
        self.position = position
        self.work_time = 0
        self.salary = 0
        self._senior_bonus = 0

        self.wage = self._base_wages[position]

    def work(self, time_: int) -> None:
        """Log worked hours and increase salary accordingly."""
        self.work_time += time_
        self.salary += self.wage * time_

    def rise(self) -> None:
        """Promote the programmer and adjust their wage or senior bonus."""
        if self.position == "Junior":
            self.position = "Middle"
            self.wage = self._base_wages["Middle"]
        elif self.position == "Middle":
            self.position = "Senior"
            self.wage = self._base_wages["Senior"]
        elif self.position == "Senior":
            self._senior_bonus += 1
            self.wage = self._base_wages["Senior"] + self._senior_bonus

    def info(self) -> str:
        """Return formatted string with work summary and total salary."""
        return f"{self.name} {self.work_time}ч. {self.salary}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

# +
# 5


class Rectangle1:
    """Define a rectangle by two corner points."""

    def __init__(self, *coords: tuple[float, float]) -> None:
        """Initialize the rectangle with two (x, y) coordinate tuples."""
        if len(coords) != 2:
            raise ValueError("Exactly two coordinate points required")
        (x1, y1), (x2, y2) = coords

        self.x1 = min(x1, x2)
        self.y1 = max(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = min(y1, y2)

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        width = self.x2 - self.x1
        height = self.y1 - self.y2
        return round(2 * (width + height), 2)

    def area(self) -> float:
        """Return the area of the rectangle."""
        width = self.x2 - self.x1
        height = self.y1 - self.y2
        return round(width * height, 2)


rect = Rectangle1((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

# +
# 6


class Rectangle2:
    """Represent a rectangle with two corners."""

    def __init__(
        self, corner1: tuple[float, float], corner2: tuple[float, float]
    ) -> None:
        """Construct a rectangle from two corner coordinates."""
        self.x1 = min(corner1[0], corner2[0])
        self.y1 = min(corner1[1], corner2[1])
        self.x2 = max(corner1[0], corner2[0])
        self.y2 = max(corner1[1], corner2[1])

    def perimeter(self) -> float:
        """Compute and return the perimeter of the rectangle."""
        return round(2 * (self.x2 - self.x1 + self.y2 - self.y1), 2)

    def area(self) -> float:
        """Compute and return the area of the rectangle."""
        return round((self.x2 - self.x1) * (self.y2 - self.y1), 2)

    def get_pos(self) -> tuple[float, float]:
        """Return the top-left corner position of the rectangle."""
        return round(self.x1, 2), round(self.y2, 2)

    def get_size(self) -> tuple[float, float]:
        """Return the rectangle's size as (width, height)."""
        return round(self.x2 - self.x1, 2), round(self.y2 - self.y1, 2)

    def move(self, dx: float, dy: float) -> None:
        """Shift the rectangle's position by the given x and y offsets."""
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy

    def resize(self, width: float, height: float) -> None:
        """Adjust the rectangle's size to the specified width and height."""
        self.x2 = self.x1 + width
        self.y1 = self.y2 - height


rect_2 = Rectangle2((3.2, -4.3), (7.52, 3.14))
print(rect_2.get_pos(), rect_2.get_size())
rect_2.move(1.32, -5)
print(rect_2.get_pos(), rect_2.get_size())

# +
# 7


class Rectangle3:
    """Represent a rectangle defined by two opposite corners."""

    def __init__(
        self, corner1: tuple[float, float], corner2: tuple[float, float]
    ) -> None:
        """Initialize the rectangle using two corner coordinates."""
        x1, y1 = corner1
        x2, y2 = corner2
        self.x = round(min(x1, x2), 2)
        self.y = round(max(y1, y2), 2)
        self.width = round(abs(x1 - x2), 2)
        self.height = round(abs(y1 - y2), 2)

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return float(round((self.width + self.height) * 2, 2))

    def area(self) -> float:
        """Return the area of the rectangle."""
        return float(round(self.width * self.height, 2))

    def get_pos(self) -> tuple[float, float]:
        """Return the top-left corner (position) of the rectangle."""
        return self.x, self.y

    def get_size(self) -> tuple[float, float]:
        """Return the current size (width and height) of the rectangle."""
        return self.width, self.height

    def move(self, dx: float, dy: float) -> None:
        """Move the rectangle by dx (horizontal) and dy (vertical)."""
        self.x = round(self.x + dx, 2)
        self.y = round(self.y + dy, 2)

    def resize(self, width: float, height: float) -> None:
        """Set a new width and height, keeping the top-left corner fixed."""
        self.width = round(width, 2)
        self.height = round(height, 2)

    def turn(self) -> None:
        """Rotate the rectangle 90° clockwise around its center."""
        cx = self.x + self.width / 2
        cy = self.y - self.height / 2
        self.width, self.height = self.height, self.width
        self.x = round(cx - self.width / 2, 2)
        self.y = round(cy + self.height / 2, 2)

    def scale(self, ratio: float) -> None:
        """Scale the rectangle by a given factor, keeping it centered."""
        cx = self.x + self.width / 2
        cy = self.y - self.height / 2
        self.width = round(self.width * ratio, 2)
        self.height = round(self.height * ratio, 2)
        self.x = round(cx - self.width / 2, 2)
        self.y = round(cy + self.height / 2, 2)


rect_3 = Rectangle3((3.14, 2.71), (-3.14, -2.71))
print(rect_3.get_pos(), rect_3.get_size(), sep="\n")
rect_3.turn()
print(rect_3.get_pos(), rect_3.get_size(), sep="\n")

# +
# 8


class Cell:
    """Represent a single cell on a checkers board."""

    def __init__(self, symbol: str = "X") -> None:
        """Initialize the cell with a given status."""
        self.value = symbol

    def status(self) -> str:
        """Get the current status of the cell."""
        return self.value

    def set_value(self, new_value: str) -> str:
        """Set a new value to the cell and return the previous one."""
        old = self.status()
        self.value = new_value
        return old

    def clear(self) -> str:
        """Clear the cell by setting its value to "X"."""
        previous = self.status()
        self.value = "X"
        return previous


class Checkers:
    """Represent an 8x8 checkers board and manages piece movements."""

    def __init__(self) -> None:
        """Initialize the checkers board."""
        self.desk = {}
        rows = "87654321"
        cols = "ABCDEFGH"
        for row in rows:
            for col in cols:
                position = col + row
                if (rows.index(row) + cols.index(col)) % 2 != 0:
                    if row in "876":
                        self.desk[position] = Cell("B")
                    elif row in "123":
                        self.desk[position] = Cell("W")
                    else:
                        self.desk[position] = Cell("X")
                else:
                    self.desk[position] = Cell("X")

    def move(self, source: str, destination: str) -> str:
        """Move a piece from one cell to another."""
        piece = self.desk[source].clear()
        return self.desk[destination].set_value(piece)

    def get_cell(self, position: str) -> Cell:
        """Retrieve the cell at the specified board coordinate."""
        return self.desk[position]


checkers = Checkers()
for row_ in "87654321":
    for col_ in "ABCDEFGH":
        print(checkers.get_cell(col_ + row_).status(), end="")
    print()

# +
# 9


class Queue:
    """A simple FIFO (first-in, first-out) queue implementation."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.queue: deque[Union[str, int, float]] = deque()

    def push(self, item_: Union[str, int, float]) -> None:
        """Insert an item at the end of the queue."""
        self.queue.append(item_)

    def pop(self) -> Union[str, int, float, None]:
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self) -> bool:
        """Check whether the queue has no items."""
        return not self.queue


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")

# +
# 10


class Stack:
    """A simple LIFO (last-in, first-out) stack implementation."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self.stack: list[str | int | float] = []

    def push(self, item_: str | int | float) -> None:
        """Add an item to the top of the stack."""
        self.stack.append(item_)

    def pop(self) -> str | int | float | None:
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self) -> bool:
        """Check whether the stack is empty."""
        return not self.stack


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
