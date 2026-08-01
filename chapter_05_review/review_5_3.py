def main():
    numbers = [3, 7, 12, 5, 9, 21, 4]

    try:

        num = int(input("Введите индекс из списка: "))

        found = False

        for i in range(len(numbers)):
            if numbers[i] == num:
                print(f"Индекс числа {num}: {i}")
                found = True
                break

        if not found:
            print("Число не найдено")

    except ValueError:
        print("Введите число!")

if __name__ == "__main__":
    main()