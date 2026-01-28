# ## Дата и время в Питоне

# ### Модуль datetime

# Импорт модуля и класса datetime

# +
# импортируем весь модуль
import datetime

# часто из модуля datetime удобнее импортировать только класс datetime
from datetime import datetime

# чтобы получить доступ к функции now(), сначала обратимся к модулю, потом к классу
print(datetime.datetime.now())
# -

# и обращаться непосредственно к нему
print(datetime.now())

# Объект datetime и функция `now()`
