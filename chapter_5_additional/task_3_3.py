numbers = [45, 12, 78, 3, 56, 23, 9]
a = numbers[0]

for i in range(0, len(numbers)):
    if numbers[i] < a:
        a = numbers[i]
        
print(f"Минимальное число: {a}")