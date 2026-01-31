"""Processing hashes and PE (ELF) files in Python."""

# # Обработка hashes и PE (ELF)-файлов на языке Python

# Исходные файлы для блокнота находятся по [ссылке](https://github.com/dm-fedorov/infosec/tree/master/re-tools/samples).

# Скачиваем весь архив с файлами для работы в Colab:

# !wget https://dfedorov.spb.ru/infosec/re/samples.zip

# # !unzip samples.zip

# !ls samples

# ## Определение сигнатуры файла

# В системах GNU/Linux, чтобы найти сигнатуру файла (уникальная последовательность байтов), можно использовать команду [xxd](https://www.opennet.ru/man.shtml?topic=xxd&category=1&russian=0), которая генерирует шестнадцатеричный дамп файла, как показано ниже:

# !xxd samples/task-1.exe

# Видим, что исполняемые файлы ОС Windows, также называемые [PE-файлами](https://ru.wikipedia.org/wiki/Portable_Executable) (например, .exe, .dll, .com, .drv, .sys и т. д.), имеют подпись файла ```MZ``` или шестнадцатеричные символы ```4D 5A``` в первых двух байтах файла.

# Выполним команду для [ELF-файла](https://ru.wikipedia.org/wiki/Executable_and_Linkable_Format) (подпись файла `ELF`):

# !xxd samples/test_01

# В следующем примере команда [file](https://www.opennet.ru/man.shtml?topic=file&category=1&russian=4) была запущена для двух разных файлов:

# !apt-get install file

# !file samples/task-1.exe

# !file samples/test_01

# В Python модуль [python-magic](https://github.com/ahupp/python-magic) может использоваться для определения типа файла:

# !pip3 install python-magic

# +
import hashlib

import magic
import pefile
# -

magic.from_file("samples/test_01")

magic.from_file("samples/task-1.exe")

# ## Обработка хеш-суммы на Python

# В системе Linux хеш-суммы могут быть сгенерированы с использованием утилит [md5sum](https://www.opennet.ru/man.shtml?topic=md5sum&category=1&russian=0), [sha256sum](https://www.opennet.ru/man.shtml?topic=sha256sum&russian=0) и [sha1sum](https://www.opennet.ru/man.shtml?topic=sha1sum&russian=0):

# !md5sum samples/task-1.exe

# !sha256sum samples/task-1.exe

# !sha1sum samples/task-1.exe

# В Python можно генерировать хеш-суммы, используя модуль [hashlib](https://docs.python.org/3/library/hashlib.html), как показано ниже:

# +
with open("samples/task-1.exe", "rb") as f:
    content = f.read()

print(hashlib.md5(content).hexdigest())
# -

print(hashlib.sha256(content).hexdigest())

print(hashlib.sha1(content).hexdigest())

# ## Извлечение строк

# Извлечение строк может подсказать, как функционирует программа, и рассказать об индикаторах, указывающих на подозрительный двоичный код. Например, если вредоносная программа создает файл, имя файла сохраняется в виде строки в двоичном файле. Или если вредоносная программа разрешает доменное имя, контролируемое злоумышленником, это имя впоследствии хранится в виде строки.
#
# Чтобы извлечь строки из подозрительного двоичного файла, вы можете использовать утилиту [strings](https://www.opennet.ru/man.shtml?topic=strings) в системах GNU/Linux.
#
# Команда `strings` по умолчанию извлекает ASCII-строки, длина которых составляет минимум четыре символа. С помощью опции ```-a``` можно извлечь строки из целого файла.

# !strings -a samples/task-1.exe

# В образцах вредоносных программ также используются Юникод-строки (2 байта на символ). Чтобы получить полезную информацию из двоичного файла, иногда нужно извлечь как ASCII-, так и Юникод-строки. Чтобы извлечь Юникод-строки с помощью команды `strings`, используйте опцию ```-el```:

# !strings -a -el samples/task-1.exe

# Модуль [FLOSS](https://github.com/fireeye/flare-floss) автоматически извлекает запутанные строки из вредоносных программ.

# Исполняемые файлы ОС Windows должны соответствовать формату PE/COFF (Portable Executable/Common Object File Format – Переносимый исполняемый/стандартный формат объектного файла).
#
# Фактическое содержимое PE-файла разделено на секции. За ними сразу же следует PE-заголовок. Эти секции представляют либо код, либо данные, они имеют ```in-memory-атрибуты```, такие как чтение/запись. Секция, представляющая код, содержит инструкции, которые будут выполняться процессором, тогда как секция, содержащая данные, может представлять различные типы данных, такие как чтение/запись данных программы (глобальные переменные), таблицы импорта/экспорта, ресурсы и т. д. У каждой секции есть свое имя, которое передает ее назначение.
#
# Например, секция с именем ```.text``` указывает на код и имеет атрибут ```read-execute```; раздел с именем ```.data``` указывает на глобальные данные и имеет атрибут ```read-write```.
#
# Следующий скрипт Python демонстрирует использование модуля [pefile](https://github.com/erocarrera/pefile) для отображения секции и её характеристик:

# !pip3 install pefile

pe = pefile.PE("samples/task-1.exe")
for section in pe.sections:
    print(
        f"{section.Name.decode()} \
    {hex(section.VirtualAddress)} \
    {hex(section.Misc_VirtualSize)} \
    {section.SizeOfRawData}"
    )

# Скрипт [Pescanner](https://github.com/hiddenillusion/AnalyzePE/blob/master/pescanner.py) использует эвристику вместо сигнатур и может помочь идентифицировать упакованные двоичные файлы, даже если для них нет сигнатур.
