"""Requests module."""

# +
# 1


import json
from collections import OrderedDict
from json.decoder import JSONDecodeError

from requests import delete, get, post, put

response = get("http://127.0.0.1:5000/")

answer = response.content.decode("utf-8")

print(answer)

# +
# 2


address = input().strip()

total = 0

while True:
    response = get(f"http://{address}/")

    number = int(response.content.decode("utf-8"))

    if number == 0:
        break

    total += number

print(total)

# +
# 3


address = input()
response = get(f"http://{address}/")

numbers = [x for x in response.json() if isinstance(x, int)]

print(sum(numbers))

# +
# 4


address = input().strip()
key = input().strip()

response = get(f"http://{address}/")
data = response.json()

print(data.get(key, "No data"))

# +
# 5


address = input().strip()

paths = []
try:
    while True:
        line = input().strip()
        if line:
            paths.append(line)
        else:
            break
except EOFError:
    pass

all_numbers = []

for path in paths:
    url = f"http://{address}{path}"
    data = get(url).json()
    all_numbers.extend(data)

print(sum(all_numbers))

# +
# 6



address = input().strip()

url = f"http://{address}/users/"
response = get(url)

users = get(url).json()

full_names = [f"{u['last_name']} {u['first_name']}" for u in users]

full_names.sort()

for name in full_names:
    print(name)

# +
# 7



address = input().strip()

user_id = input().strip()

message_lines = []
while True:
    line = input()
    message_lines.append(line)
    if line.strip() == "С уважением, команда тестового сервера!":
        break

message_template = "\n".join(message_lines)

url = f"http://{address}/users/{user_id}"
response = get(url)

if response.status_code == 404:
    print("Пользователь не найден")
else:
    try:
        user = response.json()
        message = message_template.format(**user)
        print(message)
    except JSONDecodeError as e:
        print("Ошибка при декодировании JSON:", e)

# +
# 8



address = input().strip()
username = input().strip()
last_name = input().strip()
first_name = input().strip()
email = input().strip()

user = {
    "username": username,
    "last_name": last_name,
    "first_name": first_name,
    "email": email,
}

url = f"http://{address}/users/"

response_post = post(url, json=user)

if response_post.status_code == 201:
    response_get = get(url)
    if response_get.status_code == 200:
        users = json.loads(response_get.text, object_pairs_hook=OrderedDict)
        print(json.dumps(users, ensure_ascii=False, indent=4))
    else:
        print(f"Ошибка при получении списка пользователей: {response_get.status_code}")
else:
    print(f"Ошибка при добавлении пользователя: {response_post.status_code}")

# +
# 9



address = input().strip()
user_id = input().strip()

user = {}
while True:
    try:
        line = input().strip()
        if not line:
            break
        key, value = line.split("=", 1)
        user[key] = value
    except EOFError:
        break

url = f"http://{address}/users/{user_id}"

response_put = put(url, json=user)

if response_put.status_code == 200:
    response_get = get(f"http://{address}/users/")
    if response_get.status_code == 200:
        users = response_get.json()
        print(json.dumps(users, ensure_ascii=False, indent=4))
    else:
        print(f"Ошибка при получении списка пользователей: {response_get.status_code}")
else:
    print(f"Ошибка при обновлении пользователя: {response_put.status_code}")

# +
# 10



address = input().strip()
user_id = input().strip()

url = f"http://{address}/users/{user_id}"

response_del = delete(url)

if response_del.status_code == 204:
    response_get = get(f"http://{address}/users/")
    if response_get.status_code == 200:
        users = json.loads(response_get.text, object_pairs_hook=OrderedDict)

        print(json.dumps(users, ensure_ascii=False, indent=4))
    else:
        print(f"Ошибка при получении списка пользователей: {response_get.status_code}")
else:
    print(f"Ошибка при удалении пользователя: {response_del.status_code}")
