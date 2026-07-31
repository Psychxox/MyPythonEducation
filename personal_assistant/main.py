def get_mood():
    mood = input("Какое у тебя настроение? (хорошее/плохое) ").lower()

    if mood == "хорошее":
        print("Отлично! У тебя будет продуктивный день!")
        return
    elif mood == "плохое":
        print("Не расстраивайся! Всё обязательно наладится!")
        return
    else:
        print("Надеюсь, у тебя всё хорошо!")
        return

def answer():
    print("=" * 50)
    print("🤖  МОЙ ПЕРСОНАЛЬНЫЙ ПОМОЩНИК")
    print("=" * 50)
    print("Добро пожаловать в программу обучения Python!")
    print("Мы будем развивать этот проект от консоли до микросервиса.")
    print("=" * 50)
    
    name = input("Как тебя зовут? ")
    
    print("=" * 50)
    print(f"Приятно познакомиться, {name}!")
    print("Я буду помогать тебе на протяжении всего курса.")
    print("=" * 50)

    get_mood()

    print("=" * 50)

def calculate():
    while True:
        try:

            get_number = int(input("Введите первое число: "))
            action = input("Введите действие (+, -, *, /): ")
            get_number2 = int(input("Введите второе число: "))

            # Обработка ошибок кулькулятора
            if action == "/" and get_number2 == 0:
                print("Ошибка! Деление на ноль невозможно.")
                continue
            elif action not in ("+", "-", "*", "/"):
                print("Для действия нужно ввести только \"+\", \"-\", \"*\", \"/\"")
                continue

            # Выполнение действий
            elif action == "+":
                result = get_number + get_number2
                print(f"Получившийся результат: {result}")
                break
            elif action == "/":
                result = get_number / get_number2
                print(f"Получившийся результат: {result}")
                break
            elif action == "*":
                result = get_number * get_number2
                print(f"Получившийся результат: {result}")
                break
            elif action == "-":
                result = get_number - get_number2
                print(f"Получившийся результат: {result}")
                break

        except ValueError:
            print("Для чисел нужно ввести только цифры!")

def menu():
    print("Добро пожаловать в помощника!")

    while True:
        try:
            print("=" * 50 + "\nВыбери действие из меню:\n1. Калькулятор\n2. Показать настройки\n3. Выйти из помощника\n" + "=" * 50 + "\n")

            command = int(input("\nВведите номер команды из меню: "))

            if command == 1:
                print("Открываю кулькулятор!\n")
                calculate()
            elif command == 2:
                print("Открываю настройки!\n")
                print("Настройки пока не реализованы")
                continue
            elif command == 3:
                print("До свидания!")
                break

        except ValueError:
            print("Ошибка! Введите число.")

def main():
    answer()
    menu()

if __name__ == "__main__":
    main()