### 1. Переход в другой диск в windows
Для случая если требуется просто перейти в корень другого диска, в windows
просто укажите имя диска без команды cd
```bash windows
b:
```

### 2. Переход в другую папку в windows
```bash windows
cd D:\senatorov\env_t_numpy
```

### 3. Создадим виртуальное окружение myenv
```bash
python -m venv myenv
```

### 4. Активируем виртуальное окружение myenv
```bash linux
source myenv/bin/activate
```

```bash windows
myenv/Scripts/activate
```

### 5. Установим библиотеку numpy в виртуальное окружение
```bash
pip install numpy
```

### 6. Посмотрим зависимости которые установились

```bash
pip list
```

### 7. Сохраним зависимости в файл requirements.txt

```bash
pip freeze > requirements.txt
```

### 8. Установим библиотеку pandas в виртуальное окружение
```bash
pip install pandas
```

### 9. Сохраним зависимости в файл requirements.txt по новой перезаписав файл

```bash
pip freeze > requirements.txt
```



