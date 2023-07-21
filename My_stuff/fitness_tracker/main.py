# Импортируйте необходимые модули
import datetime as dt

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) != 2 or data[0] == None or data[1] == None:
        return False
    else:
        return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True
    if len(storage_data) != 0 and time <= max(storage_data):
        return False
    else:
        return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    daysteps = sum(storage_data.values()) + steps
    return daysteps


def get_distance(daysteps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    distance = STEP_M / 1000 * daysteps
    return distance


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    hour = current_time.hour
    minute = current_time.minute
    hours = minute / 60 + hour
    mean_speed = dist / hours
    minutes = hours * 60
    calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * 0.029 * WEIGHT) * minutes
    return calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивный'
    elif dist >= 2:
        achievement = 'Завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


# Место для функции show_message.
def show_message(current_time, steps, dist, calories, achievement):
    """Получить сообщения в терминал."""
    output = (
        f'''
    Время: {current_time.strftime('%H:%M:%S')}.
    Количество шагов за сегодня: {steps}.
    Дистанция составила {dist:.2f} км.
    Вы сожгли {calories:.2f} ккал.
    {achievement}
    '''
    )
    return output


def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) == False:
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    time, steps = data
    pack_time = dt.datetime.strptime(data[0], FORMAT).time() # Преобразуйте строку с временем в объект типа time.

    if check_correct_time(pack_time) == False:
        return 'Некорректное значение времени'

    day_steps =  get_step_day(data[1])
    dist =  get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    # Вызовите функцию show_message().
    # Добавьте новый элемент в словарь storage_data.
    # Верните словарь storage_data.
    storage_data[pack_time] = data[1]
    output = show_message(pack_time, day_steps, dist, spent_calories, achievement)
    print(output)
    return storage_data


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)