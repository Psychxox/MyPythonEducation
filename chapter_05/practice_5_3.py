def main():
    n = int(input("Введите высоту пирамиды: "))
    
    for i in range(n):
        # Пробелы
        spaces = n - i - 1
        print(" " * spaces, end="")
        
        # Звезды
        stars = i * 2 + 1
        print("*" * stars)

if __name__ == "__main__":
    main()