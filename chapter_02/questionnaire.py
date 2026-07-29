# Получаем данные
def get_name():
    while True:
        name = input("Введите ваше имя: ").strip()
        if not name:
            print("Имя не может быть пустым. Попробуйте снова.")
            continue
        if len(name) > 15:
            print("Имя не должно превышать 15 символов. Попробуйте снова.")
            continue
        return name

def get_surname():
    while True:
        surname = input("Введите вашу фамилию: ").strip()
        if not surname:
            print("Фамилия не может быть пустой. Попробуйте снова.")
            continue
        if len(surname) > 25:
            print("Фамилия не должна превышать 25 символов. Попробуйте снова.")
            continue
        return surname

def get_age():
    while True:
        try:
            birth_year = int(input("Введите ваш год рождения: "))
            if birth_year > 2026:
                print("Вы ещё не родились? Попробуйте снова.")
                continue
            if birth_year < 1900:
                print("Проверьте год рождения. Попробуйте снова.")
                continue
            return 2026 - birth_year
        except ValueError:
            print("Год рождения должен быть числом. Попробуйте снова.")

def get_favorite_color():
    color = input("Введите ваш любимый цвет: ").strip()
    return color if color else "Не указан"

def get_city():
    city = input("Введите город вашего проживания: ").strip()
    return city if city else "Не указан"

def get_hobby():
    hobby = input("Введите ваше хобби: ").strip()
    return hobby if hobby else "Не указано"

# Система запуска + сообщение
def main():
    name = get_name()
    last_name = get_surname()
    age = get_age()
    like_color = get_favorite_color()
    live_country = get_city()
    hobby = get_hobby()

    print("\nВаш профиль\n" + "=" * 50 + f"\nВаше имя: {name}\nВаша фамилия: {last_name}\nВаш возраст: {age}\nВаш любимый цвет: {like_color}\nВаш город проживания: {live_country}\nВаше хобби: {hobby}\n" + "=" * 50 + "\nОтличный профиль!\n")

# Запуск
if __name__ == "__main__":
    main()
