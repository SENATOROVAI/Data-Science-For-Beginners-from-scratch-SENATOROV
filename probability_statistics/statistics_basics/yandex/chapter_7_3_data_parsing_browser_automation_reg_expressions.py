"""Data parsing and browser automation, regular expressions."""

# ## Парсинг данных и автоматизация браузера, регулярные выражения

# +
# 1


import re

from bs4 import BeautifulSoup, Tag

with open("kinopoisk.html", encoding="utf-8") as file:
    html = file.read()
soup = BeautifulSoup(html, "html.parser")

if soup.title and isinstance(soup.title.text, str):
    title_text = soup.title.text
    print(title_text)

# +
# 2


print(title_text.strip().split("—")[0].strip())

# +
# 3


directors = [
    link.text.strip()
    for link in soup.find_all("a")
    if isinstance(link, Tag) and "/name/" in (link.get("href") or "")
]
if directors:
    print(directors[0])

# +
# 4


description_tag = soup.find("meta", attrs={"name": "description"})
if description_tag and isinstance(description_tag, Tag):
    description = description_tag.get("content")
    if isinstance(description, str):
        description = description.strip()
        print(description)

# +
# 5


description_tag = soup.find("meta", attrs={"name": "description"})
if description_tag and isinstance(description_tag, Tag):
    description = description_tag.get("content")
    if isinstance(description, str):
        description = description.strip()
        for word in re.findall(r"[А-ЯЁ][а-яё]+", description):
            print(word)

# +
# 6
# fmt: off


actors = soup.find_all(
    "li", 
    class_="styles_root__vKDSE styles_rootInLight__EFZzH"
)
print(len(actors))
# fmt: on

# +
# 7
# fmt: off


actors = soup.find_all(
    "li", 
    class_="styles_root__vKDSE styles_rootInLight__EFZzH"
)
for actor in actors:
    if isinstance(actor.text, str):
        print(actor.text)
# fmt: on

# +
# 8


a_tags = soup.find_all("a")
print(len(a_tags))

# +
# 9


a_tags = soup.find_all("a")
for tag in a_tags:
    if isinstance(tag, Tag):
        href = tag.get("href")
        if isinstance(href, str):
            print(href)
