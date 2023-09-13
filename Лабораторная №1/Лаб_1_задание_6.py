set1 = set()
valid_input_1 = False

while not valid_input_1:
    n1 = input("Введите элементы первого множества через пробел: ").split()
    valid_input_1 = all(item.replace('.', '', 1).isdigit() or (item.startswith('-') and item[1:].replace('.', '', 1).isdigit()) for item in n1)

    if valid_input_1:
        set1 = set(float(item) for item in n1)

set2 = set()
valid_input_2 = False

while not valid_input_2:
    n2 = input("Введите элементы второго множества через пробел: ").split()
    valid_input_2 = all(item.replace('.', '', 1).isdigit() or (item.startswith('-') and item[1:].replace('.', '', 1).isdigit()) for item in n2)

    if valid_input_2:
        set2 = set(float(item) for item in n2)

common_elements = set1.intersection(set2)
print("Элементы первого множества, которые встречаются во втором:", common_elements)
