def main():
    total = 0
    count = 0
    
    while True:
        try:
            number = int(input("Введите число (0 для выхода): "))
            
            if number == 0:
                print("=" * 50)
                print("Вы вышли из программы!")
                print("=" * 50)
                print(f"Сумма: {total}")
                print(f"Количество чисел: {count}")
                
                if count > 0:
                    print(f"Среднее арифметическое: {total / count:.2f}")
                else:
                    print("Нет чисел для вычисления среднего.")
                break
            
            total += number
            count += 1
            
        except ValueError:
            print("Требуется только число!")

if __name__ == "__main__":
    main()