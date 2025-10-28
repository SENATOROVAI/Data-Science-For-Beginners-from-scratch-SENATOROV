"""Yandex handbook "Python Basics" answers."""

# +
from typing import Union

# 1


class Point1:
    """Представляет точку в двумерном пространстве."""

    def __init__(self, x_pos: float, y_pos: float) -> None:
        """Создает точку с указанными координатами x и y."""
        self.x_pos = x_pos
        self.y_pos = y_pos


# -

# 2
class Point2:
    """Представляет точку в двумерном пространстве с методами перемещения."""

    def __init__(self, x_pos: float, y_pos: float) -> None:
        """Создает точку с указанными координатами x и y."""
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, shift_x: float, shift_y: float) -> None:
        """Перемещает точку на указанные смещения."""
        self.x_pos += shift_x
        self.y_pos += shift_y

    def length(self, other_point: 'Point2') -> float:
        """Вычисляет расстояние до другой точки."""
        dx = (self.x_pos - other_point.x_pos) ** 2
        dy = (self.y_pos - other_point.y_pos) ** 2
        distance = (dx + dy) ** 0.5
        result: float = round(distance, 2)
        return result


# 3
class RedButton:
    """Реализует красную кнопку с счетчиком нажатий."""

    def __init__(self) -> None:
        """Инициализирует кнопку с нулевым счетчиком."""
        self.counter = 0

    def click(self) -> None:
        """Обрабатывает нажатие кнопки и выводит сообщение."""
        print("Тревога!")
        self.counter += 1

    def count(self) -> int:
        """Возвращает количество нажатий."""
        return self.counter


# 4
class Programmer:
    """Представляет программиста с учетом его позиции и работы."""

    def __init__(self, name: str, position: str = "Junior") -> None:
        """Создает программиста с указанным именем и позицией."""
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.money = 0
        self.overrises = 0

    def work(self, time: int) -> None:
        """Регистрирует отработанные часы и начисляет оплату."""
        rates = {
            "Junior": 10,
            "Middle": 15,
            "Senior": 20,
        }
        self.hours_worked += time
        self.money += time * (rates[self.position] + self.overrises)

    def rise(self) -> None:
        """Повышает позицию программиста или увеличивает надбавку."""
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.overrises += 1

    def info(self) -> str:
        """Возвращает информацию о программисте."""
        return f"{self.name} {self.hours_worked}ч. {self.money}тгр."


# 5
class Rectangle5:
    """Представляет прямоугольник по двум координатам."""

    def __init__(self, *coords: tuple[float, float]) -> None:
        """Создает прямоугольник по двум противоположным координатам."""
        self.coords = coords
        self.first_line = abs(self.coords[0][0] - self.coords[1][0])
        self.second_line = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return round(2 * (self.first_line + self.second_line), 2)

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return round(self.first_line * self.second_line, 2)


# 6
class Rectangle6:
    """Представляет прямоугольник с возможностями перемещения и изменения."""

    def __init__(self, *coords: tuple[float, float]) -> None:
        """Создает прямоугольник по двум противоположным координатам."""
        self._update_attributes(coords)

    def _update_attributes(self, coords: tuple[tuple[float, float], ...]
                           ) -> None:
        """Обновляет атрибуты прямоугольника на основе новых координат."""
        self.coords = coords
        self.upper_left_x = round(min(self.coords[0][0], self.coords[1][0]), 2)
        self.upper_left_y = round(max(self.coords[0][1], self.coords[1][1]), 2)
        self.lower_right_x = round(
            max(self.coords[0][0], self.coords[1][0]), 2)
        self.lower_right_y = round(
            min(self.coords[0][1], self.coords[1][1]), 2)
        self.width = abs(self.coords[0][0] - self.coords[1][0])
        self.height = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return round(2 * (self.width + self.height), 2)

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return round(self.width * self.height, 2)

    def get_pos(self) -> tuple[float, float]:
        """Возвращает координаты верхнего левого угла."""
        return self.upper_left_x, self.upper_left_y

    def get_size(self) -> tuple[float, float]:
        """Возвращает размеры прямоугольника."""
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx: float, dy: float) -> None:
        """Перемещает прямоугольник на указанные смещения."""
        new_coords = (
            (self.coords[0][0] + dx, self.coords[0][1] + dy),
            (self.coords[1][0] + dx, self.coords[1][1] + dy),
        )
        self._update_attributes(new_coords)

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника."""
        new_coords = (
            self.get_pos(),
            (self.upper_left_x + width, self.upper_left_y - height),
        )
        self._update_attributes(new_coords)


# 7
class Rectangle7:
    """Представляет прямоугольник с дополнительными операциями."""

    def __init__(
        self, coord1: tuple[float, float], coord2: tuple[float, float]
    ) -> None:
        """Создает прямоугольник по двум координатам."""
        self.left: float = 0.0
        self.top: float = 0.0
        self.right: float = 0.0
        self.bottom: float = 0.0
        self.width: float = 0.0
        self.height: float = 0.0
        self._update_attributes(coord1, coord2)

    def _update_attributes(
        self, coord1: tuple[float, float], coord2: tuple[float, float]
    ) -> None:
        """Обновляет атрибуты прямоугольника."""
        self.left = min(coord1[0], coord2[0])
        self.top = max(coord1[1], coord2[1])
        self.right = max(coord1[0], coord2[0])
        self.bottom = min(coord1[1], coord2[1])
        self.width = round(abs(coord1[0] - coord2[0]), 2)
        self.height = round(abs(coord1[1] - coord2[1]), 2)

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return round(
            abs(self.left - self.right) * 2 + abs(
                self.top - self.bottom) * 2, 2
        )

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return round(abs(self.left - self.right) * abs(
            self.top - self.bottom), 2)

    def get_pos(self) -> tuple[float, float]:
        """Возвращает координаты верхнего левого угла."""
        return self.left, self.top

    def get_size(self) -> tuple[float, float]:
        """Возвращает размеры прямоугольника."""
        return (
            round(abs(self.left - self.right), 2),
            round(abs(self.top - self.bottom), 2),
        )

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника."""
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top - height, 2)
        self.width, self.height = width, height

    def turn(self) -> None:
        """Поворачивает прямоугольник на 90 градусов."""
        width, height = self.get_size()
        delta = (width - height) / 2
        self.left = round(self.left + delta, 2)
        self.right = round(self.right - delta, 2)
        self.top = round(self.top + delta, 2)
        self.bottom = round(self.bottom - delta, 2)
        self.width, self.height = height, width

    def scale(self, factor: float) -> None:
        """Масштабирует прямоугольник на указанный коэффициент."""
        width, height = self.get_size()
        new_width = round(width * factor, 2)
        new_height = round(height * factor, 2)

        delta_x = (new_width - width) / 2
        delta_y = (new_height - height) / 2

        self.left = round(self.left - delta_x, 2)
        self.right = round(self.right + delta_x, 2)
        self.top = round(self.top + delta_y, 2)
        self.bottom = round(self.bottom - delta_y, 2)
        self.width, self.height = new_width, new_height


