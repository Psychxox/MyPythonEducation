def main():

    number = int(input("Введите N: "))
    total = 0

    for i in range(1, number + 1):
        total += i
    print(f"Сумма чисел от 1 до {number} = {total}")

if __name__ == "__main__":
    main()