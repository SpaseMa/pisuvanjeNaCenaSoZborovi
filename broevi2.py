def number_to_words_mk(number: float) -> str:
  
    units = ["", "еден", "два", "три", "четири", "пет", "шест", "седум", "осум", "девет"]
    teens = ["десет", "единаесет", "дванаесет", "тринаесет", "четиринаесет", "петнаесет", "шеснаесет", "седумнаесет", "осумнаесет", "деветнаесет"]
    tens = ["", "", "дваесет", "триесет", "четириесет", "педесет", "шеесет", "седумдесет", "осумдесет", "деведесет"]
    hundreds = ["", "сто", "двеста", "триста", "четиристотини", "петстотини", "шестстотини", "седумстотини", "осумстотини", "деветстотини"]
    thousands = ["", "илјада", "илјади"]

    def integer_to_words(number: int) -> str:
        if number == 0:
            return "нула"

        words = []

        if number // 1000 > 0:
            thousand_part = number // 1000
            words.append(f"{integer_to_words(thousand_part)} {thousands[1] if thousand_part == 1 else thousands[2]}")
            number %= 1000

        if number // 100 > 0:
            words.append(hundreds[number // 100])
            number %= 100

        if 10 <= number < 20:
            words.append(teens[number - 10])
            number = 0
        elif number >= 20:
            words.append(tens[number // 10])
            number %= 10

        if number > 0:
            words.append(units[number])

        return " ".join(words)

    if number < 0:
        return f"минус {number_to_words_mk(-number)}"

    integer_part = int(number)
    decimal_part = round(number - integer_part, 2) 

    result = integer_to_words(integer_part)

    if decimal_part > 0:
        decimal_as_number = int(str(decimal_part).split(".")[1].lstrip("0"))  
        result += f" запирка {integer_to_words(decimal_as_number)}"

    return result

print(number_to_words_mk(1234.56))  
print(number_to_words_mk(-45.78))   
print(number_to_words_mk(100.1))  
print(number_to_words_mk(1.11))    
