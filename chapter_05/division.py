numbers = [5, 12, 33, 17, 8, 42, 0, 99]

def main():
    try:
        divisor = int(input("Введите число: "))
        
        if divisor == 0:
            print("На ноль делить нельзя!")
            return
        
        # Строка для хранения результата
        result = ""
        count = 0  # счётчик найденных чисел
        
        # Перебираем все числа из списка
        for num in numbers:
            if num % divisor == 0:
                # Добавляем число в строку результата
                if count > 0:
                    result += ", "  # добавляем запятую перед каждым числом, кроме первого
                result += str(num)  # преобразуем число в строку и добавляем
                count += 1
        
        # Выводим результат
        if count > 0:
            print(f"Числа, которые делятся на {divisor}: {result}")
        else:
            print(f"Нет чисел, которые делятся на {divisor}")
            
    except ValueError:
        print("Ошибка! Введите число.")

if __name__ == "__main__":
    main()