# +
# 8
class Checkers:
    """Представляет игру в шашки."""

    def __init__(self) -> None:
        """Инициализирует начальную расстановку шашек."""
        self.desk = {
            "A": {
                "8": "X",
                "7": "B",
                "6": "X",
                "5": "X",
                "4": "X",
                "3": "W",
                "2": "X",
                "1": "W",
            },
            "B": {
                "8": "B",
                "7": "X",
                "6": "B",
                "5": "X",
                "4": "X",
                "3": "X",
                "2": "W",
                "1": "X",
            },
            "C": {
                "8": "X",
                "7": "B",
                "6": "X",
                "5": "X",
                "4": "X",
                "3": "W",
                "2": "X",
                "1": "W",
            },
            "D": {
                "8": "B",
                "7": "X",
                "6": "B",
                "5": "X",
                "4": "X",
                "3": "X",
                "2": "W",
                "1": "X",
            },
            "E": {
                "8": "X",
                "7": "B",
                "6": "X",
                "5": "X",
                "4": "X",
                "3": "W",
                "2": "X",
                "1": "W",
            },
            "F": {
                "8": "B",
                "7": "X",
                "6": "B",
                "5": "X",
                "4": "X",
                "3": "X",
                "2": "W",
                "1": "X",
            },
            "G": {
                "8": "X",
                "7": "B",
                "6": "X",
                "5": "X",
                "4": "X",
                "3": "W",
                "2": "X",
                "1": "W",
            },
            "H": {
                "8": "B",
                "7": "X",
                "6": "B",
                "5": "X",
                "4": "X",
                "3": "X",
                "2": "W",
                "1": "X",
            },
        }

    def move(self, from_cell: str, to_cell: str) -> None:
        """Перемещает шашку с одной клетки на другую."""
        self.desk[from_cell[0]][from_cell[1]], self.desk[
            to_cell[0]][to_cell[1]] = (
            self.desk[to_cell[0]][to_cell[1]],
            self.desk[from_cell[0]][from_cell[1]],
        )

    def get_cell(self, position: str) -> "Cell":
        """Возвращает объект клетки по указанным координатам."""
        return Cell(self.desk[position[0]][position[1]])


class Cell:
    """Представляет клетку на доске."""

    def __init__(self, coords: str) -> None:
        """Создает клетку с указанным статусом."""
        self.coords = coords

    def status(self) -> str:
        """Возвращает статус клетки."""
        return self.coords


# -

# 9
class Queue9:
    """Реализует структуру данных очередь."""

    def __init__(self) -> None:
        """Инициализирует пустую очередь."""
        self.items: list[Union[str, int, float]] = []

    def push(self, item: Union[str, int, float]) -> None:
        """Добавляет элемент в очередь."""
        self.items.append(item)

    def pop(self) -> Union[str, int, float]:
        """Удаляет и возвращает первый элемент очереди."""
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь."""
        return not self.items


# 10
class Stack10:
    """Реализует структуру данных стек."""

    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self.items: list[Union[str, int, float]] = []

    def push(self, item: Union[str, int, float]) -> None:
        """Добавляет элемент в стек."""
        self.items.append(item)

    def pop(self) -> Union[str, int, float]:
        """Удаляет и возвращает верхний элемент стека."""
        return self.items.pop()

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return not self.items
