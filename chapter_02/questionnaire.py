# Получаем данные
def p_name():
    while True:
        try:

            name = input("Введите ваше имя: ")
            if len(name) > 15:
                print(f"Вас точно зовут {name}?")
                continue
            if len(name) < 1:
                print(f"Вас точно зовут: {name}?")
                continue

            return name
        except ValueError:
            print("Не правильный формат!\n")

def p_last_name():
    while True:
        try:

            last_name = input("Введите вашу фамилию: ")
            if len(last_name) > 25:
                print(f"Ваша фамилия точно {last_name}?")
                continue

            return last_name
        except ValueError:
            print("Не правильный формат!\n")

def p_birth_year():
    while True:
        try:
            
            birth_year = int(input("Введите ваш год рождения: "))

            if birth_year > 2026:
                print(f"Вряд ли вы родились в {birth_year} году.")
                continue

            age = 2026 - birth_year

            return age
        except ValueError:
            print("Не правильный формат!\n")

def p_like_color():
    while True:
        try:

            like_color = input("Введите ваш любимый цвет: ")
            return like_color

        except ValueError:
            print("Не правильный формат!\n")

def p_live_country():
    while True:
        try:

            live_country = input("Введите город вашего проживания: ")

            return live_country
        except ValueError:
            print("Не правильный формат!\n")

def p_hobby():
    while True:
        try:

            hobby = input("Введите ваше хобби: ")

            return hobby
        except ValueError:
            print("Не правильный формат!\n")

# Система запуска + сообщение
def main():
    name = p_name()
    last_name = p_last_name()
    age = p_birth_year()
    like_color = p_like_color()
    live_country = p_live_country()
    hobby = p_hobby()

    print("\nВаш профиль\n" + "=" * 50 + f"\nВаше имя: {name}\nВаша фамилия: {last_name}\nВаш возраст: {age}\nВаш любимый цвет: {like_color}\nВаш город проживания: {live_country}\nВаше хобби: {hobby}\n" + "=" * 50 + "\nОтличный профиль!\n")

# Запуск
if __name__ == "__main__":
    main()
