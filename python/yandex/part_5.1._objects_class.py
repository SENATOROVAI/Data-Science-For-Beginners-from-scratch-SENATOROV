"""5.1 Objects, class."""

# +
# Классная точка и Классная точка 2.0


class Point:
    """Класс для представления точки."""

    def __init__(self, coord_x: float, coord_y: float) -> None:
        """Инициализация точки."""
        self.x = coord_x
        self.y = coord_y

    def move(self, delta_x: float, delta_y: float) -> None:
        """Перемещение точки."""
        self.x += delta_x
        self.y += delta_y

    def length(self, other_point: "Point") -> float:
        """Расстояние до точки."""
        x_delta = self.x - other_point.x
        y_delta = self.y - other_point.y

        return float(round((x_delta**2 + y_delta**2) ** 0.5, 2))


# +
# Не нажимай красную кнопку!


class RedButton:
    """Класс красной кнопки."""

    def __init__(self) -> None:
        """Инициализация красной кнопки."""
        self.count_click = 0

    def click(self) -> None:
        """Вывод тревоги."""
        self.count_click += 1
        print("Тревога!")

    def count(self) -> int:
        """Возвращает количество нажатий."""
        return self.count_click


# +
# Работа не волк


class Programmer:
    """Класс программиста."""

    SALARY = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self, name: str, position: str) -> None:
        """Инициализирует программиста."""
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.base_salary = self.SALARY[position]
        self.senior_bonus = 0
        self.total_salary = 0

    def work(self, time: int) -> None:
        """Новая отработка."""
        self.hours_worked += time
        self.total_salary += time * (self.base_salary + self.senior_bonus)

    def rise(self) -> None:
        """Повышение программиста."""
        if self.position == "Junior":
            self.position = "Middle"
            self.base_salary = self.SALARY["Middle"]
        elif self.position == "Middle":
            self.position = "Senior"
            self.base_salary = self.SALARY["Senior"]
        elif self.position == "Senior":
            self.senior_bonus += 1

    def info(self) -> str:
        """Строка для бухгалтерии."""
        return f"{self.name} {self.hours_worked}ч. {self.total_salary}тгр."


# +
# Классный прямоугольник 3.0


class Rectangle:
    """Прямоугольник из двух точек."""

    def __init__(
        self, corner1: tuple[float, float], corner2: tuple[float, float]
    ) -> None:
        """Инициализация прямоугольника."""
        self.x1_coord, self.y1_coord = min(corner1[0], corner2[0]), max(
            corner1[1], corner2[1]
        )
        self.x2_coord, self.y2_coord = max(corner1[0], corner2[0]), min(
            corner1[1], corner2[1]
        )

    def width(self) -> float:
        """Возвращает ширину."""
        return round(abs(self.x2_coord - self.x1_coord), 2)

    def height(self) -> float:
        """Возвращает высоту."""
        return round(abs(self.y2_coord - self.y1_coord), 2)

    def perimeter(self) -> float:
        """Возврашает периметр."""
        return round(2 * (self.width() + self.height()), 2)

    def area(self) -> float:
        """Возвращает площадь."""
        return round(self.width() * self.height(), 2)

    def get_pos(self) -> tuple[float, float]:
        """Возвращает позицию."""
        return round(self.x1_coord, 2), round(self.y1_coord, 2)

    def get_size(self) -> tuple[float, float]:
        """Возвращает размеры."""
        return self.width(), self.height()

    def move(self, dx: float, dy: float) -> None:
        """Изменение положения."""
        self.x1_coord += dx
        self.y1_coord += dy
        self.x2_coord += dx
        self.y2_coord += dy

    def resize(self, width: float, height: float) -> None:
        """Изменение размера."""
        self.x2_coord = self.x1_coord + width
        self.y2_coord = self.y1_coord - height

    def turn(self) -> None:
        """Поворачивает прямоугольник на 90 градусов по часовой."""
        center_x = (self.x1_coord + self.x2_coord) / 2
        center_y = (self.y1_coord + self.y2_coord) / 2
        new_half_width = self.height() / 2
        new_half_height = self.width() / 2
        self.x1_coord = center_x - new_half_width
        self.x2_coord = center_x + new_half_width
        self.y1_coord = center_y + new_half_height
        self.y2_coord = center_y - new_half_height

    def scale(self, factor: float) -> None:
        """Масштабирование."""
        center_x = (self.x1_coord + self.x2_coord) / 2
        center_y = (self.y1_coord + self.y2_coord) / 2
        new_half_width = (self.width() * factor) / 2
        new_half_height = (self.height() * factor) / 2
        self.x1_coord = center_x - new_half_width
        self.x2_coord = center_x + new_half_width
        self.y1_coord = center_y + new_half_height
        self.y2_coord = center_y - new_half_height


# +
# Шашки


class Cell:
    """Клетка."""

    def __init__(self, status: str) -> None:
        """Инициализация клетки."""
        self._status = status

    def status(self) -> str:
        """Статус клетки."""
        return self._status


class Checkers:
    """Игральная доска."""

    def __init__(self) -> None:
        """Инициализация игральной доски."""
        self.cells = {}
        for row in range(8):
            for col in range(8):
                pos = chr(ord("A") + col) + str(8 - row)
                if row < 3 and (col + row) % 2 == 1:
                    self.cells[pos] = Cell("B")
                elif row > 4 and (col + row) % 2 == 1:
                    self.cells[pos] = Cell("W")
                else:
                    self.cells[pos] = Cell("X")

    def move(self, f_coord: str, t_coord: str) -> None:
        """Перемещение шашки."""
        self.cells[t_coord] = self.cells[f_coord]
        self.cells[f_coord] = Cell("X")

    def get_cell(self, p_coord: str) -> Cell:
        """Возвращает клетку."""
        return self.cells[p_coord]


# +
# Очередь


class Queue:
    """Очередь."""

    def __init__(self) -> None:
        """Инициализация очереди."""
        self.queue: list[str | int | float] = []

    def push(self, item: str | int | float) -> None:
        """Добавить элемент."""
        self.queue.append(item)

    def pop(self) -> str | int | float | None:
        """Вытащить первый элемент."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self) -> bool:
        """Проверка на пустоту."""
        return len(self.queue) == 0


# +
# Стек


class Stack:
    """Стек."""

    def __init__(self) -> None:
        """Инициализация стека."""
        self.stack: list[str | int | float] = []

    def push(self, item: str | int | float) -> None:
        """Добавление элемента."""
        self.stack.append(item)

    def pop(self) -> str | int | float | None:
        """Вытащить первый элемент."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self) -> bool:
        """Проверка стека на пустоту."""
        return len(self.stack) == 0
