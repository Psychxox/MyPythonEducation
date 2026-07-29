def name_and_long():
    famile = str(input("Укажите свою фамилию: "))
    name = str(input("Укажите своё имя: "))

    result = f"Имя и фамилия: {name} " + f"{famile}. Длина Фамилии: " + str(len(famile))

    print(f"{result}")

if __name__ == "__main__":
    name_and_long()