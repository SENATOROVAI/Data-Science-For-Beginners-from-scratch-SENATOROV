"""Requests."""

# Example of usage
#
# ```python
# from requests import get
#
# response = get(
#     "https://static-maps.yandex.ru/1.x/?"
#     "ll=37.677751,55.757718&"
#     "spn=0.016457,0.00619&"
#     "l=map"
# )
# print(response)
# ```
#
# Handle exceptions
#
# ```python
# from requests import get, ConnectionError
#
# params = {"ll": "37.677751,55.757718", "spn": "0.016457,0.00619", "l": "map"}
# try:
#     response = get("https://static-maps.yandex.ru/1.x/", params=params)
# except ConnectionError:
#     print("Проверьте подключение к сети.")
# else:
#     with open("map.png", "wb") as file:
#         file.write(response.content)
# ```
#
#
# Working with Yandex API
#
# ```python
# from requests_oauthlib import OAuth2Session
# from requests import get, post, put, delete
#
#
# client_id = ""
# client_secret = ""
# auth_url = "https://oauth.yandex.ru/authorize"
# token_url = "https://oauth.yandex.ru/token"
# oauth = OAuth2Session(client_id=client_id)
# authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
# print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
# code = input("Вставьте одноразовый код: ")
# token = oauth.fetch_token(token_url=token_url, code=code, client_secret=client_secret)
# access_token = token["access_token"]
# print(access_token)
#
# headers = {"Authorization": f"OAuth {access_token}"}
# r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
# print(r.json())
#
# params = {"path": "Тест API"}
# r = put(
#     "https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params
# )
# print(r)
#
# params = {"path": "Тест API/map.png"}
# r = get(
#     "https://cloud-api.yandex.net/v1/disk/resources/upload",
#     headers=headers,
#     params=params,
# )
# href = r.json()["href"]
# files = {"file": open("map.png", "rb")}
# r = put(href, files=files)
# print(r)
# ```

# ! pip install requests

# +
# 1

from json import dumps
from sys import stdin

from requests import delete, get, post, put

print(get("http://127.0.0.1:5000").text)

# +
# 2


address = "http://" + input()
sum_val = 0
while data_val := int(get(address).text):
    sum_val += data_val
print(sum_val)

# +
# 3


address = "http://" + input()
values: list[int | str] = get(address).json()
print(sum(itm for itm in values if isinstance(itm, int)))

# +
# 4


address = "http://" + input()
key = input()
api_data = get(address).json()
print(api_data.get(key, "No data"))

# +
# 5


address = "http://" + input()
ways = [path.strip() for path in stdin]
total = 0
for way in ways:
    total += sum(get(address + way).json())
print(total)

# +
# 6


address = "http://" + input() + "/users"
user_data = get(address).json()
names = []
for user in user_data:
    names.append(f"{user_data['last_name']} {user_data['first_name']}")
for name in sorted(names):
    print(name)

# +
# 7


address = "http://" + input() + "/users/" + input()
message = "".join(msg for msg in stdin)
user_data_2 = {}
try:
    user_data_2 = get(address).json()
except ValueError:
    print("Пользователь не найден")
if user_data_2:
    for key in user_data_2:
        message = message.replace("{" + key + "}", str(user_data_2[key]))
    print(message)

# +
# 8


address = "http://" + input() + "/users"
new_user = {}
new_user["username"] = input()
new_user["last_name"] = input()
new_user["first_name"] = input()
new_user["email"] = input()
post(address, data=dumps(new_user))

# +
# 9


address = "http://" + input() + "/users/" + input()
user_line = [user_info.strip().split("=") for user_info in stdin]
new_data = {}
for user_update in user_line:
    new_data[user_update[0]] = user_update[1]
put(address, data=dumps(new_data))

# +
# 10


address = "http://" + input() + "/users/" + input()
delete(address)
