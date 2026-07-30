def get_month():
    while True:
        try:

            number_of_month = int(input("Введите номер месяца: "))

            if number_of_month < 0 or number_of_month > 12:
                print("Неккоректный месяц!")
                continue
            elif number_of_month == 1 or number_of_month == 2 or number_of_month == 12:
                print("Сейчас месяц: Зима!")
                return number_of_month
            elif number_of_month >= 3 and number_of_month <= 5:
                print("Сейчас месяц: Весна!")
                return number_of_month
            elif number_of_month >= 6 and number_of_month <= 8:
                print("Сейчас месяц: Лето!")
                return number_of_month
            elif number_of_month >= 9 and number_of_month <= 11:
                print("Сейчас месяц: Осень!")
                return number_of_month

            return number_of_month
        except ValueError:
            print("Неккоректный ввод! Нужно число месяца!")

def main():
    get_month()

if __name__ == "__main__":
    main()