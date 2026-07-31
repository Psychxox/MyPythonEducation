SECRET_NUMBER = 5

def main():
    attempts = 0
    print("Я загадал число от 1 до 10. Попробуй угадать!")
    print("Введите 'exit' для выхода из игры.")
    
    while True:
        user_input = input("Введи число: ")
        
        if user_input.lower() == "exit":
            print("Выход из игры...")
            break
        
        try:
            guess = int(user_input)
            attempts += 1
            
            if guess < SECRET_NUMBER:
                print("Загаданное число больше!")
            elif guess > SECRET_NUMBER:
                print("Загаданное число меньше!")
            else:
                print(f"Вы отгадали с {attempts} попытки!")
                break
                
        except ValueError:
            print("Нужно ввести число!")

if __name__ == "__main__":
    main()