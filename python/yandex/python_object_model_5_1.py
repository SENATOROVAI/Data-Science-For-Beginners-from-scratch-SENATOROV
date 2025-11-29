"""Объектная модель Python. Классы, поля и методы.

В этом параграфе вы сделаете первый шаг к объектно-ориентированному программированию —
подходу, который лежит в основе современных языков разработки, включая Python. Вы узнаете,
что такое классы и объекты, как создавать собственные типы данных и описывать поведение
объектов с помощью методов. Мы разберёмся с ключевыми понятиями ООП — атрибутами,
инкапсуляцией и полиморфизмом — и увидим, как они помогают писать более структурированный,
гибкий и масштабируемый код. На простом примере — модели автомобиля — вы научитесь
создавать классы, задавать свойства объектов, реализовывать действия и проектировать
интерфейс взаимодействия с объектами. Этот параграф станет основой для понимания более
сложных концепций ООП, с которыми вы познакомитесь в следующих частях главы.
"""

# ## Классная точка.
#
# - Объектно-ориентированное программирование — популярная парадигма в современном мире. Это вполне очевидно, ведь любой объект реального мира мы теперь можем представить в виде цифрового набора полей и методов. Давайте приступим к проектированию классов.
# - Разработайте класс Point, который при инициализации принимает координаты точки на декартовой плоскости и сохраняет их в поля x и y соответственно.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.

# +
from typing import Dict  # pylint: disable=unused-import
from typing import Optional, Union


class Point:
    """Класс для представления точки в 2D-пространстве."""

    def __init__(self, x_p: float, y_p: float) -> None:
        """Инициализирует точку с координатами x_p и y_p.

        Args:
            x_p: Координата по оси X
            y_p: Координата по оси Y
        """
        self.x = x_p
        self.y = y_p


# -

# ## Классная точка 2.0.
#
# - Давайте расширим функционал класса, написанного в прошлой задаче.
# - Реализуйте методы:
# - move, который перемещает точку на заданное расстояние по осям x и y;
# - length, который определяет до переданной точки расстояние, округлённое до сотых.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Point2D:
    """Класс для представления точки в 2D-пространстве."""

    def __init__(self, x_: Union[int, float], y_: Union[int, float]) -> None:
        """Инициализирует точку с координатами x_ и y_.

        Args:
            x_: Координата по оси X
            y_: Координата по оси Y
        """
        self.x_ = x_
        self.y_ = y_

    def move(self, dx: Union[int, float], dy: Union[int, float]) -> None:
        """Перемещает точку на dx по X и dy по Y."""
        self.x_ += dx
        self.y_ += dy

    def length(self, other: "Point2D") -> float:
        """Вычисляет расстояние до другой точки."""
        distance_ = ((self.x_ - other.x_) ** 2 + (self.y_ - other.y_) ** 2) ** 0.5
        result = round(distance_, 2)
        return float(result)


# ## Не нажимай красную кнопку!
#
# - Если написать предупреждение «Не нажимай красную кнопку!», то её сразу безумно хочется нажать.
# - Напишите класс RedButton, который описывает красную кнопку.
# - Класс должен реализовывать методы:
# - click() — эмулирует нажатие кнопки, выводит сообщение "Тревога!";
# - count() — возвращает количество раз, которое была нажата кнопка.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class RedButton:
    """Класс красной кнопки для вызова тревоги."""

    def __init__(self) -> None:
        """Инициализирует кнопку с нулевым счетчиком нажатий."""
        self.counter = 0

    def click(self) -> None:
        """Активирует тревогу и увеличивает счетчик."""
        print("Тревога!")
        self.counter += 1

    def count(self) -> int:
        """Возвращает количество нажатий."""
        return self.counter


# ## Работа не волк.
#
# - Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
# - Junior — с окладом 10 тугриков в час;
# - Middle — с окладом 15 тугриков в час;
# - Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
# - Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:
# - work(time) — отмечает новую отработку в количестве часов time;
# - rise() — повышает программиста;
# - info() — возвращает строку для бухгалтерии в формате:
# - <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Programmer:
    """Класс программиста с учетом рабочего времени и зарплаты."""

    def __init__(self, name: str, position: str) -> None:
        """Инициализирует программиста.

        Args:
            name: Имя программиста
            position: Должность (Junior/Middle/Senior)
        """
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.total_salary = 0
        self.salary_rate = self.get_initial_rate(position)
        self.promotions = 0

    def get_initial_rate(self, position: str) -> int:
        """Возвращает ставку зарплаты в зависимости от должности."""
        rates: dict[str, int] = {"Junior": 10, "Middle": 15, "Senior": 20}
        return rates[position]

    def work(self, time: int) -> None:
        """Учитывает отработанное время и начисляет зарплату."""
        self.hours_worked += time
        self.total_salary += time * self.salary_rate

    def rise(self) -> None:
        """Повышает должность или увеличивает ставку."""
        if self.position == "Junior":
            self.position = "Middle"
            self.salary_rate = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.salary_rate = 20
        else:
            self.promotions += 1
            self.salary_rate += 1

    def info(self) -> str:
        """Возвращает информацию о программисте."""
        return f"{self.name} {self.hours_worked}ч. {self.total_salary}тгр."


