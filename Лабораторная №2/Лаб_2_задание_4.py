while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n > 0:
            break
        else:
            print("Введите корректное натуральное число!")
    except ValueError:
        print("Введите корректное натуральное число!")

sum_of_digits = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_of_digits += digit
    n //= 10

print("Сумма четных цифр в числе:", sum_of_digits)
