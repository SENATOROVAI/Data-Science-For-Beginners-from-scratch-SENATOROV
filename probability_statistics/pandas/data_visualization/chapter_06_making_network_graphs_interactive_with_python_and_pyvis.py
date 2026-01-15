"""Making network graphs interactive with Python and Pyvis."""

# # Делаем сетевые графы интерактивными с помощью Python и Pyvis

# Библиотека [`pyvis`](https://pyvis.readthedocs.io/) предназначена для быстрой визуализации сетевых графиков с минимальным количеством кода на *Python*. Она разработана как обертка для популярной JavaScript библиотеки `visJS`, которую можно найти по [ссылке](https://visjs.github.io/vis-network/examples/).

# !pip install pyvis

# ## Начало
#
# Все сети должны быть созданы как экземпляры класса [`Network`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network):

# +
import networkx as nx
import pandas as pd
from pyvis.network import Network

net = Network(notebook=True)  # отображение в Блокноте включено
# -

# ## Добавить узлы в сеть

net.add_node(1, label="Node 1")  # node id = 1 и label = Node 1

net.add_node(2)  # node id и label = 2

# Здесь первым параметром метода [`add_node`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node) является идентификатор `ID` для `Node`. Он может быть строкой или числом. Аргумент `label` - это строка, которая будет явно прикреплена к узлу в окончательной визуализации. Если аргумент `label` не указан, то в качестве метки будет использоваться идентификатор узла.
#
# > Параметр *ID* должен быть уникальным.
#
# Вы также можете добавить список узлов:

nodes = ["a", "b", "c", "d"]

net.add_nodes(nodes)  # node ids и labels = ["a", "b", "c", "d"]

net.add_nodes("hello")  # node ids и labels = ["h", "e", "l", "o"]

# [`network.Network.add_nodes()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_nodes) добавляет в сеть несколько узлов из списка.
#
# ## Свойства узла
#
# Вызов [`add_node()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node) поддерживает различные свойства узла, которые можно установить индивидуально. Все эти свойства можно найти [здесь](https://visjs.github.io/vis-network/docs/network/nodes.html).
#
# Для прямого перевода этих атрибутов на *Python* обратитесь к документации [network.Network.add_node()](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node).
#
# > Не по вине *pyvis*, некоторые атрибуты в документации [*VisJS*](https://visjs.github.io/vis-network/docs/network/) работают не так, как ожидалось, или вообще не работают. *Pyvis* может преобразовывать элементы *JavaScript* для *VisJS*, но после этого все зависит от *VisJS*!
#
# ## Индексирование узла
#
# Используйте метод [`get_node()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_node) для определения узла по его идентификатору:

net.add_nodes(["a", "b", "c"])

net.get_node("c")

# ## Добавление списка узлов со свойствами
#
# При использовании метода [`network.Network.add_nodes()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_nodes) могут быть переданы необязательные ключевые аргументы для добавления свойств этим узлам. Допустимые свойства в этом случае:
#
# ```Python    
# ['size', 'value', 'title', 'x', 'y', 'label', 'color']
# ```
#
# Пример:

# +
g_var = Network(notebook=True)  # отображение в Блокноте

g_var.add_nodes(
    [1, 2, 3],
    value=[10, 100, 400],
    title=["I am node 1", "node 2 here", "and im node 3"],
    x=[21.4, 54.2, 11.2],
    y=[100.2, 23.54, 32.1],
    label=["NODE 1", "NODE 2", "NODE 3"],
    color=["#00ff1e", "#162347", "#dd4b39"],
)

g_var.show("basic.html")
# -

