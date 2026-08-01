word = input("Введите слово: ")

print(f"\nСлово наоборот: {word[::-1]}")
print(f"Каждый второй: {word[::2]}")

# Перемешанное слово
mixed = ""
for i in range(len(word) // 2):
    mixed += word[len(word) - i - 1]
    mixed += word[i]

# Если длина нечётная — добавляем средний символ
if len(word) % 2 == 1:
    mixed += word[len(word) // 2]

print(f"Перемешанное: {mixed}")