def is_prime(number):
    num = int(number)
    if num < 0 or num > 1000:
        raise ValueError("Число должно быть в диапазоне от 0 до 1000")

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


while True:
    try:
        number = int(input("Введите число от 0 до 1000: "))
        if 0 <= number <= 1000:
            if is_prime(number):
                print(f"{number} - простое число.")
            else:
                print(f"{number} - не является простым числом.")
            break  # Выход из цикла, если введено корректное число
        else:
            print("Число должно быть в диапазоне от 0 до 1000.")
    except ValueError:
        print("Введите корректное число.")
