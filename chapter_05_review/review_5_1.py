def main():
    try:
        number = int(input("Введите N: "))
        result = ""
        
        for i in range(1, number + 1):
            if i % 2 == 0:
                if result:  # если не первое число — добавляем запятую
                    result += ", "
                result += str(i)
        
        if result:
            print(f"Четные числа: {result}")
        else:
            print("Четных чисел нет")
        
    except ValueError:
        print("Ошибка! Введите число.")

if __name__ == "__main__":
    main()