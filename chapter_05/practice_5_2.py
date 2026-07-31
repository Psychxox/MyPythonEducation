def main():
    word = input("Введите слово: ")
    reversed_word = ""
    
    # Проходим по индексам от последнего до первого
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]  # добавляем символ
    
    print(f"Слово наоборот: {reversed_word}")

if __name__ == "__main__":
    main()