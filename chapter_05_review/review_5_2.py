def main():
    numbers = []
    
    # Запрашиваем 5 чисел
    for i in range(1, 6):
        num = int(input(f"Введите число {i}: "))
        # Добавляем в конец через срез
        numbers[len(numbers):] = [num]
    
    # Создаём список для обратного порядка
    reversed_numbers = []
    
    # Проходим по индексам от последнего до первого
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers[len(reversed_numbers):] = [numbers[i]]
    
    print(f"Исходный список: {numbers}")
    print(f"Список наоборот: {reversed_numbers}")

if __name__ == "__main__":
    main()