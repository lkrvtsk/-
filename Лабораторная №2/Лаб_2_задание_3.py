def is_matrix_rectangular(matrix):
    return all(len(row) == len(matrix[0]) for row in matrix)

def count_non_zero_columns(matrix):
    if not matrix:
        return 0
    if not is_matrix_rectangular(matrix):
        return -1  #не прямоугольная, возвращаем -1

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    non_zero_cols = 0

    for col in range(num_cols):
        has_zero = False
        for row in range(num_rows):
            if matrix[row][col] == 0:
                has_zero = True
                break
        if not has_zero:
            non_zero_cols += 1

    return non_zero_cols

def main():
    while True:
        try:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))

            if rows <= 0 or cols <= 0:
                print("Количество строк и столбцов должно быть больше 0.")
                continue

            matrix = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    element = int(input(f"Введите элемент [{i+1}][{j+1}]: "))
                    row.append(element)
                matrix.append(row)

            result = count_non_zero_columns(matrix)

            if result == -1:
                print("Матрица не прямоугольная.")
            else:
                print(f"Количество столбцов без нулей: {result}")

            break
        except ValueError:
            print("Введите корректное целое число.")

if __name__ == "__main__":
    main()
