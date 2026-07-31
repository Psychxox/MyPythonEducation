# chapter_04/atm.py

BALANCE = 1000   # наличные деньги у пользователя
TOTAL = 5000     # деньги на карте (в банкомате)

def show_balance():
    print(f"Наличные: {BALANCE} руб.")
    print(f"На карте: {TOTAL} руб.")

def withdraw():
    global BALANCE, TOTAL
    
    while True:
        try:
            amount = int(input("Введите сумму для снятия: "))
            
            if amount <= 0:
                print("Сумма должна быть положительной!")
                continue
            
            if amount > TOTAL:
                print(f"Недостаточно средств на карте! На карте: {TOTAL} руб.")
                continue
            
            # Снимаем с карты → добавляем в наличные
            TOTAL -= amount
            BALANCE += amount
            print(f"Снято {amount} руб. с карты.")
            print(f"Наличные: {BALANCE} руб.")
            print(f"На карте: {TOTAL} руб.")
            break
            
        except ValueError:
            print("Ошибка! Введите число.")

def deposit():
    global BALANCE, TOTAL
    
    while True:
        try:
            amount = int(input("Введите сумму для внесения: "))
            
            if amount <= 0:
                print("Сумма должна быть положительной!")
                continue
            
            if amount > BALANCE:
                print(f"Недостаточно наличных! У вас: {BALANCE} руб.")
                continue
            
            # Вносим из наличных → на карту
            BALANCE -= amount
            TOTAL += amount
            print(f"Внесено {amount} руб. на карту.")
            print(f"Наличные: {BALANCE} руб.")
            print(f"На карте: {TOTAL} руб.")
            break
            
        except ValueError:
            print("Ошибка! Введите число.")

def main():
    print("Добро пожаловать в банкомат!")
    
    while True:
        print("\n" + "=" * 40)
        print("Доступные команды:")
        print("B - показать баланс")
        print("W - снять деньги (с карты → в наличные)")
        print("D - внести деньги (из наличных → на карту)")
        print("E - выход")
        print("=" * 40)
        
        command = input("Ваш выбор: ").upper()
        
        if command == "B":
            show_balance()
        elif command == "W":
            withdraw()
        elif command == "D":
            deposit()
        elif command == "E":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда!")

if __name__ == "__main__":
    main()