# Если навести курсор мыши на узел, то можно увидеть, что атрибут узла `title` отвечает за отображение данных при наведении курсора. Вы также можете добавить *HTML* код в строку `title`.
#
# Атрибут `color` может быть простым *HTML* цветом, например красным или синим. При необходимости можно указать полную спецификацию *rgba*. В документации [VisJS](https://visjs.github.io/vis-network/docs/network/) содержится более подробная информация.
#
# Подробная документация по дополнительным аргументам для узлов находится в документации метода [`network.Network.add_node()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_node).
#
# ## Ребра
#
# Предполагая, что существуют узлы сети, в соответствии с идентификатором узла могут быть добавлены ребра.

net.add_node(0, label="a")
net.add_node(1, label="b")
net.add_edge(0, 1)

# Ребра также могут содержать атрибут `weight`:

net.add_edge(0, 1, weight=0.87)

# Ребра можно настроить, а документацию по параметрам можно найти в документации метода [`network.Network.add_edge()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.add_edge) или обратившись к исходной документации [`VisJS`](https://visjs.github.io/vis-network/docs/network/edges.html).
#
# ## Интеграция с Networkx
#
# Простой способ визуализировать и строить сети в *pyvis* - использовать [`Networkx`](https://networkx.github.io/) и встроенный вспомогательный метод *pyvis* для перевода в граф *networkx*.
#
# Обратите внимание, что свойства узла *Networkx* с теми же именами, что и *pyvis* (например, `title`), транслируются непосредственно в атрибуты узла *pyvis* с соответствующим именем.

# +
nx_graph = nx.cycle_graph(10)

nx_graph.nodes[1]["title"] = "Number 1"
nx_graph.nodes[1]["group"] = 1
nx_graph.nodes[3]["title"] = "I belong to a different group!"
nx_graph.nodes[3]["group"] = 10

nx_graph.add_node(20, size=20, title="couple", group=2)
nx_graph.add_node(21, size=15, title="couple", group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label="lonely", title="lonely node", group=3)

nt = Network("500px", "500px", notebook=True)

nt.from_nx(nx_graph)
nt.show("nx.html")
# -

# ## Визуализация
#
# Отображение графика достигается одним вызовом метода [`network.Network.show()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.show) после построения базовой сети. Интерактивная визуализация представлена в виде статического *HTML* файла.

net.toggle_physics(True)  # включение физического взаимодействия
net.show("mygraph.html")

# Запуск метода [`toggle_physics()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.toggle_physics) позволяет более гибко взаимодействовать с графами.

net.toggle_physics(False)  # выключение физического взаимодействия
net.show("mygraph.html")

# ## Пример: визуализация сети персонажей Игры престолов
#
# Следующий блок кода является минимальным примером возможностей *pyvis*:

# +
got_net = Network(
    height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True
)

# установить физический макет сети
# https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.barnes_hut
got_net.barnes_hut()
got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")

sources = got_data["Source"]
targets = got_data["Target"]
weights = got_data["Weight"]

edge_data = zip(sources, targets, weights)

for e_var in edge_data:
    src = e_var[0]
    dst = e_var[1]
    w_var = e_var[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w_var)

# https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.get_adj_list
neighbor_map = got_net.get_adj_list()

# добавить данные о соседях в узлы
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("gameofthrones.html")
# -

# Атрибут `title` каждого узла отвечает за отображение данных при наведении курсора на узел.
#
# ## Использование пользовательского интерфейса конфигурации для динамической настройки параметров сети
#
# У вас также есть возможность снабдить визуализацию пользовательским интерфейсом, используемым для динамического изменения некоторых настроек, относящихся к вашей сети. Это может быть полезно для поиска наиболее оптимальных параметров графика и функции компоновки.

net.show_buttons(filter_=["physics"])
net.show("mygraph.html")

# Вы можете скопировать / вставить вывод, полученный с помощью кнопки *generate options* в приведенном выше пользовательском интерфейсе, в [`network.Network.set_options()`](https://pyvis.readthedocs.io/en/latest/documentation.html#pyvis.network.Network.set_options), чтобы завершить результаты экспериментов с настройками.
#
# > Оригинальная документация [тут](https://pyvis.readthedocs.io/en/latest/tutorial.html)
