numbers = [2, 4, 6, 8, 10, 12, 14]

try:

    num = int(input("Введи число: "))
    found = False

    for n in numbers:
        if n == num:
            found = True
            break

    if found:
        print("Да")
    else:
        print("Нет")

except ValueError:
    print("Нужно число!")