# ## Классный прямоугольник.
#
# - Давайте перейдём к более сложным геометрическим фигурам.
# - Разработайте класс Rectangle.
# - При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).
# - Класс должен реализовывать методы:
# - perimeter — возвращает периметр прямоугольника;
# - area — возвращает площадь прямоугольника.
# - Все результаты вычислений нужно округлить до сотых.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Rectangle:
    """Класс прямоугольника по координатам углов."""

    def __init__(self, first: tuple[float, float], second: tuple[float, float]) -> None:
        """Инициализирует прямоугольник по двум углам.

        Args:
            first: Первая точка (x1, y1)
            second: Вторая точка (x2, y2)
        """
        x1, y1 = first
        x2, y2 = second

        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        self.x1 = x1
        self.y1 = y1
        self.width = x2 - x1
        self.height = y2 - y1

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        p_per = 2 * (self.width + self.height)
        return round(p_per, 2)

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        a_area = self.width * self.height
        return round(a_area, 2)


# ## Классный прямоугольник 2.0.
#
# - Расширим функционал класса написанного вами в предыдущей задаче.
# - Реализуйте методы:
# - get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
# - get_size() — возвращает размеры в виде кортежа;
# - move(dx, dy) — изменяет положение на заданные значения;
# - resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Rectangle2:
    """Класс прямоугольника с возможностью перемещения и изменения размера."""

    def __init__(self, first: tuple[float, float], second: tuple[float, float]) -> None:
        """Инициализирует прямоугольник по двум углам.

        Args:
            first: Первая точка (x1, y1)
            second: Вторая точка (x2, y2)
        """
        x1, y1 = first
        x2, y2 = second

        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        self.x = x1
        self.y = y1
        self.width = x2 - x1
        self.height = y2 - y1

    def get_pos(self) -> tuple[float, float]:
        """Возвращает координаты левого верхнего угла."""
        return (round(self.x, 2), round(self.y, 2))

    def get_size(self) -> tuple[float, float]:
        """Возвращает размеры прямоугольника (ширина, высота)."""
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx: float, dy: float) -> None:
        """Перемещает прямоугольник на dx и dy."""
        self.x += dx
        self.y += dy

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника."""
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        p_2 = 2 * (self.width + self.height)
        return round(p_2, 2)

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        a_2 = self.width * self.height
        return round(a_2, 2)


# ## Классный прямоугольник 3.0.
#
# - Необходимо ещё немного доработать предыдущую задачу.
# - Разработайте методы:
# - turn() — поворачивает прямоугольник на 90° по часовой стрелке вокруг его центра;
# - scale(factor) — изменяет размер в указанное количество раз, тоже относительно центра.
# - Все вычисления производить с округлением до сотых.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Rectangle3:
    """Класс прямоугольника с методами трансформации."""

    def __init__(
        self, coord1: tuple[float, float], coord2: tuple[float, float]
    ) -> None:
        """Инициализирует прямоугольник по двум углам.

        Args:
            coord1: Первая координата (x, y)
            coord2: Вторая координата (x, y)
        """
        self.left = min(coord1[0], coord2[0])
        self.top = max(coord1[1], coord2[1])
        self.right = max(coord1[0], coord2[0])
        self.bottom = min(coord1[1], coord2[1])
        self.width = round(abs(coord1[0] - coord2[0]), 2)
        self.height = round(abs(coord1[1] - coord2[1]), 2)
        self._flag = False

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return round(
            abs(self.left - self.right) * 2 + abs(self.top - self.bottom) * 2, 2
        )

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return round(abs(self.left - self.right) * abs(self.top - self.bottom), 2)

    def get_pos(self) -> tuple[float, float]:
        """Возвращает позицию левого верхнего угла."""
        return (self.left, self.top)

    def get_size(self) -> tuple[float, float]:
        """Возвращает размеры прямоугольника."""
        if self._flag:
            return (self.width, self.height)
        return (
            round(abs(self.left - self.right), 2),
            round(abs(self.top - self.bottom), 2),
        )

    def resize(self, width: float, height: float) -> None:
        """Изменяет размеры прямоугольника."""
        self._flag = False
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top + height, 2)
        self.width, self.height = width, height

    def turn(self) -> None:
        """Поворачивает прямоугольник на 90 градусов."""
        self._flag = False
        width, height = self.get_size()
        delta = (width - height) / 2
        self.left = round(self.left + delta, 2)
        self.right = round(self.right - delta, 2)
        self.top = round(self.top + delta, 2)
        self.bottom = round(self.bottom - delta, 2)
        self.width, self.height = self.height, self.width

    def scale(self, factor: float) -> None:
        """Масштабирует прямоугольник на заданный коэффициент."""
        self._flag = False
        width, height = self.get_size()

        if abs(width - self.width) <= 0.01:
            width = self.width
        if abs(height - self.height) <= 0.02:
            height = self.height

        self.left = round(self.left - (factor * width - width) / 2, 2)
        self.top = round(self.top + (factor * height - height) / 2, 2)
        width = round(width * factor, 2)
        height = round(height * factor, 2)
        self.right = round(self.left + width, 2)
        self.bottom = round(self.top - height, 2)
        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)


# ## Шашки.
#
# - Шашки очень занимательная игра, которую достаточно легко моделировать.
# - Правила подразумевают наличие двух классов: игральная доска и шашка. Однако мы немного упростим себе задачу и вместо шашки будем манипулировать клетками, которые могут находиться в трех состояниях: пустая, белая шашка и чёрная шашка.
# - Разработайте два класса: Checkers и Cell.
# - Объекты класса Checkers при инициализации строят игральную доску со стандартным распределением клеток и должны обладать методами:
# - move(f, t) — перемещает шашку из позиции f в позицию t;
# - get_cell(p) — возвращает объект «клетка» в позиции p.
# - Объекты класса Cell при инициализации принимают одно из трех состояний: W — белая шашка, B — чёрная шашка, * — пустая клетка, а также обладают методом status() возвращающим заложенное в ней состояние.
# - Координаты клеток описываются строками вида PQ, где:
# - P — столбец игральной доски, одна из заглавных латинских букв: ABCDEFGH;
# - Q — строка игральной доски, одна из цифр: 12345678.
# - Будем считать, что пользователь всегда ходит правильно и контролировать возможность хода не требуется.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


# +
class Checkers:
    """Класс для игры в шашки."""

    def __init__(self) -> None:
        """Инициализирует доску для шашек."""
        self.board: dict[str, Cell] = {}
        for row in range(8):
            for col in range(8):
                pos = self._get_position_name(col, row)
                if row < 3 and (row + col) % 2 == 1:
                    self.board[pos] = Cell("B")
                elif row > 4 and (row + col) % 2 == 1:
                    self.board[pos] = Cell("W")
                else:
                    self.board[pos] = Cell("X")

    def _get_position_name(self, col: int, row: int) -> str:
        """Возвращает имя позиции по координатам."""
        letters = "ABCDEFGH"
        return letters[col] + str(8 - row)

    def _parse_position(self, pos: str) -> tuple[int, int]:
        """Парсит имя позиции в координаты."""
        col = ord(pos[0]) - ord("A")
        row = 8 - int(pos[1])
        return col, row

    def move(self, f_: str, t_: str) -> None:
        """Перемещает шашку с позиции f_ на позицию t_."""
        piece = self.board[f_].status()
        self.board[f_] = Cell("X")
        self.board[t_] = Cell(piece)

    def get_cell(self, p_: str) -> Cell:
        """Возвращает ячейку по позиции."""
        return self.board[p_]


class Cell:
    """Класс ячейки на доске."""

    def __init__(self, status: str) -> None:
        """Инициализирует ячейку.

        Args:
            status: Статус ячейки ('W', 'B' или 'X')
        """
        self._status = status

    def status(self) -> str:
        """Возвращает статус ячейки."""
        return self._status


# -

# ## Очередь.
#
# - В программировании существует потребность не только в изученных нами коллекциях. Одна из таких очередь. Она реализует подход к хранению данных по принципу «Первый вошёл – первый ушел».
# - Реализуйте класс Queue, который не имеет параметров инициализации, но поддерживает методы:
# - push(item) — добавить элемент в конец очереди;
# - pop() — «вытащить» первый элемент из очереди;
# - is_empty() — проверят очередь на пустоту.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Queue:
    """Класс очереди (FIFO)."""

    def __init__(self) -> None:
        """Инициализирует пустую очередь."""
        self.items: list[object] = []

    def push(self, item: object) -> None:
        """Добавляет элемент в конец очереди."""
        self.items.append(item)

    def pop(self) -> Optional[object]:
        """Удаляет и возвращает первый элемент очереди."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь."""
        return len(self.items) == 0


# ## Стек.
#
# - Ещё одной полезной коллекцией является стек реализующий принцип «Последний пришёл – первый ушёл». Его часто представляют как стопку карт или магазин пистолета, где приходящие элементы закрывают выход уже находящимся в коллекции.
# - Реализуйте класс Stack, который не имеет параметров инициализации, но поддерживает методы:
# - push(item) — добавить элемент в конец стека;
# - pop() — «вытащить» первый элемент из стека;
# - is_empty() — проверяет стек на пустоту.
# - Примечание
# - Ваше решение должно содержать только классы и функции.
# - В решении не должно быть вызовов инициализации требуемых классов.


class Stack:
    """Класс стека (LIFO)."""

    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self.items: list[object] = []

    def push(self, item: object) -> None:
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self) -> Optional[object]:
        """Удаляет и возвращает элемент с вершины стека."""
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0
