def get_number():
    while True:
        try:

            number = 9
            get = int(input("Я загадал число от 1 до 10. Попробуй угадать: "))

            if get < 0 or get > 10:
                print("Загаданное число только от 1 до 10!")
                continue
            elif get == number:
                print("Поздравляю! Ты угадал!")
                return get, number
            elif get < number:
                print("Ты не угадал! Загаданное число больше!")
                continue
            elif get > number:
                print("Ты не угадал! Загаданное число меньше!")
                continue

            return get, number
        except ValueError:
            print("Нужно ввести число!")

def main():
    get_number()

if __name__ == "__main__":
    main()