while True:
    n = input("Введите натуральное число: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print("Введите корректное натуральное число!")
sum_of_digits = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_of_digits += digit
    n //= 10

print("Сумма четных цифр в числе:", sum_of_digits)
