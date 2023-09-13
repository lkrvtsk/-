
jewelry_store = {
    "Кольцо": ["Золото", 500, 10],
    "Браслет": ["Серебро", 300, 15],
    "Серьги": ["Золото", 400, 20],
    "Цепочка": ["Золото", 700, 5],
    "Часы": ["Сталь", 800, 7]
}

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][0]}")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == "2":
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][1]} рублей")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == "3":
        item_name = input("Введите название изделия: ")
        if item_name in jewelry_store:
            print(f"{item_name} - {jewelry_store[item_name][2]} штук")
        else:
            print("Такого изделия нет в магазине.")

    elif choice == "4":
        print("Вся информация о товарах в магазине:")
        for item, info in jewelry_store.items():
            print(f"{item} - {info[0]}, Цена: {info[1]} рублей, Количество: {info[2]} штук")

    elif choice == "5":
        total_price = 0
        while True:
            item_name = input("Введите название изделия (0 - завершить покупку): ")
            if item_name == "0":
                break
            if item_name in jewelry_store:
                quantity = input(f"Введите количество {item_name}: ")
                if quantity.isdigit() and int(quantity) >= 0 and int(quantity) <= jewelry_store[item_name][2]:
                    quantity = int(quantity)
                    jewelry_store[item_name][2] -= quantity
                    total_price += quantity * jewelry_store[item_name][1]
                else:
                    print("Некорректное количество. Введите целое неотрицательное число, не превышающее количество в наличии.")
            else:
                print("Такого изделия нет в магазине.")
        print(f"Общая сумма покупки: {total_price} рублей")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите пункт из меню.")
