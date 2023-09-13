def process_argument(arg):
    if isinstance(arg, list):
        if len(arg) == 0:
            return None
        total = sum(arg)
        return total / len(arg)

    elif isinstance(arg, dict):
        return dict(sorted(arg.items(), key=lambda item: item[1]))

    elif isinstance(arg, int):
        return int(str(arg)[::-1])

    elif isinstance(arg, str):
        words = arg.split()
        if len(words) == 0:
            return (0, None)
        longest_word = max(words, key=len)
        return (len(words), longest_word)

    else:
        return None


def main():
    while True:
        user_input = input("Введите данные (список, словарь, число или строку), или 'exit' для выхода: ")

        if user_input.lower() == "exit":
            break  # Выход из программы при вводе "exit"

        try:
            if user_input.isdigit():
                processed_data = process_argument(int(user_input))
            elif user_input.startswith("{") and user_input.endswith("}"):
                # Попытка интерпретировать введенную строку как словарь
                processed_data = process_argument(eval(user_input))
            else:
                # Попытка интерпретировать введенную строку как список
                processed_data = process_argument(eval(user_input))

            if processed_data is not None:
                print("Результат обработки:", processed_data)
            else:
                print("Не удалось обработать введенные данные.")
        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()


# Примеры использования функции
# arg1 = [1, 2, 3, 4, 5]
# arg2 = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}
# arg3 = 12345
# arg4 = "This is a sample sentence"
#
# result1 = process_argument(arg1)
# result2 = process_argument(arg2)
# result3 = process_argument(arg3)
# result4 = process_argument(arg4)
#
# print(result1)  # Среднее арифметическое: 3.0
# print(result2)  # Словарь отсортирован по значениям
# print(result3)  # Число в обратном порядке: 54321
# print(result4)  # (5, 'sentence') - количество слов и самое длинное слово