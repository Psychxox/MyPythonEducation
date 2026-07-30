ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "12345"

def get_login():
    while True:

        login = input("Введите логин: ")

        if login != ADMIN_LOGIN:
            print("Пользователь не найден! Попробуйте снова.")
            continue

        return login

def get_password():
    while True:

        password = input("Введите пароль: ")

        if password != ADMIN_PASSWORD:
            print("Неверный пароль! Попробуйте снова.")
            continue
        
        return password

def main():
    print("=" * 40)
    print("       АВТОРИЗАЦИЯ")
    print("=" * 40)
    
    get_login()
    get_password()
    
    print("Добро пожаловать!")

if __name__ == "__main__":
    main()