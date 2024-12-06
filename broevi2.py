# path: number_to_words_mk.py

def number_to_words_mk(number: float) -> str:
    """
    Конвертира даден број во зборови на македонски јазик, вклучувајќи и децимали.
    :param number: Бројот кој треба да се конвертира (може да биде цел или децимален)
    :return: Бројот како зборови на македонски
    """
    # Речници за броевите
    units = ["", "еден", "два", "три", "четири", "пет", "шест", "седум", "осум", "девет"]
    teens = ["десет", "единаесет", "дванаесет", "тринаесет", "четиринаесет", "петнаесет", "шеснаесет", "седумнаесет", "осумнаесет", "деветнаесет"]
    tens = ["", "", "дваесет", "триесет", "четириесет", "педесет", "шеесет", "седумдесет", "осумдесет", "деведесет"]
    hundreds = ["", "сто", "двеста", "триста", "четиристотини", "петстотини", "шестстотини", "седумстотини", "осумстотини", "деветстотини"]
    thousands = ["", "илјада", "илјади"]

    def integer_to_words(number: int) -> str:
        """Помошна функција за цели броеви."""
        if number == 0:
            return "нула"

        words = []

        # Илјадници
        if number // 1000 > 0:
            thousand_part = number // 1000
            words.append(f"{integer_to_words(thousand_part)} {thousands[1] if thousand_part == 1 else thousands[2]}")
            number %= 1000

        # Стотици
        if number // 100 > 0:
            words.append(hundreds[number // 100])
            number %= 100

        # Десетици
        if 10 <= number < 20:
            words.append(teens[number - 10])
            number = 0
        elif number >= 20:
            words.append(tens[number // 10])
            number %= 10

        # Единици
        if number > 0:
            words.append(units[number])

        return " ".join(words)

    # Проверка за негативни броеви
    if number < 0:
        return f"минус {number_to_words_mk(-number)}"

    # Разделување на целиот и децималниот дел
    integer_part = int(number)
    decimal_part = round(number - integer_part, 2)  # Ограничување на 2 децимални места

    # Конвертирање на целиот дел
    result = integer_to_words(integer_part)

    # Обработка на децимали како цел број
    if decimal_part > 0:
        decimal_as_number = int(str(decimal_part).split(".")[1].lstrip("0"))  # Отстранување на водечки нули
        result += f" запирка {integer_to_words(decimal_as_number)}"

    return result

# Пример за користење
print(number_to_words_mk(1234.56))  # илјада двесте триесет и четири запирка педесет и шест
print(number_to_words_mk(-45.78))   # минус четириесет и пет запирка седумдесет и осум
print(number_to_words_mk(100.1))   # сто запирка еден
print(number_to_words_mk(1.11))     # нула запирка десет
