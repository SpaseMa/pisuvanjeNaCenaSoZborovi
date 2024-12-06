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
    decimal_part = str(number).split(".")[1] if "." in str(number) else ""

    result = integer_to_words(integer_part)

    if decimal_part:
        decimal_words = [units[int(digit)] for digit in decimal_part]
        result += f" запирка {' '.join(decimal_words)}"

    return result

def main():
    print("Внесете број (цел или децимален):")
    try:
        user_input = input()  
        number = float(user_input)  
        print(number_to_words_mk(number))  
    except ValueError:
        print("Ве молиме внесете валиден број.")

if __name__ == "__main__":
    main()