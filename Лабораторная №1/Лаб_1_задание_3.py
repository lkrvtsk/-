n = input("Введите натуральное число n (n ≥ 2): ")
while not n.isdigit() or int(n) < 2:
    print("Число n должно быть натуральным и не меньше 2.")
    n = input("Введите натуральное число n (n ≥ 2): ")
n = int(n)
numbers = []
for i in range(n):
    while True:
        num = input(f"Введите целое число #{i + 1}: ")
        if num.isdigit():
            numbers.append(int(num))
            break
        else:
            print("Введите целое число.")
sums = []
for i in range(1, n):
    sums.append(numbers[i - 1] + numbers[i])
print("Список сумм соседних чисел:", sums)
