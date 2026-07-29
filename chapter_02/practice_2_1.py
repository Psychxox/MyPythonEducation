def calculate_age():
    age = my_age()

    calculate = 2026 - age
    return calculate

def my_age():
    while True:
        try:
            age = int(input("Укажите свой год рождения: "))
            if age < 1800:
                print("Вряд ли вы столь стары!")
                continue

            if age > 2026:
                print("Как вы можете пользоваться данной программой, если вы не родились ещё?")
                continue

            return age
        except ValueError:
            print("Возраст может быть только числом!")

def main():
    calculate = calculate_age()
    print(f"В 2026 году вам будет {calculate} лет")

if __name__ == "__main__":
    main()