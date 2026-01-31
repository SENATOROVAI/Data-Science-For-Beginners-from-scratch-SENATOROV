"""Using folium module to draw maps."""

# # Используем модуль folium для рисования карт

# [`Folium`](https://python-visualization.github.io/folium/index.html) - это библиотека, которая позволяет рисовать карты, маркеры, а также отмечать собственные данные.
#
# > Про установку см. [здесь](https://python-visualization.github.io/folium/installing.html)
#
# `Folium` позволяет выбирать поставщика карты, это определяет стиль и качество карты: для простоты рассмотрим [`OpenStreetMap`](https://ru.wikipedia.org/wiki/OpenStreetMap) (это значение по умолчанию).
#
# Начнем с основ, мы нарисуем простую карту, на которой ничего не будет.

# +
# # !pip install folium

# +
import json

import folium
import requests

m1 = folium.Map(
    location=[59.93, 30.33],
    tiles="openstreetmap",  # оно такое по умолчанию
    zoom_start=13,
)

m1
# -

# сохранение карты в html
m1.save("map1.html")

# Cоздали интерактивный файл с картой, который можно перемещать и масштабировать.
#
# > Результат HTML-документа можно увидеть [здесь](https://dfedorov.spb.ru/pandas/maps/map1.html).
#
# Можем добавить маркеры на карту:

# +
m2 = folium.Map(location=[59.93, 30.33], tiles="openstreetmap", zoom_start=14)

folium.Marker(
    location=[59.94, 30.35], popup="<i>Здесь был Вася</i>", tooltip="Метка 1"
).add_to(
    m2
)  # попробуйте добавить: icon=folium.Icon(icon="cloud")

folium.Marker(
    location=[59.92, 30.32],
    popup="<b>Хорошее кафе</b>",
    tooltip="Метка 2",
    icon=folium.Icon(color="green"),
).add_to(
    m2
)  # подкрасили метку на карте

folium.CircleMarker(
    location=[59.93, 30.33],
    radius=50,
    popup="Апраксин двор",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(
    m2
)  # добавили окружность

m2
# -

# сохранение карты в html
m2.save("map2.html")

# > Результат HTML-документа можно увидеть [здесь](https://dfedorov.spb.ru/pandas/maps/map2.html).
#
# `folium` позволяет передавать любой HTML объект в виде всплывающего окна, включая графики [`bokeh`](https://bokeh.pydata.org/en/latest), есть встроенная поддержка визуализаций [Altair](https://dfedorov.spb.ru/pandas/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B2%D0%B8%D0%B7%D1%83%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%20%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E%20Altair.html) для любого типа маркера в виде всплывающего окна.
#
# > Подробнее см. [здесь](https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Popups.ipynb).
#
# По умолчанию `tiles` установлено значение `OpenStreetMap`, но можно указать: `Stamen Terrain`, `Stamen Toner`.

# +
# pylint: disable=line-too-long


url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
vis = json.loads(requests.get(f"{url}/vis1.json").text)

# +
from folium import IFrame

m3 = folium.Map(
    location=[59.93, 30.33],
    zoom_start=14,
    tiles="https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap"
)

html = "<b>Hello!</b>"
iframe = IFrame(html, width=250, height=100)
popup = folium.Popup(iframe, max_width=450)

folium.Marker(
    location=[59.93, 30.33],
    popup=popup
).add_to(m3)

m3

# -

# сохранение карты в html
m3.save("map3.html")

# > Результат HTML-документа можно увидеть [здесь](https://dfedorov.spb.ru/pandas/maps/map3.html).
